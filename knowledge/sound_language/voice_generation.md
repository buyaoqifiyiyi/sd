# Voice Profile And Seed Audio Voice Sample Generation

## Purpose

本文件把已确认的角色事实转换为：

- 稳定、可复用的文字Voice Profile
- 可直接复制到Seed Audio类统一音频模型的纯人声音色样本Prompt
- 候选音色确认后的Audio Reference交接规范

它只属于显式调用的`AUDIO / SEED-AUDIO Voice Asset`独立辅助模块。只有用户当前请求明确要求音色提示词、音色制作、角色声音、Seed Audio、配音音色、声音资产、Voice Profile或同义角色声音身份制作时才允许读取和使用。它不是STATE-03 Character Asset Workflow的默认子流程；角色有对白、普通视频制作、Clip/Seedance请求或下游缺少Voice Profile都不能自动触发。它不创建新STATE，不定义STATE-08 Seedance视频Prompt字段，也不负责背景音乐、环境声、Foley、歌曲、多人音频场景或正式整段配音。

最终字段、顺序与排版只由`templates/21_seed_audio_voice_asset.md`拥有；禁止退化为普通自然语言音色段落。

## Explicit Invocation Boundary

进入本Knowledge前必须由`workflows/20_seed_audio_voice_asset_workflow.md`记录用户本轮的`Explicit Trigger Evidence`。没有该证据时立即返回原Workflow，不推导、不输出、不登记任何音色资产。

“继续视频制作”“下一个Clip”“输出Clip B视频提示词”“生成Seedance提示词”、普通角色分析与Character Asset均属于明确非触发。STATE-08只消费已经存在的声音资产；若不存在，它按自身Template声明未建立独立音色资产，不得调用本Knowledge补齐。

---

## Required Inputs

只使用已确认的：

- 角色年龄与性别呈现
- 角色身份、对白功能与剧情位置
- 性格、情绪基调和可观察的说话行为
- 已确认台词、语言及必要的口音/方言证据
- Active CHAR Version中的Voice Profile、候选状态与授权记录

不得从角色外貌、服装、摄影风格、导演标签或项目类型直接推断声音。不得因为角色“古风、喜剧、高级、仙气”就把这些抽象氛围词当成完整音色。

未有剧情依据时，不得新增口音、方言、地域发音、疾病嗓音、声带损伤、结巴、耳语癖或其他病理/生理特征。

---

## Acoustic Description Priority

先写可由声音模型执行和比较的声学/表演特征：

1. age and gender presentation
2. pitch / pitch range
3. timbre brightness or darkness
4. resonance placement and quality
5. vocal weight
6. articulation and consonant clarity
7. pace
8. rhythm, phrase length and pauses
9. pitch movement and emotional response
10. breath control, volume and dynamics（适用时）

“聪明、温柔、专业、儒雅、喜剧”等角色词只能作为上述声学特征之后的表演补充。必须把抽象词翻译成可听见的结果，例如：

- `喜剧` → punchline前短暂停顿、受惊时自然升调、假装镇定与突然破功的能量反差
- `专业` → 稳定音量、精确咬字、短而有意图的分句、受控动态
- `温柔` → 温暖音色、柔和起音、稳定气息、不过度气声
- `儒雅` → 温润共鸣、从容语速、清晰咬字、克制动态

---

## Seed Audio Prompt Invariant

