# Camera Language Module / Knowledge Base

## Purpose

本文件是Director Module下`Camera Language Module`的唯一owner。Camera Language用于把Director Intent转换为具体、可执行、可验证的电影镜头行为；它不是“电影感”装饰词库。

核心原则：`Camera Language is the execution language of Director Intent.` 镜头选择必须改变或控制观众知道什么、感受到什么、期待什么或理解什么。

它连接：

Script Camera-language Opportunity

↓

Scene Camera Strategy

↓

Shot Design

↓

Clip Camera Continuity / Visual Rhythm

↓

Video Prompt

↓

Editing / Review


---

## Usage Rule

当进入Shot Design阶段：

先读取统一选择路由：

[Shot Language Router](shot_language_router.md)

根据以下因素选择镜头语言：

- 剧情情绪
- 人物状态
- 空间关系
- 动作需求
- 导演视觉风格


---

## Module Contract

- **Module Type**：Director Module核心外化能力；STATE-01、04至09与Editing按阶段调用的Camera Knowledge，不是新STATE
- **Decision Owner**：`knowledge/director_decision_layer.md`决定为什么这样拍；本模块决定如何用镜头语言执行
- **Execution Owners**：STATE-06负责具体Shot Camera Language Decision，STATE-07负责Clip Camera Continuity / Visual Rhythm，STATE-08 Prompt Compiler负责模型翻译，Editing与STATE-09负责成片判断
- **Existing System Reuse**：180°轴线、人物拓扑、Pose与Delta全部调用Spatial Blocking / Relationship Topology / Relational Screen Geometry；不在本模块重建
- **Protected Boundaries**：不改剧情、资产、Scene / Shot / Clip顺序、Visual Direction或最终Prompt Schema
- **Four Core Capabilities**：Composition Direction、Camera Movement Direction、Lens / Distance Direction、Shot Rhythm Direction

## Cross-stage Mapping

- **Script**：只识别可镜头化机会、观众信息顺序、反应空间、遮挡/揭示和空间潜力；不写死景别、焦段、机位或运镜
- **Scene**：形成观察 / 跟随 / 隐藏 / 揭示 / 压住 / 释放等`Scene Camera Strategy`，不提前创建SHOT
- **Shot**：按`shot_language_router.md`把Shot Purpose具体化为构图、景别、POV、机位、焦段、运镜、Hold与Cut动机
- **Clip**：检查相邻镜头的Camera Continuity / Visual Rhythm、视觉高潮、最克制镜头、动作/信息积累和稳定降级
- **Prompt**：把已确认结果翻译成动作顺序、第一/第二注意目标、前中后景、遮挡/Reveal、焦点、摄影机Trigger与Stop，不输出理论标签
- **Editing / Review**：检查Editorial POV、反应优先级、Hold / Cut、信息时机、镜头必要性和视觉节奏是否保持导演意图

## Camera Movement Trigger

摄影机运动必须由可定位的戏剧Beat触发，例如人物进入/退出、动作启动/停止、视线捕捉、信息确认、关系距离改变、声音先行或节奏释放。每个运动写清`Trigger → Path（含Mid-path Change）→ Stop → End Composition`，并按`Emotion Translation Contract`给出运镜理由。

- 人物压抑或信息尚需保留时，Static / Locked-Off可以是主动导演选择；镜头不应比人物更激动。
- 推进、跟随或横移可以在关键表演/信息Beat完成后才启动，不能从第一帧无条件漂移。
- 演员与摄影机的运动既可以同步，也可以故意形成对照，但两者关系必须可解释、可执行，并服从空间轴线。
- 只写“镜头缓慢推进”“轻微横移”没有Trigger、Stop和功能时固定不合格。

### Movement Phase

同一个Trigger可以产生四种**运镜时相**，必须显式选择一种，因为它决定观众是“先知道”、“同时知道”还是“晚知道”：

