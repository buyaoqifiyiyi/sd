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


### Prompt Attention / Control Allocation

提示词不是越长越好。系统不声称能够直接或精准设置模型内部的交叉注意力数值；这里的“Attention / Control Allocation”只表示对最终输入信息做可执行的优先级分配、去重、去冲突与按需填充。

对每个当前生成单元必须按以下顺序处理信息：

1. 已由Active Canonical References、合法首尾帧、Confirmed Spatial Blocking或其他上游事实锁定的维度，只保留资产引用、版本/身份和不得改变项的最小确认，不在正文长篇复述。
2. 当前Clip尚未锁定、且会显著影响本次输出的动作、空间、摄影机、时间顺序、状态变化、声音或视觉质感，必须明确写出。
3. 与当前Clip无关的信息删除；仅因“可能有帮助”、Registry中存在或以前使用过，不构成保留理由。
4. 同义重复合并为一条高优先级指令；互相冲突或优先级不明的描述先按上游事实与当前镜头目的消解，不能消解时返回事实拥有者，不把冲突一起交给模型。
5. 高优先级主体、动作、空间、镜头和状态承接必须比装饰性风格词、器材名与质量形容词更清楚。

Template要求的固定字段仍必须完整、非空；“压缩”只删除低价值重复信息，不授权删字段、改字段、写“同上”或丢失已确认生产语义。STATE-08的详细矩阵、抽象转译、物理锚定与压缩QA由`knowledge/prompt_compilation/state08_projection.md`统一定义。

### Prompt Pollution Control

Prompt Pollution不是“字数过长”的同义词。长Prompt只要信息有效、优先级清楚且彼此兼容，可以成立；短Prompt如果包含冲突、抽象空词或错误语义触发，同样属于污染。判断标准固定为：信息是否服务当前Clip、是否重复、是否冲突、是否会误触发不需要的默认视觉模板，以及是否挤压主体、动作、空间、镜头、时间状态与必要风格的控制位置。

以下十类只作为现有Prompt Attention / Control Allocation、连续性、资产、参数、风格与反向限制规则的统一诊断名称，不创建平行Workflow、最终字段或第二套Schema：

1. **Repetition Pollution**：重复描述同一人物、环境、动作或风格；先执行`knowledge/prompt_compilation/state08_projection.md`的Field Ownership Assignment / State Once Gate，为每条约束指定一个权威字段，再把其他位置压成真实状态变化、边界接口或局部高风险所需的最短Delta。Template字段完整不等于同一状态全文重复。
2. **Conflict Pollution**：机位、运镜、动作、空间或状态互相冲突；按上游事实和当前Clip目标消解，无法消解则返回事实拥有者。
3. **Abstract Pollution**：重要的导演名、流派名、题材风格名、情绪标签或审美大词孤立存在，或解释仍停留在另一组抽象词；执行Abstract-to-Executable Translation与Style Label Expansion。
4. **Negative Pollution**：大段否定式提示激活不需要的概念或仍难稳定执行；能正向锁定的先改为Positive Target State。
5. **Semantic Trigger Pollution**：用高共现大词调用模型默认视觉模板，带入当前Clip不存在的场景、服装、道具、天气或美术元素；执行Semantic Template Decomposition。
6. **Asset Redescription Pollution**：正式角色、环境或道具参考已锁定后，正文仍长篇重述或与资产不一致；回到资产引用、当前状态与本Clip特有风险的最小确认。
7. **Parameter Pollution**：无可见收益的工程级小数、精密轨迹或伪物理承诺；按Physical Data Value Rule保留、降精度或删除。
8. **Cross-Shot Pollution**：把前后镜头或其他Clip的动作、机位、状态与风格残留混入当前局部镜头；只保留合法继承项、当前变化和明确Handoff。
9. **Style Stack Pollution**：同时堆叠过多导演、美术、摄影、渲染与质量标签而互相稀释；只保留彼此兼容且服务当前Clip的最小风格集合，并转译成具体行为。
10. **Priority Pollution**：关键主体、动作、空间、镜头与状态承接被装饰性描述淹没；重新按本Rule的控制优先级组织。

Semantic Template Decomposition不完全禁止“创业、约会、学生、婚礼、医院、黑帮、赛博朋克、日系青春”等上游叙事/风格标签。进入最终Prompt前必须判断该词是在表达当前Clip必要身份，还是只在调用默认视觉包；若主要为后者，拆成当前Clip实际存在的人物、动作、场景、道具、服装、光线与声音。必要标签可以保留为上游意图，但最终执行控制必须由具体可见/可听元素承担。导演名、流派名、题材风格名、情绪标签与“电影级 / 高级感 / 治愈感 / 青春感 / 潮湿夏日”等审美大词的Style Label Expansion算法统一由`knowledge/prompt_compilation/state08_projection.md`拥有，本Rule不复制载体清单。


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