角色音色样本默认只生成干净单人语音。Prompt必须逐条包含：

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
```

`Target duration`不得省略。默认写`approximately 15 seconds`；角色音色筛选与横向比较推荐10—20秒。时长是目标，不替代合理台词容量与自然语速。

上述声明之后，只使用以下固定结构与顺序：

1. `Speaker`
2. `Voice characteristics`
3. `Speaking rhythm`（需要独立节奏控制时）
4. `Performance style`
5. `Avoid`
6. `Read naturally`

不得把`Avoid`拆成散落在其他章节的负面规则。可以在`Read naturally`中为不同句子附加简短表演指令，但不得新增与本结构竞争的最终标题。

---

## Sample Text Design

试听文本用于判断稳定音色，不只是演示一句极端情绪。建议：

- 按自然语速准备约15—25秒文本容量
- 覆盖平静、正常交流、稍强情绪中的至少2—3种状态
- 保留角色常态作为主体，强情绪只用于测试响应范围
- 句子之间允许自然停顿，不用拖长空白凑时长
- 文本过长时删减句子，不用异常语速、吞字或连续喊叫硬塞
- 使用已确认台词；需要专门试听句时，不得新增剧情事实或改变角色关系

---

## Comedy Voice Rule

喜剧角色的喜感优先来自：

- timing
- pause before a punchline
- controlled pitch movement
- pace changes
- deadpan delivery
- emotional contrast
- confident baseline followed by a motivated loss of composure

不得默认使用幼稚卡通腔、尖锐儿童声、滑稽动物腔、持续高能量、无休止快语速或夸张破音。只有角色事实明确要求时，才使用更强的卡通化方向。

---

## Candidate Selection And Audio Reference

推荐的跨集一致性路径：

`Text-only Prompt → 生成多个纯人声候选 → 比较基础音色与状态响应 → 确认一个候选 → 截取15—30秒干净单人声 → 登记为同一CHAR Version的Audio Reference`

Audio Reference必须：

- 单说话者
- 无背景音乐、配乐、环境声与音效
- 以自然常态为主，并保留可判断咬字、节奏和情绪响应的片段
- 长度15—30秒
- 绑定同一CHAR-ID与Version
- 记录受控路径或外部ID、语言、来源、生成/录制方式、授权依据与批准信息

未确认候选只标记`Candidate`。没有实际文件或受控外部ID时写`Not Generated`，不得虚构Reference。目标工具支持Audio Reference时，跨集优先复用已确认Reference；不支持时回退到Confirmed Voice Profile与Voice Sample Prompt。

## STATE-08 Voice Reference Override Handoff

Voice Profile与本文件中的`Voice characteristics`只用于用户显式调用的AUDIO模块生成/筛选音色样本，并作为无Reference工具的内部回退。它们不得在已使用音色参考资产的STATE-08视频Prompt中再次出现。

当用户明确提供当前角色音色参考资产，或同一Active CHAR Version存在可用于目标模型的Confirmed Voice Audio Reference / Audio Reference / Voice Reference时：

- 将该Reference作为角色声音身份的唯一锁定来源。
- 在STATE-08【参考资产】中以声音专用Reference标明其角色、ID/受控路径与用途；不得把它当作视觉Canonical Reference。
- 保留固定字段`音色特征：`，写明声音身份由对应Voice/Audio Reference锁定且不得文字重定义；不写空字段、占位或“继承参考音色”。
- 删除Voice characteristics、pitch、timbre、resonance、vocal weight、音高、声线、音域、共鸣、语速、音色质感等文字描述，不得把Confirmed Voice Profile换一种措辞写入台词或音效。
- 只允许在准确台词旁保留必要的轻量表演指令，例如“轻声说”“无奈地说”“短暂停顿后说”；这些指令不得重新定义音色。

只有当前角色没有适用Voice/Audio Reference时，STATE-08才使用Confirmed Voice Profile填充固定字段`音色特征：`；有适用Reference时同一字段声明Reference锁定且不得文字重定义；无对白时明确无对白。本Gate不改变默认无背景音乐规则。

---

## Project Example Boundary

以下四套Voice Bible来自《竹雀六法》项目，只用于展示如何把项目角色事实写成可执行Prompt：

- 孔老板：系列核心角色
- 老板娘：系列核心角色
- 吴御史：系列核心角色
- 诸葛亮：本集Guest Voice

这些示例不得成为其他项目的默认角色、默认年龄、默认声线或默认试听台词。其他项目必须从自己的Script Analysis、Project Bible与Active CHAR Version重新推导。

---

## 《竹雀六法》Voice Bible Example — 孔老板

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
adult Chinese male character, approximately 30–38 years old.

Voice characteristics:
medium to medium-high male pitch, bright and crisp timbre, slightly thin and agile rather than deep or heavy, clear forward resonance, quick articulation, flexible pitch movement, lively vocal rhythm, highly responsive emotional changes.

The voice should have a naturally humorous and witty quality. He sounds clever, talkative, slightly narcissistic, easily startled, and very protective of his dignity. There should be a subtle comic sharpness in the voice, as if he often reacts half a beat faster than everyone else.

Speaking rhythm:
slightly fast conversational pace. Short phrases are delivered quickly and decisively. Use noticeable comic pauses before punchlines. Sentence endings may rise slightly when surprised or suspicious. When panicking, the pitch rises naturally and the speaking speed becomes slightly faster. When pretending to be calm, he deliberately lowers his energy for contrast.

Performance style:
natural spoken Mandarin Chinese. Light situational comedy. Deadpan sarcasm mixed with sudden emotional reactions. The humor should come from rhythm, timing, contrast and attitude. He often sounds confident at first, then suddenly loses composure when something threatens his peacock feathers.

Avoid:
narrator delivery,
heroic or authoritative delivery,
deep CEO voice,
anime child voice,
real bird imitation,
animal noises,
slapstick cartoon acting,
singing.

Read naturally:
“关门！东风追到店里来了！”
Start suddenly startled, slightly higher pitch, quick and urgent, but still comedic rather than genuinely frightened.

“别人把东风借走，您倒好——打包带回来了。”
Begin with deadpan sarcasm, pause briefly before “打包带回来了”, then deliver the punchline lightly and confidently.

“你这个眼神我见过。”
Lower the voice slightly, suspicious and defensive, as if he suddenly realizes something bad is about to happen.

“东风可以送——尾巴不外借！”
Start pretending to negotiate calmly, pause after “送”, then suddenly become faster, higher and more protective on “尾巴不外借”.
```

