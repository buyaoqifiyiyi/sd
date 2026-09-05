# Pipeline Rules

# AI影视生产流程规则


## Purpose


本规则用于约束SD Film整体制作流程。


确保所有影视项目按照：

项目初始化

↓

剧本分析

↓

资产准备

↓

视觉开发

↓

场景设计

↓

详细镜头设计

↓

Clip Production

↓

视频生成


的顺序执行。



---

# Rule 00

# Project Isolation

执行任何Workflow前，先由`references/project_workspace.md`解析项目身份候选，再严格按`rules/state_source.md`选择唯一State Source。本规则不复制其优先级或运行时fallback细节。

所有未限定路径的：

- project_status.md
- project_bible.md
- asset_registry.md

在Work/Codex本地模式中均指向Active Project Root中的项目文件。普通Chat无法实际读取本机Root时，project_status.md指向当前任务最新可用的portable_project_status.md。

禁止：

把完整项目状态或交付物写入Skill安装根目录中的兼容入口。portable_project_status.md只允许保存最小状态镜像。

禁止：

因为另一个项目最近被使用，就自动把它当作当前项目。

当前输入命中`rules/runtime_reload.md`的Trigger时，必须先完成该规则定义的重载与状态报告，再解析项目或Workflow。本规则不维护重载词、读取顺序或Reload Status的竞争副本。

普通Chat不是简化模式，必须完整执行STATE-00至STATE-09。状态来源与本机资源不可用时的行为统一服从`rules/state_source.md`与`rules/chat_compatibility.md`；历史聊天中的Skill规则、Pipeline或Workflow描述不得作为状态源。

如果可访问项目身份无法唯一确认：

停止状态推进并确认项目，不得合并或覆盖。


---

# Rule 01

# Pipeline Order


所有AI影视项目必须按照既定Workflow顺序执行。


禁止：

跳过前置阶段直接进入后续阶段。



标准流程：


STATE-00 Project Setup

↓

STATE-01 Script Analysis

↓

STATE-02 Asset Discovery

↓

STATE-03 Asset Development

↓

STATE-04 Visual Development

↓

STATE-05 Scene Breakdown

↓

STATE-06 Detailed Shot Design

↓

STATE-07 Clip Production

↓

STATE-08 Clip-based Video Prompt / Video Generation

↓

STATE-09 Review



---

# Rule 02

# New Project Entry


当用户输入：

- 剧本
- 小说
- 故事大纲
- 剧情文本


默认视为新项目。


必须首先进入：


STATE-00 Project Setup



禁止直接执行：


- Shot Design
- Clip Production Plan
- Video Generation



---

# Rule 03

# First Output Restriction


新项目第一次响应时：


只能执行：


- 项目确认
- 项目初始化
- 输入分析准备



禁止输出：


- 分镜表
- Clip Production Plan
- 镜头列表
- 视频Prompt
- Seedance Prompt



---

# Rule 04

# Product Request Interception Rule


当用户直接请求某个后期制作产物时：

例如：


- 生成视频提示词
- 生成Seedance提示词
- 生成AI视频Prompt
- 请求Storyboard（仅显式请求时调用Optional/Auxiliary Storyboard Workflow）
- 生成分镜表
- 生成镜头设计



系统必须首先检查当前项目状态。



用户请求的目标产物：

只代表最终目标。


不代表：

当前可以立即执行的阶段。



---

## Stage Check


执行任何后期产物生成前：

必须确认对应前置阶段已经完成。



例如：


### 用户请求视频Prompt


必须确认：


已完成：

- Project Setup
- Script Analysis
- Asset Discovery
- Asset Development
- Visual Development
- Scene Breakdown
- Shot Design



否则：

禁止生成视频Prompt。



---

### 用户请求Storyboard


必须确认：


已完成：

- Scene Breakdown
- Shot Design



否则：

禁止生成Storyboard。

前置阶段完成后，只有用户明确请求时才调用`workflows/10_storyboard_workflow.md`。Storyboard不绑定STATE、不参与Clip划分、不改变Next Workflow，并且不得作为STATE-08视觉参考。



---

### 用户请求Shot Design


必须确认：


已完成：

- Scene Breakdown
- Asset准备



