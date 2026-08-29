# Camera Angle Index

## Purpose

本目录用于根据剧情功能、人物权力、心理状态和空间尺度选择摄影机观察高度与视轴方向。Camera Angle 只定义机位与观察方向；若镜头还需要移动，必须从 Camera Movement 中选择一个主要运镜，并保持角度逻辑连续。

选择顺序：

`叙事对象 → 人物权力/心理 → 空间尺度 → 摄影机高度 → 视轴方向 → 人物与轴线连续性 → Seedance 可执行性`

## Core Execution Rules

每个角度镜头必须明确：

- 摄影机相对主体的高度
- 摄影机在主体前、后、左、右或正上/正下方
- 视轴为平视、斜向上、斜向下、垂直向上或垂直向下
- 人物左右位置、面对方向、视线和屏幕运动方向
- 固定建筑、道路、地面或天空参照
- 镜头结束时可供下一镜头继承的空间状态

默认限制：

1. 单镜头只设置一个主要角度逻辑。
2. 不在同一镜头内从低角度切换到高角度或从斜视变为顶视。
3. 多人场景保持 180 度轴线、左右位置和相互视线。
4. 角度不自动等于情绪；必须结合剧情和人物关系判断。
5. 默认固定机位或简单人物动作，复杂运动另由 Camera Movement 定义。

## Current Library

- [Low Angle](low_angle.md)：人物尺度内的斜向仰拍，表现力量、威胁或体量。
- [High Angle](high_angle.md)：人物尺度内的斜向俯拍，表现弱势、孤立或空间关系。
- [Ground Level](ground_level.md)：摄影机接近地面，强调脚步、地面接触和进入方向。
- [Top Down](top_down.md)：近 90 度垂直向下，展示局部空间的平面几何。
- [Bird's Eye View](bird_eye_view.md)：稳定高空广域俯视，用于地点、规模和群体建立。
- [Vertical Upward](vertical_upward.md)：空间底部近 90 度垂直向上，展示天空或顶部结构。
- [Dutch Angle](dutch_angle.md)：保持单一静态倾角，表达有叙事依据的失衡或不安。

## Source Terminology Mapping

本批文件吸收《镜头.docx》中的术语：

- 低角度镜头：仰拍人物或高大建筑，增强压迫或力量。
- 高角度镜头：俯视人物心理状态。
- 地面低机位、地面视角镜头：从草丛、道路或地面观察脚步经过。
- 天花板镜头：从屋顶或顶部拍摄下方。
- 鸟瞰镜头：从高空俯拍城市街区、车流和建筑。
- 天井镜头：从建筑中央垂直向上拍摄天空。

资料仅提供术语和视觉意图；实际知识文件补充了机位侧、视轴、人物方向、轴线与模型限制。

## Angle Distinction

### Low Angle vs Ground Level

- Low Angle：低于主体视线的斜向仰拍，通常仍看完整人物或建筑立面。
- Ground Level：接近地面，重点是脚步、地面材质与经过动作。

### High Angle vs Top Down

- High Angle：有侧位的斜向俯视，可看见人物面部或身体体积。
- Top Down：接近正上方垂直向下，强调地面坐标和平面几何。

### Top Down vs Bird's Eye View

- Top Down：房间、桌面、床面或小型行动区域。
- Bird's Eye View：城市、广场、港口或自然环境的大尺度建立。

### Low Angle vs Vertical Upward

- Low Angle：斜向上观察人物或建筑立面。
- Vertical Upward：从空间底部近 90 度朝上观察天空、井口或顶部结构。

## Shot Design Selection Rule

- 强化人物、建筑或威胁的力量：Low Angle。
- 表现人物弱势、孤立或受困：High Angle。
- 强调脚步、地面接触和进入方向：Ground Level。
- 展示房间或局部空间的几何关系：Top Down。
- 建立城市、广场、自然环境或群体规模：Bird's Eye View。
- 展示天井、井口、穹顶或天空中心：Vertical Upward。
- 已建立空间中的心理失衡或秩序破坏：Dutch Angle；不得把它当作持续滚转运镜。

## Camera Movement Coordination

角度与运镜组合时：

1. 先锁定 Camera Angle。
2. 再选择一个主要 Camera Movement。
3. 运动过程中保持人物方向、轴线和角度意图。
4. 若运镜导致观察角度发生根本变化，应拆成另一镜头。

高稳定组合：

- Low Angle + Static Hold
- High Angle + Slow Pull Out
- Ground Level + Static Pass
- Top Down + Static Blocking
- Bird's Eye View + Static Establishing
- Vertical Upward + Natural Motion

## Seedance Stability Priority

优先：

`固定机位高度 + 单一视轴 + 简单人物动作 + 明确空间参照 + 清楚结束状态`

常见风险：

- 只写“仰拍/俯拍”，不说明相对主体的位置
- 画面从斜向角度自动变为垂直角度
- 顶视或仰顶画面无原因旋转
- 高空视角自动变成无人机飞行
- 角度变化造成角色左右位置和屏幕方向反转

## Advanced Camera Angle Boundary

以下内容由 Advanced Camera Movement 层管理：

- 旋转俯拍
- 无人机飞行、俯冲和高空拉远
- 摄影机从地面连续升至鸟瞰
- 倒置镜头与持续翻转
- 故意越过 180 度轴线
- 复杂主观眩晕角度

[Advanced Camera Movement Library](../advanced_camera_movement/index.md)

## Final Principle

Camera Angle 负责决定观众从什么高度和方向理解人物与空间。先保证机位、视轴、人物方向和空间参照清楚，再讨论力量、孤独、压迫或宏大等情绪含义。