合法的单一首帧/尾帧；禁止Storyboard图片、分镜板、拼图、Scene Top-down Blocking Map或多画面参考。只有`knowledge/clip_preflight_check.md`的Before-Single-Clip-Prompt Gate判定REQUIRED、通过Sketch Validation并注册为当前Clip Confirmed Visual Anchor的中性单图`REF-SKETCH`，可作为受限Blocking / Pose / Axis / Camera / Action Path参考；它不是Storyboard、Canonical Asset或最终画风参考。


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
- Confirmed Clip Production Plan（Seedance 2.0每个Clip为4—15秒；Seedance 2.5为4—30秒，16—30秒须严格预检PASS；实际秒数由用户在模型窗口内选择，未知网关状态不得预先压缩；可含1个或多个相邻兼容Shot；每个Clip只生成一条连续Prompt）


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


导演名、影片名、流派名、题材名、情绪标签与审美大词首先视为上游风格意图或Knowledge Retrieval Label，不是模型必然精准复现的控制参数。不得只把“某导演式”“电影感”“高级感”“治愈感”“青春感”“黑帮感”“广告感”或类似标签加入最终Prompt。

进入STATE-08前，重要风格标签必须按`knowledge/prompt_compilation/state08_projection.md`唯一拥有的Style Label Expansion Rule处理：标签可以保留；当它在最终Prompt中首次出现时，必须在紧跟文字或同一`主风格`段给出Project-specific Style Meaning与当前Clip少量高价值、可观察且可执行的style carriers。具象化后不得默认删除标签；标签完全冗余、与当前Clip无关、互相冲突或形成Semantic Trigger Pollution时允许省略，而不是强制省略。

项目风格已由正式Visual Direction、Project Bible或Canonical视觉资产锁定时，后续连续Clip按`Source Carries State, Prompt Carries Delta`只补当前Clip差异和风险；未锁定、独立交付或含义发生变化时重新展开受影响部分。同一标签在同一Prompt中不得重复解释。

风格信息始终低于主体、动作、空间、时间顺序、摄影机行为与状态承接；复杂动作Clip必须优先压缩风格描述，不得让风格标签或载体堆叠淹没执行信息。


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


数字与物理描述按视觉控制价值使用，而不是把生成模型当作Blender / Unreal式严格物理仿真器：

- 高价值视觉关系：左右/前后、人物距离关系、90°/180°转身、约3秒/5秒、眼平/低机位、从A到B、固定距离跟随等，可直接保留。
- 中高价值摄影执行：24/35/50/85mm等焦段倾向、约5秒推进、约120°环绕、景别转换等，可作为视觉效果与摄影行为提示，但不承诺工程精度。
- 低价值工程精度：1.37m、2.43m、0.137m/s、0.166m/s²、53mm、精确轨迹坐标等，除非用户或目标模型明确要求且该数值会改变可见结果，否则压缩为眼平/低机位、近/中/远距离、慢/中/快、约X秒、约X度或起止景别等模型更可执行的关系。

生成模型消费的是数字对应的视觉关系与运动效果，不是逐项执行精密摄影测量或刚体仿真。不得为了显得专业保留无实际生成价值的小数精度。


STATE-08必须先消费与LOCKED Target Video Model一一匹配的内部Model Compilation Template；它只影响模型语义编译，绝不增加或改变最终字段。最终Prompt只允许在固定字段`时长：`中写一次来自Confirmed Clip Production Plan、由用户选择的“平台生成时长：N秒”：Seedance 2.0为4—15秒；Seedance 2.5为4—30秒，16—30秒只在内部严格预检PASS时成立；未知网关状态不得预先压缩该时长。只有`Target Model = Seedance 2.5`且`Execution Mode = Targeted Edit`时，才可在既有分镜正文的合适字段写受控时间段语义；不得新增时间轴字段。其他模式禁止写分镜时间码、单分镜时长、按秒动作区间、帧率或帧数；帧率和帧数仍只能作为Prompt外部平台参数。

STATE-08格式必须逐Clip严格服从`templates/10_video_prompt.md`固定契约：每个Clip结构完全相同，Template当前定义的无条件字段按顺序完整保留；条件字段只在Template的显式条件成立时出现，不得为了结构齐全输出空字段或状态占位。不得因批量或篇幅压缩、合并、共享、删减或改名无条件字段。内容过长时只在完整Clip之间自动分批。每个分镜的全部无条件字段必须按Template完整输出，不得增加竞争字段。任何旧格式冲突以Template为最高优先级，输出前必须逐Clip执行字段完整性检查。


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

## Voice Identity Prompt Omission And Explicit Override

STATE-08默认执行`Source Carries State, Prompt Carries Delta`：角色声音身份由外部音频资源、Confirmed Voice Profile或制作系统状态携带，常规视频Prompt不重复描述。用户没有明确要求把声音控制写进当前视频模型Prompt时：

