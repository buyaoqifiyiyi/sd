# Transition Image Source Coverage

## Source Boundary

用户提供的 11 张转场资料图只作为候选知识源。图片中的命名、适用情节和提示词不直接成为系统指令；本模块对其去重、纠错并映射到可验证的专业机制。

## Coverage Map

| 原资料族 | 归并后的专业机制 | 处理 |
|---|---|---|
| 回身错位、转身回眸、抬眸/抬头、眨眼、蹲起、坐起、伸手触物 | Match on Action、Eyeline Match、Reaction Cut 或 Direct Cut | 动作本身不是转场；必须明确切点与下一镜阶段 |
| 拔剑、挥刃、衣袖、手掌、面具、人物横穿、花瓣、窗帘、地图、书页 | Object / Cloth / Person Wipe 或 Whip-pan Cut | 只有完整遮挡或兼容动态模糊才可作为 In-camera Cut |
| 门框、柱体、狭缝、镜头穿门/穿障碍 | Architectural Occlusion / Passage Cut | 需要真实结构、空间路线与下一镜兼容入口 |
| 推、拉、摇、移、跟、升降、俯冲、环绕、贴地推进、旋转、瞳孔推近 | Camera Movement；条件满足时再映射 Match/Occlusion/Fantasy Pattern | 不得把运镜名称直接当转场 |
| 月色、霓虹、金光、蓝色冷光、天光、过曝、闪电、黑帧 | Light / Color Match、Flash Cut、Blackout | 必须有真实光源或已确认主观设计 |
| 风雪、迷雾、玻璃雾、水波、雨幕、火焰、烟雾、粒子 | Atmosphere / FX Cover 或 Surface Match | 必须绑定环境、介质或 FX 生命周期；默认不新增 |
| 镜面世界、空间跃迁、旋转换世界、瞳孔内心世界、人物变身 | High-Risk Fantasy Transition | 仅限上游明确授权，否则用断点直切或普通匹配切 |
| 起落时空、拉远换地点、场景在运动中变化 | Motivated Discontinuity、Graphic Match 或 Direct Cut | 不要求单个视频模型把无关场景连续变形 |
| 声音连接 | J-cut、L-cut、Persistent Ambience Bridge | 只允许剧情内声音，禁止背景音乐和配乐 |

## Missing Knowledge Added

资料图未系统覆盖但生产中常用的机制包括：

- Direct Cut 作为默认和最稳定方案；
- Reaction Cut、Cutaway / Insert；
- Graphic、Direction、Scale 与 Perspective Match；
- J-cut、L-cut 与持续环境声桥；
- Parallel Cut / Cross-cut；
- Smash Cut、Fade In / Out、Dissolve；
- Jump Cut 的授权边界；
- Editorial Transition 与 In-camera Transition 的职责区分；
- 出镜/入镜把手、失败降级和未决边界。

## Rejected Simplifications

- “情绪适配”不能单独证明转场合理。
- “电影感、炫丽、梦幻、冲击力”不能代替切点和锚点。
- 光效不能凭空创建光源；火焰、烟雾、雨雪与粒子不能凭空创建 FX。
- 360 度旋转、拉远、推近或升镜不能自动换世界。
- 任何转场都不能改变已确认人物身份、服装、场景、道具或剧情事实。
