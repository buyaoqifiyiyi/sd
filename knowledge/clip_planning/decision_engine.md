# Clip Production Decision Engine

## Greedy Grouping Procedure

按 Confirmed Detailed Shot Design 的正式SHOT顺序执行：

1. 用当前尚未分配的Shot建立候选Clip；单Shot可独立成Clip，也可在满足全部门槛时与相邻Shot组合。
2. 读取下一相邻分镜的时长、起始边界、结束边界、人物/环境/道具/FX状态、轴线、摄影机路径、表演与声音。
3. 若加入后超过15秒，立即结束当前Clip；不得为追求多镜Clip而压缩动作或删减覆盖。
4. 若未超过15秒，执行连续性与执行复杂度门槛。
5. 全部通过且合并确实有助于形成自然长镜头时才合并；任一失败即结束当前Clip，并从失败分镜建立下一候选Clip。
6. 候选Clip只要总时长4—15秒且边界完整即可确认。单Shot少于4秒时尝试与相邻兼容Shot组合；仍不能成立则返回STATE-06修正，不得靠新增剧情动作凑时长。单Shot超过15秒则返回STATE-06按自然边界拆分。
7. 直到所有正式分镜被且仅被一个Clip覆盖；Total Clips不得大于Total Formal Shots，允许二者相等。

不得跨过中间分镜寻找更容易合并的远端分镜。

## Compatibility Scorecard

以下项目不是平均分机制；Duration、Story、Asset、Boundary 与 Execution Capacity 均为 Hard Gate：

| Gate | Pass Requirement |
|---|---|
| Order | 来源分镜连续且顺序不变 |
| Shot Count | 每个Clip至少1个正式分镜；多镜时必须相邻且顺序不变；Total Clips ≤ Total Formal Shots |
| Duration | 单镜或多镜合计均为4—15秒 |
| Story | 无未授权时空/身份/因果断点 |
| Assets | 角色、环境、道具、FX版本可连续 |
| Boundary | 前镜 End 与后镜 Start 可直接对应 |
| Space | 轴线、方向、视线与空间锚点兼容 |
| Camera | 可形成单一主路径或低复杂度连续路径 |
| Performance | 刺激—反应—选择可在一次生成中读清 |
| Sound | 对白、环境声、动作声与Foley可连续；不依赖音乐 |
| Capacity | 模型能稳定执行，不以炫技覆盖信息 |

## Internal Handoff Priority

同一 Clip 内按以下优先级选择一种主要衔接逻辑：

1. 连续动作与连续摄影机路径
2. 动作匹配 / 视线接力 / 主体接力
3. 遮挡、门框、前景物或构图锚点揭示
4. 单次 Rack Focus 或景别自然变化
5. 同向、同轴、同平台且只有一次明确触发的自然景别或焦点演进

一个边界只选择一种主要技术，其他信息只作为支持约束。硬切、跳切或必须重建摄影机的边界不得放在同一Clip内部，必须形成新的Clip边界。

## Inter-Clip Priority

每个 Clip 必须设计：

- Outgoing Anchor
- Stable End Window
- Tail-Frame Asset：实际生成、提取并确认后统一为`REF-TAIL-XX｜CLIP-XX尾帧参考`；生成前只记录End State与待取得需求，不得虚构资产
- Tail-Frame Use Mode：Direct Start-Frame Handoff / Reference-Only Handoff / Not Inherited
- Tail-Frame Requirement：在同一连续性判定内按当前Clip是否需要严格视觉承接标记`Tail Frame Required = YES / NO`；先判需求、后查资产
- Next Clip Incoming Anchor
- 声音连续锚点（仅对白、环境声、动作声、呼吸、Foley或剧情内声源）
- Direct Cut 降级方案

Continuous Handoff必须自动选择一种尾帧用途：

1. **Direct Start-Frame Handoff**：下一Clip在人物、空间、道具、动作阶段、光色、构图和摄影机边界上必须从同一画面继续时，标记`Tail Frame Required = YES`；可用时将`REF-TAIL-XX｜CLIP-XX尾帧参考`直接作为下一段起始帧，尚未提供时主动请求用户截图并标记“待用户提供/待上传”，最终可执行版暂停。
2. **Reference-Only Handoff**：剧情与状态连续，下一Clip虽有正当的景别、机位、视角或构图变化，但仍需上一尾帧锁定人物/空间状态时，同样标记`Tail Frame Required = YES`；实际尾帧可用则将统一命名的`REF-TAIL`资产作为第一顺位连续性参考，未提供时执行同一主动请求与暂停规则。
3. **Not Inherited**：Motivated Discontinuity、明显时间跳跃、构图无需连续或画面独立重建标记`Tail Frame Required = NO`，不要求截图；明确不继承原因，并保留已确认的身份、道具、情绪或主题锚点。

系统必须依据边界自行判定，并把连续性意图与资产可用性分开检查：不得把所有尾帧机械地当作参考，不得把计划中的尾帧冒充实际资产，也不得在实际尾帧可用且可直接续接时省略`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`这一固定指令。
