# SD Film Project State Contract

## Purpose

本文件定义 `project_status.md` 与 `portable_project_status.md` 共用的持久状态合同，用于状态推进、项目恢复、Review退回和跨任务断点续作。

它不创建新的主STATE，不定义阶段交付Schema，也不替代任何Workflow。

---

## Authority

- 当前项目身份优先来自可访问Active Project Root的`project_manifest.json`与`project_status.md`；Root不可访问时来自有效Portable State中的Project ID；前两者缺失时，可从可读交付物、稳定ID/Revision、Completion Gate证据与用户明确确认中重建。历史聊天中的Skill描述、Pipeline、Workflow规则、模糊口头阶段与仅出现于文本中的路径不构成身份或状态证据。
- 当前生产状态由按`references/project_workspace.md`选择的State Source持有：可访问且Project ID一致的Active Project Root状态优先，其次是`portable_project_status.md`，再次是当前可验证Project Context；第三级必须先规范化为Portable State。只有没有项目证据时才初始化STATE-00。
- Workflow拥有状态转换行为；本合同拥有状态字段及其语义。
- Template拥有阶段交付格式，不拥有项目状态。
- Validator只检查确定性状态不变量。

---

## State Source Authority

每次Workflow开始前都必须重新确认Selected State Source：

```text
可访问且Project ID一致的Active Project Root/project_status.md
>
portable_project_status.md
>
当前可验证的Project Context（先规范化为Portable State）
>
无项目证据时初始化 STATE-00 Project Setup
```

- 当前对话中明确提供的完整Portable文档或附件属于第二级Portable State。第三级当前可验证Project Context不能直接路由；必须先只保留有证据的项目事实、补齐Canonical Portable Schema并记录`Project Context normalized`，然后才作为Portable State使用。
- Work/Codex：可访问且Project ID一致的Active Project Root是状态真源、本地项目文件与交付物的持久化目标。
- 普通Chat：本机Root、Skill安装目录或Registry实际不可读时，直接fallback到Portable State；不得因`C:\Users\Lenovo\Documents\...`不可访问而停止、报错或写入`BLOCKED`。
- 路径只出现在文本中不代表可访问；必须以实际读取是否成功判断。
- Project ID不一致时不自动合并。Work/Codex以Canonical状态刷新Portable；普通Chat无法确认当前项目身份时初始化新的Portable STATE-00。
- Portable模式不授权虚构缺失资产或剧情事实；它只消除本机路径依赖。真正缺少当前Workflow必需输入时仍记录Pending Decision。

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

允许的 `Current State`：`STATE-00` 至 `STATE-09`。

允许的 `State Status`：

- `NOT_STARTED`
- `IN_PROGRESS`
- `BLOCKED`
- `COMPLETE`

`BLOCKED`只表示缺少外部确认、必要输入或上游事实冲突。Review发现可修复问题时保持 `IN_PROGRESS`，通过 `Review Result` 和 `Return Route` 表达返工，不误标为BLOCKED或COMPLETE。

允许的 `Script Status`：

- `Source Material`：用户原始文本、尚未获锁定授权的完整剧本，或仍需分类、改编、优化范围决定的版本。
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

### Portable Schema Non-Invention Gate

普通Chat初始化、恢复或更新Portable State时，必须复制`SKILL.md`的Canonical Minimal Schema或可实际读取的`portable_project_status.md`结构，只替换字段值和区块内容。

禁止：

- 用`READY`、`INITIALIZED`、`PASSED`或`ACTIVE`作为`State Status`。
- 把`Current State`写成`STATE-00 Project Setup`；该字段只写`STATE-00`，阶段全名写入任务与说明。
- 把`Next Workflow`写成自然语言名称；必须写实际Workflow文件名。
- 省略Required Status Header中的任何字段。
- 用`Portable State Metadata`、`Current Session Mode`、`Local Path Compatibility`、`Routing Validation`或其他自创区块替代九个Required Sections。
- 把Portable声明为可以覆盖Work/Codex中可访问Active Project Root的全局权威状态。

如果普通Chat无法读取Skill资源正文，仍必须使用`SKILL.md`内嵌的Canonical Minimal Schema，不能以资源不可访问为理由降级Schema。

收到旧版或自创Portable文本时先执行Schema Migration。只迁移有明确证据的字段，不把路由验证声明当作生产阶段完成证据。`READY / INITIALIZED`且没有完成Workflow证据时规范化为`NOT_STARTED`；自然语言Workflow名称规范化为实际文件名；补齐全部Required Header与Required Sections，并在Version History记录迁移。迁移完成前该文本不得作为Valid State Source。

---

## Persistence And Synchronization

每次进入、完成、退回或恢复Workflow后，都对Selected State Source执行同一套状态写入：

1. 先更新Selected State Source的状态字段、任务、Checkpoint、Active Artifacts、资产锁摘要、Review控制、Revision与Version History。
2. Work/Codex若使用Active Project Root，真实`project_status.md`成功落盘后再同步`portable_project_status.md`。Portable同步失败只写`Portable Sync Status：PENDING`，不得回滚真实状态、报错停止或改变下一Workflow。
3. 普通Chat若使用Portable State，每次状态变化后在回复中输出更新后的完整`portable_project_status.md`，并把`Portable State Availability`设为`READY`、`Portable Sync Status`设为`PORTABLE_ONLY`。
4. Work/Codex重新获得本地访问时，先读取Active Project Root并核对Project ID；身份一致时Root状态优先并刷新Portable。不得静默合并或覆盖不同项目的状态。

