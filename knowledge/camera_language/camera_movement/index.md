# Camera Movement Index

## Purpose

本目录用于把剧情功能、人物情绪和空间关系转换为可执行的摄影机运动。它服务于 STATE-06 Detailed Shot Design，并在后续 STATE-08 中作为 Camera 信息输入；它不定义最终 Seedance 输出字段，最终 Schema 仍由对应 Template 负责。

选择运镜时优先级为：

`剧情功能 → 人物动作 → 空间关系 → 情绪强度 → 模型可执行性 → 技术参数`

## Core Execution Rules

每个镜头必须先锁定：

- 人物起始位置与结束位置
- 人物面对方向、视线方向和屏幕运动方向
- 摄影机在人物前、后、左、右或肩背哪一侧
- 人物之间的左右位置、距离和关系轴线
- 摄影机运动的起点、路径、速度与终点
- 镜头结束时可供下一镜头继承的状态

基础层默认遵守：

1. 单镜头只设置一个主要运镜。
2. 可以加入轻微焦点转移、构图修正或手持呼吸，但不能形成第二个主要运动。
3. 不在镜头中途越过 180 度轴线；需要换侧时另起镜头设计。
4. 不无原因改变人物左右位置、面对方向或屏幕运动方向。
5. 不使用“电影感运镜”“动态镜头”等无法验证的模糊词替代路径描述。
6. 先保证动作、空间和身份稳定，再增加速度、前景或情绪细节。

当一个候选描述包含两种以上运镜、多个景别/机位或“镜头顺序”时，不在本基础目录直接拼接，必须进入[Camera Movement Combination](../movement_combinations/index.md)先判断是一镜内路径、Coverage还是跨镜Sequence。

## Current Library

### Required Selection Entry

- [Camera Movement Selection Matrix](selection_matrix.md)：所有正式SHOT先根据镜头目的、情绪、人物运动、空间任务与节奏阶段选择主运镜、辅助支持、禁止运镜和Seedance稳定等级，再读取被选原子文件。禁止未检索就默认填入“缓慢推进/轻微横移”。

### Existing Basic Files

- [Push In](01_push_in.md)：逐渐靠近主体，强化信息或情绪。
- [Pull Out](02_pull_out.md)：逐渐远离主体，扩大环境关系。
- [Tracking](03_tracking.md)：通用跟随人物运动。
- [Orbit](04_orbit.md)：现有环绕镜头条目，保持原文件不变；360 度和复杂环绕不作为基础层默认选择。

### High-Utility Executable Files

- [Side Tracking](side_tracking.md)：人物侧面平行跟拍，保持方向、距离和关系连续。
- [Pan](pan.md)：固定机位水平转动视轴，用于注意力转移和空间揭示。
- [Tilt](tilt.md)：固定机位垂直转动视轴，用于上下信息转移；不同于实际升降。
- [Crane](crane.md)：沿单一垂直方向升高或降低摄影机，改变空间尺度。
- [Handheld](handheld.md)：克制手持呼吸，用于纪实、在场和心理不稳定感。
- [Shoulder Follow](shoulder_follow.md)：固定左肩后或右肩后跟随人物进入空间。
- [Dolly Tracking](dolly_tracking.md)：沿预定轨道平滑位移，强调路径、速度和真实视差。

## Source Terminology Mapping

本批文件吸收《镜头.docx》中的基础术语：

- 侧跟镜头：人物沿街跑动，镜头侧面平行跟拍。
- 摇镜头：从左向右展示城市天际线；执行时定义为固定机位的水平视轴转动。
- 升降镜头：镜头上下移动，展现楼层结构。
- 缓慢升降镜头：镜头从低处缓缓升起呈现全景。
- 手持镜头：人为晃动模拟纪实感；执行时默认限制为克制手持。
- 肩膀视角镜头：镜头从人物肩膀后紧随其步伐。
- 肩背镜头：摄影机贴近人物肩膀移动，制造沉浸感。
- 轨道镜头：镜头沿轨道平稳推进，跟随人物。

资料中的描述作为术语来源；实际文件会进一步补充方向、侧位、速度、轴线和结束状态，以满足 Seedance 可执行性。

