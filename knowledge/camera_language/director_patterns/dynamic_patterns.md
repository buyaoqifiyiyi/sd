# Dynamic Director Patterns

## Usage Rule

本表只收纳超过单一基础术语的动作与揭示模式。普通推、拉、摇、移、跟、升降、环绕、手持、航拍、POV 等继续调用各自权威文件，不在此重复定义。

## Pattern Matrix

| ID | 导演模式 | 规范原子 | 叙事用途 | 执行与降级 |
|---|---|---|---|---|
| DYN-01 | 弧线跟进 | `advanced_camera_movement/orbit_variants.md` + Tracking 意图 | 在接近人物时逐步揭示其与环境/他人的关系 | 使用 45–90 度单向弧线、固定中心和半径；失败则短直线 Push/Tracking |
| DYN-02 | 反向包抄 | 小弧线 Orbit + 已建立人物轴线 | 从人物背侧转到前侧形成一次局部关系翻转 | 只允许一次短弧线并以地标证明路径；轴线不可读则拆成背侧镜头与正面切镜 |
| DYN-03 | 侧向切入 | `camera_movement/side_tracking.md` 的短促进入变体 | 新主体突然进入、危机介入 | 从画面边缘沿单一横向路径快速进入并停住；不继续环绕或反向 |
| DYN-04 | 压迫式逼近 | `camera_movement/01_push_in.md` + 长焦压缩倾向 | 审讯、心理博弈、受限呼吸空间 | 长焦倾向与直线 Push 共同服务压迫，但只保留一次慢速靠近；脸部失稳则固定长焦近景 |
| DYN-05 | 退让式让位 | `camera_movement/02_pull_out.md` + Reveal 构图 | 为第二人物、线索或更大局面让出画面空间 | 单向后撤，以明确前景/新主体为终点；信息过多则拆成 Pull Out 与独立揭示镜头 |
| DYN-06 | 交叉穿行 | `advanced_camera_movement/traverse_shots.md` 或短距离 Tracking | 群戏调度、追逐转场、通过障碍推进 | 预先锁定通道、人物先后和一次穿越；多人交叉失稳则分成两个 Coverage 镜头 |
| DYN-07 | 贴地掠行 | `camera_angle/ground_level.md` + 短距离 Tracking | 车辆冲刺、战斗开场、地面速度冲击 | 贴地单向短路径，锁定安全距离和终点；穿模则固定贴地让主体经过 |
| DYN-08 | 顶视旋落 | `advanced_camera_movement/aerial_movements.md` | 从顶视几何过渡到人物层面，制造尺度落差 | 高风险；优先拆为固定 Top Down、遮挡/剪辑、人物层角度。单段尝试只保留一次有限旋落 |
| DYN-09 | 侧背尾随 | `camera_movement/shoulder_follow.md` 或 `side_tracking.md` | 潜行、秘密行动、警觉跟踪 | 依据肩背是否为锚点二选一；固定同一侧和距离，不在镜头中换肩 |
| DYN-10 | 突停凝视 | 单一 Tracking/Push + Static Hold | 真相刺痛、突然意识到目标、内心震荡 | 运动在事件触发点平滑急减速并稳定停住；若制动跳变，拆成运动镜头与静态反应镜头 |
| DYN-11 | 回撤揭示 | `camera_movement/02_pull_out.md` 的快速有动机变体 | 陷阱暴露、局势逆转、完整空间突然显现 | 一次短距离回撤并落在可读全局；环境重构则中景硬切至稳定远景 |
| DYN-12 | 双主体摆渡 | Pan 或 Rack Focus 二选一 | 在两名已建立角色间交接注意力或关系张力 | 同一平面用 Pan，前后景用 Rack Focus；不同时横移、反复往返或自动越轴 |
| DYN-13 | 斜向俯冲 | Aerial/Crane 高级路径 | 突袭、快速进入危险区域 | 锁定单一斜线路径、目标地标和终点高度；几何失稳则改为高角度 Fast Push 或剪辑 |
| DYN-14 | 纵深穿堂 | `advanced_camera_movement/traverse_shots.md` + Dolly 路径 | 沿走廊、门道连续探索空间 | 每段一条直线、一次边界，多个门廊用遮挡分段；不要求单段自由穿越多空间 |
| DYN-15 | 节奏点爆发 | 有动机的 Fast Push / Whip Pan /速度变化三选一 | 出场、决战前奏、动作节拍命中 | 由明确动作或声音事件触发，只发生一次；不能仅写“卡点”，需写起点、触发和落点 |
| DYN-16 | 悬停审视 | 固定机位或极短 Dolly 修正 | 权力压制、危险评估、冷静观察 | 摄影机保持稳定，只允许一次微小构图修正；若漂移则完全固定并由表演/声音承载压力 |
| DYN-17 | 前景遮挡运动 | 单一 Tracking + `composition_language/occlusion_frames.md` | 偷窥、空间切换、层次与转场 | 前景只短暂掠过或完整遮挡一次；关键表演保持可见，遮挡过强则移除运动 |
| DYN-18 | 变速运镜 | 任一基础单一路径 + 单一速度曲线 | 情绪递进、高潮铺垫或突然收束 | 路径不变，只允许慢到快或快到慢一次；方向和目标不得随速度改变 |
| DYN-19 | 快速推进变焦 | Fast Push 或 Dolly Zoom 二选一 | 强冲击、真相揭露、危机降临 | 先判断是否需要背景透视变化；不需要则 Fast Push，需要才用高风险 Dolly Zoom |
| DYN-20 | 抽离收尾 | `camera_movement/02_pull_out.md` 或 Aerial Pull Out | 结尾升华、人物离开、情绪落幕 | 选择地面后撤或高空拉远之一；终点保留环境、人物位置和声音余韵 |

## Terminology Corrections

- “甩镜”规范为 Whip Pan：机位基本固定、一次快速水平转向；不能写成随机摆动。
- “航拍”描述摄影平台或高空运动；“鸟瞰”描述观察角度，两者不是同义词。
- “滑轨镜头”属于稳定 Dolly/Truck 路径；设备名称不能替代起点、方向和终点。
- “长镜头调度”属于拍摄与剪辑结构，不是一种单独摄影机运动。
- “倾斜镜头”规范为 Dutch Angle，属于角度/构图，不属于运镜。

## Final Principle

动作模式的价值来自清楚的路径、触发、落点和降级方案。复杂名称不能替代空间说明。
