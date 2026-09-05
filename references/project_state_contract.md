# SD Film Project State Contract

## Purpose

本文件定义 `project_status.md` 与 `portable_project_status.md` 共用的持久状态合同，用于状态推进、项目恢复、Review退回和跨任务断点续作。

它不创建新的主STATE，不定义阶段交付Schema，也不替代任何Workflow。

---

## Authority

- Active Project Root的发现与项目身份候选核验由`references/project_workspace.md`拥有；State Source的选择优先级、fallback与运行环境差异只由`rules/state_source.md`拥有。
- Completion Gate与Transition Decision由`rules/completion_gate.md`和当前Workflow拥有；本合同只拥有决定作出后的状态字段、字段语义、Canonical Portable State Schema、Revision与持久化写回。
- Template拥有阶段交付格式，不拥有项目状态。
- Validator只检查确定性状态不变量。

---

## Selected State Source Field Contract

每次Workflow开始前先按`rules/state_source.md`选定唯一State Source。本合同不重新定义其优先级或fallback行为，只验证并保存选择结果：

- `Selected State Source`写实际采用的Root状态路径、`portable_project_status.md`或规范化后的Portable来源。
- `Source Selection Reason`写本次选择依据，不得把仅出现于文本中的路径记为已读取来源。
- `Project ID`必须与被选来源和Active Project身份一致；不一致时不得在本合同层静默合并。
- 从Project Context重建的候选必须先补齐Canonical Portable Schema，只迁移有证据的事实，并在Version History记录`Project Context normalized`。
- Portable模式不授权虚构缺失资产、剧情事实、确认或Completion；真正缺少当前Workflow必需输入时仍记录Pending Decision。

---

## Required Status Header

每个 `project_status.md` 必须包含：

```text
Status Schema Version: 2
Project ID
Project Name
Current State
State Status
Script Status
Active Workflow
Last Completed Step
Last Successful Checkpoint
Next Workflow
Return Route
Pending Decision
Revision ID
Updated At
```

当`Current State`为STATE-07或STATE-08，或已存在Confirmed Clip Production Plan时，还必须在`## State Control`保存唯一的批次内部执行Profile：

```text
- Target Video Model: Seedance 2.0 / Seedance 2.5 / UNLOCKED
- Model Execution Lock Status: UNLOCKED / LOCKED
- Execution Mode: Standard Clip / Long-form Clip / Video Extension / Targeted Edit / Not Applicable
- Effective Gateway Limits: <confirmed gateway limits or UNKNOWN; never infer unsupported API fields>
- Model Lock Scope: <affected CLIP IDs / current generation batch>
```

`UNLOCKED`只允许在STATE-06完成后、STATE-07 Clip整合前短暂存在；不得确认Clip Plan。锁定选择仅控制当前生成批次的执行Profile，不改变Production-Locked Script、Confirmed Assets、Scene Breakdown或Detailed Shot Design。Clip Plan确认前用户切换模型时，只将受影响STATE-07/08执行产物标为需重跑，保留上述上游Accepted Artifacts。

允许的 `Current State`：`STATE-00` 至 `STATE-09`。

允许的 `State Status`：

- `NOT_STARTED`
- `IN_PROGRESS`
- `BLOCKED`
- `COMPLETE`

`BLOCKED`只表示缺少外部确认、必要输入或上游事实冲突。Review发现可修复问题时保持 `IN_PROGRESS`，通过 `Review Result` 和 `Return Route` 表达返工，不误标为BLOCKED或COMPLETE。

允许的 `Script Status`：

- `Source Material`：尚待STATE-01生成Proposal的Idea / Brief / Concept、用户原始文本、尚未获锁定授权的完整剧本，或仍需分类、改编、优化范围决定的版本。
- `Adaptation Draft`：C类Source Material已经完成通用改编与Fidelity Check、但仍需Screenwriting Optimization和Directorial Interpretation的改编稿；不得进入STATE-02。
- `Optimized Proposal`：已经完成编剧优化与导演化处理、正在等待用户确认或局部修订的制作版剧本提案。
- `Production-Locked`：用户明确要求原版定稿制作，或用户已经确认Production Script Proposal；只有该值允许STATE-01完成并进入STATE-02。