- **抢先**：在人物反应之前给出信息（先看见门开、先看见对方的犹豫）；观众先于人物知道。
- **同步**：与人物的决定或动作同时发生；观众与人物同时知道。
- **滞后**：人物已经反应、已经决定或已经离开之后，镜头才跟上、才让出空间或才落定；观众晚于人物知道。
- **拒绝跟随**：人物离开画面或转向时镜头保持不动，用画外空间与声音承担变化；观众被迫停留在已经失去主体的画面里。

时相不增加运动数量：一镜仍然只有一个主要路径。无法说明本镜让观众先于、同时于还是晚于人物获得信息时，视为运动动机不足。

## Motion Energy Allocation｜运动能量分配

画面运动由五种载体共同承担，任何一个SHOT的运动都不应默认全部压在摄影机上：

| 载体 | 内容 |
|---|---|
| Camera Motion | 摄影机位移或视轴变化（推拉摇移跟升降环绕） |
| Performance Motion | 人物走位、手势、转头与身体重心变化 |
| Prop / Environment Motion | 鱼、抄网、水、门、车辆、烟雾、雨雪等 |
| Focus / Optical Motion | 拉焦、变焦、景深变化 |
| Editorial Motion | 切镜、景别跳转、正反打与节奏变化 |

每个SHOT在决定摄影机行为前先判断一次：**谁是本镜的主要运动载体？**

**决策规则**：当人物、道具或环境已经承担了充分的运动与注意力变化时，摄影机优先`Static / Hold`；**不得为了让“画面有运动”而重复增加轻推、横移或环绕**。画面可以很活，而摄影机仍然克制——这是允许且常见的高质量组合。

**检查**：一个SHOT若五种载体同时高强度运动，判定为运动过载，按`## Seedance Stability Priority`降级一条或改为静止。静与动是分配关系，不是风格标签。

## Functional Coverage

Camera Language必须按适用性覆盖：景别功能、构图功能、机位功能、POV / Audience Position、焦段与画面距离感、前中后景调度、遮挡 / Reveal、人物关系构图、脸部信息取舍（Face Economy）、运镜触发点与Movement Phase、Hold / Pause / Cut节奏，以及180°轴线与空间关系。

特写、浅景深、手持与慢推都不是情绪的自动同义词。特写必须由关键反应、信息确认或距离坍缩等时机“赚到”；情绪可能主要通过身体姿态或共享空间表达，此时中景/全景比自动特写更有效。重大事件后优先判断是否需要反应空间，反应可以在同一镜头中完成，也可以通过切换实现。

### Face Economy

脸是默认信息，不是默认画面。每个SHOT必须主动决定本镜**给不给脸**：给正脸、延迟给脸、只给侧背 / 手部 / 局部 / 反射 / 遮挡，或整镜不给脸（原子见`director_patterns/emotional_patterns.md`的EMO-13 / EMO-15 / EMO-16与`composition_language/occlusion_frames.md`）。

选择必须绑定信息后果：不给脸时观众因此少知道什么、多感到什么，以及这条信息是否在同一Clip的后续SHOT、尾帧或声音中偿还。上面的“赚到”规则照常生效：脸部特写不因情绪强度自动升级。整镜不给脸而写不出信息后果时，视为回避表演而不是导演选择。

## Emotion Translation Contract

情绪不是镜头的固定属性，也不能只以情绪名称进入决策：`悲伤 / 压抑 / 震撼 / 氛围感`一类描述既不是镜头理由，也不能替代画面关系。每个SHOT在选景别、焦段、机位或运镜之前，必须先写出一行可复核的**情绪变化**：

`起始状态 → 变化触发与过程 → 结束落点 / 观众残留感受`

- **起始状态**：人物与观众此刻处在什么心理位置，以及哪条已确认事实支撑它。
- **变化触发与过程**：由哪个可见刺激、表演Beat或信息披露推动，情绪朝哪一侧变化，过程中是否被压住、伪装或延迟。
- **结束落点 / 观众残留感受**：镜头停止时人物稳定在什么状态，观众应留下什么感受、判断或疑问。

