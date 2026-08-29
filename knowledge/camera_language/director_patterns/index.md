# Director Shot Patterns Index

## Purpose

本目录收纳“导演意图层”的复合镜头模式。它把叙事触发、情绪目标与现有 Camera Language 原子能力组合起来，但不重复定义景别、角度、运镜、光学、构图、视点或剪辑规则。

## Authority Boundary

1. 原子术语以 `knowledge/camera_language/` 对应分类文件为唯一权威。
2. 本目录只定义选择条件、组合顺序、风险和降级方案。
3. 图片中的“适配情节”是创意启发，不是固定语义；同一镜头在不同表演、速度、焦段、光线、声音和剪辑中可以产生不同含义。
4. 单镜头默认只有一个主要运镜。表中出现联合机制时，必须把它视为一个已定义复合动作，并删除其他主要运动。
5. 进入 STATE-08 时仍以 `templates/10_video_prompt.md` 为唯一最终 Schema，本目录不新增输出字段。

## Library

- [Emotional Patterns](emotional_patterns.md)：20 组情绪与叙事触发模式，经过去重与术语纠正。
- [Dynamic Patterns](dynamic_patterns.md)：动作、揭示、追踪和空间穿行模式。
- [Advanced Composition](advanced_composition.md)：透视、平衡、焦点、色彩与多层空间的高级构图。
- [Action Composition](action_composition.md)：动作路线、威胁方向、FX交互与高风险动作构图。
- [Character Narrative Composition](character_composition.md)：人物站位、视线、距离与环境关系构图。
- [Emotional Atmosphere Composition](atmosphere_composition.md)：反射、阴影、色块、玻璃与氛围构图。
- [Image Source Coverage](../image_source_coverage.md)：五张来源图的逐项规范映射与去重记录。
- [Composition Image Source Coverage](../composition_image_source_coverage.md)：五张构图来源图的逐项规范映射与去重记录。

## Selection Order

`剧情信息 → Coverage 功能 → 人物动作/表演 → 空间与轴线 → 选择一个原子镜头 → 必要时套用一个导演模式 → 设定降级方案`

## Stability Gate

仅当下列条件全部满足时使用复合模式：

- 人物、环境和关键道具已绑定。
- 起始状态、结束状态、屏幕方向和关系轴线清楚。
- 模式解决一个明确叙事问题，而不是只增加“电影感”。
- 可以用一句话描述唯一主要路径或唯一剪辑关系。
- 已指定失败时回退到哪个基础镜头。

## Final Principle

导演模式负责让镜头选择更有意图；原子模块负责让执行保持准确和稳定。
