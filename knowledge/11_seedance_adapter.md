# Seedance Adapter Knowledge


## Purpose

负责将电影分镜语言转换为AI视频模型可理解的视频执行信息。


Seedance Prompt不是图片描述。


而是：

时间连续的电影镜头执行方案。


本文件属于：

Knowledge Layer。


负责：

Seedance模型理解。

视频动作逻辑。

镜头执行逻辑。

时间连续性。

摄影信息适配。

声音与剪辑辅助。


本文件不负责：

定义最终Prompt字段。

定义最终镜头编号。

定义最终排版结构。


STATE-08最终输出Schema：

只能由：

templates/10_video_prompt.md


定义。

Adapter向Template交接前必须执行固定结构预检：每个Clip都准备完整且相同的八个无条件前置全局字段、一个或多个逐镜完整十字段组和末尾反向提示词；`参考资产：`、`首帧参考：`、`尾帧限制：`无条件存在。`音色特征：`只在用户明确要求把声音控制写进当前视频模型Prompt时作为第九个条件字段出现。Adapter不得创建、删除、改名、合并或重排无条件字段，不得提供“与下一镜衔接”字段，边界语义必须投影到“镜头结尾状态”。批量适配不得压缩或共享字段；内容过长时按完整Clip分批。任何旧Adapter约定与Template冲突时，以Template为最高优先级。


---

# Core Principle

Seedance视频生成必须同时理解：


视觉事件

↓

人物状态

↓

动作过程

↓

时间变化

↓

空间关系

↓

摄影机行为

↓

光线

↓

情绪

↓

声音

↓

剪辑连接


这些内容属于：

内部执行信息。


不得自动变成：

最终输出栏目。


---

# Knowledge Layer Boundary

本文件中的：

Scene

Character

Action

Composition

Camera

Lighting

Sound

Editing


全部属于：

Internal Analysis Dimensions。


它们用于：

分析镜头。

补充镜头信息。

检查Seedance执行性。

辅助Video Generation Workflow。


它们不是：

Final Output Schema。


禁止最终直接输出：

Scene:

Character:

Action:

Composition:

Camera:

Lighting:

Sound:

Editing:


作为STATE-08最终Prompt结构。


最终输出时：

这些内部信息必须经过：

11_video_generation_workflow.md

↓

knowledge/prompt_compilation/state08_projection.md

↓

Schema Mapping

↓

templates/10_video_prompt.md

↓

Final Seedance Prompt


核心原则：

Preserve Information.

Do Not Preserve Knowledge Structure.


保留信息。

不保留Knowledge内部结构。


---

# Internal Analysis Dimensions

以下8项：

只用于内部分析。


不得：

原样复制为最终输出标题。


---

# Dimension 01

# Scene

Scene用于理解：

当前镜头发生在哪里。


分析内容包括：

地点。

时间。

天气。

环境状态。

空间结构。

背景变化。

道路方向。

建筑关系。

关键环境元素。


Scene的作用：

建立Seedance需要理解的空间基础。


不得：

把Scene单独作为最终Prompt一级栏目。


---

# Dimension 02

# Character

Character用于理解：

谁出现在当前镜头。


分析内容包括：

人物身份。

Character Asset。

年龄。

五官。

脸型。

发型。

服装。

身体比例。

人物状态。

人物位置。

人物朝向。

人物关系。


已有Character Asset时：

优先使用已确认资产。


禁止：

在Video Generation阶段无原因重新设计人物。


Character信息最终必须：

根据对应Template重新组织。


不得：

直接输出Character栏目。


---

# Dimension 03

# Action

Action用于分析：

人物或物体在时间中的变化。


每个重要动作应该理解为：

开始状态

↓

动作启动

↓

动作过程

↓

状态变化

↓

结束状态


错误：

人物拥抱。


正确执行逻辑：

两人保持距离。

↓

其中一人向前靠近。

↓

另一人产生迟疑。

↓

双方缩短距离。

↓

完成拥抱。

↓

动作停留。


Seedance需要理解：

动作不是一个词。


动作是：

时间过程。


禁止：

瞬间完成复杂动作。

人物瞬移。

动作缺少原因。

动作结果与下一镜头不连续。


