# Camera Movement Selection Matrix

## Module Contract

- **Module Name**：Camera Movement Selection Matrix
- **Module Type**：STATE-06 至 STATE-09 辅助 Camera Knowledge；不是 Workflow、Template 或新 STATE
- **触发条件**：所有正式 SHOT 的 Camera Language Decision、所有 Clip Movement Plan、STATE-08 运镜语义投影及 STATE-09 Camera Language QA
- **不触发条件**：不独立改写剧情、资产、导演风格、镜头目的、Shot / Clip 顺序或 Seedance 最终 Schema
- **Required Inputs Owner**：Scene / Shot Purpose、人物情绪与动作、Blocking / Relational Screen Geometry、空间任务、节奏阶段、Visual Direction、模型复杂度和边界合同分别由其上游阶段拥有
- **Output Owner**：STATE-06 决策字段由 `templates/08_shot_design_prompt.md` 拥有；STATE-07 Clip Movement Plan 由 `templates/20_clip_plan.md` 拥有；STATE-08 仍只由 `templates/10_video_prompt.md` 拥有
- **允许读取**：本目录 `index.md`、被选主/辅助运镜的原子知识文件、适用的 Movement Combination / Advanced Camera Movement 与上游已确认项目资料
- **允许写入**：只通过当前阶段拥有者写入 Detailed Shot Design、Clip Production Plan、内部 Projection / QA 结果；不直接写项目事实或最终 Prompt 字段
- **下游消费者**：`workflows/09_shot_design_workflow.md`、`workflows/10_clip_production_workflow.md`、`workflows/11_video_generation_workflow.md`、`workflows/13_review_workflow.md`
- **禁止修改**：已确认剧情、人物关系、资产身份、Visual Direction、关系轴、Coverage、Shot Purpose、正式 Shot / Clip ID与顺序
- **冲突返回路由**：镜头目的、动作容量、轴线或运镜设计冲突返回 STATE-06；Clip 编排冲突返回 STATE-07；仅执行翻译问题留在 STATE-08；资产/剧情事实返回其拥有者
- **Validator 不变量**：本文件存在；四个 Workflow 可发现并调用它；STATE-06/07 模板拥有对应字段；STATE-08 不新增最终字段；基础优先、高风险运镜受门控；多样性规则可被静态检索

## Purpose

本矩阵把以下五项输入联合转换为 Camera Language Decision：

`镜头目的 + 情绪功能 + 人物运动 + 空间任务 + 节奏阶段 → 推荐主运镜 + 可选辅助运镜 + 禁止运镜 + Seedance稳定等级`

它解决“知道很多运镜术语，但生成时仍默认慢推或轻微横移”的调用缺口。矩阵提供候选，不替代导演判断；最终选择必须同时满足剧情、轴线、人物动作、空间可读性与模型执行能力。

## Actual Retrieval Gate

每个正式 SHOT 在确认运镜前必须按顺序实际读取：

1. 本文件；
2. `knowledge/camera_language/camera_movement/index.md`；
3. 被选“推荐主运镜”对应的原子知识文件；
4. 若“可选辅助运镜”构成真实摄影机运动，再读取其原子知识文件；
5. 候选含两种以上主要运动、多个机位/视点或一镜到底时，读取 `knowledge/camera_language/movement_combinations/index.md` 与其 Decision Engine；
6. 候选包含复杂环绕、360度、穿墙、无人机或其他高难度路径时，读取 `knowledge/camera_language/advanced_camera_movement/index.md`，并重新确认叙事必要性与模型容量。

只读取索引、只写“电影感运镜”或从习惯模板直接填“缓慢推进/轻微横移”，均不算完成检索。

## Seedance Stability Levels

