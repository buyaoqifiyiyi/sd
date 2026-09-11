# Activation And Intent Routing

## Automatic Activation

当用户目标涉及以下任一范围时自动激活SD Film：

- 从创意/题材/品牌Brief开始的剧本创作，以及剧本改编、分析、优化、导演化或制作拆解
- AI影视项目初始化、项目恢复或制作流程推进
- 角色、环境、道具、FX资产设计与一致性管理
- 视觉开发、场景拆解、电影海报或Key Art
- Detailed Shot Design、镜头语言、Clip Production
- AI视频生成、Seedance视频提示词、图生视频参考
- 最终Review、连续性检查或局部返修

## Explicit Activation

用户明确说“调用SD流程”“用SD Film”“按SD流程”或无歧义等价表达时激活。完整Runtime Reload Trigger词表只由`rules/runtime_reload.md`拥有；凡命中其中任一显式调用/重新调用/重新加载表达，必须先完成Runtime Reload Gate，再进行意图、State Source与Workflow路由。Activation不得把重载降级成仅激活，也不得另建平行触发表。

## Fast Automation Activation

用户明确说“开启自动推进”“快速制作模式”“Fast Mode”“尽量少确认”“只在关键节点停”或“自动完成可逆步骤”等无歧义表达时，在State Source合法解析后读取`rules/automation_mode.md`并启用`Automation Policy: FAST`。该表达不等于剧本锁定、外部生成提交、图片Canonical确认、首次模型选择或Review PASS授权；关闭指令恢复`STANDARD`。

## Dry Run Activation

用户明确说“跑流程测试”“演练一遍流程”“dry run”“空跑”“测试路由”或“走一遍流程不要产物”等无歧义表达时，进入`DRY RUN`。

`DRY RUN`是运行目的，不是`Automation Policy`的取值；该字段的允许值不变。它表示本次运行的目的不是生产，而是验证流程本身：不改变任何生产门槛，不新增STATE，也不放宽任何Gate。它与`rules/01_pipeline_rules.md`的“生产运行必须完整执行STATE-00至STATE-09”不冲突，因为`DRY RUN`不是生产运行。

`DRY RUN`必须：

- 按主Pipeline顺序对当前请求覆盖的STATE逐个执行路由判定；未指定范围时覆盖STATE-00至STATE-09。
- 用合成输入代替缺失的上游产物，并标明哪一部分是合成的；合成输入不是资产、不是确认，不得登记为Candidate / Canonical / Active。
- 逐STATE核验：Workflow合法、Entry Gate判据可取得、Required Reads可解析、Completion判据可判定、Next Workflow合法。
- 全程可判定时不产出任何交付物，只给出一句走通确认；只有出现断点时才输出最小断点报告，指出具体STATE、缺失证据与最近合法Checkpoint。

`DRY RUN`禁止：

- 创建、读取或写回任何真实项目状态；不得建立Active Project Root，也不得改写`portable_project_status.md`。
- 产出任何Template交付物（剧本、资产、Scene、Shot、Clip、Prompt、海报等）；`DRY RUN`的产物是判定，不是文件。
- 声称任何Artifact已生成、已确认、已锁定或已进入Canonical / Active。
- 调用外部生成、提交外部服务或使用未知凭据。

未命中显式表达时，普通制作请求不得被解释为`DRY RUN`。一次`DRY RUN`结束后的下一次请求默认回到正常生产路由。

## Intent Is Goal, Not Current State

用户提到“视频Prompt”“Seedance”“海报”“Storyboard”等通常描述目标，不证明前置阶段已经完成。激活后必须先按`rules/state_source.md`确认当前State，并按主Pipeline补齐Completion Gate，不能依据关键词直接跳转。

例外仅限已有有效State Source与Confirmed Artifact明确证明前置阶段已完成，或当前请求是独立辅助交付且其Workflow允许在主STATE不变时执行。

用户明确说“帮我写剧本 / 我只有一个想法 / 根据品牌需求从剧本开始”时，目标是STATE-01 Creation Brief分支；用户上传完整/粗略剧本或来源叙事文本时，目标是STATE-01 Existing Script / Material分支。两者都先服从STATE-00项目入口与状态证据，但不得要求Creation Brief用户先在Skill外完成剧本，也不得把Existing Script误路由为从零创作。

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
