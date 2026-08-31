# MUSIC / SEED-MUSIC Score Workflow

## Module Position

本Workflow是用户显式调用的Optional/Auxiliary Music / Score模块，不创建主STATE，不占用STATE-00—09，也不自动成为Editing或Review步骤。

唯一入口是`workflows/music_router.md`的Positive Route。未取得`ROUTE: MUSIC / SEED-MUSIC Score`时禁止读取本Workflow、`knowledge/music_score/`或最终Template。

## Core Boundary

- 非剧情内配乐永远不进入Seedance视频提示词。STATE-08无例外执行固定背景音乐禁令。
- 本模块只负责后期独立音乐规划与SeedMusic交付，不修改视频Prompt、镜头设计、Clip划分或同期声音设计。
- 用户负责后期音乐制作，不表示用户必须亲自决定每个Cue。模块激活后，系统应以配乐导演 / Music Supervisor视角专业决定哪里需要音乐、哪里必须留白。
- 音乐不是全段默认铺设层。每个范围都必须同时评估`MUSIC`与`SILENCE / PRODUCTION SOUND ONLY`，不得因“电影感”自动增加音乐。

## Activation Record

执行前记录：

- `Route: MUSIC / SEED-MUSIC Score`
- `Explicit Trigger Evidence:` 当前用户原话或无歧义摘要
- `Requested Scope:` 全片 / Scene / Sequence / Clip范围
- `Requested Deliverable:` Spotting Plan / Music Bible / Cue Sheet / SeedMusic Prompt / Revision
- `Generation Mode:` `INSTRUMENTAL`（默认）/ `VOICE TEXTURE`（显式）/ `LYRICS / SONG`（显式）

如果没有显式人声或歌词请求，`Generation Mode`必须为`INSTRUMENTAL`。

## Required Inputs

按请求范围读取最小充分输入：

1. 用户当前音乐目标、禁用项与参考方向。
2. 已锁定剧情事实或用户直接提供的片段说明。
3. 可用的Scene / Sequence / Detailed Shot Design / Confirmed Clip Production Plan及时间线。
4. 适用的对白密度、同期声音重点、叙事转折、剪辑边界和已确认后期长度。
5. 用户提供且具有合法来源的音乐、Audio Reference或乐谱；没有时不得虚构。

Clip存在时必须按Clip ID追踪；无Clip Artifact时可用Scene / Sequence标签，但不得伪造CLIP-ID。时长或切点未锁定时，Spotting结果标记`PROVISIONAL`，不输出伪精确秒点。

## Required Resources

- `knowledge/music_score/index.md`
- `knowledge/music_score/spotting_and_silence.md`
- `knowledge/music_score/music_bible_and_cues.md`
- `knowledge/music_score/seedmusic_prompting.md`
- `templates/22_seed_music_score.md`

## Execution

### Step 1｜Scope And Timeline Audit

- 确认请求覆盖的所有Clip / Scene / Sequence及其顺序、时长和边界。
- 标记关键对白、呼吸、环境声、动作声、情绪转折、揭示、动作高潮、蒙太奇和转场。
- 区分`non-diegetic score`与`diegetic music`。剧情内收音机、舞台演奏等属于画面事实；后期配乐属于本模块。两者不得混写。

### Step 2｜Professional Spotting Pass

逐段作出且说明以下选择之一：

- `MUSIC CUE`
- `SILENCE / PRODUCTION SOUND ONLY`
- `DIEGETIC MUSIC ONLY`
- `MUSIC OUT`
- `CARRY-OVER`
- `PROVISIONAL`

每个决定至少说明叙事功能、进入触发、退出触发、对白/动作关系和相邻段连续性。留白必须说明为何不进音乐，以及由哪些同期声音承担张力。不得为了平均分配而强行在每个Clip放音乐。

### Step 3｜Music Bible

为需要音乐的范围建立项目级或局部Music Bible：

- 音乐总体戏剧功能和使用密度
- 主题 / 角色 / 关系 / 地点 / 事件动机
- 每个Motif的音程轮廓、节奏指纹、和声倾向、音色身份与可变形参数
- 禁用的陈词滥调、情绪误导、过度煽情和版权 / 艺术家模仿风险
- Cue之间的继承、变体、回忆、反转和终止逻辑

没有叙事复现价值时不强造主题动机。单次Cue可以只承担结构或节奏功能。