### Portable Required Field Writeback

每次写回Portable State都必须同步`Project ID`、`Project Name`、`Current State`、`State Status`、`Script Status`、`Last Successful Checkpoint`、`Completed States`、`Confirmed Assets`、`Next Workflow`、`Last Updated`与`State Source`。`Completed States`只列出已通过Completion Gate的主STATE；进入但未完成的阶段不得加入。

普通Chat写`State Source: portable_project_status.md`；Work/Codex从真实Root同步镜像时写`State Source: <active-project-root>/project_status.md (synced)`。`Last Updated`与现有`Updated At`使用同一时间值，保留后者用于旧状态兼容。

同步只复制路由与恢复所需的状态摘要，不把完整Project Bible、Asset Registry、镜头表、Clip Plan、Prompt或媒体文件嵌入Portable State。

---

## State Transition Protocol

### Canonical Route Label Invariant

所有会参与恢复或路由判断的持久字段与任务列表，包括 `Current State`、`Last Completed Step`、`Next Workflow`、`Completed Tasks`、`Pending Tasks` 和 `Return Route`，必须使用当前主 Pipeline 的标准阶段名称。

固定主路由只能是 `STATE-06 Detailed Shot Design → STATE-07 Clip Production → STATE-08 Clip-based Video Prompt / Video Generation`。`Storyboard` 不得作为编号 STATE、`Pending Tasks` 中的固定阶段或 `Next Workflow`；它只可在用户明确请求时登记为 Optional/Auxiliary Artifact。恢复旧项目时，如 STATE-06 / STATE-08 使用非标准短名、STATE-07 被标成 Storyboard，或待办表仍按 Shot Design、Storyboard、Video Generation 三项连续排列，必须先迁移这些路由标签，再选择 Workflow。

### Runtime Reload Compatibility Mapping

Reload后以最新Pipeline的Artifact与Completion Gate语义映射旧状态，不按旧STATE编号硬复制：

- 保留当前项目、Production-Locked Script、Confirmed Assets / Active Versions / Canonical References、Visual Direction、已完成Checkpoint、已接受Artifact、用户明确约束和未受影响Revision。
- 旧状态把`STATE-07`标注为`Storyboard`，且存在Confirmed Detailed Shot Design但没有Confirmed Clip Production Plan时，映射为当前`STATE-07 Clip Production`与`10_clip_production_workflow.md`。
- 同一旧标注如已有Confirmed Clip Production Plan，映射为`STATE-08 Clip-based Video Prompt / Video Generation`与`11_video_generation_workflow.md`。
- 同一旧标注如Detailed Shot Design尚未通过Completion Gate，映射为`STATE-06 Detailed Shot Design`与`09_shot_design_workflow.md`。
- Storyboard交付物保留为Optional/Auxiliary Artifact，不计入Completed States，不要求重做，也不进入STATE-08参考资产。
- 任何其他旧名称冲突都映射到能消费现有已确认成果的最近当前State / Checkpoint；只迁移路由字段与必要状态摘要，不重写Accepted Unaffected Artifacts。

### Enter Workflow

开始Workflow前：

- `Current State`写入对应STATE。
- `State Status`设为`IN_PROGRESS`。
- `Active Workflow`写入实际文件名。
- `Last Successful Checkpoint`保留上一次已验证步骤。
- `Pending Decision`记录缺失输入；没有则写`None`。
- 按Persistence And Synchronization更新或刷新Portable State。

STATE-01另有硬门槛：`Script Status`必须为`Production-Locked`。`Source Material`、`Adaptation Draft`或`Optimized Proposal`不得写STATE-01 COMPLETE，必须保留`02_script_analysis_workflow.md`为Active / Next Workflow，并在Pending Decision记录需要分类、目标/范围决定、后续优化或用户确认。

### Complete Workflow

只有Completion Gate全部通过后：

- `State Status`设为`COMPLETE`。
- `Last Completed Step`写入完成的Workflow或辅助步骤。
- `Last Successful Checkpoint`写入可安全恢复的位置。
- `Active Artifacts`登记本次产物路径和Revision ID。
- `Next Workflow`写入合法下一步。
- `Revision ID`递增。
- 按Persistence And Synchronization更新或刷新Portable State。

### Not Applicable Auxiliary Workflow

辅助Workflow不适用时：

- 不改变主STATE编号。
- 在Completed Tasks记录`Not Applicable`及理由。
- `Last Successful Checkpoint`记录该判定。

### Review Result

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

Selected State Source不是普通进度摘要，而是项目恢复和状态推进的控制记录。所有环境均按`可访问且Project ID一致的Active Project Root/project_status.md > portable_project_status.md > 当前可验证Project Context（规范化为Portable State） > 无项目证据时初始化STATE-00`选择；Work/Codex以身份一致的Active Project Root为真源，普通Chat不依赖本机路径继续同一主Pipeline。历史聊天中的Skill定义永远不参与状态选择；只有可验证的Project Context事实可在前两级缺失时用于重建Portable State。
