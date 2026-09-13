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

## Default vs Directed｜反平庸对照

本表不是新术语，也不是新的组合定义。它只回答一个问题：**这个桥段最容易落入的省事解是什么，换成它会失去什么可指认的东西。** 每行必须通过`knowledge/director_decision_layer.md`的Default-Replacement Loss；有依据的替代仍以本目录与原子文件为唯一权威，组合与降级条件不变。只读当前桥段那一行，不整表通读。

**默认落点不是禁令**：当它确实保护了表演、信息或等待时（例如EMO-08），保留它，但必须写出保护了什么并通过检查。

| 桥段 | 默认落点（平庸解） | 可指认的损失 | 有依据的替代（原子 / EMO） | 禁止与降级 |
|---|---|---|---|---|
| 等待 / 空等 | 中景固定机位或缓慢推进看脸 | “没有人来”只能靠台词说明，观众无法自己读出时间 | 把关系轴交给门、反射、桌面边缘；用前景遮挡与负空间让“空缺”占据画面（`composition_language/occlusion_frames.md`、`reflection_frames.md`；EMO-08、EMO-18） | 禁止无触发慢推；降级为固定中景 + 空位构图 |
| 重逢 | 双人正面中景 + 慢推 | 关系轴与“谁先动”的因果被抹平 | 先给单向视线与半身，靠近由距离变量承担，一方延迟入画（EMO-14、EMO-02；`perspective_language/over_shoulder.md`） | 禁止双方同时完整正脸；降级为固定OTS |
| 告别 / 离场 | 跟拍背影 + 拉远 | “离开”变成一次运动，而不是空间吞没人物 | 人物出画后镜头不动（Movement Phase 拒绝跟随），或用固定环境承担余韵（EMO-02、EMO-20） | 禁止无理由长摇跟随；降级为固定远景 + 声音尾部 |
| 发现 / 揭示 | 立刻切到被发现的人或物 | 观众“自己先看见”的机会被抢走 | 延迟揭示：先用第二注意目标、遮挡与焦点交接给信息（EMO-10、EMO-18；`lens_language/focus_and_optics.md`） | 禁止先给答案再给反应；降级为同框Rack Focus |
| 对峙 / 谈判 | 平视双人正面交替 | 权力差与“谁占据画面”消失 | 不对称景别、谁先被切到侧背、谁被挤到边缘（EMO-14、EMO-05；`composition_language/foundations.md`） | 禁止在一个片段内自动绕行换侧；降级为固定同侧OTS |
| 追赶 / 追逐 | 背后跟拍 + 手持晃动 | 空间因果（谁追谁、还差多远）不可读 | 侧向位移让双方与地标保持同框（`camera_movement/side_tracking.md`、`advanced_camera_movement/traverse_shots.md`；EMO-11） | 禁止为紧张堆叠越轴与复杂运动；降级为侧向单路径 + 稳定终点 |
| 确认 / 真相落地 | 推近到脸部特写 | 表演被摄影机替代表达，反应变成“给答案” | 先给身体、手、呼吸，把脸留到确认之后或整镜不给（Face Economy；EMO-10、EMO-15） | 禁止情绪强度自动触发特写；降级为中近景 + 静默 |
| 崩塌 / 重大事件 | 大全景 + 环绕 + 快速摇 | 尺度与无力感被炫技抵消 | 用高机位、俯拍与尺度差把人物压小，或用固定机位与画外声承担（EMO-06、EMO-19） | 禁止事件后立刻切特写堆情绪；降级为固定大全景 + 声音先行 |

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
