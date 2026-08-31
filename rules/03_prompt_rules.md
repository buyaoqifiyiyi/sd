# Prompt Rules

# AI影视Prompt生成规则


## Purpose

本规则用于约束SD Film中的所有Prompt生成行为。

负责：

- Prompt阶段边界
- 图片与视频Prompt区分
- 资产引用
- 连续性
- 时间与动作逻辑
- Seedance执行要求
- 输出Schema归属
- 最终质量检查

本文件负责：

规则约束。

本文件不负责：

定义最终输出字段名称。

最终输出格式由对应Template统一定义。


---

# Rule 01

# General Prompt Principle

所有Prompt必须服务于当前影视生产阶段。

必须符合：

视觉逻辑。

空间逻辑。

时间逻辑。

动作逻辑。

角色逻辑。

环境逻辑。


禁止：

只堆叠形容词。

只堆叠摄影关键词。

只堆叠导演名称。

只描述静态结果而忽略生成任务需要的执行信息。


Prompt必须：

明确。

可执行。

可验证。

可以被下一生产阶段继续使用。


---

# Rule 02

# Language Rule

默认输出语言：

中文。


用户未指定语言时：

Prompt主体使用中文。


专业影视术语可以保留英文，例如：

- Close Up
- Dolly In
- Tracking Shot
- Handheld
- Shallow Depth of Field
- Eyeline Match
- Match on Action


禁止：

在用户没有要求英文Prompt时，无原因把完整Prompt切换为英文。


如果用户明确指定：

英文。

中英双语。

其他语言。


则按照用户要求执行。


---

# Rule 03

# Character Consistency Rule

涉及人物生成时：

必须优先读取已确认角色资产。


保持：

脸部特征。

脸型。

年龄感。

发型。

发色。

服装。

身体比例。

人物气质。

当前状态。


同一角色跨镜头时：

上一镜头结束状态必须成为下一镜头的连续性依据。


Continuous Handoff中直接继承。


Motivated Discontinuity中只改变已确认剧情授权的时间、场景或角色状态；身份、资产版本以及未获授权的状态仍受上一镜头约束。


禁止：

无剧情依据换脸。

无剧情依据换装。

无剧情依据改变年龄。

无剧情依据改变发型。

无剧情依据改变身体比例。


已有Character Asset时：

资产优先级高于临时文字描述。


如果角色已经有用户明确指定的外观基准，或Asset Registry中的Active CHAR Version与Canonical References：

该Active角色资产包及其Canonical References是所有图片Prompt、Storyboard Prompt、Poster/Key Art Prompt、首尾帧Prompt、视频Prompt、Seedance Prompt和最终视频生成的唯一外观基准。

Prompt必须锁定并继承：脸型、五官、年龄感、发型、头饰、体型、身高与身体比例、服装形制、主配色与辅助配色、物种形态、羽毛/毛发特征，以及非人角色身体结构和非拟人化边界。

只要求动作、姿势、表情、机位、景别、构图或镜头运动变化时，Prompt只能改变相应维度，必须明确禁止重新设计角色外貌、服装基础、物种或身体结构。锁定为非人本体的角色不得被Prompt拟人化；例如孔雀本体不得写成人形、半人形或人类身体比例。

新参考、导演风格、模型适配或生成结果与锁定角色资产冲突时，以锁定资产为最高视觉身份优先级。Prompt不得混合冲突特征求折中；需要改变外观时必须先返回STATE-03并按`references/asset_lock_contract.md`完成新Version确认。


---

# Rule 04

# Environment Consistency Rule

涉及环境生成时：

必须优先读取已确认环境资产。


保持：

地点。

时间。

天气。

空间结构。

建筑位置。

道路方向。

关键背景元素。

主要光源方向。

综合色彩关系。


连续镜头之间：

不得无理由改变环境。


禁止：

空间跳变。

天气跳变。

昼夜跳变。

建筑位置变化。

主要环境结构变化。


已有Environment Asset时：

资产优先级高于临时文字描述。


---

# Rule 05

# Image Prompt Rule

图片生成Prompt用于：

角色资产。

环境资产。

道具资产。

场景视觉开发。

合法的单一首帧/尾帧；禁止Storyboard图片、分镜板、线稿、拼图或多画面参考。


图片Prompt重点描述：

人物。

环境。

构图。

光影。

材质。

色彩。

静态瞬间。


禁止：

把复杂连续时间动作写入单张图片Prompt。


禁止：

将视频Prompt直接当作图片Prompt使用。


图片Prompt描述的是：

一个明确视觉时刻。