旧状态缺少`Script Status`时按证据迁移：STATE-01之前或没有剧本确认依据写`Source Material`；存在已完成Adaptation Draft但尚未完成优化的明确Artifact证据写`Adaptation Draft`；存在等待确认的Production Script Proposal写`Optimized Proposal`；已经有STATE-01 Completion Gate证据或Current State为STATE-02及之后写`Production-Locked`。旧值`Draft`规范化为`Source Material`。不得仅凭历史聊天摘要推定锁定。

---

## Required Sections

```text
## State Control
## Completed Tasks
## Pending Tasks
## Active Artifacts
## Confirmed Assets
## Visual Direction Lock
## Continuity And Open Risks
## Review Control
## Version History
```

无内容的栏目必须写 `None`、`Not Applicable` 或明确待确认原因，不得删除栏目。

`portable_project_status.md`还必须包含：

```text
State Routing Contract Version
Portable State Availability
State Source Mode
Canonical Project Root
Portable Snapshot Of
Portable Sync Status
Selected State Source
Source Selection Reason
Completed States
State Source
Last Updated
```

Portable State Availability允许`EMPTY`或`READY`；Portable Sync Status允许`SYNCED`、`PORTABLE_ONLY`或`PENDING`。

### Canonical Portable State Schema

本节是Portable State字段、顺序与标准区块的唯一规范来源。`portable_project_status.md`是可读写的Canonical基线实例；`SKILL.md`、Rules、Workflow和Validator只能引用本节，不得复制或发明竞争Schema。

普通Chat无法读取`portable_project_status.md`正文时，也必须使用下列Canonical Minimal Schema，只替换字段值和区块内容：

```text
# SD Film Portable Project Status

State Routing Contract Version: 1
Portable State Availability: READY
State Source Mode: PORTABLE
Canonical Project Root: UNAVAILABLE
Portable Snapshot Of: <Project ID or NEW PROJECT / UNASSIGNED>
Portable Sync Status: PORTABLE_ONLY

- Status Schema Version: 2
- Project ID: <PROJECT-...>
- Project Name: <name or 未命名项目>
- Current State: STATE-00
- State Status: NOT_STARTED
- Script Status: Source Material
- Completed States: None
- State Source: portable_project_status.md
- Active Workflow: 01_project_setup_workflow.md
- Last Completed Step: None
- Last Successful Checkpoint: Portable State Initialized
- Next Workflow: 01_project_setup_workflow.md
- Return Route: None
- Pending Decision: <required input or None>
- Revision ID: REV-0000
- Last Updated: <current timestamp>
- Updated At: <current timestamp>

## State Control
- Selected State Source: portable_project_status.md
- Source Selection Reason: Active Project Root unavailable
- Portable State Availability: READY
- Portable Sync Status: PORTABLE_ONLY

## Completed Tasks
None

## Pending Tasks
- STATE-00 Project Setup
- STATE-01 Script Analysis
- STATE-02 Asset Discovery
- STATE-03 Asset Development
- STATE-04 Visual Development
- STATE-05 Scene Breakdown
- STATE-06 Detailed Shot Design
- STATE-07 Clip Production
- STATE-08 Clip-based Video Prompt / Video Generation
- STATE-09 Review

## Active Artifacts
None

## Confirmed Assets
None

## Visual Direction Lock
None

## Continuity And Open Risks
- Active Project Root unavailable; Work/Codex must re-resolve the Canonical State before writing.

## Review Control
- Review Result: NOT_REVIEWED
- Affected IDs: None
- Return Route: None
- Recheck Scope: None
- Review Artifact: None

## Version History
- REV-0000: Portable State initialized; no production Workflow completed.
```

普通Chat初始化、恢复或更新Portable State时，必须复制本节或可实际读取的`portable_project_status.md`结构，只替换字段值和区块内容。

禁止：

- 用`READY`、`INITIALIZED`、`PASSED`或`ACTIVE`作为`State Status`。
- 把`Current State`写成`STATE-00 Project Setup`；该字段只写`STATE-00`，阶段全名写入任务与说明。
- 把`Next Workflow`写成自然语言名称；必须写实际Workflow文件名。
- 省略Required Status Header中的任何字段。
- 用`Portable State Metadata`、`Current Session Mode`、`Local Path Compatibility`、`Routing Validation`或其他自创区块替代九个Required Sections。
- 把Portable声明为可以覆盖Work/Codex中可访问Active Project Root的全局权威状态。