---

# Dimension 04

# Composition

Composition用于理解：

摄影机如何组织画面空间。


分析内容包括：

景别。

摄影机位置。

摄影机高度。

摄影机方向。

人物左右关系。

人物面对方向。

前景。

中景。

背景。

视觉重点。

画面留白。

空间层次。

构图主原子与支持层。

内框、遮挡、反射、引导线与色光区域的真实来源。

构图从起始状态到结束状态是否保持或发生一次可追踪变化。


多人场景必须额外分析：

人物距离。

视线方向。

180度轴线。

运动方向。


Composition属于：

镜头空间分析。


不得：

因为这里存在Composition，

就在最终输出中自动使用：

Composition:

或其他自创字段。


最终字段名称：

由Template决定。


构图模式名称不得作为执行终点。


适配时必须把模式拆成：

主体画面位置 + 前中后景关系 + 摄影机位置/运动 + 视觉焦点 + 人物路线/视线 + 稳定结束构图。


高风险反射、群体、复杂遮挡、视差、曲面或动作构图不稳定时，按照对应Camera Language知识降级，不接受身份复制、空间融化或轴线混乱。


---

# Dimension 05

# Camera

Camera用于理解：

摄影机如何观察并跟随事件。


分析内容包括：

焦段。

画幅基准或全画幅等效倾向。

摄影机与主体距离。

焦段和景别共同形成的前后尺度、背景叠合/分离与边缘表现。

对焦对象、焦点行为与必要景深。

机位。

摄影机运动方式。

运动方向。

运动速度。

摄影机起点。

摄影机终点。

手持或稳定状态。

景深倾向。

摄影质感。


焦段不自动提高画面质感，也不单独决定透视或背景虚化。透视由摄影机位置决定；景深还取决于光圈、对焦距离、主体背景距离、画幅和画面放大率。未确认画幅时，具体毫米数只作为全画幅等效倾向。

焦段Applicable时按`knowledge/camera_language/lens_language/focal_length_and_perspective.md`序列化，并用`focal_length_continuity.md`检查跨镜脸部几何、背景尺度、焦点与机位距离。内部FLN编号不得输出。


常见摄影运动包括：

Fixed Camera。

Dolly In。

Dolly Out。

Tracking Shot。

Side Tracking。

Pan。

Tilt。

Orbit。

Crane。

Handheld。


摄影机运动必须：

服务剧情。

服务人物关系。

服务情绪。


禁止：

为了电影感随机增加复杂运动。


尤其禁止无理由使用：

360度环绕。

高速推进。

无人机运动。

穿墙。

旋转。

复杂连续变焦。


Camera属于：

内部摄影分析。


最终如何命名和排版：

由templates/10_video_prompt.md决定。


---

# Dimension 06

# Lighting

Lighting用于理解：

人物与环境为什么能够呈现当前视觉状态。


分析内容包括：

主光。

环境光。

轮廓光。

背景光。

反射光。

自然光。

人工光。

光线方向。

综合色温。

冷暖关系。

光比。

人物面部受光。

环境反射。

光源身份与空间锚点。

光质、强度 / 曝光与衰减。

遮挡、材质、参与介质与动态光态。

起始光态、镜中变化、稳定结束光态与下一镜继承。


光线必须与：

时间。

天气。

环境。

视觉开发。


保持一致。


例如：

雨夜环境中：

可以存在：

冷色环境光。

暖黄色店铺光。

湿润路面反射。

逆光雨丝高光。


但不得：

无剧情依据突然增加新的强光源。


Lighting属于：

内部光影分析维度。


不得：

成为另一套最终Prompt Schema。


需要匹配专业光影参考、环境实用光源、低调/散射策略、体积光、反射、火光或水下焦散时，按需读取knowledge/lighting/index.md。内部模式必须拆成光源、方向、光质、强度、光比、色温、衰减、介质和可见结果；不得输出LGT模式ID。


---

# Dimension 06A

# Color

Color用于理解已确认资产、光源和材质颜色如何形成稳定综合色彩，而不是创造新的彩色光源或重绘资产。

分析内容包括：

