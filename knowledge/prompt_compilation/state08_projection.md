# STATE-08 Semantic Projection

## Module Contract

- Module Type：STATE-08 Knowledge Adapter。
- Trigger：所有 Video Prompt / Seedance Prompt 撰写任务。
- Inputs：已确认项目事实、STATE-06 Detailed Shot Design、STATE-07 Confirmed Clip Production Plan、适用Knowledge、`knowledge/clip_planning/continuity_and_projection.md`与`knowledge/11_seedance_adapter.md`；只有用户明确要求把声音控制写进当前视频模型Prompt时，才读取适用的Confirmed Voice Profile或Voice/Audio Reference作为条件输入。
- Output Owner：`templates/10_video_prompt.md`；本文件不拥有、增加、删除或改名最终字段。
- Consumer：`workflows/11_video_generation_workflow.md`。
- Forbidden：新增剧情、重选资产、改变镜头目的、创建新主STATE、创建另一套最终Schema。

## Fixed-Template Projection Gate

投影粒度固定为Clip。每个Confirmed Clip分别投影为一个完整的`# CLIP-X｜标题 Seedance视频提示词`区块，完整重复Template规定的全局字段；每个`分镜X`完整重复Template规定的十个分镜字段。

禁止使用方头括号旧章节、独立CLIP标题字段、无授权条件字段、“与下一镜衔接”或其他新增字段。`音色特征：`只按Template显式授权条件出现；下一镜承接与Boundary Class语义投影到“镜头结尾状态”；跨Clip首尾帧语义投影到“参考资产”“首帧参考”“尾帧限制”和首/末分镜的起止状态。

批量授权只改变本轮Clip数量，不改变逐Clip结构。不得压缩、合并、共享、删减或改名字段；内容过长时按完整Clip自动分批，批次边界不得拆开单个Clip。

Template Mapping后与交付前各执行一次字段完整性检查。标题、八个无条件前置全局字段、一个或多个逐镜十字段组、末尾反向提示词必须完整、非空、无重复、无额外字段并严格按顺序。`音色特征：`只在用户明确要求把声音控制写进当前视频模型Prompt时作为第九个条件字段出现。任一项失败不得输出。

## Core Rule

所有适用且已确认的上游知识必须在最终Prompt中留下可见、可执行、可连续检查的语义证据。知识模块名称、内部表格、模式ID、Ledger标题与分析栏目不得原样输出。

## Prompt Attention / Control Allocation Gate

本Gate只管理最终输入信息的优先级、冲突、重复与控制价值，不声称能够直接或精准设置模型内部的交叉注意力数值。提示词不是越长越好；固定Template必须完整，但每个字段只保留对当前Clip真实有控制价值的最小充分语义。

逐Clip执行：

1. **Locked / Minimal Confirmation**：Active Canonical References、合法首尾帧、Confirmed Spatial Blocking、Director Decision Notes、Detailed Shot Design或Clip Plan已经锁定的维度，不在正文长篇复述。只保留资产ID/版本/用途、当前状态、不得改变项与当前风险所需的最小一致性确认。
2. **Unlocked / Must Specify**：上游尚未锁死、且会显著改变当前Clip结果的动作、方向、空间、摄影机、时间顺序、状态演变、声音与影像质感，必须明确写出。
3. **Irrelevant / Delete**：与当前Clip无关、未出场、未使用、不能解决当前风险或只起装饰作用的信息删除。
4. **Duplicate / Merge**：同义重复、跨字段机械复述与多次外貌/环境长描述合并为一条最高价值指令；必要的首帧、逐镜起止状态和连续性重复不视为机械重复。
5. **Conflict / Resolve Or Return**：机位、运动、动作、站位、光线、资产或时间顺序互相冲突时，按上游事实与本Clip导演目标选择唯一合法表达；无法消解则走Return Route，不把互斥指令同时序列化。

控制优先级为：`剧情与资产事实 / 边界连续性 → 主体身份与精确数量 → 主要动作与物理空间 → 摄影机路径与结束状态 → 必要光色/声音/质感 → 装饰性风格词与器材名`。高优先级信息必须比低优先级修饰更短、更明确、更靠近其目标字段核心位置。

逐Clip使用`rules/03_prompt_rules.md`中的十类Prompt Pollution作为内部诊断标签，不把标签输出到最终Prompt。清洗顺序固定为：

