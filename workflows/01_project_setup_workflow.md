# Project Setup Workflow

# 项目初始化流程


## Workflow Purpose

本Workflow负责：

创建新的AI影视项目。


目标：

建立项目基础结构。

确认制作目标。

初始化项目状态。


本阶段只负责：

项目初始化。


不负责：

剧本深度分析。

资产设计。

视觉开发。

镜头设计。

Clip Production。

视频Prompt生成。


---

# Workflow Position

当前阶段：

STATE-00 Project Setup


下一阶段：

STATE-01 Script Analysis


对应下一Workflow：

02_script_analysis_workflow.md


---

# Project Workspace Gate

在判断现有项目或初始化新项目之前，先按`rules/runtime_reload.md`判断并执行任何已触发的Runtime Reload。本Workflow不重复维护重载词、读取顺序或Reload Status语义。

在当前运行环境能够提供已安装Skill资源时读取：

references/project_workspace.md

references/project_state_contract.md

只有`rules/state_source.md`的Intent Scope Gate明确要求恢复、保存、登记、归档或核验用户指定项目时，才读取`project_registry.json`或解析Active Project Root候选；不得为新项目、首次剧本请求或相似项目查找而扫描它们。随后只按`rules/state_source.md`选定唯一State Source。本Workflow不复制State Source优先级或fallback细节。

当前没有项目证据时，在会话内建立最小STATE-00即可；Project Root、Registry和完整Portable State只在用户明确要求持久化或当前环境的恢复任务确实需要时创建/读取。无论持久化与否，STATE-00的生产边界、Project ID、事实记录与后续Gate均保持不变。

继续现有项目且Selected State Source是Active Project Root时读取：

- project_manifest.json
- project_status.md
- project_bible.md
- asset_registry.md

本Workflow中的文件别名按`references/project_workspace.md`解释；普通Chat的可用资料与输出行为按`rules/chat_compatibility.md`解释。

禁止在Skill安装根目录的兼容入口初始化完整项目状态；Portable STATE-00只写最小状态镜像。

禁止覆盖非空Project Root。


---

# Trigger Condition

当用户输入：

- 一个创意、题材、品牌需求、角色设定、情绪/场景或“帮我写剧本 / 先从剧本开始”
- 完整剧本
- 剧情大纲
- 小说文本
- 小说章节
- 故事设定
- 世界观设定
- 新影视项目素材

并且当前没有正在执行的同一项目时：

启动本Workflow。


如果当前已经存在项目，先按`rules/state_source.md`验证其Selected State Source，再判断是否继续当前项目或建立新项目。本Workflow不根据“最近项目”、孤立路径或历史Skill描述自行选择状态。


判断：

是否继续当前项目。

是否为新项目。


禁止：

无条件覆盖现有项目状态。


---

# Required Files

执行本Workflow时：

读取：

config.md

rules/01_pipeline_rules.md

rules/05_output_rules.md

knowledge/director_decision_layer.md

templates/00_project_start_template.md

references/project_state_contract.md

references/asset_lock_contract.md

references/artifact_revision_contract.md

templates/17_execution_ledger.md

templates/18_artifact_revision_ledger.md


如果以下项目文件可实际访问：

同时读取：

`<active-project-root>/project_bible.md`

`<active-project-root>/asset_registry.md`

`<active-project-root>/project_status.md`


用于判断：

当前是否已有项目。

已有信息是否需要保留。

读取`rules/state_source.md`已经选定并验证的来源；本Workflow不得根据路径可见性自行改变选择或初始化新状态。


---

# First Action

收到新项目输入后：

先在当前会话建立最小Project ID、项目基础事实、输入类型、Script Entry Route与STATE-00 Checkpoint；不得先登记项目、创建Project Root、读取Registry、查找同名/相似项目或读取Skill Experience。

用户明确要求保存、登记、归档、跨会话恢复，或当前任务已经指定有效Project Root时，才在不覆盖非空目录的前提下创建或更新持久化项目资料：

- project_manifest.json
- project_bible.md
- asset_registry.md
- project_status.md
- execution_ledger.md
- artifact_registry.md

