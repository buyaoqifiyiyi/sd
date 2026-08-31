# Activation And Intent Routing

## Automatic Activation

当用户目标涉及以下任一范围时自动激活SD Film：

- 剧本改编、分析、优化、导演化或制作拆解
- AI影视项目初始化、项目恢复或制作流程推进
- 角色、环境、道具、FX资产设计与一致性管理
- 视觉开发、场景拆解、电影海报或Key Art
- Detailed Shot Design、镜头语言、Clip Production
- AI视频生成、Seedance视频提示词、图生视频参考
- 最终Review、连续性检查或局部返修

## Explicit Activation

用户明确说“调用SD”“用SD Film”“按SD流程”“重新加载SD”或无歧义等价表达时激活。凡`SKILL.md` Runtime Reload Entry或`rules/runtime_reload.md`列出的重载表达，必须先完成Runtime Reload，再进行意图、State Source与Workflow路由；Activation不得把重载降级成仅激活。

## Intent Is Goal, Not Current State

用户提到“视频Prompt”“Seedance”“海报”“Storyboard”等通常描述目标，不证明前置阶段已经完成。激活后必须先按`rules/state_source.md`确认当前State，并按主Pipeline补齐Completion Gate，不能依据关键词直接跳转。

例外仅限已有有效State Source与Confirmed Artifact明确证明前置阶段已完成，或当前请求是独立辅助交付且其Workflow允许在主STATE不变时执行。

## Optional Storyboard Isolation

- 只有用户明确请求Storyboard、故事板或分镜图时，才调用`workflows/10_storyboard_workflow.md`与`templates/09_storyboard_prompt.md`。
- Storyboard是Optional/Auxiliary Artifact，不是独立STATE，不进入Completed States，不是固定Next Workflow，也不得替代Detailed Shot Design或Clip Production。
- Storyboard产物不得作为STATE-08 Canonical Reference；合法首/尾帧与其他图生视频Source Data按对应Workflow和Template处理。

## AUDIO / SEED-AUDIO Explicit-Only

只有用户明确请求“音色提示词、音色制作、角色声音、Seed Audio、配音音色、Voice Asset或声音身份资产”时，才读取唯一Router `workflows/audio_router.md`。只有Router返回`ROUTE: AUDIO / SEED-AUDIO Voice Asset`，才可调用`workflows/20_seed_audio_voice_asset_workflow.md`及其Knowledge与Template；返回`ROUTE: ORIGINAL WORKFLOW`时不得加载声音资产Workflow或其依赖。

普通视频制作、人物分析、角色视觉资产、Storyboard、Clip、Seedance、对白、音效或“声音设计”不得自动触发声音身份资产制作。未激活时默认外部已有可用角色音色资源：不检查缺失、不创建、不补建、不提示必须制作、不登记Not Applicable，也不作为STATE-02/03或STATE-08的Gate。已有Confirmed Voice Profile / Voice Reference只保留为Source State；除非用户明确要求把声音控制写进当前视频模型Prompt，否则STATE-08不得序列化其内容、资产存在状态或任何音色字段。

## MUSIC / SEED-MUSIC Explicit-Only

只有用户当前请求明确要求配乐规划、Music Spotting、Cue Sheet、主题动机、场景 / 转场音乐、SeedMusic / Seed-Music提示词或同义音乐交付物时，才读取唯一Router `workflows/music_router.md`。只有Router返回`ROUTE: MUSIC / SEED-MUSIC Score`，才可调用`workflows/21_seed_music_score_workflow.md`、`knowledge/music_score/`与`templates/22_seed_music_score.md`；返回`ROUTE: ORIGINAL WORKFLOW`时不得加载这些资源。

普通视频制作、Detailed Shot Design、Clip Production、Seedance视频Prompt、Storyboard、Review、Editing、“继续”“下一步”“下一个Clip”或项目资料中出现音乐词汇，都不得自动触发Music模块。用户只声明“视频不要配乐”属于STATE-08边界，不触发完整模块。

Music模块Positive Route默认`INSTRUMENTAL`。歌词、演唱、说唱、合唱、哼唱、吟唱、Vocalise或其他人声纹理只有用户当前另行明确要求时允许。模块激活后，由系统专业审阅整个请求范围并决定哪里使用音乐、哪里只保留同期声音或留白；不得要求用户逐Clip手工指定，也不得默认全段铺音乐。

同一请求同时要求视频Prompt与配乐时必须拆分路由、拆分Template：视频Prompt永久执行背景音乐禁令，Music Package可用标题和`Related Clip(s)`表明服务的Clip，但Clip标签不得混入SeedMusic `style + structure`执行正文。