否则：

返回前置阶段。



---

# Rule 05

# Asset Priority


影视视觉制作必须遵循：

资产优先原则。



顺序：


角色资产

↓

环境资产

↓

道具资产

↓

场景设计

↓

镜头设计

↓

视频生成



禁止：

未完成必要资产确认前，

直接进入镜头制作。



---

# Rule 06

# Screenplay Development And Script Analysis Boundary


STATE-01剧本开发与分析阶段负责：


- 故事理解
- 人物分析
- 环境识别
- 视觉元素发现
- 先识别`Creation Brief / Existing Script / Material`两条互斥入口
- 对Creation Brief执行`Idea / Brief → Director-first Screenplay Development → Directorial Interpretation → Directable Screenplay QA → Production Script Proposal → User Confirmation`；用户要求创作本身已授权生成Proposal，不要求先在Skill外提供剧本
- 对Existing Script / Material在任何内容改写前执行`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`
- 对C类小说、故事梗概、品牌文案、历史事件、影视桥段或长篇素材先报告Adaptation Need，只有用户明确授权后才执行STATE-01内部Script Adaptation
- 对B类粗略剧本/初稿先报告轻度/结构优化空间，只有用户明确授权后才执行优化，且不强制改编
- 只在短剧、竖屏剧情或1—3分钟剧情视频目标下加载Short-form Drama Adapter
- 在用户确认后锁定唯一制作版剧本



不负责：


- 角色设计
- 环境设计
- 道具设计
- 镜头设计


Script Optimization Gate硬规则：

- Creation Brief不输出Optimization Opportunity Report，也不询问“是否允许写剧本”；只在真正缺失会改变架构或造成品牌/事实风险的关键信息时最小澄清。原创Proposal必须经过Scene Director Intent与十项Directable Screenplay QA，但最终剧本不得变成分析表或提前写好的分镜表。
- Optimization Opportunity Report只指出问题、影响与可优化方向，不得直接重写剧本正文；至少检查开场钩子、核心冲突进入时机、信息重复、台词效率、动作可视化、人物记忆点、节奏、高潮力度、情绪价值、结尾Hook、时长适配、场景/人物复杂度。
- 报告只使用A无明显优化必要、B有轻度优化空间、C有明显结构问题三档，并分别询问直接锁定、轻度优化或结构优化。
- Existing Script / Material只有在用户明确表示“优化 / 分析并优化 / 继续优化 / 进入优化 / 直接优化 / 直接改写”或无歧义同义授权后，才执行Script Adaptation、编剧优化、导演化处理或Production Script Proposal；授权可在初始请求中给出，已明确时不得在报告后重复确认。单独“继续 / 下一步 / 好的”不构成授权。
- C类获准路径必须完成`Script Adaptation → Adaptation Draft → 编剧优化 → 导演化处理 → Production Script Proposal → 用户确认`。
- A/B类获准路径只完成`编剧优化 → 导演化处理 → Production Script Proposal → 用户确认`，不得强制改编。
- 用户拒绝优化/改编时，不改一字，原版本完成Script Analysis后直接Production-Lock并进入STATE-02。
- Production Script Proposal输出后必须再次等待用户明确确认，确认前不得Production-Lock或进入STATE-02。
- Adaptation Intensity只使用LEVEL 1 / LEVEL 2 / LEVEL 3，并选择最低足够等级；用户明确“基本不要改剧情”时只能LEVEL 1。
- `Script Status: Adaptation Draft`时STATE-01保持IN_PROGRESS，不得进入STATE-02。
- `Script Status: Optimized Proposal`时STATE-01保持IN_PROGRESS，不得进入STATE-02。
- 局部优化只能修改用户指定范围。
- 不得擅自修改世界观、角色身份、核心创意、关键设定或品牌要求。
- 用户明确“不要改剧本 / 严格按这个版本制作 / 已定稿”时跳过Optimization Opportunity Report与内容改写，只做原有Script Analysis并按授权锁定。
- 剧本阶段只决定事件、行动、信息、关系、表演机会、空间潜力与节奏；不得机械写入35mm、特写、推镜、摇镜、机位、SHOT、CLIP或正式分镜表，Camera继续由STATE-06具体化。