| 等级 | 含义 | 默认处理 |
|---|---|---|
| S1 高稳定 | 单一方向、起止点清楚、人物动作简单、轴线固定；固定机位、Push In、Pull Out、Pan、Tilt、简单 Side Tracking / Dolly Tracking 常处于此级 | 可直接进入执行翻译，仍须写清起点、路径、速度、终点与限制 |
| S2 可控 | 路径或人物配合稍复杂，但可通过固定侧位、距离、方向和低动作密度稳定执行；Tracking、Shoulder Follow、Crane、克制 Handheld 常处于此级 | 必须提供安全降级；多人镜头先锁关系几何 |
| S3 条件执行 | 路径与稳定质感组合、快速移动、复杂前景、一次低复杂度复合路径或模型容量接近上限 | 只有明确叙事收益时使用；失败先删辅助、降速、缩短路径或拆镜 |
| S4 高风险 | 复杂 Orbit / 360、穿墙、无人机大范围路线、连续越轴、多次方向反转、多段一镜到底 | 默认禁止；只有上游明确需要、已读高级知识、模型复杂度允许且有基础降级时才可采用 |

稳定等级由具体人物动作、场景、焦段、FX、镜头长度和模型能力共同决定；同一运镜不是永久固定等级。

## Selection Matrix