`原始创作意图 → 识别抽象词与语义模板 → 具象化 → 否定转肯定 → 检查已锁定参考资产 → 删除重复 → 消除冲突 → 删除/压缩无效精密参数 → 删除跨镜头残留 → 检查主体/动作/空间/镜头/时间状态 → Prompt Compression → Final Clip Prompt`

清洗不得机械删除文学/导演意图、合法连续性重复、Template必填字段或已经确认的生产语义。任何无法在当前Clip内部消解的事实冲突必须先走Return Route。

进入控制矩阵前还必须消费STATE-07的Clip Scope Firewall：`already_happened`只作为起始事实，不重播；`this_clip_only`是唯一允许被执行的可见剧情/动作范围；`reserved_for_later`只保留为边界上下文，不写成当前事件；`do_not_show_yet`用正向目标状态和必要的少量反向高风险项防止提前出现。一个Clip原则上只实现一个主要可见Beat与改变后的Endpoint；同一Beat所需的连续动作不被机械拆成一个动作。

## Generation Budget Allocation Gate

本Gate是Five-Dimensional Prompt Control Matrix之前的逐Clip内部判断，不是数学额度、不创建最终字段，也不替代Director Decision、Clip Movement Plan或Knowledge Reflection。它把有限的生成控制能力收敛到当前Clip最重要的结果，防止Identity Fidelity、Motion Boldness、Scene Density、复杂Camera、Crowd、Dialogue / Lip-sync、FX与光色变化同时拉满。

每个Clip在内部Projection Ledger记录：

- `Primary Spend`：当前Clip必须最可靠实现的一个核心生成目标；优先来自已确认Narrative Objective、主要可见Beat与最高Continuity Risk。
- `Secondary Spend`：最多一至两个支持Primary、但失败不会改变本Clip核心意义的目标。
- `Economized`：主动降低复杂度、不追求或保持稳定的维度，并写明采用固定机位、单一路径、减少群体活动、缩减口型/FX/光色变化、降低场景活动密度或其他既有Safe Downgrade中的哪一种。

分配时先保护剧情/资产/边界正确和Primary Spend，再允许Secondary；其余高负荷维度必须进入Economized或返回STATE-07/06拆分。Five-Dimensional Matrix随后只对Primary、Secondary及仍未锁定的必要风险做高控制，不允许五维全部因为“可能有用”而同时补满。三项决策只进入既有内部Ledger与最终字段的具体执行语义，禁止输出`Primary Spend / Secondary Spend / Economized`标签。

## Five-Dimensional Prompt Control Matrix

这是STATE-08内部检查层，不是最终Prompt的五个新字段。逐Clip只检查并填补“参考资产或上游信息尚未锁死、但当前Clip需要控制”的维度；已锁定且无当前风险的内容标记`Locked / Minimal Confirmation`，不重复成长篇描述。

| 内部维度 | 检查内容 | 需要进入现有字段的条件 |
|---|---|---|
| Subject & Physical Motion | 主体、姿态、动作链、方向、受力/速度感、人物物理关系 | 当前动作、方向、速度感、接触/受力或人物关系未锁定且会改变可见结果 |
| Environment & Emotional Lighting | 场景、天气、时间、主光方向、色温、氛围变化 | 当前环境状态、光源/色温或有剧情触发的变化未被资产与上游合同完整锁定 |
| Optics & Camera Choreography | 景别、焦段倾向、机位、运镜、轴线、构图变化 | 摄影机起点/路径/触发/终点、焦段倾向、轴线或构图结果仍需执行化 |
| Timeline & State Evolution | 起始状态、动作顺序、中间变化、结束状态、首尾承接 | 当前Clip的变化过程、动作先后、稳定结果或与前后Clip的继承/重建需要明确 |
| Aesthetic Medium & Rendering | 写实/动画/胶片等媒介、材质、颗粒、动态模糊、景深、整体质感 | 这些项目尚未由Visual Direction/资产锁定，且对当前Clip辨识或稳定性有实际收益 |

矩阵结果只进入既有Projection Ledger与Template字段，不得逐条打印、输出内部英文维度名或强迫每个维度都增加内容。未触发维度不虚构填充。

## Abstract-To-Executable And Physical Anchoring

