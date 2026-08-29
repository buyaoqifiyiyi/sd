# Camera Movement Combination Knowledge

## Purpose

本模块把“运镜组合”规范为可执行的镜头路径或Coverage方案。它回答的不是“堆多少镜头术语”，而是：当前设计应当作为一个单镜头、多个镜头的Coverage、跨镜转场，还是需要FX/后期完成的Sequence。

本模块服务STATE-06至STATE-08，不建立新的主STATE，也不拥有最终Seedance字段。

## Authority Boundary

- 基础运动定义：`knowledge/camera_language/camera_movement/`。
- 高级路径与越轴风险：`knowledge/camera_language/advanced_camera_movement/`。
- 景别、焦段、对焦与光学变化：`knowledge/camera_language/lens_language/`。
- OTS、POV、正反打与眼线：`knowledge/camera_language/perspective_language/`。
- Coverage和Required信息：`knowledge/sequence/coverage_design.md`。
- 跨镜边界与转场：`knowledge/transitions/`。
- 本目录只负责分类、组合、拆分、连续性和Prompt投影，不重复定义上述原子。

## Required Files

1. [Foundations](foundations.md)
2. [Decision Engine](decision_engine.md)
3. [Combination Patterns](combination_patterns.md)
4. [Continuity And Projection](continuity_and_projection.md)
5. [Image Source Coverage](image_source_coverage.md)

## Activation Gate

出现以下任一情况时启用：

- 一个镜头描述包含两种或以上摄影机运动；
- 用户给出“镜头顺序”“运镜组合”“一镜到底”或连续摄影路径；
- 同一叙事节拍需要建立、动作、反应、细节和结果等多种Coverage；
- 需要判断某段描述应当一镜完成还是拆成多个分镜；
- 运镜、景别、机位、对焦、FX和转场被混写。

单一固定机位或单一基础运镜无需为了形式完整启用本模块。

## Core Invariant

`先分类 → 再锁定镜头目的 → 再判断一镜/多镜 → 再选择原子 → 再检查连续性 → 最后投影现有字段`

默认每个正式SHOT只有一个主要摄影机路径。只有在两段运动共享主体、方向、轴线、摄影平台和叙事目的，且第二段只是同一路径的有动机延续时，才允许一个低复杂度复合路径。

## Final Principle

运镜组合的专业性来自功能分工、路径兼容和稳定落点，不来自术语数量。无法明确起点、触发、路径、终点和降级时，必须简化或拆镜。
