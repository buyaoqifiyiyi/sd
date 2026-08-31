# Consistency Rules

# AI影视项目一致性规则


## Purpose


本规则用于保证AI影视项目中的视觉连续性。


管理：

- 角色一致性
- 环境一致性
- 道具一致性
- 风格一致性
- 镜头连续性


本规则负责检查和维护。


不负责创建资产。


---

# Rule 00

# Clip Preflight High-Priority Gate

STATE-07与STATE-08逐Clip强制执行`knowledge/clip_preflight_check.md`。本Gate先于Reference Budget、Prompt润色和模型适配，且不得被下游反向提示词替代。

三条最高优先级规则：

1. **视觉连续 ≠ 剧情连续；尾帧需求 ≠ 尾帧当前可用性。** 当前Clip必须先在`视觉连续 / 剧情连续 / 主动切场或切世界`中三选一，再在同一Previous-Clip Continuity Decision内把尾帧使用方式收敛为A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】，并据此标记`Tail Frame Required = YES / NO`。A与B均为`YES`，C为`NO`；不得用“系统当前是否已有尾帧图”反向改变分类。A/B所需尾帧尚未提供时，STATE-07 / STATE-08仍必须在当前Clip【参考资产】中直接列出统一`REF-TAIL`名称，明确“待用户提供/待上传、未确认”，并提示用户从上一Clip最终成片手动截取最终有效尾帧后添加；这是一项待补充参考资产声明，不代表图片已存在、已上传或已确认，也不计入已提交图片数。Prompt可以完整编译和交付，但实际提交生成前必须补入该尾帧。
2. **参考资产必须先通过当前世界状态检查。** 每分镜明确现实、幻想、耳中玉境或项目已确认的其他时空层；只有当前阶段实际存在、实际出场且状态适用的资产可进入候选。预算只能在World-State过滤后执行。
3. **跨世界镜头必须先设计转场，再生成提示词。** 现实↔幻想/耳中玉境、地点/时间跳跃、尺度与角色/道具形态转换，先锁定起点状态、转换媒介、运动方向/过程、终点状态与转场后首个稳定构图；除非用户明确要求，不得用含糊闪光或突然切换替代。

每个分镜同时必须锁定：实际角色精确数量；追逐/战斗/对峙/多人镜头的前后景、左右、朝向、关系轴、运动方向、正脸与同景深许可；关键道具当前形态、尺寸、持有者、悬浮许可与转换完成状态。剧情规定唯一角色时，正向设计明确唯一一只/名且前中后景无第二个同类，反向提示词再禁止复制、分身、镜像重复、背景第二个和相似替身。追逐默认后追前逃，禁止双方并排正对镜头、同景深海报式合影或群像站桩。

任一适用项FAIL：STATE-07不得确认Clip Plan；STATE-08不得Template Mapping或输出Prompt。先最小修正Affected Clip / Shot / Asset并从连续性分类重跑。



---

# Rule 01

# Character Consistency


所有角色必须保持一致。


包括：


- 面部特征
- 脸型与五官
- 年龄状态
- 年龄感
- 身体特征、体型、身高比例与身体比例
- 发型
- 头饰
- 服装形制、结构、主配色与辅助配色
- 物种形态、羽毛/毛发等物种识别特征
- 非人角色身体结构、肢体组织、头身关系与非拟人化边界
- 气质表现


同一角色在不同镜头中：

必须引用同一角色资产。


凡角色已经有用户明确指定的外观基准，或Asset Registry中的Active CHAR Version与Canonical References，该Active角色资产包及其Canonical References必须作为后续全部外貌与形态内容的唯一基准。适用范围包括角色设定图、动作状态图、比例图、场景示意图、Storyboard/分镜参考图、海报、Key Art、封面、Detailed Shot Design、Clip Production、图片/视频Prompt、Seedance Prompt和最终视频生成。

只要求动作、姿势、表情、机位、景别、构图或镜头运动变化时，只允许相应表演与摄影维度变化，不得借机重新设计外貌、服装基础、配色、物种或身体结构。非人角色与真人角色同等严格；被锁定为孔雀本体的角色不得变成人形、半人形或其他未授权拟人化形态。

新参考、视觉风格、导演知识、Prompt、模型适配或生成结果与锁定角色资产冲突时，以锁定资产为最高视觉身份优先级。冲突结果必须拒绝、重生或返回上游修正，不得混合两套外貌求折中。只有用户明确批准并按`references/asset_lock_contract.md`切换的新Active Version可以取代旧基准。



