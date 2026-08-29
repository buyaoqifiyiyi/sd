# Movement Combination Foundations

## Core Corrections

“运镜组合”不是单一技术类别。候选资料中常把下列层级写在同一行：

- 摄影机物理运动：Push、Pull、Pan、Tilt、Truck、Track、Crane、Orbit。
- 稳定方式/质感：Fixed、Dolly、Gimbal、Handheld、肩扛呼吸。
- 景别/机位/视点：远景、特写、低机位、高机位、OTS、POV。
- 光学行为：Optical Zoom、Rack Focus、Dolly Zoom。
- 剪辑结构：正反打、蒙太奇、快切、反应切、时间跳跃。
- 转场/后期：遮挡切、叠化、闪白、场景变形、时间流逝。
- FX/动作：爆炸、法术、烟雾、粒子、慢动作。

这些元素可以协作，但不能全部被称作摄影机运动，也不能自动塞入同一个SHOT。

## Four Execution Classes

### Class A｜Single-Move Shot

一个正式SHOT、一个主要路径。例如固定机位Pan、直线Push、侧向Tracking。优先级最高、稳定性最好。

### Class B｜Low-Complexity Compound Path

一个正式SHOT内最多两个连续阶段，第二阶段必须由同一主体或同一空间事件触发，并保持同一轴线、方向、摄影平台和焦段倾向。例如“后方跟拍跑者，随后轻微横移露出追兵”。

第二阶段不是新的叙事节拍，也不得反向、换侧、换人物或产生新时空。

### Class C｜Coverage Sequence

多个正式SHOT共同完成建立、动作、反应、关系、细节或结果。例如“双人中景→过肩→面部反应→双人收束”。每个箭头默认代表剪辑边界，不得写成一个连续镜头。

### Class D｜Transition / FX Sequence

涉及地点、时间、主观层次、场景变形、爆炸接新场景、抬头看时间流转等内容。摄影机只负责各镜头内部执行；跨镜方法交给`knowledge/transitions/`，FX事实交给已确认资产或Inline Effect。

## One-Shot Compatibility Test

只有以下条件全部成立，才允许Class B：

1. 同一连续时空与同一主要观察对象；
2. 一个Shot Purpose，没有新的Required Coverage节拍；
3. 同一摄影平台能够完成；
4. 运动方向不反转，摄影机不换侧、不越轴；
5. 焦段倾向与摄影距离不发生突变；
6. 人物动作容量仍可执行；
7. 第二阶段只有一次明确触发；
8. 能落在稳定、可验证的结束构图。

任一条件不成立，拆为Class C或D。

## Compatibility Matrix

| 组合 | 默认判定 | 条件 / 降级 |
|---|---|---|
| Track → 轻微侧移Reveal | 可作为Class B | 同向、同侧、同一主体；否则切镜 |
| Push → Static Hold | 可作为Class B | Hold只是落点，不算第二主要运动 |
| Pan → 短Push | 高风险Class B | 仅同一触发和同一目标；优先Pan后切近景 |
| Tilt → Crane | 容易混淆 | 先判断视轴转动或机位升降，通常二选一 |
| Orbit → Push/Pull | 高风险 | 优先短弧线单一路径；否则拆镜 |
| Handheld + Tracking | 可组合 | Tracking是路径，Handheld只是低幅稳定质感 |
| Whip Pan → 精准特写 | 拆镜优先 | 甩镜结束处切入稳定特写 |
| Push/Pull + Optical Zoom | 禁止默认叠加 | 仅明确Dolly Zoom时使用，且提供固定/单Push降级 |
| 超长焦 + 快速手持跟拍 | 不兼容优先 | 降低焦段、减速或改稳定平台 |
| 快速动作 + 复杂Orbit + FX | 超载 | 动作、相机、FX三者至少简化两项 |

## Split Triggers

出现以下任一情况必须拆镜：

- 改变叙事观察对象或出现新的刺激—反应节拍；
- 从远景切特写、低角度切高角度、OTS切反打等景别/机位切换；
- 摄影机运动反向、换肩、换侧、越轴或改用不同平台；
- 地点、时间、现实/回忆/梦境层次发生变化；
- 需要独立道具细节、表情特写、碰撞特写或结果确认；
- 需要新的焦段、对焦逻辑、灯光方案或FX阶段；
- 不能写出唯一可执行终点。

## Stability Budget

每个SHOT内部同时占用以下预算：人物动作、摄影机运动、表演细节、FX、群体/反射/遮挡、光学变化。摄影机已使用Class B时，应减少次要表演、FX或群体变化；动作戏和复杂表演镜头优先Class A。

## Final Principle

一个镜头能做的事不等于它应该做的事。Coverage完整性通过镜头之间分工完成，单镜头稳定性通过运动约束完成。