- 主色、辅助色、强调色及其真实空间来源和画面占比
- 综合色相关系，以及人物、背景、道具和FX的饱和度层级
- 整体明度、黑位、高光、局部对比和关键可读区
- 白平衡/综合色温与绿色—品红偏色
- 肤色、眼白、白衣、灰墙、金属和关键资产固有色保护
- 皮肤、织物、玻璃、金属、水面、湿地和介质综合色彩响应
- 起始色态、本镜必要变化、稳定结束色态和下一镜继承

需要综合色彩设计时按需读取`knowledge/color/index.md`。内部CLR模式必须拆成颜色来源、层级、饱和度、明暗/偏色、肤色保护、材质响应和连续性；不得输出CLR编号。

暗调不等于欠曝，高饱和不等于全局拉满，低饱和不等于灰度，霓虹必须绑定实用光源，糖果/清透色不得用过曝或塑料磨皮伪造。Color属于内部分析维度，最终仍映射到`templates/10_video_prompt.md`现有字段。


---

# Dimension 07

# Sound

Sound用于帮助Seedance视频方案建立：

听觉空间。


分析内容包括：

环境声。

动作声。

对白。

呼吸。

衣料摩擦。

脚步。

雨声。

车辆声。

如果剧情无对白：

明确理解为：

无对白。

## Voice Identity Omission / Explicit Video-Control Gate

默认不检查或投影角色声音身份。用户没有明确要求把声音控制写进当前视频模型Prompt时，即使Active CHAR Version已有Confirmed Voice Profile或Voice/Audio Reference，也不在`参考资产：`列出、不输出`音色特征：`、不写任何已存在/缺失状态。默认外部已有可用角色音色资源，缺少登记不阻塞STATE-08。

只有用户当前明确要求本次视频Prompt包含声音/音色控制，或明确要求当前视频模型使用某Voice/Audio Reference时，才启用条件字段`音色特征：`：

1. `Reference Delta`：仅列实际使用且获授权的Reference标识、speaker映射与当前Clip必要控制；Reference自身携带Voice Identity，不在文字中完整重述。
2. `Text Delta`：只有用户明确要求文字音色控制时，才从Confirmed Voice Profile提取当前模型所需的最小特征；不得复制完整Profile或跨字段重复。
3. `Dialogue Performance`：准确台词旁可保留当前情绪、力度、停顿、节奏或韵律要求；它只说明这一句怎么说，不得重新定义稳定pitch、timbre、resonance、vocal weight、音高、声线、音域、共鸣或音色质感。

没有适用Reference/Profile时也不写`No Voice Asset`，不自动调用AUDIO模块或返回STATE-03。Candidate、未授权或与当前Active CHAR Version不一致的音频不得使用。该Gate不改变台词、环境声、动作声、Foley、自然声、声音尾部及默认无背景音乐规则。


默认禁止：

在最终“音效”中写入背景音乐、配乐、BGM、歌曲、电影配乐、主题音乐、氛围音乐、节拍或“无配乐”等音乐说明。

因为场景情绪强烈或用户提出配乐要求而让Seedance生成音乐。所有后期音乐工作只由显式调用的独立MUSIC / SEED-MUSIC模块处理，STATE-08没有任何Clip例外。


声音必须：

与空间一致。

与动作一致。

与剪辑一致。


Sound是：

内部执行信息。


最终输出方式：

由Template规定。


---

# Dimension 08

# Editing

Editing用于分析：

当前镜头与前后镜头如何连接。

必须按需读取`knowledge/transitions/`。先使用rules/04_consistency_rules.md判定Boundary Class，再由Transition Decision Engine选择一种主要技术。


分析内容包括：

镜头进入方式。

镜头内部节奏。

动作结束点。

下一镜头连接点。

情绪留白。

视线匹配。

动作匹配。

声音连接。


默认Direct Cut。只有存在真实动作、视线、反应、构图、方向、尺度、同期声、完整遮挡、光态或FX锚点时才使用匹配切、声音桥、遮挡切、Dissolve、Fade、Flash或其他已确认方式。

每个边界只使用一种主要视觉技术。同期Sound Bridge可以辅助，但不得使用背景音乐、配乐或歌曲。