声音公式：明亮偏高的基础音色 + 略快但不持续抢速 + 一本正经吐槽 + 包袱前停半拍 + 受惊时自然升调 + 护尾羽时突然加速。整体约七成聪明老板、三成喜剧活宝。

---

## 《竹雀六法》Voice Bible Example — 老板娘

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
an adult Chinese woman, approximately 28–35 years old.

Voice characteristics:
medium female pitch, soft and warm timbre, clear and smooth vocal texture, relaxed breath support, gentle resonance, mature but youthful. The voice should feel calm, comfortable and naturally trustworthy. Stable volume and a subtle natural smile in the voice, without excessive sweetness or breathiness.

Speaking rhythm:
moderate to slightly slow conversational pace, soft articulation, natural pauses and unhurried phrase endings. Keep the rhythm stable even when the surrounding situation is strange. Use a brief understated pause before mild teasing.

Performance style:
natural spoken Mandarin Chinese. Calm, composed and effortless, as if she has already seen every strange customer imaginable. Friendly toward customers, with occasional understated teasing toward familiar people. Never overly sweet or flirtatious.

Avoid:
childlike female voice,
cute anime voice,
customer-service announcer tone,
seductive breathy delivery,
overly sweet delivery,
singing.

Read naturally:
“店里有工具，不用老板。”
Deliver calmly, with a short pause before “不用老板” and only a trace of teasing.

“耳里总不清净的，先别自己乱掏。”
Warm, practical and reassuring, like normal customer guidance rather than an announcement.