三段的事实输入由`knowledge/director_decision_layer.md`的`Audience Experience / Emotional Delta`拥有；本模块只负责把它翻译成画面关系。缺任一段、或只有情绪名称时，本SHOT的Camera Language Decision不成立。

### 画面关系翻译

情绪变化必须落到画面关系上。下表是本模块的翻译清单与路由索引，**不是九项同时调整的配额**：每项的定义、触发条件与降级仍在对应原子文件，不得据此把情绪标签当作固定公式。

| 变量 | 情绪功能指向 | 执行 owner |
|---|---|---|
| 距离（景别 / 摄影机距离） | 近＝亲密、压迫、窥视、细节、主观体验；远＝孤独、渺小、环境力量、旁观、疏离 | `lens_language/framing_and_scale.md` |
| 构图 | 居中＝稳定、正面、力量、被审视；偏移、切边、负空间、失衡＝不安、缺失、压迫、未知 | `composition_language/foundations.md` |
| 空间 | 封闭、狭窄、低矮、遮挡多＝束缚；开阔、纵深、留白、尺度差＝自由、孤独、宏大、无力 | `composition_language/foundations.md`、Spatial Blocking |
| 机位 / 视角 | 低机位＝力量、威胁、崇高；高机位＝脆弱、失控、被俯视；平视＝中性、亲近、写实 | `camera_angle/index.md` |
| 稳定性 | 稳定、平滑、方向明确＝秩序、决心、掌控；漂移、晃动、不规则＝主观、危险、混乱、不确定 | `camera_movement/selection_matrix.md` |
| 速度与节奏 | 慢＝观察、沉浸、压抑、悲伤、悬念；快＝冲击、行动、失控、信息爆发；静止＝凝视、僵持、压迫、情绪余波 | `camera_movement/index.md` |
| 视野与信息 | 限制视野、延迟揭示＝悬念；逐步扩展＝发现、震撼；突然展示＝惊吓、反转、冲击 | 由已确认Information Presentation / Reveal Strategy决定；本模块不重新定义揭示策略 |
| 前景 / 遮挡 / 焦点 | 前景遮挡＝偷窥、隔阂、未知；焦点转移＝认知交接；清晰与模糊切换＝注意、记忆、醉意、心理失衡 | `composition_language/occlusion_frames.md`、`lens_language/focus_and_optics.md` |
| 人物关系 | 靠近、分离、同向、对向、谁占据画面、谁被挤到边缘＝权力、亲密、冲突与距离变化 | 既有Relationship Topology与Relational Screen Geometry；不在本模块重建 |

**排他纪律**：每个SHOT只指定**一个主要承担变量**，其余变量保持稳定或明确让位，并说明为什么由它承担这次情绪变化。多个变量同时追求变化会同时削弱情绪落点与生成稳定性；确有多项必须共同改变时，说明它们服务同一个情绪变化，并按Complexity Priority复核降级。

### Causal Move And Empty-Word Rewrite

主运镜必须能写出`Trigger → Path（含Mid-path Change）→ Stop → End Composition`，并附**运镜理由**：这个变化让观众多知道、多感到或多期待了什么。`Mid-path Change`写运动过程中构图、空间、焦点或人物—环境关系发生的具体改变，不重复路径本身；有理由的Static / Locked-Off同样要写出它保护了什么、为何不运动。

出现抽象词时必须改写成可执行的、连续的视觉动作与构图变化，不得用形容词充数：不写“电影感 / 高级感 / 震撼 / 氛围感 / 有张力”，不只写运镜名称而不给Trigger、Path、Stop与落点，不用情绪形容词替代画面关系，也不无理由地快速环绕、频繁推拉、炫技转场或持续运动。相邻镜头的多样性、重复与复杂度纪律仍由`camera_movement/selection_matrix.md`拥有，本模块不重复定义。

## Camera Motif And Recurrence

项目级`视觉母题与变化轨迹`由STATE-04的Aesthetic Decision Lock唯一拥有（`templates/01_project_bible_template.md`要求至少三次可出现、变化或反转）。本模块**不新建第二套母题**，只规定它如何落到镜头语言上：机位、摄影机距离、观察侧位、景别与运动族本身也可以是母题载体，而不只是构图与光色。