推、拉、摇、移、跟、升降、环绕、甩镜、俯冲、贴地推进和变焦本身不是转场；没有明确切点和下一镜匹配条件时只作为镜头运动。

当资料使用“中景→特写→环绕→拉远”等镜头顺序时，必须先读取`knowledge/camera_language/movement_combinations/`：多个景别、机位、视点或观察对象默认拆为Coverage Sequence；只有同一主体、同一目的、同向同轴且同平台的一次延续可保留为低复杂度复合路径。

大多数转场属于后期剪辑。Seedance适配负责生成兼容的出镜/入镜把手，不得无依据要求单个镜头变形到另一个场景。


剪辑方式必须：

服务叙事。

保持连续。


禁止：

为了炫技随机使用转场。


Editing属于：

内部镜头连接分析。


不得：

直接成为最终结构来源。


---

# Shot Boundary And Handoff Adaptation


Seedance适配必须把每个镜头理解为：


起始边界

↓

镜头内变化

↓

最后一帧稳定限制

↓

下一镜衔接

按Confirmed Clip Production Plan序列化：`一个Clip = 一个G Prompt Package = 一条连续Prompt`。一个Clip可包含一个或多个按原顺序排列、可在合计4—15秒内稳定执行的正式Shot；多Shot只作为同一条Prompt中的连续导演镜头阶段，不按Shot拆Prompt。Clip内保留起始、连续变化、空间/道具/摄影机关系、结尾和衔接，跨Clip关系通过上一G段尾帧资产与边界字段传递。禁止为了减少Clip数量强行合并。

## Delivery Mode Gate

多Clip项目默认只适配并交付当前一个Clip Prompt Package，把该Clip作为独立Checkpoint。用户只说“下一个”“下一步”或“继续”时，只进入下一个Clip；不得继续展开其余Clip。只有用户在当前请求中明确要求全部、一次性、批量或连续输出多个Clip时，才允许同轮适配多个Package。批量覆盖不放宽任何逐Clip边界、资产、首尾帧、Voice Reference或声音规则。

## Four-Part Boundary Gate

每个Clip适配前必须同时建立：实际参与约束的显式【参考资产】清单、每个分镜的首帧来源/要求、稳定清楚可继承的尾帧接口，以及与前后Clip的Boundary Class。跨Clip尾帧使用方式必须在既有Handoff中明确为A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】。A/B列`REF-TAIL`并分别标注“同镜头连续承接用途”或“空间/站位/景别参考用途”；C不列`REF-TAIL`并写明Canonical资产、Spatial Blocking与文字重建依据。任一项缺失时Adapter不得把数据交给Template。


这四项属于内部执行信息。


最终字段名称与顺序只由templates/10_video_prompt.md定义。


## Stable End Window


每个镜头结尾应保留一个足以形成可读参考帧的低动作稳定窗口。


主要动作完成后自然进入低动作稳定状态，足以形成清楚、可复用的最后一帧。


不使用精确秒数、百分比或帧数描述稳定窗口。


如果镜头动作无法在既定时长内完成并稳定：


优先减少次要动作或降低运镜复杂度。


仍无法完成时返回Shot Design调整，不得把动作结果瞬间化。


稳定不等于人物冻结。


允许自然呼吸、衣物或头发的微小物理变化、雨声和环境持续运动。


禁止在稳定窗口中出现新的剧情动作、突然转头、抬手、换位、道具换手、表情跳变、摄影机急停或遮挡关键主体。

除非剧情明确要求并已在上游确认，尾帧不得处于高速运动、动作未完成、主体严重遮挡或构图不可读状态；默认必须清楚可读、低动作、可继承并能作为下一Clip接口。


## Handoff Types


Continuous Handoff：

保留所有仍然有效的身份、位置、方向、动作阶段、情绪、道具、环境、摄影机与持续声音状态，并进一步区分A/B：