如果普通Chat无法读取Skill资源正文，仍必须使用本合同中的Canonical Minimal Schema，不能以资源不可访问为理由降级Schema。

收到旧版或自创Portable文本时先执行Schema Migration。只迁移有明确证据的字段，不把路由验证声明当作生产阶段完成证据。`READY / INITIALIZED`且没有完成Workflow证据时规范化为`NOT_STARTED`；自然语言Workflow名称规范化为实际文件名；补齐全部Required Header与Required Sections，并在Version History记录迁移。迁移完成前该文本不得作为Valid State Source。

---

## Persistence And Synchronization

每次进入、完成、退回或恢复Workflow后，都对Selected State Source执行同一套状态写入：

1. 先更新Selected State Source的状态字段、任务、Checkpoint、Active Artifacts、资产锁摘要、Review控制、Revision与Version History。
2. Work/Codex若使用Active Project Root，真实`project_status.md`成功落盘后再同步`portable_project_status.md`。Portable同步失败只写`Portable Sync Status：PENDING`，不得回滚真实状态、报错停止或改变下一Workflow。
3. 普通Chat若使用Portable State，每次状态变化后在内部更新完整`portable_project_status.md`，并把`Portable State Availability`设为`READY`、`Portable Sync Status`设为`PORTABLE_ONLY`；仅在用户明确要求保存、导出、恢复核对或查看项目状态时输出该完整文档。
4. Work/Codex重新获得本地访问时，重新调用`rules/state_source.md`；如果它选中身份一致的Active Project Root，再以Root状态刷新Portable。不得静默合并或覆盖不同项目的状态。

### Portable Required Field Writeback

每次写回Portable State都必须同步`Project ID`、`Project Name`、`Current State`、`State Status`、`Script Status`、`Last Successful Checkpoint`、`Completed States`、`Confirmed Assets`、`Next Workflow`、`Last Updated`与`State Source`。`Completed States`只列出已通过Completion Gate的主STATE；进入但未完成的阶段不得加入。

普通Chat写`State Source: portable_project_status.md`；Work/Codex从真实Root同步镜像时写`State Source: <active-project-root>/project_status.md (synced)`。`Last Updated`与现有`Updated At`使用同一时间值，保留后者用于旧状态兼容。

同步只复制路由与恢复所需的状态摘要，不把完整Project Bible、Asset Registry、镜头表、Clip Plan、Prompt或媒体文件嵌入Portable State。

---

## State Mutation And Writeback Protocol

`rules/completion_gate.md`与当前Workflow先作出`ENTER`、`COMPLETE`、`AUXILIARY_NOT_APPLICABLE`、`REVIEW_RETURN`或`REVIEW_PASS`决定。本合同不重新判断是否满足Completion Gate，只把已获准决定确定性地投影到状态字段并持久化。

### Canonical Route Label Invariant

所有会参与恢复或路由判断的持久字段与任务列表，包括 `Current State`、`Last Completed Step`、`Next Workflow`、`Completed Tasks`、`Pending Tasks` 和 `Return Route`，必须使用当前主 Pipeline 的标准阶段名称。

固定主路由只能是 `STATE-06 Detailed Shot Design → STATE-07 Clip Production → STATE-08 Clip-based Video Prompt / Video Generation`。`Storyboard` 不得作为编号 STATE、`Pending Tasks` 中的固定阶段或 `Next Workflow`；它只可在用户明确请求时登记为 Optional/Auxiliary Artifact。恢复旧项目时，如 STATE-06 / STATE-08 使用非标准短名、STATE-07 被标成 Storyboard，或待办表仍按 Shot Design、Storyboard、Video Generation 三项连续排列，必须先迁移这些路由标签，再选择 Workflow。

### Runtime Reload Compatibility Mapping

旧State、旧Storyboard路由和旧Portable Schema的迁移行为统一由`rules/compatibility_mapping.md`拥有。本合同只要求迁移后的字段符合Canonical Route Label Invariant与Canonical Portable State Schema，并在Version History保存迁移证据；不得重写Accepted Unaffected Artifacts。

### Apply ENTER Decision

收到合法`ENTER`决定后：

