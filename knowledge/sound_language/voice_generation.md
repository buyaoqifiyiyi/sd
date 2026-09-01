# Character Voice Identity And Seed Audio Prompting

## Purpose And Invocation Boundary

本Knowledge只服务用户显式调用的`AUDIO / SEED-AUDIO Voice Asset`独立辅助模块，把已确认角色事实转换为稳定Voice Profile、独立Seed Audio兼容Prompt，以及按需的授权Reference Audio交接。

它不是STATE-02/03默认流程，不创建Asset Gate或主STATE。角色有对白、普通视频/Clip/Seedance请求、下游没有Voice Profile或用户只说“继续”都不得触发。没有`Explicit Trigger Evidence`时立即返回原Workflow，不推导、不输出、不登记任何声音资产或Not Applicable状态。

最终输出Schema只由`templates/21_seed_audio_voice_asset.md`拥有。

## Official Capability Boundary

以ByteDance Seed Audio 1.0官方资料为能力边界：

- Prompt可描述speaker、emotional tone、line delivery、surrounding environment、key sound effects与scene progression。
- 可控制角色对白timing；官方当前公开精度为100 ms间隔。
- 可使用文本描述、授权参考音频或两者结合塑造声音。
- 可在不同情绪、节奏、韵律和说话风格下保持可识别声音身份，并支持场景级speech、ambience与sound effects协同。

官方资料没有规定唯一字段模板，也没有要求固定15秒、固定干声开头、固定单说话者声明或固定数量的`No...`否定项。因此`templates/21_seed_audio_voice_asset.md`必须明确标记为SD Film兼容组织模板，不能冒充官方格式。

官方依据：

- https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model
- https://seed.bytedance.com/en/seedaudio1_0

## Source Facts

只使用用户当前明确输入、已确认剧本/Project Bible或Active CHAR Version中的事实：

- 角色身份、年龄与性别呈现（剧情确有定义时）
- 对白功能、性格与可观察的说话行为
- 已确认台词、语言，以及有证据的口音/方言要求
- 当前用户要求的情绪、表演、timing或场景声音目标
- 实际存在、已授权并明确用于当前任务的Reference Audio

不得从外貌、服装、摄影风格、导演标签或项目类型静默推断口音、病理嗓音、声带损伤或身份事实。不得把项目示例投影到其他角色。

## Concept Separation

- **Character Voice Identity / Voice Profile**：长期稳定的speaker身份与可复用声音基线。
- **Dialogue Performance**：当前一句/当前场景的情绪、力度、停顿、节奏、韵律、呼吸与强调方式。
- **Sound Effects**：动作、道具与事件声。
- **Acoustic Environment / Ambience**：空间底声、环境纹理与声学空间。
- **BGM / Score**：后期配乐，只由独立MUSIC / SEED-MUSIC模块处理。

当前情绪、距离、体力或剧情状态可以改变Dialogue Performance，但不得被写成新的稳定Voice Identity。

## Voice Description

优先写可听、可比较、可执行的维度：

1. speaker identity and presentation
2. pitch tendency / usable range
3. timbre brightness or darkness
4. resonance quality
5. vocal weight
6. articulation and consonant clarity
7. stable pace/rhythm tendency（确有身份价值时）
8. emotional responsiveness without identity drift

抽象角色词只能作为补充，并转成可听结果。例如“克制”可转成受控动态、清楚咬字和较小音高起伏；“喜剧”可转成包袱前停顿、节奏反差和有动机的音高变化。不得把抽象词单独当作Voice Description。

## Prompt Construction

按照`templates/21_seed_audio_voice_asset.md`，只输出当前任务需要的字段：

- 声音身份任务至少描述Character / Speaker Identity与Voice Description。
- Emotional Tone、Delivery / Prosody与Dialogue属于Dialogue Performance，按需输出。
- Timing只在配音、卡点或用户明确要求时输出；100 ms能力只用于对白，不为ambience、effects或其他元素虚构同等精度。
- Acoustic Environment / Ambience、Key Sound Effects与Scene Progression只在用户请求场景级音频时输出；纯音色试听默认不复制视觉场景。
- Reference Audio只在真实存在、用途明确且有授权时输出。

优先用正向目标描述声音。否定项只保留当前任务真实高风险且无法由正向目标充分锁定的少量内容，避免把无关声音概念写入Prompt造成污染。

## Reference Audio

Reference Audio必须真实存在、speaker明确、来源和授权可核对，并绑定正确角色/版本。未确认候选只能标记`Candidate`，不得伪装为Confirmed。没有Reference时不输出Reference字段，也不虚构`Not Generated`记录。

Reference的长度、格式与质量要求服从目标平台真实规范或用户明确要求；不得把本地经验秒数冒充官方要求。

## STATE-08 Isolation

Voice Profile与Seed Audio Prompt属于独立AUDIO模块交付，不强行并入常规Seedance视频Prompt。

STATE-08默认执行`Source Carries State, Prompt Carries Delta`：即使已有Confirmed Voice Profile或Reference Audio，也不复制、不声明锁定、不写`音色特征：`或声音资产状态。只有用户明确要求把声音控制写进当前视频模型Prompt时，STATE-08才按其Template输出最小必要Delta；该授权不自动延续到后续Clip。

## QA

- 有本轮显式Trigger Evidence；普通视频/Clip请求没有误触发。
- 描述了speaker，且事实来源可核对。
- 稳定Voice Identity与当前Dialogue Performance没有混淆。
- 没有同义重复、跨字段冲突或完整Profile机械复制。
- 没有否定词堆砌；主要声音目标使用正向描述。
- 没有无官方依据的固定字段、固定时长或无意义精密参数。
- 100 ms只在确需对白timing时使用。
- 没有把视觉Prompt、外貌、镜头与美术信息大量复制进音频Prompt。
- Ambience、Sound Effects与BGM / Score边界清楚。
- Reference Audio真实、已授权且用途明确；不存在时字段已省略。
- 输出明确说明模板是SD Film兼容组织，不是官方唯一模板。