- 命中母题节点（出现 / 变化 / 反转）时必须写明本次改变的是哪一个变量、哪些变量保持不变；未命中的镜头不得无理由重复该母题。
- 变奏优先用距离、侧位、遮挡、焦点与Movement Phase完成，不自动升级为更复杂的运动；确需升级复杂度时占用`selection_matrix.md`的Movement Novelty Budget。
- 未到确认节点时写`Not Applicable`，不得为了“呼应”提前复用同一构图或同一运镜。
- 回响必须可指认：观众能在成片里认出这是同一个视觉动作的第二次或第三次，而不是只存在于主创自述里。

---

## Relational Screen Geometry Contract

### Activation

战斗、双主体、对峙、对话、追逐、相向行走、拥抱、交接物品，或任何需要观众持续辨认“谁面对谁、谁从哪里作用于谁”的镜头强制启用。

### Geometry Before Prose

在写动作、情绪或“电影感”描述前，先建立一行可画出的Blocking：

`A＝画面左侧/前中后景/朝右/视线→B；B＝画面右侧/前中后景/朝左/视线→A；关系轴＝A—B或主攻击线；Camera＝轴线同一侧；Connector＝来源→路径→目标。`

把这行语义映射到当前阶段已有的Camera Position、Composition、Start Boundary、空间关系、镜头结尾状态与Handoff字段；它是内部设计方法，不创建STATE-08新字段。

### Mandatory Geometry Locks

1. **Screen Position**：明确A、B的画面左/右，以及必要的高低和前/中/后景层级。
2. **Facing And Eyeline**：分别写明朝左/朝右、正侧/三分之二侧/背侧和视线目标；不得用“面对彼此”替代两个独立方向。
3. **Axis And Camera Side**：以A—B关系、主运动或主攻击确定唯一主轴，并说明摄影机在轴线哪一侧。
4. **Spatial Connector**：用眼线、武器指向、攻击轨迹、追逐路线、水流、能量或抛射物连接来源与目标；方向必须与人物身体、喷口/武器、受击面和屏幕运动一致。
5. **Distance And Change**：说明双方距离，以及谁靠近/远离、从何处到何处；无动作不得交换位置。

### Default Camera Choice

- 连续关系镜头优先单一轴线、固定侧面双人、侧后双人或Over-the-Shoulder。
- 复杂动作优先让摄影机稳定、人物运动可读；需要反应切换时拆为保持同一轴线侧的Reverse Shot。
- 双方同时出镜并相互面对时，最多一方接近完整正脸；另一方必须保留三分之二侧面、侧面、背侧或过肩锚点。双方同时完整正脸通常意味着关系几何已丢失。
- 只有在空间关系已经建立且有明确叙事理由时，才按[Axis Crossing](advanced_camera_movement/axis_crossing.md)执行有意越轴；失败时回退到原轴线侧。

### First-Frame Geometry Lock

以下任一情况出现时，优先使用合法首帧或上一Clip尾帧锁定几何：连续动作、悬空主体、攻击/水流/能量交互、双主体快速运动、模型曾发生左右翻转，或下一段必须直接承接上一段。

从帧中逐项读取并冻结：双方身份、画面左右、高低、前后、身体朝向、视线、距离、摄影机轴线侧，以及来源—目标空间连线。后续文字只能描述从该状态开始的运动，不得把角色重新摆位。若参考帧不支持目标镜位，只能选择Reference-Only并建立兼容新边界，或返回Shot Design；不得一边声称直接继承一边改变几何。

### Tail-Frame Geometry Check

结尾帧必须保留可复核的A/B左右、朝向、视线、距离、轴线侧和Connector终点。Continuous Handoff时，下一首帧逐项继承；需要有动机的景别/机位变化时只作第一顺位连续性参考；有已确认断点时明确不继承。若尾帧出现随机换位、双正脸、无授权跨轴或Connector反向，该镜头不得通过Review。