禁止：

同一角色出现不同视觉版本。

不得用下游动作图、Storyboard、海报、首尾帧或最终生成结果反向覆盖角色资产。


## Stage Inheritance Gate

- STATE-03 Asset Development：把用户明确指定的角色外观基准登记到当前CHAR Version；未确认资料保持Candidate，但不得被AI自由生成覆盖。
- STATE-04 Visual Development与Poster/Key Art：只改变项目级风格、光色、构图与宣传表达，不拥有角色外观重设计权。
- STATE-05 Scene Breakdown与场景示意：只安排场景、空间和角色状态，不拥有角色外观重设计权。
- STATE-06 Detailed Shot Design：只设计景别、机位、构图、动作、表演与镜头语言；逐Shot继承Active CHAR Version。
- STATE-07 Clip Production：只组织已确认Shot为生成单元；逐Clip继承相同角色锁。
- STATE-08 Prompt / Video Generation：逐角色列出并锁定Active CHAR Version与实际Canonical References；Prompt编译和模型适配不得稀释或改写外貌锁。
- Optional Storyboard：只作视觉预演，不得成为新的角色Canonical Reference或改写角色身份。
- STATE-09 Review：任何脸、年龄、发型、头饰、体型、比例、服装形制、配色、物种、羽毛/毛发或非人身体结构漂移均判定失败并路由到最小必要上游修正。



---

# Rule 02

# Environment Consistency


同一环境必须保持空间连续。


包括：


- 建筑结构
- 空间布局
- 材质
- 色彩
- 光照逻辑



同一地点再次出现时：

优先使用已有环境资产。



禁止：

无原因改变环境结构。



---

# Rule 03

# Prop Consistency


关键道具必须保持一致。


包括：


- 外观
- 尺寸
- 材质
- 使用状态
- 当前世界状态与形态版本
- 尺寸
- 持有者、左右手、位置、方向与接触关系
- 是否允许悬浮
- 形态转换是否完成及其可见过程


剧情中重复出现的道具：

必须引用同一道具资产。

同一道具在不同世界或阶段具有现实形态、武器化形态等状态时，必须按逐分镜World-State使用对应Canonical State。完全位于转换后世界的Clip不得继续引用转换前形态；只有正在执行已确认转换的Clip才可按Pre/Post阶段同时引用两种状态，并必须完成转场五要素。不得把两种形态混成同时存在的两件道具、无过程瞬变或无授权悬浮。



---

# Rule 04

# Visual Style Consistency


整个项目必须保持统一视觉方向。


检查：


- 色彩体系
- 光影风格
- 摄影语言
- 美术风格



避免：

不同章节出现明显风格变化。



---

# Rule 05

# Shot Continuity


镜头设计阶段必须检查：


- 人物位置
- 动作连续性
- 时间连续性
- 空间关系



避免：

角色位置突然变化。


动作无逻辑跳跃。


---

# Rule 05A

# Relational Screen Geometry


战斗、双主体、对峙、对话、追逐、相向运动或任何需要观众持续辨认双方关系的镜头，必须把人物朝向升级为可验证的镜头几何合同，而不是只写“面对彼此”“看向对方”。


每个适用镜头必须先锁定：

- A、B的画面左/右与前/中/后景位置
- 双方身体朝左/朝右、侧身程度、视线目标和距离
- A—B关系轴，或由主攻击/主运动建立的唯一主轴
- 摄影机所在轴线侧
- 连接双方的视线、攻击、武器、追逐路线、水流、能量或抛射物的来源—路径—目标


默认规则：

- 一个连续Shot或Clip只使用一条主要关系轴
- 摄影机保持在180度轴线同一侧；侧面双人、侧后双人或Over-the-Shoulder优先
- 双方同时出镜并相互面对时，不得同时完整正脸朝摄影机；最多一方接近正脸，另一方保留侧面、背侧或过肩锚点
- 屏幕左右、人物朝向、眼线、攻击方向和受击位置必须相互一致
- 攻击、视线、水流、能量和追逐路线必须形成可追踪的空间连线，不能从错误一侧、错误喷口/武器或错误主体发出


