# AUDIO / SEED-AUDIO Voice Asset Template

## Ownership And Status

本文件是显式调用的`AUDIO / SEED-AUDIO Voice Asset`模块唯一输出规范，拥有Voice Profile、独立Seed Audio兼容Prompt与可选Reference Handoff的字段、顺序和排版。不得由Character Asset、普通视频制作、STATE-08或“继续/下一个Clip”自动调用。

本结构是**SD Film为Seed Audio 1.0组织的兼容模板**，不是ByteDance官方唯一字段模板。ByteDance官方公开资料说明Seed Audio 1.0可由Prompt描述speaker、emotional tone、line delivery、surrounding environment、key sound effects与scene progression，可进行对白timing控制，并可通过文本描述、授权参考音频或两者结合塑造声音；官方没有规定本文件中的字段标题或固定排列。

官方依据：

- https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model
- https://seed.bytedance.com/en/seedaudio1_0

## Output Contract

### Module Routing Record

- Module Name：`AUDIO / SEED-AUDIO Voice Asset`
- Explicit Trigger Evidence：
- Character / Speaker：
- Project / CHAR-ID / Version（如有）：
- Requested Deliverable：

### Character Voice Identity / Voice Profile

只写长期稳定的声音身份，不混入某一句的临时表演：

- Character / Speaker Identity：
- Voice Description：
- Language / Pronunciation Basis（适用时）：
- Identity Basis：
- Voice Asset Status：`Confirmed` / `Pending`

`Voice Description`优先使用可听、可比较的特征，例如音高倾向、音色明暗、共鸣、声音重量、咬字和稳定响应范围；不得仅用“高级、古风、喜剧、温柔”等抽象标签。未知事实不补写。

### Dialogue Performance（按需）

只描述当前一句或当前场景怎么说，与上面的稳定Voice Identity分离。按需包含：

- Emotional Tone：
- Delivery / Prosody：
- Dialogue / Spoken Content：
- Timing：

Timing只在配音、卡点或用户明确要求时输出。Seed Audio 1.0官方说明当前对白timing可按100 ms间隔控制；不得把这一能力泛化成默认逐字时间码，也不得为其他声音元素虚构同等精度。

### Seed Audio-Compatible Prompt

输出一个可独立复制的纯文本代码块。以下是SD Film建议组织顺序，不是官方固定字段；只输出实际有控制价值的部分，未使用字段直接省略，不写`N/A`、`None`或状态占位：

```text
Character / Speaker Identity:
[who is speaking; stable identity only]

Voice Description:
[stable, audible voice characteristics]

Emotional Tone:
[omit unless the current delivery needs emotional direction]

Delivery / Prosody:
[omit unless pace, pauses, rhythm, emphasis, breath or intonation needs control]

Dialogue / Spoken Content:
[omit when the task does not require fixed spoken text]

Timing:
[omit unless dialogue entry/exit timing is required]

Acoustic Environment / Ambience:
[omit for isolated voice work or when the user did not request scene audio]

Key Sound Effects:
[omit unless a requested scene-level audio event must be coordinated]

Scene Progression:
[omit unless the audio scene changes over time]

Reference Audio:
[omit unless an authorized reference is actually supplied and intended for use]
```

对于纯角色音色试听，可用正向语言说明“isolated clean speech, one speaker”，但这只是任务需要时的制作选择，不是官方固定开头。不得默认堆叠`No background music / No ambience / No sound effects...`等否定词；仅保留无法通过正向目标充分约束的少量真实高风险项。

Acoustic Environment、Key Sound Effects与Scene Progression属于可选的场景声音控制，不得混入稳定Voice Identity。BGM / Score始终由独立MUSIC / SEED-MUSIC模块处理，不进入角色音色资产Prompt。

### Reference Audio Handoff（仅实际使用或登记时）

- Reference Audio Status：`Candidate` / `Confirmed`
- Reference路径或受控外部ID：
- Speaker / CHAR Version绑定：
- 语言与内容说明：
- 来源与生成/录制方式：
- 授权依据：
- 批准信息：

没有实际Reference时整节省略，不写`Not Generated`，不得虚构路径、ID或授权。Reference时长只服从目标平台的真实要求或用户当前明确要求；本Template不设无官方依据的固定秒数。

## Hard QA

- 是否存在用户本轮显式音色制作请求与可核对的Trigger Evidence。
- 是否明确描述speaker。
- 是否把长期Character Voice Identity与当前Dialogue Performance分开。
- 是否只输出适用字段，没有重复、冲突或状态占位。
- 是否避免否定词堆砌，并使用正向目标描述主要声音结果。
- 是否没有使用模型未宣称支持的无意义精密参数；100 ms只用于确有需要的对白timing。
- 是否没有把视觉Prompt、角色外貌、镜头运动或美术描述大量复制进音频Prompt。
- Reference Audio是否真实存在、用途明确且有授权依据。
- Sound Effects、Ambience与BGM / Score是否保持概念边界。
- 是否明确本结构是SD Film兼容模板，而非官方唯一模板。
