# SeedMusic Prompting

## Source Basis

本适配基于ByteDance Seed官方资料：

- Instrumental Music Generation：`https://seed.bytedance.com/en/seed-music/instrumental-music-generation`
- Seed-Music主页与技术报告：`https://seed.bytedance.com/en/seed-music`
- Audio Prompting：`https://seed.bytedance.com/en/seed-music/audio-prompting`
- Shortform / Longform Audio Generation：官方将自然语言输入区分为Lyrics与Descriptors；纯器乐生成省略Lyrics，只提供描述。

官方器乐示例把输入拆为`style`和`structure`，并使用`[Verse]: 0s`、`[Chorus]: 10s`、`[Bridge]: 45s`、`[Outro]: 75s`等绝对秒点控制段落转换。本模块保留该原生格式，不虚构额外SeedMusic字段。

## Default Instrumental Mode

默认输出纯音乐。除非用户当前明确要求，否则禁止：

- Lyrics / sung words
- Lead or backing vocals
- Spoken word / dialogue / narration / rap
- Choir
- Humming
- Chanting / vocalise / wordless vocal texture

同时避免生成非音乐层：环境声、Foley、动作音效、对白和旁白不属于SeedMusic配乐Cue。

`style`中应明确写出等价约束：`instrumental only; no vocals, no singing, no lyrics, no spoken word, no choir, no humming, no vocalise; music only, no dialogue, ambience, Foley or sound effects.`

## Native Execution Block

```text
style:
<descriptors>

structure:
[Verse]: 0s
[Chorus]: <absolute seconds>s
[Bridge]: <absolute seconds>s
[Outro]: <absolute seconds>s
```

要求：

- 执行块只包含`style`和`structure`。
- `structure`至少包含一个从`0s`开始的段落；后续秒点严格递增。
- 秒点是当前Cue内部的绝对时间，不是全片TC，也不是Clip编号。
- 不要求使用全部标签；选择与Cue弧线相符的最少结构。
- 官方标签是结构控制语法。电影Cue可把`Verse`理解为建立、`Chorus`理解为主陈述 / 峰值、`Bridge`理解为转折、`Outro`理解为退出，但这些解释不得写进执行块。

## Style Descriptor Order

`style`优先按以下顺序压缩成一个连贯描述：

1. Instrumental-only与音乐层排除声明
2. Narrative function and emotional arc
3. Genre / cultural / period frame
4. Tempo, meter, pulse and rhythmic density
5. Instrumentation and timbre hierarchy
6. Motif, harmony and tonal tension
7. Dynamic and arrangement evolution
8. Relationship to dialogue, action and edit points
9. Mix, space, ending and loop / non-loop requirement
10. Avoid list

不要堆砌互相冲突的形容词。优先可听见、可编曲、可混音的描述，而不是“高级、震撼、电影感”等空词。

## Film Cue Timing

- 根据Cue Target Duration设置结构转折，最后一个标签是最后一段的开始时间，不等于结束时间。
- 对话保护区可通过降低密度、减少中频主奏、降低瞬态和退出旋律表达；若需要真正留白，应在Spotting Map中切断Cue，而不是要求模型“生成一段无音乐”。
- 转场Cue的结构点对齐剪辑或叙事触发，不机械匹配每个镜头切点。
- 一个Cue跨多个Clip时使用一份连续Prompt并在外部列出全部Related Clip(s)；不要为每个Clip重置同一音乐。

## Clip Traceability

Clip归属属于交付元数据，推荐标题：

`# MUS-CUE-003｜CLIP-006｜标题 SeedMusic纯音乐提示词`

跨Clip时可写：

`# MUS-CUE-003｜CLIP-006—CLIP-008｜标题 SeedMusic纯音乐提示词`

并在代码块外记录`Related Clip(s):`。不得在`style`或`structure`中加入“给CLIP-006配乐”“用于某视频”等追踪文字。

## Explicit Vocal Modes

### VOICE TEXTURE

只有用户明确要求人声纹理、合唱、哼唱、吟唱或Vocalise时使用。必须写明是否有可辨识词语、语言、声部、性别 / 年龄范围、进入段落及与器乐的关系；不得自动升级为歌词歌曲。

### LYRICS / SONG

只有用户明确要求歌词或歌曲时使用。Lyrics与Descriptors分离；先确认语言、歌词内容、段落分配和演唱要求。不得从剧情对白自动生成歌词。

## Audio Reference

用户提供并授权Audio Reference时，明确选择：

- `Continuation`：保留参考中的旋律、节奏等特征，像其后续段落。
- `Style Transfer`：旋律与和弦不同，但整体风格相属。

没有实际Reference不得声称使用Audio Prompt。不得要求复制受版权保护作品或模仿特定在世艺术家；应转译为类型、年代、配器、节奏、和声、动态和混音特征。