持久化与否不改变本阶段的事实边界，也不得成为首次剧本交付的等待条件。


三个文件分别负责：

Project Bible：

项目长期视觉与世界观标准。


Asset Registry：

项目视觉资产管理入口。


Project Status：

当前生产阶段与进度控制。

普通Chat或会话内执行时仅保留必要Checkpoint；只有用户要求导出状态、保存项目或恢复项目时，才输出/刷新完整`portable_project_status.md`。不得伪造本机文件已经创建。


---

# Project Initialization


## 01 Project Bible

建立：

项目基础信息入口。


STATE-00只记录：

当前已经明确的信息。


包括：

项目名称。

项目类型。

输入素材类型。

时代背景。

故事世界基础信息。

用户明确提供的视觉方向。


如果用户尚未提供：

不得自行补全详细视觉设定。


例如：

用户没有指定导演风格。

不得自动选择导演风格。


用户没有指定摄影体系。

不得在STATE-00直接建立详细摄影方案。


这些内容：

应在后续Visual Development阶段完成。


---

## 02 Asset Registry

建立：

资产管理入口。


初始化资产类别：

Character。

Environment。

Prop。

FX。


STATE-00只负责：

建立Registry结构。


不得：

正式创建Character Asset。

不得：

正式创建Environment Asset。

不得：

正式创建Prop Asset。


具体需要哪些资产：

由后续：

Script Analysis

↓

Asset Discovery


确定。


---

## 03 Project Status

初始化Selected State Source：先使用当前会话中刚建立的STATE-00状态，并输出或写入portable_project_status.md；Work/Codex在Project ID一致且本地写入可用时，同时把该状态持久化到Project Root中的project_status.md。


当前状态：

```text
STATE-00
Project Initialized
```


当前执行Workflow：

```text
01_project_setup_workflow
```


记录：

项目名称。

项目类型。

当前版本。

创建日期。

当前状态。

已完成任务。

待完成任务。

下一步行动。


下一步行动：

```text
02_script_analysis_workflow.md
```


---

# Project Information Extraction

从用户输入中：

只提取当前能够直接确认的项目级信息。


允许提取：

- 项目名称
- 项目类型
- 输入素材类型
- 用户明确说明的时代背景
- 用户明确说明的主要故事空间
- 用户明确说明的制作目标
- 用户明确说明的视觉参考


例如：

用户提供：

“现代城市雨夜双女主短片。”


STATE-00可以记录：

项目类型：

短片。


时代背景：

现代。


主要空间：

城市。


已知视觉元素：

雨夜。


不得在本阶段继续展开为：

人物关系分析。

完整剧情结构。

正式环境列表。

正式资产需求。

镜头设计。


这些内容：

属于后续Workflow。


---

# Input Material Registration

确认：

用户提供了什么类型的项目素材。


输入类型可以包括：

- Idea / Brief / Concept（尚无可诊断的剧本或来源叙事正文）
- 完整剧本
- 粗略剧本 / 初稿
- 剧情大纲
- 小说章节
- 故事文本
- 人物设定
- 世界观设定
- 品牌需求 / 品牌文案

记录：

输入素材类型。

输入素材名称。

素材完整程度。

Script Entry Route：

- `Creation Brief`：用户要从创意/需求开始写剧本，且没有可供逐段诊断的既有剧本或来源叙事文本。
- `Existing Script / Material`：用户已提供完整剧本、粗略剧本、初稿、小说/故事文本、剧情大纲、品牌文案或其他需要保留/转换的既有内容。

STATE-00只负责识别并登记入口，不在本阶段创作、诊断或改写。`Creation Brief`的Next Workflow仍是`02_script_analysis_workflow.md`，由STATE-01正式执行Screenplay Generation；`Existing Script / Material`由同一Workflow执行Script Diagnosis。若用户同时上传剧本并说“调用sd”，必须优先登记Existing Script route，不得误入从零创作。


如果素材存在明显缺失：

记录：

待确认信息。


禁止：

为了补齐项目资料自行创作剧情。

本禁令只约束STATE-00初始化；不得据此拒绝用户在STATE-01明确请求的剧本创作。


---

