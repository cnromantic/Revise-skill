# 推荐工具链与降级策略

本文件用于指导 Revise 在可用工具不同的环境中选择稳妥处理方式。工具不可用时，应降级并在修改说明中说明限制，不得夸大输出能力。

## 一、Word 处理

| 任务 | 推荐库/工具 | 用法建议 |
|---|---|---|
| 复制源文件 | `shutil.copy2` | 先复制源 Word，再在副本上修改 |
| DOCX 读取与低风险修改 | `python-docx` | 段落、表格、run 级替换、黄色高亮 |
| OOXML 底层处理 | `lxml`、`zipfile` | 识别自动编号、复杂样式、必要时保留结构 |
| Windows Word 自动化 | `pywin32` | 可选，用于批注、更新目录、导出 PDF；要求本机安装 Word |
| DOC 转 DOCX | LibreOffice headless | 可选，用于 `.doc` 转换 |
| 文本差异 | `difflib` | 生成修改前后差异说明 |

降级策略：

1. 无法可靠保留格式时，不直接重建整个 Word。
2. 无法处理 `.doc` 时，说明需转换为 `.docx` 后再处理。
3. 无法保留上标、脚注、超链接或域代码时，缩小修改范围或只在修改说明中给建议。

## 二、PDF 处理

| 任务 | 推荐库/工具 | 用法建议 |
|---|---|---|
| 文本提取、坐标定位、批注 | `PyMuPDF` / `fitz` | 首选；用于 `search_for`、高亮、FreeText 批注、保存 PDF |
| PDF 元数据、拆分合并 | `pypdf` | 辅助处理页数、合并说明页等 |
| 表格/文本提取 | `pdfplumber` | 可选，用于辅助识别表格文本 |
| 生成说明 PDF | `reportlab`、`weasyprint`、Pandoc、LibreOffice | 优先保证表格清晰、中文可读 |

降级策略：

1. 扫描件或无文本层 PDF 不默认强制 OCR。
2. 无法精准定位时，使用页面级批注并说明限制。
3. 未真正替换正文时，只输出批注式修改稿。

## 三、参考文献核验

| 任务 | 推荐库/工具 | 用法建议 |
|---|---|---|
| 联网请求 | `requests` | 查询 DOI、Crossref、期刊官网、网页标题 |
| DOI 解析 | `urllib.parse`、`requests` | 访问 `doi.org` 跳转，记录最终 URL |
| Crossref 查询 | `habanero` 或 Crossref REST API | 按题名、作者、年份检索英文文献 |
| 字符串相似度 | `rapidfuzz` | 比较文献题名、作者、来源相似度 |
| HTML 解析 | `beautifulsoup4` | 获取网页标题、meta 信息 |
| 中文文献 | 搜索引擎、期刊官网、CNKI/万方/维普页面 | 能访问则核验，不能访问则标注未核验 |

降级策略：

1. CNKI、万方、维普可能需要登录或本校 IP。可用则核验，不可用则列为人工核验。
2. 当前环境无法联网或用户禁止联网时，不做真实性断言。
3. 检索结果不充分时，不补造 DOI、URL、卷期、页码或出版信息。

## 四、修改说明 PDF

修改说明 PDF 应优先保证可读性：

1. 使用真实表格线，不把 Markdown 管道表格原样写成纯文本。
2. 中文字体可用时优先选择 Microsoft YaHei、SimSun、SimHei 或系统可用中文字体。
3. 宽表应拆分或使用横向页面，不把字号压得过小。
4. 如果当前工具无法生成友好 PDF，应先生成 HTML 或 DOCX 中间稿再转 PDF，并说明工具限制。

## 五、中文编码与终端显示

Revise 的 Markdown、YAML 和说明文件默认使用 UTF-8。Windows 终端或 PowerShell 可能按本地代码页显示输出，导致中文看起来像乱码；这通常是显示问题，不代表文件已经损坏。

推荐做法：

1. PowerShell 读取中文文本时使用 `Get-Content -Encoding UTF8`。
2. Python 脚本读取中文文件时显式传入 `encoding='utf-8'`。
3. 运行 Python 校验脚本前可设置 `$env:PYTHONUTF8='1'`。
4. 需要在终端查看大量中文输出时，可先执行 `chcp 65001`，并设置 `$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new()`。
5. 如果 UTF-8 解码正常、文件中没有 `�`、`锟斤拷` 等替换字符，但终端显示异常，应在处理日志中说明“终端显示编码异常”，不要把它写成论文或 Skill 文件损坏。