视频Prompt描述的是：

一段时间中的变化。


二者必须区分。


---

# Rule 06

# Video Prompt Rule

视频Prompt必须表现：

时间。

动作。

空间变化。

摄影机行为。

人物表演变化。


每个重要动作必须能够理解为：

开始状态

↓

动作过程

↓

结束状态


错误：

人物拥抱。


正确逻辑：

人物保持距离。

↓

其中一人靠近。

↓

另一人产生反应。

↓

双方完成接触。

↓

动作停留形成结果。


禁止：

只描述人物最终状态。


禁止：

把静态图片Prompt增加“cinematic”后直接作为视频Prompt。


---

# Rule 07

# Video Generation Stage Rule

最终视频生成Prompt只允许在：

STATE-08 Clip-based Video Prompt / Video Generation


阶段生成。


进入STATE-08前：

必须确认当前项目已经具备相应生产输入。


包括：

- 已确认资产
- Visual Development结果
- Scene Breakdown
- Shot Design
- Confirmed Detailed Shot Design（生产数据，不作为视觉参考）
- Confirmed Clip Production Plan（Prompt最小单位）
- Confirmed Clip Production Plan（每个Clip为4—15秒，可含1个或多个相邻兼容Shot；每个Clip只生成一条连续Prompt）


如果必要前置阶段没有完成：

不得直接生成最终Seedance Prompt。


用户要求的最终结果：

不能自动覆盖生产流程。


---

# Rule 08

# Shot Execution Rule

STATE-08的视频Prompt必须建立在：

Shot Design

和

Detailed Shot Design

和

Confirmed Clip Production Plan

基础上。


最终视频Prompt必须保持：

镜头独立性。

动作可执行性。

空间可理解性。

人物方向明确。

镜头间连续。


其中：

镜头独立性表示每个镜头的指令能够单独理解和执行。


它不允许每个镜头重新初始化人物、道具、环境或动作状态。


每个镜头仍必须遵守：

rules/04_consistency_rules.md中的Shot Boundary Contract与Transition Classification。


禁止：

把整段剧情直接整理成一个长段落Prompt。


禁止：

只输出：

剧情简介。

人物介绍。

环境介绍。

摄影风格列表。

关键词合集。


这些信息可以作为输入。

但必须在Video Generation Workflow中转换为：

可执行镜头信息。


---

# Rule 09

# Final Schema Ownership Rule

这是SD Film中关于视频Prompt格式的唯一归属规则。


Rules负责：

约束生成行为。


Workflow负责：

转换生产信息。


Knowledge负责：

提供专业辅助。


Template负责：

最终输出Schema。


因此：

STATE-08最终Seedance视频Prompt的：

字段名称。

字段顺序。

镜头编号格式。

章节结构。


必须以：

templates/10_video_prompt.md


为唯一格式来源。


本文件不得：

定义另一套最终字段。


Workflow不得：

定义与Template竞争的另一套最终字段。


Knowledge不得：

把内部分析维度作为最终输出字段。


如果其他文件中的字段名称：

与templates/10_video_prompt.md不同。


最终输出时：

必须以templates/10_video_prompt.md为准。


---

# Rule 10

# Input Format Remapping Rule

上游生产阶段可以拥有自己的字段。


例如Shot Design可能包含：

景别。

焦段。

机位。

运镜。

速度。

光影。

色调。

情绪功能。


这些字段属于：

Shot Design生产信息。


进入STATE-08后：

不得因为上游已经存在这些字段，

就直接复制为最终Seedance Prompt格式。


必须执行：

上游信息读取

↓

语义解析

↓

Seedance执行转换

↓

Template Schema映射

↓

最终输出


也就是说：

保留信息。

不保留上游字段结构。


禁止：

DO NOT PRESERVE THE INPUT SHOT FORMAT。


最终格式必须服从：

templates/10_video_prompt.md。


---

# Rule 11

# Asset Reference Rule

视频Prompt优先引用：

已确认资产。


优先级统一服从：

references/asset_lock_contract.md

Prompt只能使用Asset Registry中Active Version及其Canonical References。用户当前补充若改变资产，应先返回Asset Workflow建立并批准新Revision。


已有明确Asset时：

不得重新设计角色。

不得重新设计环境。

不得重新设计关键道具。


用户明确要求修改资产时：

先更新对应资产阶段。

再进入后续视频生成。


角色外观与形态还必须执行`references/asset_lock_contract.md`中的Canonical Character Appearance And Form Lock。任何Prompt都不得把构图参考、动作参考、风格参考、Storyboard或上一轮生成结果提升为新的角色身份来源；它们只能提供已授权的动作、姿势、表情、机位、景别、构图、光影或镜头运动信息，且不得覆盖Active CHAR Version。


