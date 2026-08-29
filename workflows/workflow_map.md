# SD Film Workflow Map

## Purpose

本文件只负责主Pipeline、STATE关系、Workflow / Template路由和辅助流程边界。它不拥有阶段算法、资源门槛、Completion Checklist或最终输出Schema。

执行时：

1. 命中Runtime Reload Trigger时，先完整执行`rules/runtime_reload.md`。
2. 按`references/project_workspace.md`解析项目候选。
3. 按`rules/state_source.md`选择唯一State Source，并由`references/project_state_contract.md`验证与写回状态。
4. 读取当前Workflow全文及其Required / Applicable / Conditional Resources。
5. 最终字段、顺序与排版只服从当前Template。

## Core Production Pipeline

固定主Pipeline：

```text
STATE-00 Project Setup
→ STATE-01 Script Analysis
→ STATE-02 Asset Discovery
→ STATE-03 Asset Development
→ STATE-04 Visual Development
→ STATE-05 Scene Breakdown
→ STATE-06 Detailed Shot Design
→ STATE-07 Clip Production
→ STATE-08 Clip-based Video Prompt / Video Generation
→ STATE-09 Review
```

Editing不作为独立STATE插入主Pipeline。Storyboard只在用户显式请求时作为Optional/Auxiliary Workflow执行，不创建STATE，也不改变固定路由。

## Main Workflow Routing

| STATE | Stage | Workflow | Final template owner | Core result |
|---|---|---|---|---|
| STATE-00 | Project Setup | `workflows/01_project_setup_workflow.md` | `templates/00_project_start_template.md` | 已建立项目身份、工作空间与状态入口 |
| STATE-01 | Script Analysis | `workflows/02_script_analysis_workflow.md` | `templates/02_script_analysis_prompt.md` | Production-Locked Script及分析结果 |
| STATE-02 | Asset Discovery | `workflows/03_asset_discovery_workflow.md` | `templates/03_asset_discovery_prompt.md` | 已分类并可路由的CHAR / ENV / PROP / FX需求 |
| STATE-03 | Asset Development | 对应资产Workflow | 对应资产Template | 已确认并登记的Canonical视觉资产 |
| STATE-04 | Visual Development | `workflows/07_visual_development_workflow.md` | `templates/01_project_bible_template.md` | 已确认的可执行Visual Direction |
| STATE-05 | Scene Breakdown | `workflows/08_scene_breakdown_workflow.md` | `templates/07_scene_design_prompt.md` | Scene / Sequence / Unit生产拆解 |
| STATE-06 | Detailed Shot Design | `workflows/09_shot_design_workflow.md` | `templates/08_shot_design_prompt.md` | Confirmed Professional Detailed Shot Script |
| STATE-07 | Clip Production | `workflows/10_clip_production_workflow.md` | `templates/20_clip_plan.md` | Confirmed Clip Production Plan |
| STATE-08 | Clip-based Video Prompt / Video Generation | `workflows/11_video_generation_workflow.md` | `templates/10_video_prompt.md` | 按Confirmed Clip编译并验证的最终视频执行Prompt |
| STATE-09 | Review | `workflows/13_review_workflow.md` | `templates/16_review_report.md` | PASS或带最小Return Route的REVISE / REBUILD |

## STATE Route Boundaries

### STATE-00 Project Setup

- Required boundary：新项目、无法验证的项目上下文，或State Source合法指向STATE-00。
- Authority：`workflows/01_project_setup_workflow.md`。
- Next route：仅在其Completion Checklist通过后进入`workflows/02_script_analysis_workflow.md`。

### STATE-01 Script Analysis

- Required boundary：读取项目输入和当前Script Status。
- Authority：`workflows/02_script_analysis_workflow.md`；剧本改编、优化、授权与锁定细则不得在本地图复制。
- Completion boundary：只有`Script Status: Production-Locked`才可进入STATE-02。