## Movement Distinction

### Pan vs Side Tracking

- Pan：摄影机位置基本不动，只水平转动视轴。
- Side Tracking：摄影机本体沿人物侧面平行移动。

### Tracking vs Dolly Tracking

- Tracking：通用“跟随人物”类别，路径和稳定方式较宽泛。
- Dolly Tracking：预先确定的平滑路径，强调直线、速度、距离和真实视差。

### Side Tracking vs Shoulder Follow

- Side Tracking：从人物侧面观察，适合并行关系和环境横向变化。
- Shoulder Follow：从固定肩后跟随，适合进入、寻找和沉浸式探索。

### Crane vs Tilt

- Crane：摄影机实际高度上升或下降。
- Tilt：摄影机位置不变，只上下转动视轴；执行规则见 [Tilt](tilt.md)。

### Handheld vs Tracking Path

- Handheld：摄影稳定性和运动质感。
- Tracking Path：摄影机在空间中的实际路径。
- 二者组合时，必须先确定唯一简单路径，再把手持限制为轻微呼吸，不允许随机漂移。

## Shot Design Selection Rule

先实际读取[Camera Movement Selection Matrix](selection_matrix.md)，形成Camera Language Decision；再读取下方被选主运镜对应的原子文件。只读本索引不算完成运镜检索。

### 人物持续向前，关系需要在侧面被观察

优先：Side Tracking。

### 固定观察点，从一个对象转向另一个对象

优先：Pan。

### 从人物局部展开至更大空间，或从高处落到人物

优先：Crane。

### 需要纪实在场感或轻微心理失衡

优先：Handheld；先锁定空间与主体，再设置低幅度呼吸。

### 观众需要跟在人物肩后进入或寻找

优先：Shoulder Follow。

### 需要平稳、几何清楚、起止点可控的真实位移

优先：Dolly Tracking。

### 只需稳定靠近或远离静态主体

优先：Push In 或 Pull Out。

### 只需一般性跟随，尚未确定具体侧位和设备路径

先使用 Tracking 作为上位类别；进入执行阶段前必须进一步具体化。

## Execution Description Pattern

每次调用运镜知识时，按以下顺序形成执行描述：

1. Start State：人物位置、方向、摄影机侧位、距离、景别。
2. Movement Process：摄影机路径、速度、人物配合、背景视差或空间揭示。
3. End State：摄影机终点、人物动作结果、结束构图和下一镜头连续状态。
4. Stability Limits：单一主要运镜、不越轴、不换侧、不反向、不叠加复杂运动。

推荐句法：

`摄影机从哪里开始 → 位于人物哪一侧 → 沿什么单一路径 → 以什么速度 → 与人物如何同步 → 在哪里停下 → 保持哪些方向和轴线限制`

## Seedance Stability Priority

优先组合：

`明确方向 + 单一主要运镜 + 简单人物动作 + 固定空间关系 + 清楚结束状态`

降低稳定性的组合：

- 同一镜头多次改变运动方向
- 同时推拉、横移、升降、环绕和变焦
- 人物快速转身、交叉换位和复杂动作同时发生
- 摄影机侧位、距离或目标未定义
- 仅写情绪与形容词，不写实际运动过程

## Advanced Camera Movement Boundary

以下术语已由独立高级层管理，不作为基础层默认建议：

- 穿墙、墙后穿越、墙体移动穿越
- 360 度环绕与复杂人物绕行
- 无人机俯拍、高空飞升和大范围航拍路径
- 旋转俯拍
- 一镜多场景穿越与连续转场
- 故意越过 180 度轴线
- 水下潜入、复杂垂直穿越等高难度路径

[Advanced Camera Movement Library](../advanced_camera_movement/index.md)

Advanced 层定义启用条件、失败风险、空间重建限制和连续性校验，不能直接套用基础运镜规则。

## Final Principle

运镜不是为了增加“电影感”，而是为了让剧情、人物关系和空间变化更清楚。基础 Camera Movement 优先稳定、单一、连续、可验证；复杂性必须延后到叙事确有需要且模型能够执行的层级。