- `Current State`写入对应STATE。
- `State Status`设为`IN_PROGRESS`。
- `Active Workflow`写入实际文件名。
- `Last Successful Checkpoint`保留上一次已验证步骤。
- `Pending Decision`记录缺失输入；没有则写`None`。
- 按Persistence And Synchronization更新或刷新Portable State。

STATE-01另有硬门槛：`Script Status`必须为`Production-Locked`。`Source Material`、`Adaptation Draft`或`Optimized Proposal`不得写STATE-01 COMPLETE，必须保留`02_script_analysis_workflow.md`为Active / Next Workflow，并在Pending Decision记录需要Screenplay Development、分类、目标/范围决定、后续优化或用户确认。

### Apply COMPLETE Decision

只有上游已作出合法`COMPLETE`决定后：

- `State Status`设为`COMPLETE`。
- `Last Completed Step`写入完成的Workflow或辅助步骤。
- `Last Successful Checkpoint`写入可安全恢复的位置。
- `Active Artifacts`登记本次产物路径和Revision ID。
- `Next Workflow`写入合法下一步。
- `Revision ID`递增。
- 按Persistence And Synchronization更新或刷新Portable State。

### Apply AUXILIARY_NOT_APPLICABLE Decision

收到合法`AUXILIARY_NOT_APPLICABLE`决定后：

- 不改变主STATE编号。
- 在Completed Tasks记录`Not Applicable`及理由。
- `Last Successful Checkpoint`记录该判定。

### Apply REVIEW_RETURN / REVIEW_PASS Decision

STATE-09必须额外记录：

```text
Review Result: PASS / REVISE / REBUILD / NOT_REVIEWED
Affected IDs
Return Route
Recheck Scope
Review Artifact
```

- `PASS`：允许 `STATE-09 + COMPLETE`。
- `REVISE`：保持 `STATE-09 + IN_PROGRESS`，Return Route指向最小修复Workflow。
- `REBUILD`：保持 `STATE-09 + IN_PROGRESS`，Return Route指向事实或设计拥有者。
- 未实际查看生成结果不得写`PASS`。

修复Workflow开始后可以临时把Current State切换到返回STATE，但必须记录 `Return After Completion: STATE-09 Review`。修复完成后重新进入STATE-09，不得直接完成项目。

---

## Checkpoint Rule

Checkpoint必须是已完成、已落盘、可重复读取且通过对应确定性检查的步骤。

不得把以下内容记录为成功Checkpoint：

- 仅存在于对话、尚未保存的分析
- 未通过Completion Gate的阶段
- REVISE或REBUILD后尚未修复的结果
- 引用不存在或版本不匹配的资产/交付物

项目恢复必须从 `Last Successful Checkpoint` 之后继续，不重写该Checkpoint之前已接受的内容。

---

## Revision Rule

Revision ID格式：`REV-0001`、`REV-0002`……。

每次以下变化必须创建新Revision：

- STATE完成
- Review结果变化
- 已确认资产Active Version变化
- Detailed Shot Design / Clip Production Plan / STATE-08 Prompt发生实质修改
- Return Route完成并重新进入Review

仅排版修正可以沿用当前Revision，但必须在Version History记录。

---

## Validation Invariants

- Project ID与Manifest、Bible、Registry一致。
- Current State合法，State Status合法。
- Script Status只能为Source Material、Adaptation Draft、Optimized Proposal或Production-Locked；STATE-01 COMPLETE及STATE-02之后必须为Production-Locked。
- `COMPLETE`状态必须有Last Completed Step、Checkpoint和Next Workflow；STATE-09 PASS可将Next Workflow写为`Project Complete / Post`。
- `IN_PROGRESS`必须有Active Workflow。
- `BLOCKED`必须有Pending Decision。
- Review Result为REVISE或REBUILD时，不得标记STATE-09 COMPLETE。
- Active Artifact路径必须位于Active Project Root内或是明确登记的外部只读源。
- Revision ID格式正确且Version History存在对应记录。

---

## Final Principle

Selected State Source不是普通进度摘要，而是项目恢复和状态推进的控制记录。其选择与运行时行为统一服从`rules/state_source.md`；本合同只保存已验证选择、Canonical状态字段和写回结果。历史聊天中的Skill定义永远不参与状态选择；只有按State Source Rule验证并规范化的项目事实才能进入持久状态。