“下一位，请进。”
Relaxed, welcoming and steady, with a natural smile but no promotional tone.
```

声音公式：soft + warm + smooth + relaxed + stable。她是四位角色里最让顾客感到可信和舒服的声音。

---

## 《竹雀六法》Voice Bible Example — 吴御史

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
an adult Chinese man, approximately 30–38 years old.

Voice characteristics:
medium-low male pitch, clean and cool timbre, controlled resonance, clear chest voice without excessive bass, precise articulation and restrained dynamics. Slight natural vocal depth, but not a deep CEO voice. Very stable delivery.

Speaking rhythm:
moderate to slightly slow speaking pace. Use short, deliberate phrasing and economical pauses. Keep pitch movement small and controlled. Stronger conclusions become firmer and more concise, not louder or more dramatic.

Performance style:
natural spoken Mandarin Chinese. Calm, analytical and professional. Emotion is deliberately restrained. Humor comes from delivering unusual lines with complete seriousness. He should sound competent and trustworthy rather than stern or theatrical.

Avoid:
overly deep bass,
dominant CEO voice,
angry authority,
medical announcement tone,
dramatic trailer voice,
theatrical declamation,
singing.

Read naturally:
“东风早走了。留下来的东西，还在跟着风转。”
Analytical, quiet and exact, as a normal professional observation.

“该扫了。”
Short and decisive, with no added drama.

“竹雀六法——扫。”
Pause deliberately before “扫”, then land the final word cleanly and calmly.
```

声音公式：medium-low + clean + cool + controlled + precise。冷面幽默来自平静与内容的反差，不来自压低声线。

---

## 《竹雀六法》Voice Bible Example — 诸葛亮

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
an adult Chinese man, approximately 35–42 years old.

Voice characteristics:
medium-low male pitch, warm and refined timbre, smooth resonance, gentle vocal weight, clear articulation and calm breath control. Mature and intelligent without sounding old. Slight natural fatigue in the voice, as if he has spent years thinking deeply and sleeping too little.

Speaking rhythm:
slow to moderate speaking pace, measured rhythm and relaxed pauses. Mild irritation tightens the phrasing slightly without increasing volume. When relieved, breathing opens and phrase endings become softer and lighter.

Performance style:
natural spoken Mandarin Chinese. Scholarly, composed and thoughtful. Never theatrical. His humor is subtle and delivered seriously. At the beginning he carries mild irritation and mental fatigue; when relaxed, his tone becomes noticeably softer and lighter.

Avoid:
elderly voice,
opera-style delivery,
historical-drama declamation,
overly deep authoritative voice,
comedic caricature,
modern jokey delivery,
singing.

Read naturally:
“怪了。自赤壁回来，这东风就没停过。”
Mildly irritated and mentally tired, but still controlled and thoughtful.

“茶。原来这么安静。”
Let the breath relax; make the second sentence softer, lighter and genuinely relieved.

“若借孔老板三根……”
Return to composed seriousness, with a subtle humorous implication and an unfinished ending.
```

声音公式：medium-low + warm + refined + measured + lightly fatigued。与吴御史的中低音区分是：吴御史冷、准、静；诸葛亮温、雅、缓。

---

## Validation Checklist

- 是否存在用户本轮显式音色制作请求与`Explicit Trigger Evidence`；只有角色有对白或潜在对白需求不构成触发
- 是否包含`Generate speech only.`与不可省略的`Target duration`
- 是否逐条包含`Clean dry studio voice recording.`、`Single speaker only.`和八条No声明
- 是否保持`Speaker → Voice characteristics → Speaking rhythm（需要时）→ Performance style → Avoid → Read naturally`顺序
- 是否优先描述年龄、性别呈现、pitch、timbre、resonance、vocal weight、articulation、pace、rhythm与emotional response
- 是否没有只用“古风、喜剧、高级感”等抽象词
- 试听文本是否覆盖至少2—3种状态，并以自然语速为前提
- 喜剧角色是否用timing、pause、pitch movement、pace changes与emotional contrast，而非默认幼稚卡通腔
- 候选确认后是否建议15—30秒干净单人声Audio Reference，并记录版本、来源与授权
- Audio/Voice Reference已用于STATE-08时，是否明确交接`Reference Override / Keep Fixed Voice Field`，保留非空`音色特征：`并声明Reference锁定且没有任何文字音色重定义；无适用Reference但已有Confirmed Voice Profile时是否回退；两者都不存在时是否明确交接`No Voice Asset`且未触发本模块
- 竹雀四角色是否始终标记为项目示例，而非全局默认
- 是否严格使用`templates/21_seed_audio_voice_asset.md`，没有退化为普通自然语言音色描述
- “输出Clip B视频提示词”与“继续视频制作”是否保持非触发