进入Template Mapping前，重要文学化、情绪化或导演化描述必须尽可能转译为至少一种可见或可听执行项：人物行为/微表情、环境变化、光线变化、摄影机行为、声音或时间状态。保留原描述的情绪功能，但不得让“宿命感、勇气、压迫、温柔、电影感”等孤立词替代执行信息。

执行Positive Specification：把能正向定义的否定约束改写为目标状态，例如`不要下雨 → 晴天，空气清透，阳光照亮地面`，`不要夸张表情 → 表情克制，嘴角和眉眼只有轻微变化`。反向提示词只保留固定平台边界及当前Clip少量、正向状态仍难锁死的高风险错误；不得扩展成所有可能错误的清单。

执行Semantic Template Decomposition：遇到“创业、约会、学生、婚礼、医院、黑帮、赛博朋克、日系青春”等高共现词，先判断它是当前Clip必要身份/风格事实，还是只在调用模型默认视觉模板。若主要为模板触发，删除该大词并只写当前Clip真实存在的人物、动作、场景、道具、服装、光线与声音；若标签确有叙事价值，可保留其上游意图，但最终控制仍由具体可见/可听元素承担，不允许自动补入默认场景包。

数字与物理描述按执行价值分层：

- **High Value / 保留**：左右/前后、人物距离关系、90°/180°转身、约3秒/5秒、眼平/低机位、从A到B、固定距离跟随等直接可视关系。
- **Medium-High Value / 作为视觉提示**：24/35/50/85mm焦段倾向、约5秒推进、约120°环绕、景别转换等摄影执行信息。它们描述视觉效果和行为倾向，不承诺严格物理精度。
- **Low Value / 默认压缩或删除**：1.37m、2.43m、0.137m/s、0.166m/s²、53mm、精确工程轨迹等无额外可见收益的小数或工程参数；除非用户或特定模型明确要求并且该精度会改变可见结果。

物理锚定优先把低价值数字转换成眼平/低机位、近/中/远距离、慢/中/快、约X秒、约X度、固定距离或起止景别。生成模型理解的是数字对应的视觉关系，不是Blender / Unreal式严格物理仿真。

STATE-08内部转换链固定为：

`Director Intent / Literary Intent → Visual Translation → Physical Anchoring → Prompt Compression → Final Clip Prompt`

该链嵌入现有STATE-08，不新增主STATE、Workflow或最终字段。

## Clip Preflight Projection Gate

每个Clip在Reference Budget与Template Mapping前必须读取并执行`knowledge/clip_preflight_check.md`最终版。内部顺序固定为：`Continuity Classification（含Tail Frame Required判定）→ World-State → Character Count → Spatial Composition → Prop State → Transition Five Elements（适用时）→ Reference Asset Check / Budget`。

- 连续性必须在`视觉连续 / 剧情连续 / 主动切场或切世界`中三选一，并在同一判定中明确A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】，再查资产可用性。A/B均标记`Tail Frame Required = YES`并把统一`REF-TAIL-XX｜CLIP-XX尾帧参考`直接写入`参考资产`：A标“同镜头连续承接用途”，B标“空间/站位/景别参考用途”；未提供时写“待用户提供/待上传、未确认”，不声称存在或确认，Prompt可完整交付但实际提交生成前补图。C标记`NO`，不列`REF-TAIL`、不要求截图，可由Canonical基础资产、Spatial Blocking与文字状态承接或重建。
- 每个分镜明确World-State；只投影当前阶段实际存在、实际出场且适用的角色、环境、道具与FX。完全位于转换后世界的Clip删除转换前资产；转换Clip按Pre/Post阶段投影两种状态及其转换过程。
- 每个分镜锁定角色精确数量。剧情唯一角色必须在`人物一致性`及适用的`画面描述 / 空间关系`中正向明确唯一一只/名、前中后景无第二个同类，并在`反向提示词`禁止复制、分身、镜像重复、背景第二个与相似替身。
- 追逐/战斗/多人空间锁投影到`镜头/机位`、`空间关系`、`画面描述`与`镜头结尾状态`。追逐默认后追前逃，禁止并排正对镜头、同景深海报式合影或群像站桩。
- 道具当前形态、尺寸、持有者/左右手、位置、方向、悬浮许可、转换完成状态与结束状态投影到`起始状态`、`道具状态`和`镜头结尾状态`；不同世界形态不得混用。
- 适用转场必须先具备起点状态、转换媒介、运动方向/过程、终点状态与转场后首个稳定构图，再分别投影到`首帧参考`、`起始状态`、`画面描述`、`空间关系`、`道具状态`和`镜头结尾状态`。不得新增“转场”字段。

