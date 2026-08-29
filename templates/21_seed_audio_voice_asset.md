# AUDIO / SEED-AUDIO Voice Asset Template

## Ownership

本文件是AUDIO / SEED-AUDIO Voice Asset模块的唯一输出规范，独占Voice Profile、Seed Audio Voice Sample Prompt与Voice Audio Reference Handoff的最终字段、顺序和排版。

只有用户显式请求音色提示词、音色制作、角色声音、Seed Audio、配音音色、声音资产、Voice Profile或同义角色声音身份制作时，才允许调用本Template。不得由Character Asset、普通视频制作、角色分析、STATE-08或“继续/下一个Clip”自动调用。

## Required Output

### Module Routing Record

- Module Name：`AUDIO / SEED-AUDIO Voice Asset`
- Explicit Trigger Evidence：
- Character / Speaker：
- Project / CHAR-ID / Version（如有）：
- Requested Deliverable：
- Output Language：

### Voice Profile

- 角色名：
- 性别/年龄感（仅剧情设定层面）：
- 基础音色：
- 音域倾向：
- 声音质感：
- 语速：
- 咬字/发音特征：
- 情绪表达方式：
- 说话力度：
- 停顿与呼吸特征：
- 特殊状态下的声音变化：
- 禁止项：
- 最终可直接引用的音色描述：
- Voice Asset Status：`Confirmed` / `Pending`
- Voice Profile Basis：

### Seed Audio Voice Sample Prompt

必须输出一个可独立复制的纯文本代码块，并严格保持以下内容、字段名称与顺序：

```text
Generate speech only.
Target duration: approximately 15 seconds.

Clean dry studio voice recording.
Single speaker only.
No background music.
No instrumental music.
No soundtrack.
No ambience.
No environmental sound.
No sound effects.
No singing.
No chanting.

Speaker:
[age and gender presentation grounded in confirmed character facts]

Voice characteristics:
[pitch, timbre brightness/darkness, resonance, vocal weight, articulation and emotional responsiveness]

Speaking rhythm:
[pace, phrase length, pauses, rhythm and pitch movement; omit this section only when no separate rhythm control is needed]

Performance style:
[language, delivery, emotional range and character behavior expressed as executable performance direction]

Avoid:
[voice qualities and performances that would break the confirmed character]

Read naturally:
“[sample text covering calm, normal conversation and/or slightly stronger emotion across at least 2–3 states]”
```

`Target duration`不得省略；用户未指定时固定使用`approximately 15 seconds`。除`Speaking rhythm`在确实不需要独立节奏控制时可省略外，其余标题、声明和顺序不得删除、改名、合并或改写。不得只输出一段普通自然语言音色描述代替本结构。

### Voice Audio Reference Handoff

- Voice Audio Reference Status：`Not Generated` / `Candidate` / `Confirmed` / `Not Required`
- Reference路径或受控外部ID（如有）：
- 时长（Confirmed时必须15—30秒）：
- 干净单人声检查：
- 语言：
- 来源与生成/录制方式：
- 授权依据：
- 绑定CHAR Version：
- 批准信息：
- STATE-08 Voice Text Policy：`Reference Override / Keep Fixed Voice Field` / `Voice Profile Fallback` / `No Voice Asset`

未实际生成或选择候选时写`Not Generated`，不得虚构Reference。只有已确认候选才能写`Confirmed`。

## Hard Validation

- 必须有用户本轮显式触发证据。
- 必须包含`Generate speech only.`、`Target duration`、`Clean dry studio voice recording.`、`Single speaker only.`与八条`No ...`声明。
- 必须保持`Speaker → Voice characteristics → Speaking rhythm（需要时）→ Performance style → Avoid → Read naturally`顺序。
- Voice characteristics必须使用可执行声学特征，不得只写“古风、喜剧、高级感”等抽象标签。
- 不得生成背景音乐、环境声、Foley、音效、歌曲、多人声场或STATE-08视频Prompt。
