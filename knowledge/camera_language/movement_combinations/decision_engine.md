# Movement Combination Decision Engine

## Gate 0｜Confirm The Unit

先确认输入描述对应一个正式SHOT、多个SHOT、Sequence Plan还是仅是创意候选。未创建SHOT时不得用组合模式越权创建剧情；只能给STATE-06提供建议。

## Gate 1｜Separate The Layers

把输入拆为：

- Shot Purpose / Coverage Function；
- Shot Scale、Angle、Perspective；
- Physical Camera Path；
- Stability / Rig Character；
- Focus / Optical Behavior；
- Performance / Blocking；
- Editing / Transition；
- FX / Sound。

若“镜头顺序”包含多个景别、视点或观察对象，默认按Coverage Sequence处理。

## Gate 2｜Classify A / B / C / D

- 单一主要路径：Class A。
- 同一目的、同向、同轴、同平台的两阶段连续路径：Class B。
- 多个信息任务或多个景别/机位/视点：Class C。
- 时空/主观层次变化或依赖后期/FX：Class D。

Class D即Transition / FX Sequence；摄影机路径只负责各SHOT内部执行。

不确定时优先Class C；不要为了“流畅”强行伪一镜到底。

## Gate 3｜Coverage Sufficiency

读取`knowledge/sequence/coverage_design.md`，检查Required COV。合并镜头不得导致建立、主要动作、反应、关系、细节或结果的可见证据消失。可由一个SHOT兼容完成多个COV时才合并。

## Gate 4｜Choose One Primary Path

每个SHOT确定：

`Start State → Primary Path → Optional Motivated Continuation → Stable End State`

Class B中的Optional Continuation必须说明触发点；不能只写“随后炫酷环绕/升降/变焦”。

## Gate 5｜Continuity And Geometry

检查：

- 180度轴线、人物左右与屏幕运动方向；
- 摄影机侧位、高度、距离与焦段倾向；
- 背景锚点、视差和遮挡顺序；
- 人物路线和相机路线是否碰撞；
- 起始/结束景别、焦点、构图是否可继承。

Orbit、换肩、反向包抄和大幅侧移必须执行高级轴线检查；无法证明空间时拆镜。

## Gate 6｜Performance And Action Capacity

摄影机运动不能遮蔽必须可见的眼神、嘴部、手部、道具或动作结果。精细微表情、复杂对白、武打碰撞、群体调度和重FX镜头默认降低相机复杂度。

## Gate 7｜Transition Boundary

Class C/D的每个SHOT边界必须转交`knowledge/transitions/decision_engine.md`。默认Direct Cut；只有真实动作、视线、构图、遮挡、光态、FX或剧情内声音锚点才选择匹配切或其他方式。普通运镜不能自动成为转场。

## Gate 8｜Stable Downgrade

按以下顺序降级：

1. 删除无功能的次级运动；
2. 把Class B改为Class A；
3. 把复杂镜头拆为Class C；
4. 把高级路径改为固定机位或单向Push/Pull/Track；
5. 把场景变形改为独立镜头与Direct Cut；
6. 保留Required Coverage，删除Optional炫技镜头。

## Internal Output

内部记录：

- Combination Class；
- Pattern Candidate（如CMG-xx）；
- Coverage Function；
- Primary Path；
- Optional Continuation及触发；
- Split Points；
- Axis / Focal / Performance风险；
- Stable Downgrade；
- 最终字段投影位置。

以上分析不得原样进入STATE-08。