除非Shot Design已明确标记`intentional axis crossing`，并提供已建立轴线、中性机位或连续可见越轴路径、固定地标和新轴线侧，否则禁止跨轴。无法稳定执行有意越轴时，必须降级为轴线同一侧的固定侧面或Over-the-Shoulder，不得接受随机左右翻转。


存在合法首帧、上一Clip尾帧或连续段既有构图时，优先把该帧作为几何锚点，逐项锁定左右、朝向、高低、距离、摄影机轴线侧及空间连线。文字不得推翻参考帧已确认的几何关系；参考帧与已确认剧情冲突时按Rule 11判定边界，不得混合猜测。


尾帧检查必须复核：

- 双方左右与前后是否仍正确
- 身体朝向、视线与连接线是否仍指向正确目标
- 摄影机是否仍在授权轴线侧
- 是否发生无动作换位、随机转身、双正脸或来源—目标反转
- Continuous Handoff时，该尾帧能否直接成为下一镜首帧；不能直接继承时是否已明确Reference-Only或合法断点


任一项无法从文字或参考帧中唯一判断，视为空间合同未完成，返回STATE-06补齐，不得留给STATE-08模型自行猜测。



---

# Rule 06

# Reference Priority


资产版本与参考优先级统一服从references/asset_lock_contract.md。

角色、环境、道具和FX各自使用Registry中对应实体的Active Version；不同资产类别之间不存在互相覆盖的优先级。

Detailed Shot Design与Clip Production只能记录已批准资产在具体Shot/Clip中的状态，不得改变资产身份；不得用Storyboard图片重新定义资产。

Reference Selection / Routing除决定“是否使用”外，还必须为每个入选Reference声明唯一`Primary Role / Purpose`，并按以下Authority边界消费；不同Authority只控制自己的维度，不得凭画面相似度跨权覆盖：

- **Identity Authority**：Active Character Canonical References；唯一负责角色身份、脸、年龄、体型、基础服装、物种与身体结构。
- **Environment Authority**：Active Environment Canonical References；负责正式环境结构、固定布局、材质与长期空间识别。
- **Prop Authority**：Active Prop Canonical References；负责正式道具身份、造型、材质与Canonical形态。
- **Transient State Authority**：用户已接受Take的Accepted Canon State，以及与该Take绑定的上一Clip / `REF-TAIL`；只负责姿态、站位、朝向、人物距离、动作阶段、短时道具持有、临时光态/天气/环境状态与起始构图。
- **Motion Authority**：实际入选的已确认动作或视频参考；只负责动作路径、节奏、受力、速度感或表演阶段，不负责身份、环境结构或道具造型。
- **Camera Authority**：实际入选的已确认镜头/机位/运动参考；只负责机位、景别、构图、轴线侧、焦点与摄影机路径，不负责角色身份或资产设计。
- **Audio Authority**：当前系统已支持且实际入选的Confirmed Voice/Audio Reference；只负责声音身份或授权的音频执行，不得改变视觉身份。它默认由输入音频自身携带状态，不投影进STATE-08视频Prompt；只有用户明确要求把声音控制写进当前视频模型Prompt时，才按最小Delta引用。没有适用声音资产不构成缺失项，不写`No Voice Asset`，也不自动触发AUDIO模块。

同一Reference可以有一个Primary Role和必要的兼容Secondary用途，但Secondary不得越过上述Authority。发生冲突时，正式角色/环境/道具Authority分别高于Transient、Motion、Camera与风格参考；临时状态Reference中的脸部、服装、环境结构或道具造型漂移不得被下一Clip继承。尤其`REF-TAIL`脸部轻微漂移时，下一Clip仍以Active Character Canonical References保持身份，只从尾帧或Accepted Canon State消费已确认的姿态、站位、动作阶段与其他合法瞬时状态。



---

# Rule 07

# Version Control


资产发生变化时：

必须记录版本。


例如：


CHAR-001@v001


CHAR-001@v002



禁止：

同一项目混用不同版本资产。

实体ID保持稳定，版本按references/asset_lock_contract.md独立记录；不得把版本后缀误当作新实体ID。



---

# Rule 08

# Correction Rule


发现一致性问题时：


优先检查：


资产版本。


镜头设计。


参考信息。



禁止：

仅通过修改Prompt掩盖资产问题。



---

# Rule 09

# Workflow Boundary


一致性检查可以发生在：


- Asset Development后
- STATE-07 Clip Production阶段
- Video Review阶段



但不替代：


资产制作。


