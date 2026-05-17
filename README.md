# Revise Skill

Revise 是一个面向中文本科毕业论文（设计）的通用 AI Skill，用于论文评审、保守修订、Word/PDF 批注和结构化修改说明生成。它可根据“本科毕业论文（设计）抽检评议要素”进行初步评审，并在修改建议落实后辅助进行复评；同时可检查论文结构、语言表达、图表编号、测试说明和参考文献引用关系。针对软件开发类论文，Revise 额外优化了需求、设计、实现、测试之间一致性的检查。

本仓库中的 Skill 采用 Markdown + YAML + reference files 的轻量结构，不绑定单一平台。只要工具支持自定义指令、项目规则、Agent Skill、知识文件或上下文加载，就可以使用本 Skill。

## 适用工具

本 Skill 可在目前主流 AI 编程与文档处理工具中使用，包括但不限于：

- OpenClaw
- Cursor、Windsurf、Trae、Continue、Cline、Roo Code 等支持规则文件或上下文文件的 IDE/Agent 工具；
- OpenAI Codex / ChatGPT Agent 类工具；
- Claude Code、Gemini CLI 等命令行 Agent；
- 其他可读取 Markdown 指令并访问本地 Word/PDF 文件的 AI 工具。

如果工具原生支持 Skill，可直接安装 `revise` 目录。  
如果工具不支持 Skill 概念，可将 `SKILL.md` 作为系统提示词、项目规则或 Agent 指令使用，并让工具按需读取 `references/` 中的参考文件。
处理数学、管理、文学、外语等特定类型论文时，可在调用 Revise 时追加该学科的额外处理提示，例如要求重点检查数学论文中的定义、定理、证明逻辑、公式编号和 LaTeX 公式显示。

## 主要能力

- 自动识别并处理当前目录中的 `.docx`、`.doc` 或 `.pdf` 论文。
- 根据本科毕业论文（设计）抽检评议要素进行初评打分，并给出逐项依据。
- 检查题目、摘要、关键词、英文题名、目录、章节、正文、图表、测试、参考文献等关键部分。
- 在修改建议落实后辅助进行复评，展示预计改进情况。
- 对软件开发类论文额外检查需求分析、系统设计、数据库、接口、实现、测试、截图和技术路线一致性。
- 对可安全修改的问题生成修改稿，并用黄色突出显示或就近批注。
- 对不能可靠直接修改的问题，在修改说明中列出并提示人工确认。
- 输出 Markdown 与 PDF 两种格式的修改说明。
- 默认不联网核验 DOI 或参考文献真实性，除非用户明确要求。

## 仓库结构

```text
revise/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── docx-workflow.md
    ├── pdf-workflow.md
    ├── report-template.md
    ├── rubric.md
    ├── software-engineering-checklist.md
    └── style-rules.md
```

各文件作用：

- `SKILL.md`：Skill 主入口，包含触发条件、默认行为、处理流程、输出要求和风险边界。
- `agents/openai.yaml`：面向支持 Agent/Skill 列表的工具的展示信息。
- `references/rubric.md`：毕业论文评审评分标准。
- `references/software-engineering-checklist.md`：软件工程类论文专项检查清单。
- `references/style-rules.md`：中文论文语言、标点和中英文混排规则。
- `references/docx-workflow.md`：Word 论文处理规则。
- `references/pdf-workflow.md`：PDF 论文处理规则。
- `references/report-template.md`：修改说明模板。

## 安装方式

### 方式一：用于支持 Skill 的工具

将整个目录复制到目标工具的 Skill 目录中：

```text
revise
```

安装后目录名建议保持为：

```text
revise
```

Skill 的 frontmatter 名称也是 `revise`，对外显示名称为 `Revise`。

### 方式二：用于项目规则或自定义指令

在不支持原生 Skill 的工具中，可以这样使用：

1. 将 `revise/SKILL.md` 作为主要规则文件或系统指令。
2. 将 `revise/references/` 保持在同一项目中。
3. 要求工具在处理论文时按需读取 `references/` 中的文件。
4. 确保工具具有读取和写入当前论文目录的权限。

### 方式三：一次性使用

把 `SKILL.md` 的内容提供给 AI 工具，并附上论文文件或论文所在目录，再使用类似提示：

```text
请使用 Revise 处理当前目录中的论文。
默认跳过参考文献 DOI 和出版真实性联网核验。
如果是 PDF 论文，请输出修改稿 PDF、修改说明 MD 和修改说明 PDF。
```

## 推荐使用流程

1. 将待处理论文放入工作目录。
2. 启用或加载 Revise Skill。
3. 发出处理指令，例如：

```text
请使用 Revise 处理当前目录中的论文，并生成修改稿和修改说明。
```

4. 检查输出文件。
5. 对 Skill 标记为“仍需人工确认”的内容进行人工复核。

Word 输入时默认输出：

```text
论文题目-修改稿.docx
论文题目-修改说明.md
论文题目-修改说明.pdf
```

PDF 输入时默认输出：

```text
论文题目-修改稿.pdf
论文题目-修改说明.md
论文题目-修改说明.pdf
```

## 默认边界

Revise 默认采用保守策略：

- 不伪造实验数据、测试结果、截图、系统功能、源码行为或参考文献信息。
- 不主动联网搜索 DOI。
- 不声称参考文献真实性已经核验，除非用户明确授权联网核验。
- 对无法可靠修改的问题，只给出建议或列入人工确认事项。
- 对 Word 修改稿尽量保留原有字符级格式，尤其是参考文献引用上标、超链接、域代码等格式。
- 对 PDF 论文优先采用就近黄色批注，不轻易声称完成原位正文替换。

## 版本信息

当前版本：`3.0`  
Skill 名称：`revise`  
显示名称：`Revise`

建议使用 Git tag 管理公开版本，例如：

```text
v3.0
```

## 共享与贡献建议

- 不要在仓库中提交真实学生论文、隐私信息或处理后的敏感文件。
- 修改 Skill 时优先保持 `SKILL.md` 简洁，将详细规则放入 `references/`。
- 如新增工作流文件，应在 `SKILL.md` 中说明何时读取。
- 发布前建议用脱敏样例论文测试 Word、PDF、修改说明三类输出。
- 公开共享前请根据你的授权意图补充 `LICENSE` 文件。

## 免责声明

Revise 生成的评审意见、修改稿和修改说明仅供论文修改与评审参考，不能替代指导教师、评阅教师、学校管理部门或学术规范审查的最终意见。使用者应对论文内容、引用真实性、数据真实性和最终提交版本负责。
