# SD Film Portable Project Status

本文件是普通 Chat 与 Work/Codex 之间的最小可移植状态镜像。它不保存完整项目资产或阶段交付物，也不替代可访问的 Active Project Root。

State Routing Contract Version：1
Portable State Availability：EMPTY
State Source Mode：PORTABLE
Canonical Project Root：UNAVAILABLE
Portable Snapshot Of：NEW PROJECT / UNASSIGNED
Portable Sync Status：PORTABLE_ONLY

- Status Schema Version：2
- Project ID：PROJECT-PORTABLE-UNASSIGNED
- Project Name：未命名项目
- Current State：STATE-00
- State Status：NOT_STARTED
- Script Status：Source Material
- Completed States：None
- State Source：portable_project_status.md
- Active Workflow：01_project_setup_workflow.md
- Last Completed Step：None
- Last Successful Checkpoint：None
- Next Workflow：01_project_setup_workflow.md
- Return Route：None
- Pending Decision：等待项目输入
- Revision ID：REV-0000
- Last Updated：Not Initialized
- Updated At：Not Initialized

## State Control

- Selected State Source：portable_project_status.md
- Source Selection Reason：Active Project Root不可访问或尚未建立
- Portable State Availability：EMPTY
- Portable Sync Status：PORTABLE_ONLY

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

- Active Project Root尚不可用；恢复到Work/Codex后按Project ID核对，不自动合并不同项目。

## Review Control

- Review Result：NOT_REVIEWED
- Affected IDs：None
- Return Route：None
- Recheck Scope：None
- Review Artifact：None

## Version History

- REV-0000：Portable State bootstrap；尚未建立项目。

## Portable Update Rule

- 每次开始 Workflow 前先读取可访问且Project ID一致的Active Project Root/project_status.md；Root不可访问时读取当前任务最新可用的本文件内容。本机绝对路径不可访问不是错误。
- 普通 Chat 每次状态推进或保存后，必须在回复中给出更新后的完整 Portable State，供下一轮继续。
- Work/Codex 成功更新 Active Project Root 的 `project_status.md` 后，同步本文件的状态字段、任务、Checkpoint、Artifact摘要、资产锁、Review控制与Revision；同步失败只记录 `Portable Sync Status：PENDING`，不得回滚真实项目状态或中断主 Pipeline。
- 所有环境均按“可访问且Project ID一致的Active Project Root/project_status.md → 本文件 → 初始化STATE-00”选择State Source。当前对话中明确提供的完整Portable文档或附件仍属于本文件这一层；历史聊天文本、聊天摘要与口头阶段描述不是状态源。
- 项目ID不一致时不得合并。Work/Codex用真实项目状态刷新本文件；普通 Chat 无法确认身份时初始化新的 Portable STATE-00。