### STATE-02 Asset Discovery

- Required boundary：消费Production-Locked Script与STATE-01分析结果。
- Authority：`workflows/03_asset_discovery_workflow.md`与`rules/02_asset_rules.md`；资产分级算法和Board规则不得在本地图复制。
- Next route：按已确认需求进入对应STATE-03资产Workflow。

### STATE-03 Asset Development

| Asset route | Workflow | Template |
|---|---|---|
| Character | `workflows/04_character_asset_workflow.md` | `templates/04_character_asset_prompt.md` |
| Environment | `workflows/05_environment_asset_workflow.md` | `templates/05_environment_asset_prompt.md` |
| Prop | `workflows/06_prop_asset_workflow.md` | `templates/06_prop_asset_prompt.md` |
| Formal FX（条件） | `workflows/15_fx_asset_workflow.md` | `templates/13_fx_asset_prompt.md` |

- Authority：资产生产Gate、确认闭环、Active Version和Canonical Reference由对应Workflow、`rules/02_asset_rules.md`与`references/asset_lock_contract.md`定义。
- Completion boundary：当前项目所需资产全部通过对应Completion Checklist，或对应类别已合法记录Not Applicable。

### STATE-04 Visual Development

- Required boundary：消费Production-Locked Script、已确认资产和用户视觉要求。
- Authority：`workflows/07_visual_development_workflow.md`。
- Next route：完成可执行Visual Direction后进入STATE-05。

### STATE-05 Scene Breakdown

- Required boundary：消费已锁剧本、Visual Direction与Confirmed Assets。
- Authority：`workflows/08_scene_breakdown_workflow.md`；本阶段不创建正式SHOT或CLIP ID。
- Conditional route：满足条件时调用`workflows/16_sequence_planning_workflow.md`；不适用时按其合同记录Not Applicable。
- Next route：完成Scene / Sequence / Unit拆解后进入STATE-06。

### STATE-06 Detailed Shot Design

- Required boundary：消费Scene Breakdown、适用的Sequence Plan、Visual Direction与Confirmed Assets。
- Authority：`workflows/09_shot_design_workflow.md`；Spatial Blocking、Camera Language、Director Decision与逐镜完整性细则不得在本地图复制。
- Output owner：`templates/08_shot_design_prompt.md`。
- Next route：Confirmed Detailed Shot Design通过Completion Gate后进入STATE-07。

### STATE-07 Clip Production

- Required boundary：必须有实际可读、Revision匹配且已确认的Detailed Shot Design Artifact。
- Authority：`workflows/10_clip_production_workflow.md`；Shot到Clip的组织、时长、Preflight、Reference Budget与连续性算法不得在本地图复制。
- Output owner：`templates/20_clip_plan.md`。
- Next route：Confirmed Clip Production Plan通过Completion Gate后进入STATE-08。

Shot是导演镜头设计单位；Clip是AI视频生成执行单位。Source Script Label、SCENE、BEAT、COV与UNIT均不得直接改名或机械映射为CLIP。

### STATE-08 Clip-based Video Prompt / Video Generation

- Required boundary：必须消费Confirmed Clip Production Plan、Confirmed Detailed Shot Design、适用资产、Visual Direction与连续性事实。
- Authority：`workflows/11_video_generation_workflow.md`；它拥有资源清单、语义编译、Preflight、Knowledge Reflection、Projection与验证流程。
- Final schema owner：`templates/10_video_prompt.md`。Workflow、Rules、Knowledge、Adapter和本地图都不得维护竞争Schema。
- Image-to-video boundary：`templates/11_image_to_video_prompt.md`只拥有参考帧Source Data与边界约束。
- Next route：最终Prompt通过Template与Workflow验证后进入STATE-09。

### STATE-09 Review