### Step 4｜Cue Architecture

为每个实际`MUSIC CUE`分配独立`MUS-CUE-001...`，不得占用SHOT或CLIP命名空间。建立：

- Related Clip(s) / Scene / Sequence
- Start / End / Target Duration
- Entry / Exit Trigger
- Narrative Function
- Energy Arc
- Dialogue And Action Relationship
- Motif / Harmony / Rhythm / Instrumentation
- Transition And Carry-over Logic
- Silence Before / After

Clip标签是交付追踪元数据，不是SeedMusic生成字段。一个Cue跨多个Clip时明确列出范围；一个Clip含多个Cue时分别列出，不把它们强行合并。

### Step 5｜SeedMusic Compilation

只为`MUSIC CUE`编译提示词；`SILENCE / PRODUCTION SOUND ONLY`不得生成SeedMusic Prompt。

默认`INSTRUMENTAL`执行块只包含：

```text
style:
<音乐描述>

structure:
[Verse]: 0s
<后续段落与绝对秒点>
```

- 纯音乐省略Lyrics输入；`style`中明确器乐限定和人声排除。
- `structure`使用SeedMusic官方示例的`[Verse]`、`[Chorus]`、`[Bridge]`、`[Outro]`标签与绝对秒点。标签是模型结构控制语法，可按电影Cue功能映射，不意味着必须采用流行歌曲形式。
- 第一个结构秒点必须为`0s`；后续秒点严格递增并对齐Cue内部转折。
- Clip归属、Cue标题、时长、叙事功能和使用说明必须放在代码块外，防止污染模型执行输入。
- `VOICE TEXTURE`或`LYRICS / SONG`只有显式触发时允许。歌词文本与演唱要求必须独立标识，不能回写成默认。
- 用户提供Audio Reference时，明确选择`Continuation`或`Style Transfer`；没有Reference时不输出伪造引用。

### Step 6｜Music Review

输出前检查：

- 全范围是否既有配乐判断也有留白判断
- 音乐进入是否晚于必要信息建立，退出是否为对白、动作或情绪留出空间
- 是否出现持续铺底、重复煽情、每Clip必配、主题滥用或无理由转场音乐
- Cue起止、Clip归属与时间线是否一致
- 默认纯音乐是否彻底排除歌词、人声、合唱、哼唱、吟唱、旁白、对白和说唱
- SeedMusic执行块是否只有`style + structure`，结构秒点是否从0开始并严格递增
- 是否把任何配乐指令写进Seedance视频Prompt；如有，删除并恢复STATE-08固定禁令

## Output Routing

最终用户可见字段、顺序和排版只由`templates/22_seed_music_score.md`拥有。

- 用户只要“规划”：可输出Spotting Map + Music Bible + Cue Sheet，不强制生成Prompt。
- 用户要“SeedMusic提示词”：必须先完成必要的Spotting，再输出所需Cue的Prompt，不要求用户逐Cue决定哪里配乐。
- 用户只要某个Clip：审阅该Clip与相邻边界，至少说明前后留白 / Carry-over关系。
- 用户明确要歌词：切换显式模式并输出歌词区；否则永远不输出歌词区。

## Conflict And Return Routes

- 剧情或时间线冲突：返回事实拥有者，不在音乐模块静默改写。
- Clip时长或顺序未确认：标记`PROVISIONAL`，请求最小必要事实；不得伪精确。
- 用户要求把配乐写入Seedance视频Prompt：拒绝混写，拆成视频Prompt与独立Music Package。
- 用户要求模仿特定在世艺术家或复刻受版权保护歌曲：转译为高层音乐特征，不直接模仿或引用。
- 完成本模块后返回调用前Checkpoint；不自动推进主Pipeline。

## Completion Checklist

- Router为Positive且记录显式触发证据
- 范围、模式和交付类型明确
- 全范围Spotting完成，音乐与留白都有专业理由
- 请求范围内或相邻进入 / 退出边界至少存在一处明确的`SILENCE / PRODUCTION SOUND ONLY`；不得交付无留白的全段持续配乐方案
- Cue ID唯一且Clip / Scene归属可追踪
- 默认模式为纯音乐；任何人声或歌词均有当前显式证据
- 每个SeedMusic执行块符合`style + structure`
- 无任何配乐内容进入STATE-08视频Prompt
- 最终输出服从`templates/22_seed_music_score.md`