任一Preflight项FAIL时停止投影并按Return Route修正；不得把失败设计交给反向提示词兜底。

## Reference Budget Projection Gate

每个Clip在Clip Preflight通过后才可建立`参考资产：`。读取并执行`knowledge/reference_budget.md`：先删除当前World-State不适用、当前Clip无关与重复项；A/B无论尾帧是否已上传都预留1个Projected位，并直接列出统一`REF-TAIL`名称、用途和真实状态；未提供时为“待用户提供/待上传、未确认”，不计入已提交图片数。C不加入或预留旧尾帧。得到Projected Final Count后执行既有阈值：≤7不整合；8张且无额外帧需求不整合；9张只有在没有未计入的合法连续性需求时允许直接使用；已有9张且仍需上一Clip尾帧/当前首帧时按10张处理并至少释放1位；>9必须整合同类非角色信息，仍超限则按规定优先级裁剪，最终≤9。

当前Clip每个核心角色的独立三视图/角色锁定图必须分别保留，动作/互动图不得替代外貌基准。整合仅限环境多视角、道具组、空间关系、动作/互动关系与使用示意等非角色信息。独立资产更清晰且总数未超限时继续独立使用；已有总图不构成强制替换理由。

最终`参考资产：`逐项写资产ID或名称、真实引用或明确待补充状态、用途与锁定约束。除A/B所需`REF-TAIL`外，只能序列化真实存在且已确认的资产/帧；不得输出未生成/未确认的总图、空间关系图或动作关系图。A/B尾帧统一命名为`REF-TAIL-XX｜CLIP-XX尾帧参考`，缺图时仍列名但必须同时写“待用户提供/待上传、未确认”，不得写假路径或冒充图片已经存在；任何`REF-TAIL`都必须标明“同镜头连续承接用途”或“空间/站位/景别参考用途”。预算审计保留在STATE-07 Clip Plan与内部Projection Ledger，不新增最终字段。

每个Clip投影前必须通过四项硬门槛：

1. `参考资产：`显式列出实际使用资产及用途/锁定约束；A/B所需`REF-TAIL`缺图时仍直接列名、用途与“待用户提供/待上传、未确认”，并与已提交图片清单分开计数。只要出现`REF-TAIL`，用途类型不可省略。
2. `首帧参考：`在既有内容中标记A/B/C与`Tail Frame Required = YES / NO`。A逐字包含`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`并完整锁定所有承接维度；B说明参考该尾帧延续站位/朝向/距离/景别/空间/道具或构图逻辑，但当前Clip另起新镜头重新构图，禁止使用A的固定直接承接句；C不列`REF-TAIL`并写Canonical资产、Spatial Blocking与文字重建依据。三类均须与分镜1“起始状态”一致。
3. “镜头结尾状态”与前置`尾帧限制：`形成稳定、清楚、可冻结、可继承的尾帧接口；当前Clip使用上一尾帧时，必须定义本Clip新的结束状态供下一Clip承接。
4. “镜头结尾状态”同时明确Continuous Handoff、Motivated Discontinuity或Unresolved Handoff，不另建字段。

Sound属于逐镜必投影模块。每个“音效”包含具体环境底声/空间底噪或有理由的有意静默、至少一个同步前景声层和声音尾部。禁止用“无”“静音”“有效内容”或背景音乐禁令替代正向制作声音。

声音身份执行默认省略Gate：

- 用户没有明确要求把声音控制写进当前视频模型Prompt时，不检查声音资产，不投影Voice Profile / Voice/Audio Reference，不输出`音色特征：`或任何声音资产状态文字。默认外部已有可用角色音色资源，主流程继续。
- 即使已存在Confirmed Voice Profile或Voice/Audio Reference，也由Source携带身份，Prompt不重复描述。
- 只有用户当前明确授权把声音控制写进当前视频模型Prompt时，才在Template允许的条件位置输出`音色特征：`，并按`Source Carries State, Prompt Carries Delta`只写当前Clip必要的Reference映射或最小文字控制。
- Dialogue Performance仍投影到`人物动作与情绪 / 台词 / 音效`中的适用位置，只说明当前一句/当前场景怎么说，不得重定义稳定Voice Identity。