- Required boundary：必须实际检查生成结果及适用的项目事实、资产、镜头、Clip与连续性记录。
- Authority：`workflows/13_review_workflow.md`。
- PASS：完成STATE-09。
- REVISE / REBUILD：携带最小Return Route回到事实或设计拥有者，修复后重新进入STATE-09。

## Auxiliary Workflow Routing

以下Workflow不占用固定STATE：

| Intent / condition | Workflow | Template / contract | Boundary |
|---|---|---|---|
| 用户显式请求Storyboard | `workflows/10_storyboard_workflow.md` | `templates/09_storyboard_prompt.md` | Optional/Auxiliary；不替代STATE-06/07，不进入STATE-08 Canonical Reference |
| 用户显式请求声音身份资产 | `workflows/audio_router.md` | AUDIO Route → `workflows/20_seed_audio_voice_asset_workflow.md` → `templates/21_seed_audio_voice_asset.md` | 必须先过唯一Router；普通视频、Clip、Seedance、对白或声音设计不自动触发 |
| 中断恢复、Review退回或生成重试 | `workflows/18_project_resume_workflow.md` | `references/project_state_contract.md` | 从已验证Checkpoint恢复，不创建STATE |
| Sequence级Coverage规划 | `workflows/16_sequence_planning_workflow.md` | `templates/14_sequence_plan.md` | 条件执行；不创建SHOT或CLIP ID |
| 电影海报 / Key Art | `workflows/17_poster_design_workflow.md` | `templates/15_poster_design_package.md` | 按需辅助视觉交付 |
| 已有视频结果的局部修改 | `workflows/12_editing_workflow.md` | `templates/12_edit_prompt.md` | 修复后必须返回STATE-09 Review |
| 系列项目管理 | `workflows/14_series_management_workflow.md` | `templates/19_series_status.md` | 不替代单个制作单元的完整主Pipeline |

### Storyboard Isolation

Storyboard只在用户明确请求时调用`workflows/10_storyboard_workflow.md`。它不进入Completed States，不成为固定Next Workflow，不参与Clip划分，也不得作为STATE-08 Canonical Reference。

### AUDIO / SEED-AUDIO Explicit Trigger Gate

当前请求明确要求音色提示词、音色制作、角色声音、Seed Audio、配音音色、声音资产、Voice Profile或同义声音身份制作时，先读取`workflows/audio_router.md`：

- Router返回`ROUTE: AUDIO / SEED-AUDIO Voice Asset`时，才进入`workflows/20_seed_audio_voice_asset_workflow.md`。
- Router返回`ROUTE: ORIGINAL WORKFLOW`时，声音资产模块优先级为零，继续原Workflow路由。
- 同一请求同时明确要求视频与音色资产时，分别路由、分别使用Template，不混合Schema。

## Legacy Compatibility

- `workflows/10_shot_execution_plan_workflow.md`
- `workflows/19_clip_planning_workflow.md`

以上仅用于旧项目兼容，不参与新项目主路由。旧State、旧Storyboard标签与旧Portable Schema统一按`rules/compatibility_mapping.md`基于Artifact和Completion Gate迁移。

## Resume And Revision Loop

```text
STATE-09 Review
→ 定位最小受影响范围
→ 返回对应Workflow修复
→ 重新生成或修改
→ STATE-09 Review
```

修订只影响必要范围，保留Accepted Unaffected Artifacts。纯推进命令服从`rules/progression_rules.md`；恢复与重试调用`workflows/18_project_resume_workflow.md`。

## Ownership Boundaries

- `rules/`：跨阶段约束与全局行为。
- `workflows/`：阶段输入、步骤、资源、Completion Checklist和错误路由。
- `knowledge/`：专业判断方法，不拥有主路由或最终格式。
- `templates/`：用户可见最终Schema的唯一所有者。
- `references/`：状态、项目工作空间、资产锁与模块合同。

最终原则：本地图只告诉运行时“当前应读哪个Workflow与Template”。它不得重新实现被指向文件中的算法、字段骨架或完成规则。