- A【同镜头连续承接 / Direct】：上一Clip最后一个镜头继续，目标接近一镜到底。标记`Tail Frame Required = YES`；【参考资产】列`REF-TAIL-XX｜CLIP-XX尾帧参考（同镜头连续承接用途）`；【首帧参考】使用固定直接承接句，并锁定姿态、位置、朝向、距离、动作阶段、构图、景别、机位、环境、光线、天气、道具、情绪与持续声音。
- B【新镜头参考型 / Reference-Only】：当前Clip另起新镜头重新构图，但需尾帧保持站位、朝向、人物距离、景别衔接、空间关系、道具状态或起始构图。也标记`Tail Frame Required = YES`；【参考资产】列`REF-TAIL-XX｜CLIP-XX尾帧参考（空间/站位/景别参考用途）`；【首帧参考】明确另起新镜头、保持项和允许变化，禁止使用A固定直接承接句。

A/B尾帧尚未提供时仍必须在【参考资产】列统一名称、对应用途及“待用户提供/待上传、未确认”，并提示用户从上一Clip最终成片截取后在实际生成前添加；不得伪造路径或声称已上传/已确认。该声明占Projected位但不计入已提交图片数，Prompt可以完整编译和交付。


Motivated Discontinuity：

对已确认的场景切换、时间跳跃、硬切、蒙太奇、闪回或故意跳切，不生成虚假的连接动作；只明确切点、保留锚点以及下一镜经剧情授权的新起始状态。

若当前Clip为C【新镜头且无需尾帧】，标记`Tail Frame Required = NO`，不在【参考资产】或【首帧参考】写`REF-TAIL`，只明确不继承上一Clip画面状态、经确认的断点、Canonical基础资产、Spatial Blocking、文字重建原因与保留锚点，防止模型误把断点当作图生视频连续首帧。


Unresolved Handoff：

下一镜未知或信息矛盾时，使用安全稳定的暂定结尾，不编造下一镜内容；后续镜头确定后成对复核。


## Special Subjects


空镜：

不虚构人物进入。继承或重建环境、光线、天气、固定道具、痕迹、摄影机和持续声音。


首镜：

从已确认的Scene初始状态、开场资产或参考首帧建立，不声称继承不存在的上一镜。


末镜：

下一镜已知时保留续接锚点；下一镜未知或本段完结时形成稳定收束，并明确不虚构后续动作。


故意跳切：

只允许跳变Shot Design明确授权的时间、构图或动作阶段；角色身份、资产版本和未获授权的道具/环境事实仍保持锁定。


## No Anticipation


自动衔接只描述边界。


它不得让上一镜提前执行下一镜的首个叙事动作。


如果下一镜从人物偷看、转身、开口、起步、松手或接触开始：


上一镜结尾必须停留在该动作启动之前，除非Shot Design明确要求Match on Action，并清楚规定动作切点。


---

# Time Continuity

Seedance视频最重要的能力之一：

是理解时间变化。


这里的时间分析主要用于内部动作顺序与密度判断。最终Prompt只在【时长】保留Confirmed Clip的4—15秒平台生成时长，不输出时间码、总片时长、单分镜时长或按秒分段。

该平台生成时长必须直接复制Confirmed Clip Production Plan，并在交付前与Clip表交叉核对；Clip Production Plan内部必须先完成来源Shot逐项求和、合计、目标时长与平台生成时长四项一致性核算。任一不一致都返回STATE-07 Clip Production，不进入生成。

每镜“音效”是正向可听内容：具体环境底声/空间底噪或有理由的有意静默，加至少一个同步动作声、Foley、呼吸、对白或剧情内声源，并写明声音尾部。背景音乐禁令只放在【反向提示词】，不能替代上述声音；其首个非空内容行必须无例外逐字写“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”。


每个镜头必须判断：

镜头开始时发生什么。

↓

中间发生什么。

↓

镜头结束时发生什么。


动作复杂度必须与：

单镜头稳定执行容量。


匹配。


例如，一个镜头内不应该同时完成：

发现人物。

认出人物。

穿越整条街。

拥抱。

哭泣。

离开。


如果动作无法自然完成：

应该：

拆分镜头。

或减少动作。


---

# Spatial Continuity

Seedance生成多人镜头时：

必须明确空间关系。


内部分析必须检查：

谁在左。

谁在右。

谁朝左。

谁朝右。

谁正在靠近谁。

谁正在远离谁。

人物看向哪里。

摄影机位于哪一侧。


尤其处理：

双人对话。

相向行走。