# Initial Production Goal

确认：

用户最终希望完成什么。


例如：

- AI短片
- AI电影片段
- AI漫剧
- 系列视频
- 完整影视项目
- 最终Seedance视频制作


用户最终目标：

用于确定整个项目的生产方向。


但：

Final Goal

不等于

Current Workflow。


例如：

用户说：

“调用sd，最后给我Seedance视频提示词。”


当前仍然是：

STATE-00 Project Setup。


不得直接进入：

STATE-08 Clip-based Video Prompt / Video Generation。


---

# Project Writer Foundation｜Internal

STATE-00从用户已明确输入中提取最小Writer Foundation：`Premise / Theme or Thematic Question / Dramatic Question / Genre Promise / Story Engine / Core Conflict`。只记录当前可证实内容与清楚标记的Assumption；不要求用户填写完整WRITER INTENT PACKET，不在STATE-00分析完整人物心理、创建Scene、生成剧本或决定Camera。

该Foundation由`knowledge/screenplay_development.md`拥有，Work/Codex只投影到`project_bible.md`既有Story Foundation / Project Intent区域，普通Chat保留在当前Checkpoint。未知项留给STATE-01，不新增Portable State字段或平行Writer文件。

---

# Project Director Baseline｜Internal

STATE-00除Final Goal、平台、时长和画幅外，必须从用户已明确输入中建立最小`Project Director Baseline`：

- Directorial Thesis：这部作品最终要让观众经历什么变化
- Audience Contract / Intended Viewing Experience：观众被邀请以何种距离、信息位置和情绪预期观看
- Genre Presentation Strategy：如何让观众体验Writer已建立的类型承诺
- Non-negotiable Dramatic Presentation Core：后续呈现、资产和生成都不能丢失的体验、关系可读性或品牌目的

这四项属于`knowledge/director_decision_layer.md`定义的Project-level Director Intent source data。只记录用户直接提供或可明确标为Assumption的内容；未知项保持待后续STATE-01确认。不得在STATE-00据此创作剧情、分析完整人物关系、建立Scene、写Camera Language或预选镜头参数。

Work/Codex把Baseline投影到`project_bible.md`既有Story Foundation / Narrative Style / Emotional Direction / Production Notes区域；普通Chat保留在当前STATE-00 Checkpoint。不得新增Portable State字段或平行Director文件。

---

# Initial Visual Direction

STATE-00只记录：

用户已经明确提供的视觉方向。


例如：

- 真人写实
- 动画
- 水墨
- 现代都市
- 古装
- 科幻
- 雨夜
- 日系青春电影感


如果用户明确提供：

导演参考。

影片参考。

综合色彩。

画面质感。


记录为：

Visual Reference。


本阶段不得：

完成正式Visual Development。


正式视觉开发：

由：

07_visual_development_workflow.md


在STATE-04执行。


---

# Initial Production Analysis Boundary

templates/00_project_start_template.md中存在：

Initial Production Analysis。


该区域在STATE-00只能填写：

当前素材中可以直接确认的项目概览。


可以记录：

Story Overview：

简短项目概述。


Genre：

用户已经明确或素材可以直接确认的类型。


Era：

已经明确的时代背景。


Main Location：

已经明确的主要空间。


Visual Direction：

用户已经明确的初步视觉参考。


禁止：

在这里执行正式Script Analysis。


不得：

为了填写模板而提前完成：

故事结构分析。

人物关系分析。

剧情节点分析。

完整环境分析。


正式分析必须留给：

STATE-01 Script Analysis。


---

# Asset Discovery Preparation Boundary

templates/00_project_start_template.md中存在：

Asset Discovery Preparation。


在STATE-00：

该区域只用于：

准备后续资产分析。


不得：

正式确认资产需求。


不得：

因为模板存在：

CHAR-001

ENV-001

PROP-001


就自动创建资产。


如果资产需求尚未经过：

STATE-01 Script Analysis

和

STATE-02 Asset Discovery


则：

保持为：

待分析。


正式资产编号与资产制作：

由后续Workflow确定。


---

# Project File Initialization


## project_bible.md

初始化：

Project Information。


