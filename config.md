# SD Film Configuration

本文件只保存运行默认值、索引入口与能力开关。行为约束由`rules/`拥有，阶段算法由`workflows/`拥有，专业方法由`knowledge/`拥有，最终输出格式由`templates/`唯一拥有。版本只从`SKILL.md`读取。

## Runtime Defaults

- Default Output Language: Chinese
- Professional Terms: English allowed when clearer
- Execution Model: Full STATE-00 through STATE-09 Pipeline
- State Persistence Mode: runtime-dependent
- Work/Codex State Target: Active Project Root
- Chat State Target: complete Portable State in the response
- Portable Baseline: `portable_project_status.md`
- Default STATE-08 Delivery: one pending Clip per response
- STATE-08 Clip Duration: 4—15 seconds, inherited from Confirmed Clip Production Plan
- STATE-08 Image Reference Limit: 9 per Clip after Preflight and World-State filtering
- Storyboard Activation: explicit only
- AUDIO / SEED-AUDIO Voice Asset Activation: explicit only
- STATE-08 Voice Identity Text: omitted by default; conditional minimal Delta only on explicit current-video-Prompt request
- MUSIC / SEED-MUSIC Score Activation: explicit only
- MUSIC Default Generation Mode: instrumental only
- STATE-08 Music Policy: permanent ban; no Clip exceptions
- Legacy Workflow Routing: compatibility only

这些默认值不得覆盖用户当前明确指令、Confirmed Project Facts、Completion Gate或当前Template。用户明确要求批量输出时，只覆盖当前轮STATE-08交付数量，不覆盖逐Clip完整性与确认规则。

## Runtime Entry Points

- Skill Entry: `SKILL.md`
- Global Rules: `rules/`
- Workflow Map: `workflows/workflow_map.md`
- Knowledge Index: `knowledge/00_knowledge_index.md`
- Project State Contract: `references/project_state_contract.md`
- Project Workspace Contract: `references/project_workspace.md`
- Asset Lock Contract: `references/asset_lock_contract.md`
- Module Contracts: `references/module_contracts.md`
- Portable State Baseline: `portable_project_status.md`
- Repository Index: `index.md`

## Global Rule Index

- Runtime Reload: `rules/runtime_reload.md`
- State Source: `rules/state_source.md`
- Chat Compatibility: `rules/chat_compatibility.md`
- Progression: `rules/progression_rules.md`
- Activation: `rules/activation_rules.md`
- Completion Gate: `rules/completion_gate.md`
- Compatibility Mapping: `rules/compatibility_mapping.md`
- Resource Loading: `rules/resource_loading.md`
- Pipeline Constraints: `rules/01_pipeline_rules.md`
- Asset Constraints: `rules/02_asset_rules.md`
- Prompt Constraints: `rules/03_prompt_rules.md`
- Consistency Constraints: `rules/04_consistency_rules.md`
- Output Constraints: `rules/05_output_rules.md`

## Routing And Template Discovery

- 主STATE、辅助Workflow与对应Template路由：`SKILL.md`的Routing表和`workflows/workflow_map.md`。
- 当前阶段资源与Template：当前Workflow的Required Resources / Output Owner声明。
- AUDIO / SEED-AUDIO路由：`workflows/audio_router.md`。
- MUSIC / SEED-MUSIC路由：`workflows/music_router.md`。
- Legacy兼容：`workflows/10_shot_execution_plan_workflow.md`与`workflows/19_clip_planning_workflow.md`；新项目不得把它们写为主Pipeline的Next Workflow。

每个Template文件独占其用户可见Schema，其他文件不得复制完整字段骨架。STATE-08最终Schema唯一由`templates/10_video_prompt.md`拥有；`templates/11_image_to_video_prompt.md`只提供参考帧Source Data与边界约束。

## Loading Defaults

采用渐进式加载，不预读整个Knowledge库：

1. 入口、当前需要的全局规则与状态合同。
2. 当前Workflow全文。
3. Workflow列出的Required / Applicable / Conditional Resources。
4. 当前交付对应Template。

完整行为服从`rules/resource_loading.md`。STATE-08资源清单以`workflows/11_video_generation_workflow.md`为权威；Knowledge Index只负责发现，不定义竞争门槛。

## Output Defaults

- 默认使用中文；必要的电影术语可保留英文。
- 优先清楚的视觉描述、专业制作逻辑、空间关系、连续性、资产一致性与AI生成可执行性。
- Prompt是下游生产动作，不是流程起点。
- STATE-08 Prompt正文不写分镜时间码、逐秒区间、帧数区间或帧率限制；平台参数置于Prompt之外。
- STATE-08反向提示词首个非空内容行永久使用固定背景音乐禁令；任何配乐请求都由独立MUSIC / SEED-MUSIC模块处理。
- MUSIC模块默认输出纯音乐SeedMusic提示词；歌词或任何人声纹理只有用户当前明确要求时才允许。
- 最终字段与格式始终服从当前Template，本配置不拥有任何最终Schema。
