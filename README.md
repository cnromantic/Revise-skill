# Revise Agent Skill V5.0

Revise 是用于中文本科毕业论文（设计）评审与保守修改的智能体技能。V5.0 将专业识别纳入初评：每篇先核对封面、题目和摘要，再按专业及研究方法选择评分证据。单篇修改说明和多篇汇总均从 Markdown 生成可编辑的 LaTeX 源文件，再编译为 PDF。

[下载 V5.0（ZIP）](https://github.com/cnromantic/Revise-skill/archive/refs/tags/v5.0.zip) · [浏览 V3.2](https://github.com/cnromantic/Revise-skill/tree/v3.2) · [查看全部版本标签](https://github.com/cnromantic/Revise-skill/tags)

## 开始使用

1. 取得包含 `SKILL.md`、`references/`、`assets/`、`scripts/` 和 `agents/` 的完整 `revise/` 目录。可使用本地副本，也可在公开仓库下载 ZIP，解压后查看 `SKILL.md` 的版本。[GitHub 仓库](https://github.com/cnromantic/Revise-skill) · [备用下载](https://pan.baidu.com/s/180KQ9x4b-wztz8_--FtGEQ?pwd=t2jq)
2. **可直接让 AI Agent 安装**：“请把我提供的 revise 文件夹安装到当前工具的个人技能库。如有旧版，先备份。安装后核对版本、专业目录和四个报告模板，告诉我如何调用。”也可以按下表手动安装；最终应能读取 `skills/revise/SKILL.md` 或在技能界面看到 Revise。
3. 打开论文目录，输入“使用 Revise 处理这里的本科论文，生成修改稿和修改说明”。学校量表、格式要求或自定义模板可一并提供。缺少原生技能入口时，将整个技能目录加入项目，明确要求按其中的 `SKILL.md` 执行并读取指定资源。

## 工具与模型

下表按工具列出安装位置。以 `~/` 开头的是当前用户主目录（Windows 通常为 `%USERPROFILE%`），以点开头且无 `~/` 的是项目相对路径。云端工作区与本地桌面端的文件系统可能不同，安装前确认本次会话能打开论文、运行编译器并写入输出目录。

| 工具 | 用户目录、项目目录或安装入口 |
|----------------|------------------------------------------------------------------|
| WorkBuddy | `~/.workbuddy/skills/`（本机核对）；企业版可在技能界面上传本地技能包。 |
| TRAE | 国内版本机用户目录为 `~/.trae-cn/skills/`；其他版本从技能设置确认。 |
| ZCode | 用户目录 `~/.zcode/skills/`，项目目录 `.zcode/skills/`。 |
| Kimi Work | 桌面端在技能界面导入完整 ZIP。本机受管位置为 Windows 漫游应用数据目录下的 `kimi-desktop/daimon-share/daimon/skills/`。 |
| 豆包工作 | 从“插件&技能&伙伴”管理技能。尚未核实跨版本通用的用户安装目录；如当前版本提供本地导入，选择完整技能包。 |
| 千问办公 | 用户目录 `~/.qwenwork/skills/`，也支持手动上传。 |
| Codex | 用户目录 `~/.agents/skills/`，项目目录 `.agents/skills/`；本机桌面环境也加载 `~/.codex/skills/`。 |
| Claude Code | 用户目录 `~/.claude/skills/`，项目目录 `.claude/skills/`。 |
| Cursor | 用户目录 `~/.cursor/skills/`，项目目录 `.cursor/skills/`。 |
| Cline | 用户目录 `~/.cline/skills/`，项目目录 `.cline/skills/`。 |

安装入口与路径核对资料（2026 年 11 月）：[WorkBuddy](https://cloud.tencent.com/document/product/1831/134432) · [TRAE](https://docs.trae.cn/ide_skills) · [ZCode](https://zcode.z.ai/cn/docs/skill) · [Kimi Work](https://www.kimi.com/features/skills) · [豆包工作](https://open.doubao.com/document) · [千问办公](https://www.alibabacloud.com/help/zh/qwenwork/skills) · [Codex](https://developers.openai.com/codex/skills) · [Claude Code](https://code.claude.com/docs/en/skills) · [Cursor](https://cursor.com/docs/skills) · [Cline](https://docs.cline.bot/customization/skills)。

国内工作流可结合工具实际支持的 **Kimi、GLM、DeepSeek** 等模型；Claude Code、Codex 等也可在各自支持的模型配置下使用。OpenClaw 用户可沿用其技能机制。安装对象是运行工具，模型名称本身不能确定 Skills 目录。

## 评审如何适配专业

- 技能随附教育部《普通高等学校本科专业目录（2026 年）》的 Markdown 转录。封面专业明确时核对专业名称、代码与门类，结合题目、摘要识别论文类型。只能判断专业类、材料相互冲突或候选不唯一时，先向使用者询问专业全称。校内名称或旧专业匹配不到时记录原称。[本科专业目录](revise/references/undergraduate-major-catalogue.md)
- 文史论文检查史料、版本及引文如何支撑论点；数学论文检查定理条件、证明及符号；艺术设计检查创作意图、迭代与作品；软件开发继续检查需求、设计、实现与测试。专项证据进入同一份评分表。默认使用含否决性指标的本科抽检量表；用户提供学校量表时按学校口径评分。[专业评审指引](revise/references/discipline-review.md) · [评分量表](revise/references/rubric.md)
- 默认检查参考文献引用顺序、真实性和引用正确性。数据库不可达、禁止联网或证据不足时逐项列出。核实的 DOI 或链接写入修改说明。仅有正文时，按呈现出的工作量与写作形式评价进度安排。[参考文献核验](revise/references/reference-verification.md)

## 修改稿和报告

Word 先复制源文件，在副本局部修改并黄色高亮，保留上标、自动编号、域和原有版式；PDF 先复制，再添加就近批注。属于同一篇的 Word 与 PDF 默认处理 Word 并记录跳过原因。摘要保留作者的叙述和正文能支持的结果，删去夸大结论后可直接在已有完整句收尾。PDF 页边写明应删除或替换的原文；仅因无法取得来源而待核的文献列在说明的核验表中。

| 输入 | 每篇交付 | 额外交付 |
|---|---|---|
| 单篇 Word 或 PDF | 同格式修改稿（旧 .doc 转 .docx），以及同名修改说明 .md、.tex、.pdf | — |
| 多篇论文 | 各篇独立的修改稿和三种格式的说明 | `X篇论文处理汇总.md`、`.tex`、`.pdf`，X 为实际处理篇数 |

修改说明的三张表分别列出初评、具体修改和复评。已改正文按实稿评分；仅有 PDF 批注时，第三张表按落实明确建议的条件逐项估分，缺少依据时标为待复评。需要更正内容时，编辑 MD 后重新生成 TeX 和 PDF。

## 自定义报告模板

| 用途 | Markdown 内容模板 | LaTeX 排版模板 |
|---|---|---|
| 单篇说明 | [revision-report.md](revise/assets/templates/revision-report.md) | [revision-report.tex](revise/assets/templates/revision-report.tex) |
| 多篇汇总 | [batch-summary.md](revise/assets/templates/batch-summary.md) | [batch-summary.tex](revise/assets/templates/batch-summary.tex) |

四个文件均可单独自定义。将要调整的文件复制到**报告输出目录下的 `revise-templates/`** 并保留表中的文件名，或在调用时指明模板路径。技能对每个文件分别优先使用明确指定的模板，其次取输出目录的模板，余下的使用技能默认模板。例如只提供 `batch-summary.tex`，即可更换汇总 PDF 的版式。MD 可调整字段和校级评分行，TeX 可改页眉、颜色、字号与栏距，保留 Pandoc 的 `$body$` 插槽。两类报告都保留三张核心表和指定的文末说明。

报告生成使用 Pandoc 和 XeLaTeX。先检测本机 **TeX Live 或 MiKTeX**，已有环境直接使用，二者均未安装时安装 MiKTeX。中文默认使用 Fandol 字体；安装或编译受限时列明错误并保留已完成文件。[编译步骤和命令](revise/references/technical-tooling.md) · [渲染脚本](revise/scripts/render_report.py)

更多操作示例见[快速使用指南（Markdown）](Revise快速使用指南.md)和[快速使用指南（PDF）](Revise快速使用指南.PDF)。公开仓库仅维护技能、模板与使用文档，学生原稿、修改稿、报告和未脱敏测试材料保存在本地。

说明：使用 Revise 技能生成的论文修改稿、批注和评审意见由人工智能辅助生成，仅供论文评审与修改参考。最终结论请以指导教师、评阅教师及学校相关管理部门的审核意见为准。