只写入：

已经确认的项目基础信息。


可以包括：

项目名称。

项目类型。

已知时代。

已知世界基础信息。

用户明确提供的Visual Reference。

已确认或明确标记Assumption的Project Director Baseline；只写入既有项目/故事/制作方向区域，不创建新Schema。


其他尚未确认区域：

保持未确定。


禁止：

在STATE-00完成正式：

Color System。

Lighting Rules。

Camera Language。


这些内容：

由后续Visual Development建立。


---

## asset_registry.md

初始化：

Character。

Environment。

Prop。

FX。


初始状态：

Planning。


不得：

在STATE-00把未经分析的资产标记为：

Approved。

Active。


不得：

根据原始剧本直接完成正式Asset Registry。


---

## project_status.md

填写：

项目名称。

项目类型。

当前版本。

创建日期。


当前状态：

```text
STATE-00
```


状态说明：

```text
Project Initialized
```


当前Workflow：

```text
01_project_setup_workflow
```


Completed Tasks：

```text
Project Setup
```


Pending Tasks至少包括：

```text
Script Analysis
Asset Discovery
Asset Development
Visual Development
Scene Breakdown
Detailed Shot Design
Clip Production
Clip-based Video Prompt / Video Generation
Review
```


Next Action：

```text
02_script_analysis_workflow.md
```

完成上述状态决定后，只按`references/project_state_contract.md`执行字段写回与Portable同步；本Workflow不复制环境分支或同步失败语义。


---

# Output

STATE-00默认无独立用户可见输出。`templates/00_project_start_template.md`只在用户明确要求查看/导出项目启动信息，或持久化操作需要核对时使用。

完成最小启动后，本Workflow在同一响应内进入STATE-01；最终回复使用STATE-01的剧本交付Schema，而不是项目启动页。若存在会实质影响剧本架构或品牌/事实风险的缺失信息，只提出最少必要问题后停止。


---

# Output Content

仅在用户明确要求项目启动资料时，输出Project Information、Input Material、Script Entry Route、持久化状态和Next Workflow。不得把内部Project Director Baseline、Visual Reference推导、Pipeline Lock或状态账本扩写为独立报告。


---

# Output Restriction

STATE-00禁止输出：

- 完整Story Analysis
- Character Analysis
- Character Relationship Analysis
- 正式Environment List
- 正式Visual Element List
- Asset Discovery结果
- Character Asset
- Environment Asset
- Prop Asset
- Scene Breakdown
- Detailed Shot Design
- 镜头列表
- Clip Production Plan
- Video Prompt
- Seedance Prompt


---

# First Response Rule

新影视项目第一次进入SD Film时：

先静默完成项目识别、输入登记、最小项目事实和制作目标；随后在同一轮进入STATE-01。Creation Brief直接交付剧本提案；Existing Script / Material按STATE-01的授权边界交付剧本诊断或剧本提案。

不得因合并首轮而跳过STATE-00、STATE-01的事实边界、Script确认Gate或任一后续STATE；也不得在首轮越级输出资产、分镜表、Clip表或最终视频提示词。


---

# Existing Project Rule

如果project_status.md显示：

项目已经进入STATE-01或之后阶段。


则：

不得重新初始化同一项目。


应该：

继续当前项目。


只有以下情况可以重新进入STATE-00：

用户明确创建新项目。

用户明确要求重新初始化当前项目。

当前输入明确属于另一个独立项目。


禁止：

因为用户再次上传剧本，

自动清空已有项目状态。


---

# No Premature Asset Rule

STATE-00不得：

正式判断所有角色需要制作哪些资产。


不得：

正式判断所有环境需要制作哪些资产。


不得：

正式判断所有道具需要制作哪些资产。


原因：

这些工作依赖：

STATE-01 Script Analysis

↓

STATE-02 Asset Discovery。


STATE-00只能建立：

资产管理入口。


---

# No Premature Visual Development Rule

如果用户已经指定：

王家卫。

岩井俊二。

某部电影。

某种综合色彩。

某种摄影美学。


STATE-00：

可以记录该信息。


但不得：

在当前阶段展开：

焦段体系。