`时长：`的4—15秒平台生成时长只复制Confirmed Clip Production Plan的目标时长，不得重新估算；最终Prompt不写逐镜时长、时间码、按秒动作区间、帧率或帧数。

## Global Projection Matrix

| 来源知识 | 固定目标字段 | 必须保留的语义 |
|---|---|---|
| Project / Clip Plan | Markdown标题；时长 | 正式Clip编号、人类可读标题、4—15秒平台生成时长；不输出独立CLIP标题字段，不把SEQ/BEAT/COV/UNIT变成栏目 |
| Format / Visual Development / Color | 画幅；主风格 | 已确认画幅、媒介、色彩来源与层级、明度/对比、白平衡/偏色、肤色保护、光线体系、镜头稳定性与表演尺度 |
| Character / Environment / Prop / FX Assets | 参考资产 | 当前Clip实际使用并经Reference Budget审计后Projected Final Count≤9；除A/B待补充`REF-TAIL`外，图片资产必须真实存在且已确认；逐项写资产ID/名称、真实引用或待补充状态、用途与禁止修改特征；任何`REF-TAIL`写明同镜头连续承接用途或空间/站位/景别参考用途；核心角色独立图不可合并。Voice/Audio Reference默认省略，只有用户明确要求当前视频模型使用时才作为非视觉输入最小列出 |
| Previous Clip / Opening State | 首帧参考 | A/B/C与`Tail Frame Required = YES / NO`；A使用统一`REF-TAIL`名称和固定直接承接句并完整锁定；B明确参考尾帧但另起新镜头重新构图，不使用Direct固定句；C不列尾帧，以Canonical资产、Spatial Blocking与文字规则重建；人物姿态/位置/朝向/距离、摄影机/构图、环境/天气、道具、动作、光线与情绪状态 |
| Clip End State / Next Clip | 尾帧限制 | 可冻结最终帧、人物/摄影机/道具/环境/声音最终状态、最后1秒限制与下一Clip用途 |
| Character Continuity / Performance | 人物一致性；主风格 | 外观与状态锁定、表演尺度、跨镜湿润/伤痕/体力/情绪连续性 |
| Environment / Spatial / Lighting / Color | 环境一致性 | 地点、天气、固定结构、光源方向、色彩来源与锚点、材质响应、运动方向、轴线和背景逻辑 |
| Sound / Dialogue | 台词；音效 | Dialogue Performance、口型/同步、声源位置与同期空间；Voice Identity默认不投影。`音色特征`只在用户明确要求当前视频Prompt包含声音控制时条件输出最小Delta |
| Cross-shot Risk | 反向提示词 | 永久固定禁BGM首句及本Clip真实高风险项；不存在音乐例外 |

## Per-Shot Projection Matrix

