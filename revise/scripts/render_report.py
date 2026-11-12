"""Render a completed Revise Markdown report with Pandoc and XeLaTeX."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--kind", choices=("revision-report", "batch-summary"), required=True)
    parser.add_argument("--templates", type=Path, help="Directory containing custom templates")
    parser.add_argument("--tex-template", type=Path, help="Explicit Pandoc LaTeX template")
    args = parser.parse_args()

    source = args.markdown.resolve(strict=True)
    if source.suffix.lower() != ".md":
        parser.error("Expected a completed .md file")
    defaults = Path(__file__).resolve().parents[1] / "assets" / "templates"
    filename = args.kind + ".tex"
    directories = [source.parent / "revise-templates", defaults]
    if args.templates:
        if not args.templates.is_dir():
            parser.error(f"Template directory not found: {args.templates}")
        directories.insert(0, args.templates)
    if args.tex_template:
        template = args.tex_template.resolve(strict=True)
    else:
        template = next((folder / filename for folder in directories if (folder / filename).is_file()), None)
        if template is None:
            parser.error(f"Missing template {filename}; check the Revise installation")
    target = source.with_suffix(".tex")
    if target == template.resolve():
        parser.error("Choose an output folder separate from the template")
    pandoc = shutil.which("pandoc")
    if not pandoc:
        parser.exit(1, "Pandoc is required to generate the LaTeX source.\n")

    # Stage each build so a failed compilation cannot publish a partial PDF.
    with tempfile.TemporaryDirectory(dir=source.parent, prefix=".revise-") as scratch:
        build = Path(scratch)
        tex = build / target.name
        subprocess.run([
            pandoc, str(source), "--from=markdown-raw_tex-raw_html", "--to=latex",
            "--standalone", "--no-highlight", "--wrap=none", "--columns=1",
            "--template", str(template.resolve()), "--output", str(tex),
        ], cwd=source.parent, check=True)
        os.replace(tex, target)
        engine = shutil.which("xelatex")
        if not engine:
            parser.exit(1, f"Saved {target}. Locate TeX Live/MiKTeX or install MiKTeX, then retry.\n")
        command = [engine, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
                   "-output-directory=" + build.name, target.name]
        for _ in range(2):
            subprocess.run(command, cwd=source.parent, check=True)
        os.replace(build / target.with_suffix(".pdf").name, target.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