---

# Rule 12

# Spatial Continuity Rule

涉及两个或多个角色时：

必须明确检查：

人物左右位置。

面对方向。

视线方向。

行进方向。

距离变化。

180度轴线。

动作连接。


尤其是：

相向行走。

对峙。

战斗。

对话。

拥抱。

追逐。


禁止：

剧情要求人物面对彼此，

但两人同时正面对摄影机。


禁止：

人物上一镜头向右运动，

下一镜头无原因改为向左运动。


禁止：

视线方向与人物空间位置矛盾。


---

# Rule 13

# Prop Continuity Rule

关键道具必须具有：

持有者。

位置。

方向。

状态。


如涉及：

雨伞。

武器。

手机。

书籍。

信件。

车辆。

关键饰品。


必须检查：

上一镜头结束状态

↓

下一镜头开始状态


禁止：

道具瞬移。

自动换手。

无动作消失。

无原因重新出现。

状态突然改变。


---

# Rule 14

# Emotional Continuity Rule

人物情绪必须具有合理过程。


推荐逻辑：

初始状态

↓

刺激事件

↓

人物反应

↓

确认

↓

行动选择

↓

情绪变化

↓

结果


禁止：

无铺垫情绪突变。


禁止：

为了戏剧效果自动增加：

夸张哭泣。

尖叫。

突然奔跑。

突然拥抱。

夸张肢体动作。


除非：

剧情明确要求。


情绪优先通过：

眼神。

呼吸。

停顿。

手部动作。

身体距离。

面部微表情。


进行表达。


---

# Rule 15

# Camera Language Rule

Camera Language必须服务于：

剧情。

情绪。

人物关系。

空间表达。


禁止：

为了增加“电影感”随机加入复杂镜头。


例如：

无理由360度环绕。

无理由快速推镜。

无理由无人机镜头。

无理由穿墙镜头。

无理由旋转镜头。


复杂摄影机运动：

必须存在明确叙事目的。


镜头语言知识：

用于辅助Shot Design和Video Generation。


不得：

替代剧情逻辑。


---

# Rule 16

# Director Style Rule

如果用户指定：

导演。

影片。

视觉美学。

摄影参考。


不得：

仅把导演姓名加入Prompt。


必须转换为：

构图特征。

镜头运动。

焦段倾向。

灯光逻辑。

色彩关系。

剪辑节奏。

人物表演。

情绪表达。


最终Prompt主要使用：

可执行视觉语言。


导演或作品名称：

只作为辅助参考。

不能替代实际摄影描述。


---

# Rule 17

# Cinematic Parameter Rule

摄影设备与技术参数：

必须服务于已确认视觉开发。


可以包含：

摄影机。

镜头。

焦段。

滤镜。

光圈。

画幅。

胶片模拟。


禁止：

为了显得专业而无逻辑堆叠：

ARRI。

RED。

IMAX。

Cooke。

Anamorphic。

8K。

cinematic masterpiece。

award winning。


如果项目没有确认某项参数：

不得强制虚构不必要的设备设置。


STATE-08最终Prompt只允许在固定字段`时长：`中写一次来自Confirmed Clip Production Plan的“平台生成时长：N秒”，且N必须为4—15秒。禁止写分镜时间码、单分镜时长、按秒动作区间、帧率或帧数；帧率和帧数仍只能作为Prompt外部平台参数。

STATE-08格式必须逐Clip严格服从`templates/10_video_prompt.md`固定契约：每个Clip结构完全相同，Template当前定义的全部字段按顺序完整保留；不得因批量或篇幅压缩、合并、共享、删减或改名字段。内容过长时只在完整Clip之间自动分批。前置资产/首尾帧/声音身份等无条件语义与每个分镜的全部字段必须按Template完整输出，不得增加竞争字段。任何旧格式冲突以Template为最高优先级，输出前必须逐Clip执行字段完整性检查。


---

# Rule 18

# Sound Rule

视频生成阶段必须考虑声音逻辑。


STATE-08 Seedance提示词中的声音只可以包括：

环境声。

动作声。

对白。

呼吸、衣料、脚步、道具与其他同期Foley。

剧情内真实播放源或现场声。

## Voice Reference Override Gate

每个Clip在编译声音文字前，必须先检查当前有对白角色是否已经由用户明确提供音色参考资产，或Active CHAR Version是否存在可用于当前目标模型的Confirmed Voice Audio Reference / Audio Reference / Voice Reference。

