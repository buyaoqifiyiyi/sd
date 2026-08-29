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

- 每次开始Workflow前只按`rules/state_source.md`选择唯一State Source；本文件不维护选择优先级或运行环境fallback规则。
- 每次状态变化后只按`references/project_state_contract.md`写回、同步或输出完整Portable State；本文件不维护字段、顺序或失败语义的竞争副本。
- Project ID不一致时不得合并；具体身份候选解析由`references/project_workspace.md`负责。