镜头设计。


视频生成。


---

# Rule 10

# Shot Boundary Contract


从STATE-06 Detailed Shot Design开始，任何逐镜输出都必须为每个镜头保存三类边界信息：


- 起始状态如何取得：继承上一镜头、继承场景初始状态，或由已确认的叙事断点重新建立
- 本镜头最后一帧必须锁定的稳定、可验证状态
- 本镜头如何进入下一镜头，或为什么不能直接继承


对应阶段的Template负责这些信息的最终字段名称和顺序。

进入STATE-08后，边界信息不得因“一个Clip包含多个分镜”而被隐式处理。同一Clip内每个分镜都必须保留起始、结尾和下一镜衔接；每个Confirmed Clip成为独立G生成段，在【主风格】之前输出【首帧参考】与定义自己新结束状态的【尾帧限制】，并输出独立反向提示词。跨Clip必须先根据当前Clip Start Requirement判定A/B/C：A/B标记`Tail Frame Required = YES`并在【参考资产】列统一`REF-TAIL`、用途与真实状态，缺图时标待补充；C标记`NO`且不列`REF-TAIL`。资产是否已存在不得反向改变分类。

## Cross-Clip End-State Record

STATE-07必须把已经散布在Entry、内部Shot状态链、Exit、Spatial Blocking、道具连续性、摄影机路径、稳定尾帧与Handoff中的事实，合并为每个Clip一份简洁的内部`Clip End-State Record / Next-Clip Carryover`。这是Shot-State Memory所需语义在现有Shot Boundary Contract内的实现，不新增STATE、ID命名空间、资产类型或STATE-08最终字段，也不得复制Professional Detailed Shot Script的全部专业字段。

记录固定使用八组语义：

- `Character State`：各人物位置、左右/前后、朝向、坐/站/移动姿态、人物间距离、动作结果/阶段，以及谁持有什么。
- `Spatial State`：环境锚点、关系轴/180度轴线、路径、视线或来源—路径—目标连线、不可穿越与不可换边事实。
- `Prop State`：关键道具身份、形态、持有者/左右手、位置、方向、接触、损伤/开合/转换等当前状态。
- `Camera State`：摄影机位置、高度、朝向、轴线侧、最终机位、景别、构图、焦点与稳定状态。
- `Environment State`：当前Scene / World-State、固定结构、时间、天气、光线、综合色彩、材质/介质与持续声音状态。
- `Performance State`：情绪、公开状态/泄漏、呼吸或体力、动作完成度与稳定表演结果。
- `Continuity Risks`：下一边界最可能发生的状态断裂、人物/道具重置、左右/轴线翻转、身份/环境/道具/光态漂移及模型执行风险。
- `Next-Clip Carryover`：下一Clip必须保持、允许有动机改变、明确不继承或仍待确认的事实，连同A/B/C、Tail Frame Requirement、参考用途和重建依据。

下一Clip的`首帧参考`与首镜`起始状态`必须消费这份记录；A逐项直接继承，B区分保持项与允许改变项，C只继承剧情仍有效事实并用当前Scene / World-State、Canonical资产、Confirmed Spatial Blocking与文字规则重建。记录与上游事实冲突时按Rule 12返回，不得在STATE-07/08取平均或猜测。

### Accepted Take Canon

`Clip End-State Record / Next-Clip Carryover`首先是计划合同，不得把计划状态与实际生成结果混为同一层。每个实际生成Take按现有Execution Ledger / Generation Run Record区分：

- `Planned Start State / Planned End State`：来自Confirmed Clip Production Plan与Prompt边界合同。
- `Observed Start State / Observed End State`：对该Take实际画面核验得到的八组状态；只记录可观察事实，不把计划值抄成观察值。
- `Accepted Canon State`：只有用户明确接受该Take，且Acceptance证据绑定Run ID、Prompt Revision与Review结果后，才从Observed State建立的后续连续性权威状态。

下一Clip已存在Accepted Canon State时，必须用它覆盖同维度的Planned State并形成当前首帧；不得为了回到原计划而无过程改手、换位、重播动作或重置摄影机/环境状态。没有Accepted Take时继续使用最近Confirmed Planned State；被拒绝、未确认或仅生成未审的Take不得写入Canon。