| 镜头目的 | 情绪功能 | 人物运动 | 空间任务 | 节奏阶段 | 推荐主运镜 | 可选辅助运镜/支持行为 | 禁止运镜 | Seedance稳定等级 |
|---|---|---|---|---|---|---|---|---|
| 建立城市/室内空间并给出人物位置 | 观察、等待、秩序 | 静止或缓慢入画 | 从环境范围落到主体，保持地标可读 | 开场/段落进入 | Pan；存在垂直层级时用 Crane Down | 到达主体后 Static Hold；一次轻微 Rack Focus不算第二主运镜 | 默认慢推；大范围无人机；Pan同时横移 | S1；Crane为S2 |
| 从人物局部揭示完整人物或上方信息 | 好奇、确认 | 静止或单一小动作 | 固定机位内完成垂直注意转移 | 信息铺垫 | Tilt Up / Tilt Down | 终点稳定停住 | Crane、推拉与Tilt叠加；上下往返 | S1 |
| 人物进入未知空间、寻找目标 | 犹豫、警觉、期待 | 向前行走 | 保留人物肩背、前方目标和进入方向 | 进入/蓄势 | Shoulder Follow | 极轻微步伐呼吸；终点Static Hold | 中途换肩、绕正面、环绕、快速推拉 | S2 |
| 单人沿街/走廊持续前进，同时展示环境变化 | 克制、孤独、行动感 | 单向步行或中低速跑动 | 保持屏幕方向与连续视差 | 发展 | Side Tracking 或 Dolly Tracking | 前景掠过；一次轻微焦点修正 | 无理由慢推；换侧；侧跟同时环绕 | S1-S2 |
| 双人并肩行走或边走边谈 | 陪伴、疏离、关系试探 | 同向步行 | 锁定两人内外侧、距离与步速 | 关系发展 | Side Tracking | 一次极轻微同向靠近；短暂Rack Focus | 连续正面慢推；换侧；双方同为完整正脸 | S2 |
| 稳定陪同人物穿过走廊/站台 | 秩序、控制、仪式感 | 单一路径行走 | 起点、终点和真实视差清楚 | 发展/推进 | Dolly Tracking | 门框/柱体前景视差；人物停步时同步减速 | 自由漂移、轨道转Orbit、多次方向反转 | S1-S2 |
| 从一个人/物转向其视线目标 | 发现、怀疑、对照 | 主体先转眼或轻转头 | 固定观察点内连接因果目标 | 刺激/发现 | Pan | 终点一次Rack Focus或Static Hold | 横移冒充Pan；来回摇；同时推近 | S1 |
| 逐步确认人物意识到关键信息 | 压抑、吸引、心理压力 | 静止、呼吸、细微反应 | 缩短观察距离且保持轴线 | 确认/上升 | Push In | 终点低动作稳定；必要时轻微焦点修正 | 每个反应镜都慢推；同时横移/环绕/变焦 | S1 |
| 强调人物主动靠近、步步施压 | 紧张、逼近、决心 | 人物向前或对方后退 | 摄影机与人物路径/距离变化可读 | 上升/冲突前 | Dolly Tracking 或 Tracking | 克制Handheld质感仅在现场感成立时使用 | Push、Tracking、Handheld三者无主次叠加；越轴 | S2-S3 |
| 紧张事件突然进入现场感 | 警觉、焦虑、失控边缘 | 简单移动或近距离反应 | 保持主体和轴线可读 | 突变/上升 | Handheld（克制） | 一条短而简单的Tracking路径；结束时减弱呼吸 | 剧烈随机抖动；长焦强抖；复杂群体换位 | S2；组合为S3 |
| 保持双人静态对话的压抑与可读性 | 克制、疏离、试探 | 坐/站，表演为主 | 稳定关系轴、眼线与距离 | 铺垫/停顿 | Static / Locked-Off | 只有关键确认点才允许一次Push In，或克制Handheld呼吸 | 每句对白都慢推；连续横移；日常对话Orbit | S1 |
| 展示两人距离缩短或关系松动 | 试探、靠近、释然 | 一人靠近/并肩 | 让身体距离变化成为主信息 | 转折 | Side Tracking（移动中）或 Dolly Tracking（直线靠近） | 终点短暂Static Hold | 无人物动作却默认横移；复杂Orbit替代关系Blocking | S2 |
| 关键反应需要短暂凝视 | 迟疑、确认、压抑泄漏 | 基本静止 | 保持面部证据与背景锚点 | 转折/停顿 | Static / Locked-Off | 极轻微Push In只能在信息权重确实上升时使用 | 自动慢推模板；摇移寻找不存在目标 | S1 |
| 动作追随、奔跑或追逐路径可读 | 紧迫、参与感 | 单向跑动/追逐 | 保持来源—目标、屏幕方向和路径 | 加速/高潮前 | Tracking 或 Side Tracking | Moderate Handheld质感；扩大景别 | 快速Orbit、无人机、越轴、多次折返同镜执行 | S2-S3 |
| 从局部扩展到整体空间后果 | 释然、渺小、余韵 | 完成动作后静止/缓行 | 揭示垂直层级或整体规模 | 释放/收束 | Crane Up | 到达终点后Static Hold | 同时Pull Out、环绕、无人机远飞 | S2 |
| 人物从关系中退开或被环境吞没 | 失落、离别、孤独 | 静止或缓慢离开 | 扩大人与环境距离 | 释放/结尾 | Pull Out | 人物继续单向离开；终点稳定大景 | 高速推进；临近情绪高潮时无理由拉远 | S1 |
| 强情绪高潮但人物表演是核心 | 决绝、崩溃、重逢 | 简单动作、拥抱前后或静止 | 让表演和关系清楚，不靠摄影炫技 | 高潮 | Push In、Static或克制Handheld三选一 | 只允许与主路径不冲突的呼吸/焦点支持 | 默认Slow Orbit；360；推拉摇移叠加 | S1-S2 |
| 明确英雄时刻、空间转化或主观眩晕，且普通方案无法表达 | 觉醒、失衡、仪式性 | 动作极简、主体位置稳定 | 明确绕行半径、轴线策略和稳定终点 | 单一视觉高潮 | Orbit仅作为高级条件候选 | 无；先准备Static/Push In降级 | 日常对白使用Orbit；360与复杂人物动作/FX并发 | S4 |
| 段落结束后留下城市/环境余韵 | 平静、空缺、未决 | 人物离画或保持远景 | 恢复环境主导权 | 尾声 | Pull Out、Crane Up或Static三选一 | 持续环境运动和声音，不新增主运镜 | 继续慢推；无动机横移；复杂转场式运镜 | S1-S2 |

## Atomic Knowledge Map