Camera Movement体系。

综合色彩系统。

Lighting System。

Composition System。


这些内容：

属于：

STATE-04 Visual Development。


---

# No Premature Shot Rule

STATE-00不得：

根据用户剧本直接设计镜头。


即使用户说：

“我要最终生成视频。”


当前阶段也不得输出：

景别。

焦段。

运镜。

镜头时间码。

镜头编号。


这些内容：

属于后续生产阶段。


---

# Forbidden Actions

当前阶段禁止：

正式生成角色资产。


禁止：

正式生成环境资产。


禁止：

正式生成道具资产。


禁止：

完成正式视觉开发。


禁止：

进行Scene Breakdown。


禁止：

设计Shot。


禁止：

生成Clip Production Plan、Storyboard视觉材料或视频Prompt。


禁止：

生成Video Prompt。


禁止：

生成Seedance Prompt。


禁止：

根据用户最终目标跳过Pipeline。


禁止：

为了填写模板而虚构当前尚未分析的信息。


---

# Completion Condition

当以下内容完成：

- 项目已经识别
- Project ID已经确定
- 会话Project ID已经确定；如用户明确要求持久化，独立Project Root、project_manifest.json与Registry已按合同初始化/更新
- 输入素材已经登记
- Script Entry Route已经登记；同时存在上传剧本时优先为Existing Script / Material
- 项目基础信息已经记录
- 最终制作目标已经确认
- 最小Project Director Baseline已经建立，或所有未知项已明确留给STATE-01而未虚构
- 已在会话Checkpoint记录最小项目事实；如用户明确要求持久化，project_bible.md、asset_registry.md、project_status.md、execution_ledger.md与artifact_registry.md已按合同初始化
- 当前STATE已经确认
- 下一Workflow已经确定


则：

STATE-00 Project Setup完成。

状态完成后只在用户要求保存、导出或恢复时同步/输出portable_project_status.md；不得因普通Chat无法访问本机Project Root而改走旧Pipeline或停止。输出时必须使用完整Canonical文档。STATE-00初始化时`Script Status: Source Material`。


项目状态记录：

```text
STATE-00
Project Initialized
```


当前Workflow：

```text
01_project_setup_workflow
```


下一步：

```text
02_script_analysis_workflow.md
```


---

# State Transition

STATE-00完成：

不代表：

STATE-01已经完成。


下一步执行：

02_script_analysis_workflow.md


开始STATE-01时：

再进行正式Script Analysis。


默认在同一响应中从STATE-00切入STATE-01；两阶段仍使用各自Workflow与Gate，用户可见内容只呈现STATE-01的剧本交付，不把STATE-00内部账本混入剧本。


---

# Next Workflow

进入：

02_script_analysis_workflow.md


下一阶段负责：

故事结构分析。

人物分析。

环境分析。

重要视觉元素分析。

视觉需求分析。


STATE-01解决：

“这个故事讲什么？”


“有哪些人物、地点和重要视觉元素？”


---

# Core Boundary

Project Setup解决：

“这是什么项目？”


“用户提供了什么？”


“最终生产目标是什么？”


“项目基础文件是否已经建立？”


“当前生产状态是什么？”


Script Analysis解决：

“故事具体讲了什么？”


“故事结构是什么？”


“有哪些人物？”


“有哪些地点？”


“有哪些重要视觉元素？”


Asset Discovery解决：

“哪些内容需要成为正式视觉资产？”


三个阶段：

不得混合。


---

# Final Principle

STATE-00 Project Setup：

是SD Film的项目入口。


它的任务是：

建立项目。

登记输入。

锁定Pipeline。

初始化项目状态。

为Script Analysis准备基础信息。


它不是：

剧本分析阶段。


不是：

资产制作阶段。


不是：

视觉开发阶段。


不是：

镜头设计阶段。


不是：

Prompt生成阶段。


正确流程：

Project Setup

↓

Script Analysis

↓

Asset Discovery

↓

Asset Development

↓

Visual Development

↓

Scene Breakdown

↓

Detailed Shot Design

↓

Clip Production

↓

Clip-based Video Prompt / Video Generation

↓

Review