Accepted Canon State只提升被接受的**实际瞬时状态**，不提升错误资产身份。若Accepted Take或`REF-TAIL`与Active Character / Environment / Prop Authority冲突，正式Canonical资产继续控制身份、结构与造型；只继承该Take中已接受且不越权的姿态、站位、动作阶段、持有关系、临时光态等状态，并把冲突列入`Continuity Risks`。任何Canon更新都复用现有八组语义、Execution Ledger与Project State的现有`Continuity And Open Risks`/Artifact指针，不新增Clip Registry、资产类型、主STATE或STATE-08字段。

## Cross-Clip Tail-Frame Carryover

必须沿用现有Previous-Clip Continuity Decision、`参考资产：`、`首帧参考：`、`尾帧限制：`和逐镜起止状态，把上一尾帧使用方式明确区分为以下三类；这是对既有Direct / Reference-Only / Not Required的补强，不新增最终Prompt字段或平行Schema。

- **A【同镜头连续承接 / Direct】**：上一Clip最后一个镜头在当前Clip继续，目标接近一镜到底；连续运镜、连续动作、摄影机位置、方向与构图都应无缝接上。必须标记`Tail Frame Required = YES`，并在【参考资产】写`REF-TAIL-XX｜CLIP-XX尾帧参考（同镜头连续承接用途）`。当前Clip【首帧参考】必须逐字包含`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`，并继续锁定人物姿态、位置、左右/前后、朝向、视线、人物间距离、动作阶段、构图、景别、机位与轴线侧、环境、光线、天气、道具、情绪和持续声音；不得重新初始化或重播已完成动作。
- **B【新镜头参考型 / Reference-Only】**：当前Clip另起新镜头重新构图，但上一尾帧仍用于保持人物站位、朝向、人物间距离、景别衔接、空间关系、道具状态或起始构图。也必须标记`Tail Frame Required = YES`并把上一尾帧列入【参考资产】，推荐写法为`REF-TAIL-XX｜CLIP-XX尾帧参考（用于延续上一镜头结尾的角色站位、朝向、景别与空间关系；空间/站位/景别参考用途）`。【首帧参考】必须说明`参考 REF-TAIL-XX｜CLIP-XX尾帧参考，延续上一镜头结尾的角色站位、朝向、人物距离、景别与空间关系逻辑，但当前Clip另起新镜头重新构图。`，同时写清允许改变的新机位、景别、视角或构图及保持不变的空间事实；不得使用A类“直接承接依据起镜”句式，不得把新镜头误写成同镜头续拍。
- **C【新镜头且无需尾帧 / Not Required】**：当前镜头明确换机位、换景别、反打、特写、俯拍/仰拍或重构图，且不依赖上一尾帧画面状态。标记`Tail Frame Required = NO`，不得在【参考资产】加入`REF-TAIL`或要求用户截图；只依靠Active Character / Environment / Prop等正式资产、Confirmed Spatial Blocking与文字空间规则保持连续性，并在【首帧参考】说明新镜头的重建依据。
- **用途声明硬规则**：任何情况下只要【参考资产】出现`REF-TAIL`，同一条目必须明确标注“同镜头连续承接用途”或“空间/站位/景别参考用途”。只写资产名、只写“尾帧参考”、混用两种用途或用途与【首帧参考】不一致，均判定失败。
- **待补充资产声明**：A/B由连续性需求决定，不由文件是否存在决定。即使当前对话尚未上传图片，【参考资产】仍必须直接列出`REF-TAIL-XX｜CLIP-XX尾帧参考`、对应用途及`待用户提供/待上传、未确认`状态；不得省略，也不得声称已上传、可访问或已确认，不得伪造路径。它占1个Projected连续性图片位但不计入已提交图片数；用户在实际生成前自行截取并添加。
- 尾帧参考只锁定当前时刻的构图、姿态、位置和状态，是连续性锚点，不是基础资产替代物。角色身份/外貌仍以Active Character Canonical References为最高依据；环境结构仍以Active Environment资产为最高依据；道具造型仍以Active Prop资产为最高依据。尾帧与基础资产冲突时按Rule 12处理，不得让尾帧覆盖正式设定。
- 当前Clip一旦使用上一Clip尾帧，自己的`尾帧限制：`必须定义新的结束状态和可用性条件，供下一Clip在实际生成、提取并确认后建立新的尾帧资产；不得把上一Clip尾帧名沿用为当前Clip尾帧。

标准链路：