---

# Rule 07

# Asset Development Boundary


资产制作阶段负责：


- 创建资产
- 完善视觉信息
- 建立参考规范



不负责：


- 场景拆解
- 镜头设计
- Clip Production
- 视频Prompt生成



---

# Rule 08

# Shot Design Entry


进入Shot Design前：

必须存在：

- STATE-05 Scene Breakdown Complete
- Confirmed Scene Breakdown Artifact
- Sequence Plan，或已登记的Sequence Planning Not Applicable理由
- 已确认角色资产
- 已确认环境资产
- 已确认必要道具资产
- 项目需要的正式FX资产，或明确Not Applicable

用户原剧本中的“镜头1 / 镜头2 / Scene 1 / 段落A / Clip A”只属于Source Script Labels，不得视为正式SCENE、SHOT或CLIP，也不得作为STATE-05完成证据。



否则：

返回资产阶段。



---

# Rule 09

# Clip Production Boundary


Clip Production只能基于：

- 实际可读且Status为Confirmed的Detailed Shot Design Artifact
- 与该Artifact匹配的Source Detailed Shot Design Revision
- STATE-06 Complete状态证据
- 从SHOT-001开始、按原顺序完整列出的正式SHOT清单



Clip Production用于：


- 按原顺序记录每个Clip包含的正式Shot
- 确认起始状态、连续动作、摄影机/空间关系、道具连续性与结尾状态
- 根据场景、时间、动作、摄影机、模型复杂度与Model Execution Lock后的模型窗口划分生成单元：2.0为4—15秒；2.5为4—30秒，16—30秒须严格预检PASS，实际秒数由用户选择



禁止：

Clip Production替代Detailed Shot Design、改写正式Shot或引用Storyboard视觉材料。

禁止在上述四项证据不完整时创建Draft、Provisional、Tentative、占位或正式CLIP ID。禁止把Source Script Label、SCENE、BEAT、COV或UNIT直接改名或一对一映射为CLIP。



---

# Rule 10

# Video Generation Boundary


Video Generation只能使用：


- Confirmed Detailed Shot Design
- 已确认资产
- Confirmed Clip Production Plan

视频参考资产禁止包含Storyboard图片、分镜板、拼图、多画面材料、Scene Top-down Blocking Map或Detailed Shot Design / Clip Plan截图。唯一受限例外是STATE-08 Before-Single-Clip-Prompt Gate判定REQUIRED、通过Sketch Validation并绑定当前Clip / Blocking Signature的Confirmed `REF-SKETCH`；它不得反向成为Storyboard、Canonical Asset或新主阶段。



禁止：

直接根据剧本生成视频。



---

# Rule 11

# Workflow Responsibility


每个Workflow只负责自身阶段。


禁止：


后续Workflow重复执行前置任务。


禁止：

通过Prompt绕过流程。



---

# Rule 12

# Project Status Update


每完成一个阶段：


必须更新：


按优先级选定的State Source

并严格服从：

references/project_state_contract.md



记录：


当前状态。

State Status。

Script Status。

Active Workflow。

Last Successful Checkpoint。

Active Artifacts与Revision ID。

Portable State还必须同步Script Status、Completed States、Confirmed Assets、Last Updated与State Source。


完成内容。


下一阶段。

只有Completion Gate通过后才允许写COMPLETE。

状态保存只服从`references/project_state_contract.md`的Persistence And Synchronization；本Pipeline Rule不复制Root / Portable顺序、字段或失败语义。

普通Chat输出的完整Portable副本必须逐字段服从`references/project_state_contract.md`的Canonical Portable State Schema。禁止自创Portable Schema；`READY`和`INITIALIZED`不得作为State Status，Next Workflow必须使用实际文件名。

STATE-09只有Review Result为PASS时才允许写STATE-09 Complete；REVISE或REBUILD必须记录Return Route并保持Review闭环未完成。



---

# Final Principle


SD Film不是：

剧本 → Prompt → 视频


的快速生成工具。


而是：


剧本

↓

分析

↓

资产

↓

场景

↓

详细镜头

↓

Clip Production

↓

视频


的AI影视生产流程系统。


用户指定结果：

不能覆盖生产流程。