- Push In：`knowledge/camera_language/camera_movement/01_push_in.md`
- Pull Out：`knowledge/camera_language/camera_movement/02_pull_out.md`
- Tracking：`knowledge/camera_language/camera_movement/03_tracking.md`
- Orbit：`knowledge/camera_language/camera_movement/04_orbit.md`；复杂版本另读 Advanced Camera Movement
- Side Tracking：`knowledge/camera_language/camera_movement/side_tracking.md`
- Pan：`knowledge/camera_language/camera_movement/pan.md`
- Tilt：`knowledge/camera_language/camera_movement/tilt.md`
- Crane：`knowledge/camera_language/camera_movement/crane.md`
- Handheld：`knowledge/camera_language/camera_movement/handheld.md`
- Shoulder Follow：`knowledge/camera_language/camera_movement/shoulder_follow.md`
- Dolly Tracking：`knowledge/camera_language/camera_movement/dolly_tracking.md`

## Camera Language Decision Record

每个 Detailed Shot 必须先形成并确认以下内部生产决策，再写 Camera Movement 与执行描述：

- 镜头目的
- 情绪功能
- 空间功能
- 人物运动
- 节奏阶段
- 推荐主运镜（或明确 Static / Locked-Off）
- 可选辅助运镜/支持行为
- 禁止运镜
- Seedance稳定等级
- 选择理由
- 实际读取的主运镜原子知识文件；适用时记录辅助/组合/高级知识文件

如果任一项缺失，或主运镜只写“跟拍、电影感、动态镜头”而没有具体类别与空间路径，不得确认 Detailed Shot。

## Diverse, Not Chaotic

1. 每个 Clip 必须先确立一种**主导镜头语言逻辑**，例如“固定观察→一次关键靠近”“同向跟随→停住确认”“稳定关系轴→结尾拉远”。主导逻辑是叙事组织，不等于所有 Shot 使用同一种运镜。
2. 一个 Clip 超过4个 Shot 时，通常至少使用2种不同运镜逻辑；若只用1种，必须记录它如何服务连续动作、长镜观察或刻意重复。
3. 同类主运镜连续出现3次及以上，必须逐镜记录不同的叙事功能或保留重复的明确理由；“保持电影感”不成立。
4. 不强制每个 Shot 都不同。相邻镜头属于同一动作、同一关系观察或同一节奏段时，可以保持一致；变化必须发生在刺激、关系、空间或节奏功能改变处。
5. 多样性优先来自“固定/跟随/揭示/靠近/释放”等逻辑变化，不来自随机叠加摄影机运动。
6. 可选辅助运镜默认不是第二个主要路径。优先使用Static Hold、轻微构图修正、一次Rack Focus或低幅度手持呼吸；若形成第二个物理路径，必须进入Movement Combination判定。
7. 禁止把“缓慢推进/轻微横移”当作未检索时的默认填充。确需使用时必须说明它在本镜承担的独特叙事功能、起止点和为何不与前后镜重复。

## Complexity Priority

默认优先：Push In、Pull Out、Tracking、Side Tracking、Pan、Tilt、Crane、Handheld、Shoulder Follow、Dolly Tracking与Static / Locked-Off。

复杂Orbit / 360、穿墙、无人机大范围运动、连续越轴和多段一镜到底仅在以下条件全部成立时使用：

- 镜头目的无法由基础运镜等价完成；
- 上游已明确该视觉高潮或空间变化；
- 人物动作、FX、口型与场景重建复杂度仍在模型容量内；
- 已读取Advanced与Movement Combination规则；
- 已提供基础稳定降级方案。

## STATE-08 Translation Rule

Camera Language Decision和Clip Movement Plan不得复制为STATE-08新字段。必须把语义投影到`templates/10_video_prompt.md`现有字段：

- `镜头/机位：`承载摄影机起点、人物侧位、唯一主要路径、方向、速度、触发、终点与稳定限制；
- `画面描述：`承载运镜与人物动作、前后景视差、揭示/遮挡和焦点变化的同步过程；
- `空间关系：`承载轴线侧、屏幕方向、距离与来源—目标连线；
- `镜头结尾状态：`承载摄影机终点、结束景别、稳定构图与下一镜可继承锚点；
- 边界与切点语义写入固定字段`镜头结尾状态：`，不把普通运镜误写成转场；不得另增`与下一镜衔接：`字段。

最终Prompt不得输出“Camera Language Decision”“Clip Movement Plan”“S1-S4”或本矩阵表头。