如果存在适用音色参考资产：

- 声音身份只由该Reference锁定；STATE-08不得再用文字重新定义角色音色。
- 最终Prompt仍必须保留固定字段`音色特征：`，写明声音身份由Reference锁定且不得以文字重新定义；不得输出空字段、占位或“见参考资产”。
- “台词”“音效”及其他字段不得出现Voice characteristics、音高、声线、音域、共鸣、语速、音色质感等描述，也不得把Confirmed Voice Profile换一种措辞重新写入。
- “台词”只允许保留准确台词和必要的轻量表演指令，例如“轻声说”“无奈地说”“短暂停顿后说”；不得借表演指令重新规定声音身份。
- “音效”仍可记录对白/口型同步、声源位置、距离、遮挡与同期声空间，并继续满足环境底声、同步前景声和声音尾部硬门槛。

只有当前角色没有适用音色参考资产、但已经存在Confirmed Voice Profile时，才在`音色特征：`中投影必要的文字声音描述。两者都不存在且有对白时，必须写明未建立独立音色资产、本Clip不创建或推导声音身份，不得自动调用AUDIO模块或返回STATE-03。全段无对白时也必须保留字段并明确无对白。Candidate、未授权或与当前CHAR Version不一致的音频不得触发本Gate，除非用户明确把当前已提供资产指定为本次Voice Reference。

每个“音效”字段必须同时具备：

- 具体环境底声/空间底噪，或说明理由的有意静默
- 至少一个与可见动作同步的前景层：动作声、Foley、呼吸、对白或剧情内声源
- 本镜声音尾部及其跨镜Bridge / Cut / Fade / Unresolved状态

“无”“静音”“无音效”“有效内容”以及只写背景音乐禁令均判定为声音缺失。


如果没有对白：

应明确无对白。


默认禁止：

在“音效”字段中写入背景音乐、配乐、BGM、歌曲、电影配乐、主题音乐、氛围音乐、节拍或“无配乐”等音乐说明。

由Seedance生成任何背景音乐。音乐设计只属于用户显式调用的独立MUSIC / SEED-MUSIC模块，不进入STATE-08声音或其他字段。

最终【反向提示词】首个非空内容行必须逐字写“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”，不得省略、改写或移到其他限制之后。

该禁令不存在用户、Clip、批量或模型例外。用户要求配乐时必须经`workflows/music_router.md`分流至独立MUSIC / SEED-MUSIC模块；视频Prompt仍保留固定首句，现有“音效”及其他字段不得追加任何非剧情内音乐指令。


声音变化必须：

服务镜头情绪。

服务空间。

服务剪辑。


---

# Rule 19

# Editing Rule

视频生成阶段必须考虑镜头连接。


检查：

镜头如何进入。

当前镜头如何保持。

动作在哪里结束。

如何进入下一镜头。


转场必须读取`knowledge/transitions/`并按Decision Engine自动判断：先判定Continuous Handoff、Motivated Discontinuity或Unresolved Handoff，再选择一种主要技术。

默认使用Direct Cut。只有存在可验证的动作、视线、反应、构图、方向、尺度、同期声音、完整遮挡、光态或FX锚点时，才选择相应的Match、Sound Bridge、Occlusion、Dissolve、Fade、Flash或其他已确认技术。

推、拉、摇、移、跟、升降、环绕、甩镜、俯冲、贴地推进和变焦本身不是转场；没有明确切点与下一镜匹配条件时只作为运镜。

大多数转场由后期完成。STATE-08优先生成可剪辑的出镜/入镜把手，不得要求模型无依据地把两个无关场景连续变形。


禁止：

为了炫技无理由增加转场。

在同一边界堆叠多个主要视觉转场。

在上游未确认时新增火焰、烟雾、雨雪、强光、镜面传送、魔法、人物变身或空间穿越。

使用背景音乐、配乐或歌曲建立STATE-08声音转场。


剪辑必须优先保证：

动作连续。

空间连续。

情绪连续。


---

# Rule 20

# Model Adaptation Rule

最终Prompt必须根据目标视频模型进行适配。


模型适配可以调整：

描述密度。

动作粒度。

镜头运动复杂度。

参考图使用方式。

内部动作节奏与动作密度。

模型特定限制。


但是：

模型适配不得改变：

剧情事实。

角色身份。

资产设定。

人物关系。

镜头核心目的。

连续性。


Seedance适配知识：

用于辅助执行。


不得：

重新定义最终输出Schema。


---

# Rule 21

# Prompt Revision Rule

用户要求修改视频Prompt时：