对峙。

战斗。

拥抱。

追逐。


必须保持：

180度轴线逻辑。


禁止：

两个人应该互相面对，

却同时正面面对摄影机。


---

# Character Continuity

跨镜头必须保持：

角色身份。

五官。

脸型。

年龄。

发型。

服装。

身体比例。


还必须保持：

上一镜头结束时的人物状态。


例如：

头发已经被雨淋湿。

下一镜头：

不得重新变干。


服装已经受雨。

下一镜头：

湿润程度应保持或继续增加。


---

# Prop Continuity

关键道具必须遵守物理连续性。


需要分析：

谁持有。

哪只手持有。

道具朝向。

道具当前位置。

道具当前状态。


例如雨伞：

上一镜头：

角色B右手撑伞。


下一镜头：

如果雨伞落地，

必须先存在：

松手。

倾斜。

滑落。


禁止：

雨伞突然消失。


禁止：

自动换手。


禁止：

无动作改变位置。


---

# Emotional Continuity

人物情绪必须具有：

可见变化过程。


人物表情适用时按需读取`knowledge/performance/index.md`，并使用：

Baseline → Stimulus → Attention Shift → Appraisal → Control / Leakage → Action Choice → Settled State。


内部分析优先观察：

视线目标、路径、速度与停留。

眉眼、眼睑、嘴角、唇部与下颌的一项主要变化。

呼吸。

停顿。

嘴角。

手指。

肩部。

步伐。

身体距离。

泪液、红肿、颤抖等仍可见后果（如有）。


情绪可以理解为：

初始状态

↓

受到刺激

↓

确认信息

↓

身体反应

↓

行动选择

↓

情绪结果


禁止：

用一句：

“她非常悲伤。”


替代真正的表演设计。


同样禁止只写“温柔眼神、冰冷眼神、坚定眼神”、PEX/AU编号，或把瞳孔、脸红、落泪、露齿数和颤抖当成固定情绪按钮。压抑或混合情绪只保留公开状态与一处短暂泄漏；口部表情必须与对白、哭笑、吞咽和呼吸容量相容。


---

# Seedance Action Density

一个镜头中的动作数量：

必须控制在模型能够稳定执行的范围内。


优先：

一个主要动作。

一个主要情绪变化。

一个清晰摄影机运动。


复杂镜头：

可以存在多个连续子动作。


但这些动作必须：

因果明确。

顺序明确。

空间明确。


禁止：

同时堆叠大量无关联动作。


---

# Camera Complexity Rule

视频生成稳定性优先于：

炫技摄影。


摄影机设计优先级：

剧情清晰

>

人物关系

>

动作连续

>

情绪表达

>

摄影复杂度


当简单摄影能够完成叙事时：

使用单一主要路径。若两阶段路径确有必要，只允许一次由人物或空间事件触发的同向延续，并必须保持同一轴线、侧位、焦段倾向和稳定平台。出现换景别、换视点、换主体、换侧、反向、越轴、时空变化或新FX阶段时，拆为多个SHOT并使用Transition模块处理边界。

优先简单摄影。


例如：

人物第一次认出对方：

缓慢推进

通常优于：

360度高速环绕。


---

# Reference Priority

存在参考资产时：

必须先执行`knowledge/reference_budget.md`。参考资产预算按Clip独立计算，默认保留原始独立资产；≤7张不整合，8张且无额外帧需求不整合，9张仅在没有未计入连续性图片时允许，>9张才对同类非角色信息执行去重/整合/裁剪并最终≤9。已有9张且还需上一Clip尾帧或当前首帧时，必须按10张真实需求释放至少1位。

当前Clip每个核心角色必须保留各自独立三视图/角色锁定图，动作/互动图不得替代外貌基准；多个角色不得合并成角色总表。环境多视角、道具组、空间关系、动作关系或使用示意只有在超限风险触发且总图真实存在、已确认、完整覆盖时才可整合。独立图更清晰且未超限时继续独立使用。

Seedance Prompt应该优先保持：