| 来源知识 | 固定目标字段 | 必须保留的语义 |
|---|---|---|
| Shot Scale / Focal Length | 景别；镜头/机位；画面描述；空间关系；镜头结尾状态；反向提示词 | 景别与焦段分离；摄影机距离、尺度、边缘安全、对焦/景深、运动约束与结束连续性；不输出FLN编号 |
| Camera Movement / Combination | 镜头/机位；画面描述；空间关系；镜头结尾状态 | 起点、路径、速度、触发、终点、轴线与稳定落点；每镜一个主要路径；边界语义进入镜头结尾状态；不输出CMG编号 |
| Composition / Director Patterns | 镜头/机位；画面描述；空间关系；镜头结尾状态 | 主体位置、前中后景、负空间、内框/遮挡/反射/引导线来源、焦点主次、变化过程与最终几何 |
| Lighting / Color | 起始状态；画面描述；空间关系；道具状态；镜头结尾状态；主风格；环境一致性；反向提示词 | 光源、方向、光质、曝光、介质、颜色来源与层级、材质响应、起止光色状态及连续性；不新增光线或Color字段 |
| Character Action / Performance | 起始状态；画面描述；人物动作与情绪；台词；音效；镜头结尾状态；人物一致性 | 刺激、注意/视线、主要面部与身体动作、呼吸、公开状态与泄漏、行动选择、强度、Settled State与连续性 |
| Dialogue Performance | 人物动作与情绪；台词；音效 | 准确台词、当前情绪/力度/停顿/节奏/韵律、口型与空间声；不得把当前表演写成稳定Voice Identity，也不得因缺少Voice Profile而临时推导 |
| Character Count | 人物一致性；画面描述；空间关系；反向提示词 | 每镜实际角色精确数量；唯一角色的正向唯一性和前中后景无第二个同类；复制、分身、镜像重复、背景第二个与相似替身禁令 |
| Spatial / Blocking | 起始状态；空间关系；画面描述；镜头结尾状态；反向提示词 | A/B左右、前后景、朝向、视线、距离、路线、遮挡顺序、关系轴线、正脸/侧背许可、同景深许可及最终位置；追逐默认后追前逃并禁止并排合影 |
| Prop | 起始状态；画面描述；道具状态；镜头结尾状态 | 当前World-State、形态、尺寸、持有者、左右手、位置、方向、悬浮许可、转换完成状态、物理变化过程和最终状态 |
| Sound | 音效；台词；镜头结尾状态 | Persistent Ambience、同步Foley/动作声/呼吸/对白/剧情内声源、距离与Sound Bridge/Cut/Fade |
| FX | 画面描述；人物动作与情绪；空间关系；道具状态；音效；镜头结尾状态；反向提示词 | 来源、触发、阶段、方向、尺度、强度、物理交互、光影/声音影响、残留后果与专项风险 |
| Editing / Handoff / Transition | 参考资产；首帧参考；尾帧限制；起始状态；镜头结尾状态 | Boundary Source、Transition Class、Outgoing/Incoming Anchor、Cut Point、继承/断点/未决状态与禁止提前动作；不新增边界字段，不输出TRN编号 |
| Sequence / Coverage / Clip | 画面描述；镜头结尾状态；Markdown标题；时长 | Required Coverage完成证据、Clip内逐镜状态链与跨Clip状态；内部ID不成为栏目 |

## Serialization Rules

Color、Lighting、Focal Length、Composition、Camera Movement和Director Pattern必须拆成固定字段中的具体执行语义，不得只保留“电影感”“冷色调”“85mm”“压迫构图”“缓慢推进”等标签。

最终Prompt不得输出CLR编号、CMG编号、FLN编号或其他内部模式ID。`反向提示词：`首句永久固定为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”。

连续性投影固定为：

`首帧参考 → 分镜1起始状态 → 可见动作过程 → 分镜1镜头结尾状态 → 下一分镜起始状态或下一Clip首帧参考 → 尾帧限制`

同一Clip内的连续分镜在前一分镜“镜头结尾状态”中写明Boundary Class、同一Clip连续生成、Outgoing Anchor与禁止提前动作；后一分镜“起始状态”逐项继承。跨场景时明确断点与重建依据，不伪造连续动作。

## Applicability Gate

逐镜内部判断：资产与状态、Coverage目的、主要动作与表演、Camera/Composition、焦段、Lighting、Color、Sound、FX、Prop、Dialogue、群体表演、转场、Sequence与模型稳定性是否Applicable。只有Applicable模块进入投影；每个Applicable模块至少在矩阵指定的一项固定字段中留下具体证据。

未触发模块不得为了形式完整而虚构事实。模板字段始终完整，但不适用内容应明确写出“不适用”及具体原因，不得留空或写“同上”。

## Internal Projection Ledger

Template Mapping前建立一次性内部核对，不得原样输出：

| Applicable Source | Confirmed Fact / Design | Target Existing Field(s) | Evidence Present | Conflict / Return Route |
|---|---|---|---|---|

Ledger只防止语义丢失，不拥有最终Schema。发现上游冲突时返回事实拥有者，不以Prompt文案掩盖冲突。

## Semantic And Structure Loss Check

最终格式化前后各检查一次：