### Quick Test

如果无法在纸上画出`A → 目标`、`B → 目标`、A—B轴线、摄影机所在半平面和一条来源—目标连线，说明指令仍是文学描述，尚未成为可执行镜头几何。


---

## Camera Language Categories


## Camera Movement

用于表现：

- 空间变化
- 人物运动
- 情绪推进


包含：

- 推进镜头
- 拉远镜头
- 跟拍镜头
- 轨道镜头
- 升降镜头
- 旋转镜头


执行型知识库：

- [基础 Camera Movement](camera_movement/index.md)
- [Camera Movement Selection Matrix](camera_movement/selection_matrix.md)：STATE-06先完成逐SHOT Camera Language Decision，STATE-07再组织Clip Movement Plan，STATE-08只把已确认语义投影到既有Prompt字段。
- [Advanced Camera Movement](advanced_camera_movement/index.md)
- [Camera Movement Combination](movement_combinations/index.md)：判断候选描述应为单一运镜、低复杂度复合路径、Coverage Sequence或Transition / FX Sequence，并在稳定性不足时自动拆镜。


---

## Director Shot Patterns

用于把叙事触发与基础镜头原子组合成可降级的导演模式，包括情绪推进、动作揭示、追踪、穿行、突停与收尾。

[Director Shot Patterns](director_patterns/index.md)

调用顺序必须是：先选择原子镜头，再决定是否需要导演模式。导演模式不建立第二套术语定义，也不改变 STATE-08 Schema。


---

## Camera Angle

用于表现：

- 权力关系
- 心理状态
- 空间规模


包含：

- 低角度
- 高角度
- 地面机位
- 垂直俯拍
- 鸟瞰建立
- 垂直仰拍


执行型知识库：

[Camera Angle Library](camera_angle/index.md)


---

## Composition Language

用于表现：

- 人物关系
- 视觉隐喻
- 空间层次


包含：

- 居中对称、三分法与引导线
- 负空间、层次纵深与双人平衡
- 镜中镜
- 玻璃反射
- 遮挡
- 裂缝透视


执行型知识库：

[Composition Language Library](composition_language/index.md)


---

## Emotional Camera

用于表现：

- 回忆
- 梦境
- 心理变化


包含：

- 重影
- 慢动作
- 时间冻结
- 倒置镜头


执行型知识库：

[Temporal Language Library](temporal_language/index.md)


---

## Perspective Language

用于角色主观视点、对话眼线与正反打关系。

[Perspective Language Library](perspective_language/index.md)


---

## Lens And Framing Language

用于焦段、摄影机距离、透视关系、焦点/景深、光学效果、景别与局部细节。焦段不自动提高画面质感，也不等于景别。

[Lens And Framing Library](lens_language/index.md)


---

## Lighting Camera

用于光线范围变化、光影运动与光源驱动的视觉揭示。

[Lighting Camera Library](lighting_camera/index.md)


---

## Editing Language

用于长镜头、快切、景别切换、叠化、黑场和遮挡转场。

[Editing Language Library](editing_language/index.md)


---

## Selection Principle

禁止随机选择镜头。

跨景别、角度、视点、焦段、构图和运镜的联合选择必须先通过shot_language_router.md；具体原子定义再进入对应子目录。

必须：

剧情需求 → 情绪分析 → 镜头选择

图片或术语表中的“适配情节”只能作为候选提示。最终选择必须同时通过人物动作、空间关系、轴线连续、镜头功能和模型可执行性检查。


例如：

孤独人物：

推荐：

- 拉远镜头
- 背影镜头
- 环境大景


紧张追逐：

推荐：

- 手持摄影
- 跟拍
- 快切


心理压迫：

推荐：

- 推进镜头
- 特写
- 低角度


---

## Output

镜头语言最终转换为：

- 景别
- 摄影机位置
- 摄影机运动
- 构图方式
- 情绪效果

并进入Video Prompt生成。


---

