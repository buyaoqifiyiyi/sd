# AUDIO / SEED-AUDIO Voice Asset Workflow

## Module Position

本Workflow是显式调用的Optional/Auxiliary Workflow，不创建新主STATE，不属于STATE-03 Character Asset Workflow的默认步骤，也不修改STATE-08 Seedance视频Prompt Schema。

唯一输出Template：`templates/21_seed_audio_voice_asset.md`。

专业Knowledge：`knowledge/sound_language/voice_generation.md`。

唯一Router：`workflows/audio_router.md`；只有其返回`ROUTE: AUDIO / SEED-AUDIO Voice Asset`时才可执行本Workflow。

## Explicit Trigger Gate

只有当前用户请求明确要求创建、设计、生成、修改或更新以下任一内容时才触发：

- 音色提示词
- 音色制作
- 角色声音
- Seed Audio / SeedAudio
- 配音音色
- 声音资产 / Voice Asset
- Voice Profile、角色音色样本Prompt或Audio Reference（且语义明确指向角色声音身份制作）

仅仅出现角色有对白、旁白、口播、画外音、通话或呼喊，不构成触发。系统不得从剧本、Asset Discovery、Character Asset、Detailed Shot Design、Clip Production或STATE-08自动推断用户想制作音色资产。

## Explicit Non-Trigger Gate

以下请求不得触发本模块：

- “继续视频制作”“下一步”“下一个Clip”“继续”“下一个”
- “输出Clip B视频提示词”“生成Seedance提示词”“生成视频Prompt”
- 普通角色分析、角色视觉资产、场景、道具、FX、Storyboard、分镜或海报制作
- STATE-06 / STATE-07 / STATE-08发现角色有对白，但用户本轮未明确要求音色制作
- 只要求台词、口型、环境声、Foley、音效、配乐、歌曲、正式整段配音或多人声场

这些请求按原Workflow Map继续；不得顺带生成Voice Profile、Seed Audio Prompt或Audio Reference。

## Routing Priority

1. 当前请求显式命中本模块时，声音资产部分优先路由到本Workflow，不要求先推进主Pipeline，也不把该请求误判为STATE-08视频Prompt。
2. 同一请求同时显式要求视频交付与音色资产时，两个交付分别执行各自Workflow与Template；不得把Seed Audio字段混入STATE-08 Template，也不得以视频交付隐含替代声音资产交付。
3. 当前请求没有显式命中时，本模块优先级为零：继续当前主Pipeline或其他显式辅助Workflow，不读取本Workflow、Knowledge或Template。
4. 模糊的“声音做一下”“处理一下声音”不足以证明用户要制作角色音色资产；按当前任务语境处理对白/同期声/音效，只有语义明确指向声音身份或音色Prompt时才进入本模块。

## Required Inputs

优先使用已确认的：

- 角色名称、年龄与性别呈现
- 角色身份、性格、对白功能与剧情位置
- 情绪基调和可观察的说话行为
- 已确认台词、语言以及有证据的口音/方言要求
- 现有Voice Profile、Voice Sample Prompt或Audio Reference及其版本/授权状态
- 用户本轮明确指定的目标时长、目标模型和表演要求

项目存在时可读取Active Project Root中的`project_bible.md`、`asset_registry.md`和相关已确认剧本/角色事实；项目不存在时直接使用用户当前提供的角色事实，不得为了生成音色Prompt强制初始化或推进影视主Pipeline。

关键角色事实不足且无法安全推导时，只请求缺失的必要事实。不得从外貌、服装、导演标签、题材或示例角色静默推断口音、病理嗓音或身份事实。

## Execution

1. 记录`Explicit Trigger Evidence`，引用用户本轮明确的音色制作意图。
2. 读取`knowledge/sound_language/voice_generation.md`全文。
3. 从已确认输入建立长期稳定的Character Voice Identity / Voice Profile；未知事实标记Pending，不虚构，并与当前Dialogue Performance分开。
4. 使用`templates/21_seed_audio_voice_asset.md`生成独立Seed Audio兼容Prompt，只输出当前交付需要的字段。speaker与Voice Description是声音身份任务核心；情绪、delivery/prosody、台词、timing、ambience、key sound effects、scene progression与Reference Audio均按需输出。
5. 若用户只要求Prompt，到模板输出完成即停止；不得自动生成音频。
6. 只有用户同时明确要求实际音频、工具可用且来源/授权条件满足时，才生成候选音频。
7. 用户确认候选后，才可按目标平台真实要求和授权条件登记同一CHAR Version的Audio Reference；未确认时保持`Candidate`，没有实际Reference时不创建占位记录。
8. 项目存在且用户要求保存/更新资产时，按`references/asset_lock_contract.md`把结果绑定到同一CHAR-ID与Version；不得创建独立视觉Canonical Reference。

## Output Ownership

`templates/21_seed_audio_voice_asset.md`是本模块Voice Profile、Seed Audio兼容Prompt、Audio Reference Handoff字段、顺序和排版的唯一来源。该Template是SD Film为Seed Audio 1.0组织的兼容结构，不是ByteDance官方唯一字段模板。

禁止退化为普通自然语言音色段落，禁止改用`templates/04_character_asset_prompt.md`，禁止把`templates/10_video_prompt.md`的`音色特征：`当作音色资产模板。

## Return And Fallback

- 完成独立音色交付后，返回调用前的主Pipeline Checkpoint；不自动推进或回退主STATE。
- 若请求未显式命中本模块，直接返回原路由，不创建Not Applicable资产记录，也不阻塞主Pipeline。
- STATE-08缺少Voice Asset时不得调用本Workflow，也不得在视频Prompt中写缺失声明；默认外部已有可用角色音色资源并继续。
- 角色事实冲突返回其事实拥有者；音频候选/授权未确认时停在本模块的Pending/候选状态，不把它伪装为Confirmed。

## Completion Gate

- 有可核对的`Explicit Trigger Evidence`。
- 已读取唯一Knowledge与唯一Template。
- Seed Audio Prompt明确描述speaker，并分离稳定Voice Identity与当前Dialogue Performance。
- 只输出适用字段；未使用字段直接省略，没有固定时长、固定否定声明、无意义精密参数或视觉Prompt复制。
- Ambience、Key Sound Effects与Scene Progression仅在用户请求场景级音频时出现；BGM / Score仍由独立MUSIC模块处理。
- 明确说明输出结构是SD Film兼容模板，不冒充官方唯一模板。
- 若登记Audio Reference，来源、授权、CHAR-ID、Version、时长和批准信息完整。