- Applicable Knowledge是否留下具体执行证据，未触发模块是否没有被虚构。
- 是否丢失摄影机终点、人物最终状态、FX后果、声音尾部或下一镜锚点。
- 是否泄漏内部知识标题、模式ID、Ledger或SEQ/BEAT/COV/UNIT栏目。
- 是否严格按Confirmed Clip Production Plan分组，每个Clip、每个分镜和每个字段都完整、顺序不变。
- 是否因批量或篇幅压缩、共享、合并、删减、改名字段，或使用“同上/沿用前文/略”。
- 用户未明确要求把声音控制写进当前视频模型Prompt时，是否完全省略`音色特征：`、Voice Profile、Voice/Audio Reference和声音资产状态文字；用户明确授权时，是否只输出当前Clip必要的最小声音控制Delta。
- 是否只保留当前Clip有控制价值的信息；已由正式角色/环境/道具资产锁定的外观与结构是否只作最小确认，没有在人物一致性、环境一致性或逐镜正文中长篇重复。
- 是否存在同义重复、跨字段机械复述、优先级不明，或互相冲突的机位/运动/动作/站位指令；冲突是否已消解或返回上游。
- 重要抽象形容词是否具有至少一个可见或可听执行对应，并保留原情绪功能而非机械删除。
- 能以正向状态锁定的约束是否已经执行`Negative Constraint → Positive Target State`；反向提示词是否只保留固定平台边界和少量真实高风险项，而不是所有可能错误的清单。
- 高共现大词是否经过Semantic Template Decomposition；是否没有把“创业、约会、学生、婚礼、医院、黑帮、赛博朋克、日系青春”等默认视觉包无依据带入当前Clip。
- 是否存在无可见收益的工程级小数、精确轨迹或伪物理参数；有价值数字是否按视觉关系/摄影倾向使用而非承诺严格仿真。
- 是否遗漏当前Clip真正变化的主要动作、时间顺序、中间变化、结束状态或首尾承接；高优先级动作/空间/镜头信息是否比装饰性风格词更清楚。
- 是否已在五维检查前完成Generation Budget Allocation；Primary目标是否唯一清楚，Secondary是否真正支持它，Economized是否主动降低至少一个非必要高负荷维度；是否仍把身份、复杂动作、高密场景、复杂运镜、群体、口型、FX与光色变化同时拉满。
- 是否只执行`this_clip_only`的主要可见Beat并形成改变后的Endpoint；是否重播`already_happened`、提前表演`reserved_for_later`或让`do_not_show_yet`元素提前出现。
- 是否只保留从上一镜/上一Clip合法继承的状态，没有混入其他镜头的动作、机位、结束状态或风格残留；是否没有堆叠互相稀释的导演、美术、摄影与渲染风格。
- 是否没有方头括号旧章节、独立CLIP标题字段、“与下一镜衔接”或其他额外字段。
- `参考资产：`、`首帧参考：`、`尾帧限制：`是否无条件存在且非空。
- `参考资产：`是否通过Reference Budget Check：Projected Final Count与已提交图片数≤9、无当前Clip无关项、无重复占位；除明确待补充的A/B `REF-TAIL`外无虚构资产；每个`REF-TAIL`用途与状态明确；核心角色各自独立；是否仅在超限风险触发后整合同类非角色信息。
- 是否通过Clip Preflight：连续性三选一且尾帧引用正确；逐分镜World-State与资产一致；角色精确数量、追逐/多人空间构图、关键道具状态和适用转场五要素均有现有字段证据；失败设计没有被反向提示词兜底。
- 是否明确A/B/C并据此标记`Tail Frame Required = YES / NO`；A/B无图时是否在`参考资产`直接列统一`REF-TAIL`、对应用途与“待用户提供/待上传、未确认”，且未冒充已提交图片；A是否使用固定直接承接句，B是否明确另起新镜头且未使用该句，C是否完全未列`REF-TAIL`；本Clip新尾帧限制是否完整。
- 每个分镜是否完整重复十个固定字段；下一镜语义是否已进入“镜头结尾状态”。
- `反向提示词：`首句是否无例外使用固定禁BGM句。

## Priority On Conflict

格式冲突优先级固定为：

`templates/10_video_prompt.md固定输出契约 > 任何旧Template / Workflow / Adapter / Knowledge / Rules / Validator / 示例 / 历史格式`

内容事实仍服从已确认上游资产、剧情和生产决策；Template只拥有格式，不拥有改写事实的权限。

## Final Principle

知识架构的价值不在于Prompt中出现多少专业名词，而在于每项适用知识都被转换成模型可执行、可观察、可连续验证的固定字段内容，同时每个Clip严格保持完整统一模板。