- 不检查Voice Profile / Voice Reference是否存在，不把缺失视为错误；默认外部已有可用角色音色资源。
- 即使存在Confirmed Voice Profile或Voice/Audio Reference，也不把它们列入`参考资产：`，不复制或改写Voice Profile，不输出`音色特征：`字段。
- 不写“默认音色”“已有音色”“参考音色锁定”“未建立音色资产”“No Voice Asset”“无对白”等声音身份状态文案。
- “台词”可保留准确文本与当前句/当前场景的必要Dialogue Performance，例如轻声、克制、短暂停顿、说到某词时加重；不得借此重定义pitch、timbre、resonance、vocal weight、音高、声线、音域、共鸣或音色质感。
- “音效”只处理对白同步、声源位置/距离/遮挡、环境声、动作声、Foley、呼吸与声音尾部；不得承载Voice Identity。

只有用户当前请求明确要求“把声音/音色控制写进本次视频Prompt”、明确要求当前视频使用某Voice/Audio Reference，或给出无歧义同义授权时，才启用`音色特征：`条件字段，并只写当前模型执行所需的最小Delta：优先引用实际适用且获授权的Reference；用户明确要求文字控制时才提取必要Voice Profile特征。不得跨字段重复，不得自动调用AUDIO模块，不得把该授权外推到后续Clip。Candidate、未授权或与当前CHAR Version不一致的音频不得使用。

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


最终Seedance视频Prompt中，`反向提示词：`必须逐Clip且只出现一次，并由`templates/10_video_prompt.md`固定为当前Clip最后一个字段、最后一个段落；其后不得再出现分镜、说明、备注或其他正文。

`主风格 / 人物一致性 / 环境一致性 / 参考区 / 各分镜字段`等位于其前的正文必须以正向、可执行、可观察的目标状态为主。通用的“禁止…… / 不要…… / 避免……”限制、生成错误规避项和跨字段适用的负向清单不得零散塞入正文，必须统一归并到末尾唯一的`反向提示词：`。

执行`Negative Constraint → Positive Target State`：优先描述画面应该是什么，而不是反复提及不应出现的概念。例如“不要下雨”优先改为“晴天，空气清透，阳光照亮地面”；“不要夸张表情”优先改为“表情克制，嘴角和眉眼只有轻微变化”。“禁止夸张微笑、甜宠式表演、广告摆拍、MV慢动作与炫技运镜”应优先转成“表演克制含蓄，镜头调度简洁自然，优先服务人物关系与情绪留白”等正向执行要求；仍属当前Clip高风险且正向状态难以完全锁定的残余错误，才压缩后进入末尾反向提示词。如果正向状态已经充分锁定，不再把同一要求重复塞进反向提示词。

唯一局部例外：某项约束若必须紧贴某个具体分镜动作、空间关系或物理连续性才能消除指代歧义或防止执行错误，允许在该分镜对应字段保留一条最小必要的约束性说明。仍优先写成正向持续状态，例如`左手持续握住伞柄，整个动作链保持左手持有`；只有正向句仍无法明确边界时才保留最短局部否定。该例外不得扩展成通用负向清单，也不得把同一通用限制复制到多个分镜；跨镜通用部分仍归入末尾唯一反向提示词。逐镜的结尾稳定、禁止提前动作和合法衔接属于此类局部边界，但必须保持最小、贴近受控动作并服务连续性，不能被机械移走导致执行不清。


反向提示词只汇总当前生成段真正高风险、难以通过正文正向状态完全锁定的错误。删除低价值、抽象化、与正文重复、同义重复或与当前Clip无关的项；历史事故物、其他Clip状态和未来情节默认删除，同类项合并压缩为当前Clip失败类别，且不得在篇幅或语义权重上压过主体、动作、空间、摄影机、时间顺序和状态承接。具体Negative Compression算法只由`knowledge/prompt_compilation/state08_projection.md`拥有，本Rule不复制类别表或阈值。

“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”是STATE-08永久平台边界，不受“只选项目高风险项”规则影响，必须作为【反向提示词】首个非空内容行保留，不存在任何省略或Clip例外。


禁止：

- 把每镜边界合同替换成一长串负面词
- 在每个镜头重复相同负面限制
- 在`主风格`、一致性字段或逐镜正文散布通用负向清单
- 在同一Clip创建多个`反向提示词：`段，或在其后追加任何正文
- 用反向提示词掩盖人物、空间、道具或剧情状态矛盾
- 机械复制与当前项目无关的通用限制
- 把已经正向锁定的要求在反向提示词中同义复述
- 为压缩反向提示词而移走必须贴近具体动作、空间或物理连续性的最小局部约束


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

用户未明确要求把声音控制写进当前视频模型Prompt时，是否完全省略`音色特征：`、Voice/Audio Reference、Voice Profile及声音资产状态文案；用户明确授权时，是否只投影当前Clip所需的最小声音控制Delta且没有跨字段重复。Dialogue Performance是否只说明当前一句怎么说，没有重定义稳定Voice Identity，也没有自动触发AUDIO模块。

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


除【时长】中来自Confirmed Clip Production Plan、由用户选择的单一“平台生成时长：N秒”（2.0为4—15秒；2.5为4—30秒且16—30秒内部严格预检PASS）外，且不属于已锁定Seedance 2.5 Targeted Edit在既有分镜正文中的受控时间段语义时，最终Prompt是否完全不包含：

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