优先修改：

用户指出的问题。


例如：

人物方向错误。

角色面向镜头。

动作过快。

人物不一致。

环境变化。

雨伞错误。

表演过度。


禁止：

因为修改一个局部问题，

无必要重新设计：

整个剧情。

全部镜头。

角色资产。

视觉风格。


遵守：

最小必要修改原则。


---

# Negative Prompt Boundary Rule


逐镜的结尾稳定要求、禁止提前动作和合法衔接必须优先写成对应镜头的正向可执行约束。


反向提示词只汇总当前生成段真正高风险的错误。

“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”是STATE-08永久平台边界，不受“只选项目高风险项”规则影响，必须作为【反向提示词】首个非空内容行保留，不存在任何省略或Clip例外。


禁止：

- 把每镜边界合同替换成一长串负面词
- 在每个镜头重复相同负面限制
- 用反向提示词掩盖人物、空间、道具或剧情状态矛盾
- 机械复制与当前项目无关的通用限制


反向提示词的最终位置和字段名称仍由当前阶段Template定义。


---

# Rule 22

# Final Validation Rule

所有视频Prompt输出前必须执行最终检查。


检查：

## Stage

当前是否已经进入STATE-08。


## Assets

角色、环境、道具是否引用正确。


## Story

是否改变原剧情。


## Character

角色是否一致。

是否逐角色核对Active CHAR Version与Canonical References，并完整继承脸型、五官、年龄感、发型、头饰、体型、比例、服装形制、主配色/辅助配色、物种形态、羽毛/毛发特征及非人身体结构。

动作、姿势、表情、机位、景别、构图或镜头运动变化是否被错误扩展为外观重设计；非人本体是否出现人形、半人形或其他未授权拟人化。

任何新参考或生成结果与锁定资产冲突时，是否明确保留锁定资产并拒绝冲突特征，而不是混合折中。


## Environment

环境是否一致。


## Space

人物方向和空间关系是否正确。


## Action

动作是否具有开始、过程、结果。


## Continuity

前后镜头能否自然衔接。


每镜是否包含起始边界、最后一帧限制和下一镜连接语义。


连续镜头是否直接继承；场景切换、时间跳跃、硬切或故意跳切是否明确重新建立起始状态而没有伪造过渡。


自动衔接是否保持剧情、人物站位逻辑、资产与道具状态，并且没有提前执行下一镜动作。


## Camera

摄影机行为是否合理。


## Sound

声音是否与当前镜头匹配。

有适用音色参考资产时，是否保留非空`音色特征：`并声明由Reference锁定且不得文字重定义，同时删除其他字段中的全部文字音色重定义，只在台词层保留必要轻量表演指令；无适用音色参考资产但已有Confirmed Voice Profile时，是否以其作为文字回退；两者都不存在时是否使用`No Voice Asset`声明且没有自动触发AUDIO模块；全段无对白时是否仍保留字段。

每个Clip的“音效”是否只包含对白、环境声、动作声、呼吸、Foley和剧情内真实声源，且没有任何背景音乐、配乐、BGM、主题音乐、氛围音乐、歌曲、节拍或“无配乐”等说明。

每个Clip的`反向提示词：`首个非空内容行是否无例外逐字为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”，且没有改写、后移或省略。


## Editing

剪辑是否具有连续逻辑。

是否先判定Boundary Class，再只选择一种主要转场技术；是否存在真实切点和出/入镜锚点；普通运镜是否被误当转场；高风险FX/奇幻转场是否有上游依据。


## Schema

最终输出是否严格服从：

templates/10_video_prompt.md。


如果Schema不符合：

重新映射格式。


不得：

自行创造新的输出字段。


## Timeline


除【时长】中来自Confirmed Clip Production Plan的单一“平台生成时长：N秒”（4—15秒）外，最终Prompt是否完全不包含：

- 时间码或起止时间戳
- 总片时长、单分镜时长或Clip内部逐镜时长
- 按秒分段
- 帧率、帧数或帧区间限制


Clip目标时长映射到【时长】一次；其余上游时长只允许用于内部执行性判断。


---

# Final Principle

Prompt不是最终目的。

Prompt是影视生产执行工具。


SD Film中的Prompt必须做到：

资产可追踪。

动作可执行。

镜头可理解。

空间可验证。

连续性可检查。

格式可稳定复用。


在STATE-08：

Rules定义约束。

Workflow完成转换。

Knowledge提供辅助。

Template定义最终Schema。


最终Seedance Prompt只能有：

一个最终格式真源：

templates/10_video_prompt.md