`上一Clip结束状态 → 判定A/B/C与用途 → A/B在参考资产声明REF-TAIL（缺图则标待补充）→ 首帧按Direct或Reference-Only分别说明 → 实际生成前补入尾帧 → 当前Clip生成 → 当前Clip尾帧限制定义新结束状态 → 下一Clip重新判定`


Rules只规定：

这些语义不得缺失。


不得只在单个示例中临时补写。


如果存在已确认首帧或尾帧参考：

- 首帧是本镜头可见起始状态的边界锚点
- 尾帧是本镜头可见结束状态的边界锚点
- 参考帧只锁定其被确认的用途，不自动授权修改剧情、资产身份、人物关系或道具逻辑
- 参考帧与上一镜头状态或已确认剧情冲突时，不得混合猜测；必须判定为Motivated Discontinuity或Unresolved Handoff
- 尾帧中若已经包含下一镜动作，只有该尾帧与动作切点已被明确确认时才可保留，否则应返回上游修正


最后一帧限制必须锁定当前镜头已经发生的结果。


禁止：

- 为了衔接擅自改变剧情
- 无依据移动人物或交换左右站位
- 无动作改变道具持有者、位置、方向或状态
- 提前执行下一镜头才应发生的转头、抬手、对白、离开、接触或其他动作
- 把未知的下一镜头内容当作事实补写


---

# Rule 11

# Transition Classification


每一对相邻镜头必须先判定连接类型，再决定是否继承状态：


## Continuous Handoff


同一连续时间与空间内的直接切换、动作匹配、视线匹配或声音桥接。


必须继承所有仍然有效的人物、环境、道具、动作、情绪与持续声音状态。

STATE-08中必须先比较上一Clip End State与下一Clip Start Requirement，确定A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】，再核验对应尾帧可用性。A/B均标记`Tail Frame Required = YES`并在下一段【参考资产】直接列出统一`REF-TAIL`名称、用途与状态：缺图时写“待用户提供/待上传、未确认”，有图时才可写实际引用及已确认状态；Prompt可完整交付，但实际提交生成前必须补图。A在【首帧参考】使用固定直接承接句；B明确另起新镜头重新构图且不得使用该直接承接句。C标记`NO`，不列`REF-TAIL`、不要求截图，只用Canonical基础资产、Confirmed Spatial Blocking与文字状态核对或重建首帧。下一段起始状态不得与合法尾帧或已记录End State冲突，也不得重播已完成动作。


## Motivated Discontinuity


已确认的场景切换、时间跳跃、硬切、蒙太奇、闪回、故意跳切或其他叙事断点。


不得伪造镜头之间不存在的过渡动作。

STATE-08中C类或跨场景的下一G段不得把上一尾帧列入【参考资产】、作为生成输入或写成`REF-TAIL`资产引用；【首帧参考】必须写明不继承上一Clip画面状态、经确认的重建原因，并只保留剧情授权的身份、服装、道具后果、情绪或主题锚点。连续性核对依靠上一Clip文字End State、Canonical基础资产、Confirmed Spatial Blocking与文字空间规则，不得虚构资产名。


下一镜头必须基于已确认剧情重新建立起始状态，同时继续锁定角色身份、资产版本以及剧情没有授权改变的事实。


## Unresolved Handoff


下一镜头尚未设计、上游信息不足，或前后状态互相矛盾。


不得猜测。


应标记为暂定或无法直接继承，保留安全、稳定的当前结尾；当下一镜头确定后，必须成对复核并以最小必要修改更新边界信息。


---

# Rule 12

# Boundary Priority And Conflict Resolution


镜头边界发生冲突时，按以下顺序判定：


1. 用户明确要求且已经确认的剧情、剪辑意图与镜头目的
2. 已确认的场景/时间断点和Shot Design
3. 已确认资产、人物站位逻辑、空间轴线、道具物理状态与动作结果
4. 相邻镜头的状态连续性与情绪连续性
5. Seedance执行稳定性、结尾稳定窗口与提示词简化
6. 文字美化、炫技运镜和装饰性细节


低优先级要求不得覆盖高优先级事实。


“自动衔接”只负责描述合法的镜头边界，不拥有改写剧情、资产、站位或动作的权限。


如果高优先级信息本身矛盾：


不得用自动衔接掩盖矛盾。


应返回对应上游阶段修正，或在逐镜输出中明确标记无法继承。


---

# Rule 13

# Boundary Validation


