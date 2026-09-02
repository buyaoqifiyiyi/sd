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

摄影机运动必须由可定位的戏剧Beat触发，例如人物进入/退出、动作启动/停止、视线捕捉、信息确认、关系距离改变、声音先行或节奏释放。每个运动写清`Start Condition → Path → Stop Condition → End Composition`。

- 人物压抑或信息尚需保留时，Static / Locked-Off可以是主动导演选择；镜头不应比人物更激动。
- 推进、跟随或横移可以在关键表演/信息Beat完成后才启动，不能从第一帧无条件漂移。
- 演员与摄影机的运动既可以同步，也可以故意形成对照，但两者关系必须可解释、可执行，并服从空间轴线。
- 只写“镜头缓慢推进”“轻微横移”没有Trigger、Stop和功能时固定不合格。

## Functional Coverage

Camera Language必须按适用性覆盖：景别功能、构图功能、机位功能、POV / Audience Position、焦段与画面距离感、前中后景调度、遮挡 / Reveal、人物关系构图、运镜触发点、Hold / Pause / Cut节奏，以及180°轴线与空间关系。

特写、浅景深、手持与慢推都不是情绪的自动同义词。特写必须由关键反应、信息确认或距离坍缩等时机“赚到”；情绪可能主要通过身体姿态或共享空间表达，此时中景/全景比自动特写更有效。重大事件后优先判断是否需要反应空间，反应可以在同一镜头中完成，也可以通过切换实现。

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

## Source Coverage

《镜头.docx》全部来源术语与规范知识文件的映射：

[Source Coverage](source_coverage.md)

[五张“导演级专业运镜术语”图片覆盖表](image_source_coverage.md)

[五张“导演级专业镜头构图”图片覆盖表](composition_image_source_coverage.md)

[三张“AI短剧焦段篇”图片覆盖表](lens_language/focal_length_image_source_coverage.md)

[六张“AI漫剧常用运镜组合”图片覆盖表](movement_combinations/image_source_coverage.md)