先判定A/B/C。A/B标记`Tail Frame Required = YES`并把统一`REF-TAIL`名称、对应用途及真实状态直接列入【参考资产】；尚未提供时写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。A使用固定直接承接句；B说明另起新镜头重新构图且不使用该句。C标记`NO`，不要求截图、不列`REF-TAIL`，依靠Canonical基础资产、Spatial Blocking与文字End State承接或重建首帧。

Character Asset。

Environment Asset。

Prop Asset。

Canonical FX Asset（如适用）。

合法首/尾帧。

Final Visual Blocking Assessment=`REQUIRED`且经Sketch Validation确认、绑定当前Clip / Blocking Signature的`REF-SKETCH`；只控制Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path，不控制身份、环境 / 道具造型、材质、色彩、灯光或最终画风。

当前角色的Voice/Audio Reference属于声音身份专用Source，不得作为视觉Canonical Reference使用。默认不写入【参考资产】；只有用户明确要求当前视频模型使用该Reference进行声音控制时，才按最小必要信息列出。Confirmed Voice Profile同样默认不投影，不作为无Reference时的自动文字回退。


禁止把Storyboard图片、分镜板、漫画格、接触表、拼图、多画面参考、Scene Top-down Blocking Map或Detailed Shot Design / Clip Plan截图提供给Seedance。此类材料不是Canonical Asset，容易把线条、边框、标注或多画面结构带入生成结果。唯一例外是按`knowledge/clip_preflight_check.md`为单一Clip生成 / 接收、通过Sketch Validation并注册的中性`REF-SKETCH`；它只承担Visual Blocking Authority，Prompt不得复制全部标注或让其覆盖Canonical资产。


文字描述用于：

解释动作。

解释镜头运动。

解释变化过程。


不得：

使用新的文字描述覆盖已经确认的视觉资产。


---

# Visual Style Adaptation

Visual Style用于：

影响摄影执行方式。


可以影响：

综合色彩。

焦段倾向。

运动方式。

光影。

曝光。

镜头节奏。

人物表演。

画面质感。


Visual Style不应该：

改变剧情事实。

改变人物身份。

改变场景。

改变动作结果。


综合色彩参考必须经`knowledge/color/foundations.md`校正为可执行层级；导演、影片、类型或色调名称不能替代颜色来源、明暗、饱和度、综合色温、肤色保护和稳定结束色态。


导演风格必须：

转换成可执行影视语言。


不得只依赖：

导演姓名。

文学化或导演化意图可以保留其情绪功能，但重要抽象语义必须补充至少一种可见或可听执行项：人物行为/微表情、环境或光线变化、摄影机行为、具体声音或时间状态。不得把“镜头像终于鼓起勇气一样靠近她”“宿命感”“压迫感”等孤立表达当作已完成的Seedance适配。


---

# Cinema Parameter Reference

摄影参数可以作为：

辅助执行信息。


只有在：

用户明确提供。

Visual Development已经确认。

项目具有明确摄影方案。


时使用。


可以包括：

Camera System。

Lens Family。

Focal Length。

Filter。

Aperture。

Film Emulation。

只有焦段还不构成可执行参数。至少同时说明摄影机距离、景别、空间效果、焦点/景深与运动约束；否则删除无意义毫米数，保留可见结果。

## Physical Data Value Rule

Seedance对数字的消费以视觉关系为主，不等于精密摄影测量、刚体动力学或Blender / Unreal式物理仿真。只保留能显著改变当前Clip可见结果的精度：

- 高价值：左右/前后、近/中/远距离关系、90°/180°转身、约3秒/5秒、眼平/低机位、从A到B、固定距离跟随。
- 中高价值：24/35/50/85mm等焦段倾向、约5秒推进、约120°环绕、景别转换；把它们当作视觉效果与摄影行为提示，不承诺工程精度。
- 低价值：1.37m机高、2.43m主体距离、0.137m/s推进、0.166m/s²加速度、53mm或逐点工程轨迹。除非用户/目标模型明确要求且小数精度会改变可见结果，否则压缩为眼平机位、近/中距离、缓慢推进、约X秒、约X度或起止景别。

不得为了技术感保留无意义小数，也不得用超细参数替代主体、动作、空间、摄影机起止与状态演变。


例如：

ARRI Alexa Mini LF。

Cooke Panchro/i。

Black Pro-Mist。