逐镜输出前必须进行相邻镜头成对检查：


STATE-08每个Clip还必须先通过四项不可缺省的交付门槛：

- 【参考资产】显式列出当前Clip实际采用的已确认角色、环境、道具、FX、声音Reference与合法首尾帧，并写明用途和不可改动约束；A/B所需`REF-TAIL`是唯一允许的待补充声明例外，即使缺图也必须列名、用途与“待用户提供/待上传、未确认”，但不得写成已提交资产；任何`REF-TAIL`均必须标明“同镜头连续承接用途”或“空间/站位/景别参考用途”
- 前置【首帧参考】明确A/B/C：A使用固定直接承接句并逐项锁定；B说明另起新镜头重新构图、列出保持项与允许变化且禁止使用直接承接句；C不列`REF-TAIL`并写明Canonical资产、Spatial Blocking与文字重建依据；每个分镜第一帧来源必须与之相符
- 前置【尾帧限制】与每个分镜稳定尾帧要求一致，Package尾帧默认清楚、低动作、可冻结、可继承、可作为下一Clip接口，最后1秒不启动新复杂动作；除非剧情明确授权，不得停在高速运动、动作未完成、主体严重遮挡或构图不可读状态
- 每个分镜明确与前后分镜/Clip的连续性关系；叙事性场景切换必须判定为“实体首帧继承”或“状态基准参考”，或明确不继承及重建原因，不得无说明丢失连续性

上述任一项缺失、使用占位文字或互相矛盾时，STATE-08 Final Validation必须失败，不得直接交付。


- 上一镜头结尾状态是否与连接类型一致
- 下一镜头起始状态是直接继承还是重新建立
- 人物、环境、道具、空间、动作、情绪、摄影机与持续声音中，哪些状态继承、哪些状态有合法变化
- 内部动作容量是否能够容纳结尾稳定限制且不会截断必要动作；该判断不得转写为最终Prompt时间轴
- 是否提前执行下一镜头动作
- Continuous Handoff是否自动判定为：上一尾帧直接作为下一G段起始帧，或仅作为第一顺位连续性参考并重建兼容边界；Motivated Discontinuity是否显式声明不继承及重建原因
- 是否每个G段只对应一个Confirmed Clip、包含1个或多个相邻正式分镜；单镜独立执行、多镜作为同一次连续长镜头执行，且各自拥有结尾帧要求、尾帧用途判定与反向提示词
- 是否Total Clips不大于Total Formal Shots，且所有单分镜Clip均为4—15秒并具有独立生成理由
- 战斗、双主体、对峙、对话、追逐或相向运动是否已经锁定左右、朝向、关系轴、摄影机轴线侧和来源—目标空间连线，而非只写抽象人物朝向
- 上一尾帧与下一首帧的镜头几何是否兼容；是否出现无授权跨轴、左右交换、双正脸或攻击/视线/水流方向反转


镜头独立性只表示：

单个镜头的生成指令必须自足、可执行。


镜头独立性不表示：

人物、道具和环境可以在每个镜头重新初始化。


空镜也必须保存环境、光线、天气、持续声音、固定道具和摄影机的边界状态；不得因为没有人物而省略镜头边界检查。


---

# Rule 14

# Sequence Coverage And Unit Contract


项目存在Sequence Plan时：

- SEQ、BEAT、COV与UNIT只由Sequence Planning拥有
- SHOT只由STATE-06 Detailed Shot Design拥有
- 每个Required COV必须至少映射一个正式SHOT
- 每个UNIT必须有稳定Entry、Authorized Change、Exit与Next-unit Handoff
- State Ledger只允许已确认剧情授权的变化
- UNIT重试不得修改已接受的前序UNIT结果


后续Workflow可以读取和验证Sequence Plan。


不得：

- 在STATE-08临时新增COV来掩盖漏拍
- 用UNIT ID替代SHOT或最终分镜编号
- 为达到Coverage完整而新增剧情事实
- 把Sequence内部时长自动带入最终Prompt
- 在Clip Production或Video Generation中无原因重新划分UNIT


发现Required COV遗漏时：

设计层遗漏返回Sequence Planning。


COV存在但未映射SHOT时返回Shot Design。


SHOT正确但生成未执行时返回Video Generation或Editing。



---

# Final Principle


一致性不是Prompt修饰。


而是：

资产管理。

视觉规范。

镜头控制。


共同保证的结果。