35mm / 50mm / 85mm。

T2.0-T2.8。

Film Grain。


但：

这些参数不是必填。


禁止：

为了增加“电影感”随机堆叠设备名称。


禁止：

同时无逻辑使用：

ARRI。

RED。

IMAX。

Cooke。

Anamorphic。

8K。


技术名称：

不能替代摄影设计。


Duration、Frame Rate、Frame Count等时间轴参数只允许作为Prompt外部的平台设置，不得写入最终Seedance Prompt。


---

# Model Adaptation Principle

Seedance Adapter负责：

把电影语言调整为视频模型更容易执行的描述。

## Model Profile Routing

本Adapter是所有Seedance目标的共通层，不替代Model Execution Lock。STATE-07只在`Target Video Model`已锁定后选择Profile：`Seedance 2.0`继续执行现有稳定4—15秒短Clip与≤9图片预算；`Seedance 2.5`额外读取`knowledge/seedance_25_profile.md`。Profile能力上限不等于已接入网关限制：所有执行时长、图片/视频/音频输入数和输入格式先受实际API/网关可确认限制约束。

Profile只能改变STATE-07/08的执行路由与编译策略，不能改变Production-Locked Script、Canonical Character / Environment / Prop Authority、资产双确认、REF-TAIL A/B/C、End-State合同、Voice opt-in、视频Prompt无BGM和`templates/10_video_prompt.md`固定Schema。


重点优化：

动作顺序。

人物方向。

镜头运动。

空间关系。

时间变化。

道具连续。

视觉连续。


适配时：

允许降低不必要的复杂度。


不得：

改变剧情核心。

改变角色关系。

改变资产。

改变镜头叙事目的。


适配完成后必须调用：

knowledge/prompt_compilation/state08_projection.md


检查所有Applicable Knowledge是否已映射到templates/10_video_prompt.md现有字段。映射只保留语义，不输出内部分析标题、模式ID或Projection Ledger。


---

# Output Schema Boundary

这是本文件最重要的边界规则。


knowledge/11_seedance_adapter.md：

只提供：

Seedance执行知识。


它不拥有：

最终输出Schema。


不得规定：

最终镜头编号格式。

最终字段名称。

最终字段顺序。

最终章节结构。


所有STATE-08最终格式：

必须读取：

templates/10_video_prompt.md


并完全服从该Template。


本文件中出现的：

Scene。

Character。

Action。

Composition。

Camera。

Lighting。

Sound。

Editing。


只允许用于：

内部思考。

内部整理。

内部检查。


禁止：

原样复制成最终Prompt栏目。


---

# Workflow Relationship

正确执行关系：

Detailed Shot Design

↓

Confirmed Clip Production Plan

↓

11_video_generation_workflow.md

↓

knowledge/11_seedance_adapter.md

提供Seedance执行知识

↓

knowledge/prompt_compilation/state08_projection.md

完成Applicable Knowledge到现有字段的语义投影检查

↓

内部信息整理

↓

templates/10_video_prompt.md

进行最终Schema映射

↓

Final Seedance Prompt


Knowledge不得：

跳过Workflow。


Knowledge不得：

跳过Template。


Knowledge不得：

直接输出最终Prompt。


---

# Quality Rules

最终Seedance执行信息必须帮助实现：

Confirmed Clip与独立G生成段一对一；Clip内可含1个或多个正式分镜。单镜独立执行，多镜按原顺序作为同一次长镜头连续执行。

每段时长为4—15秒，拥有可复用尾帧、独立反向提示词、完整逐镜字段和明确的前后段关系。

角色一致。

环境一致。

空间连续。

动作自然。

摄影合理。

道具连续。

情绪连续。

时间可执行。


禁止：

静态图片描述。

随机镜头运动。

无意义技术参数堆叠。

动作瞬移。

空间混乱。

角色无原因变化。


---

# Final Goal

让AI生成的视频结果接近：

真实电影镜头。


而不是：

AI图片动画。


Seedance Adapter的目标不是：

决定最终Prompt长什么样。


而是：

确保最终Prompt中的信息：

能够被视频模型正确执行。


最终格式唯一真源：

templates/10_video_prompt.md
