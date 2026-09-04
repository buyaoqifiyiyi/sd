# Clip Production Decision Engine

## Greedy Grouping Procedure

按 Confirmed Detailed Shot Design 的正式SHOT顺序执行：

1. 用当前尚未分配的Shot建立候选Clip；单Shot可独立成Clip，也可在满足全部门槛时与相邻Shot组合。
2. 读取下一相邻分镜的时长、起始边界、结束边界、人物/环境/道具/FX状态、轴线、摄影机路径、表演与声音。
3. 若加入后超过15秒，立即结束当前Clip；不得为追求多镜Clip而压缩动作或删减覆盖。
4. 若未超过15秒，先由Director Decision判断观众需要看到什么、何时揭示信息、是否需要切镜；再执行连续性与执行复杂度门槛。
5. 无切镜必要时只可选多Shot连续生成；有明确叙事切镜必要时才评估多Shot有动机剪辑的完整切镜合同。无动机机位跳变、连续长镜头中途换轴或未稳定重建的新世界一律失败。
6. 全部通过且合并确实有助于形成自然长镜头或已确认的有动机揭示时才合并；任一失败即结束当前Clip，并从失败分镜建立下一候选Clip。
7. 候选Clip只要总时长4—15秒且边界完整即可确认。单Shot少于4秒时尝试与相邻兼容Shot组合；仍不能成立则返回STATE-06修正，不得靠新增剧情动作凑时长。单Shot超过15秒则返回STATE-06按自然边界拆分。
8. 直到所有正式分镜被且仅被一个Clip覆盖；Total Clips不得大于Total Formal Shots，允许二者相等。

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
| Boundary | 连续生成时前镜End与后镜Start可直接对应；有动机剪辑时切点、媒介、切前结束、切后稳定重建与锚点完整 |
| Space | 轴线、方向、视线与空间锚点兼容 |
| Camera | 可形成单一主路径或低复杂度连续路径；有动机剪辑后必须明确新机位/轴线与稳定构图 |
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

一个边界只选择一种主要技术，其他信息只作为支持约束。硬切、跳切或必须重建摄影机默认形成新的Clip边界；仅当Director确认其叙事功能，且切点/视觉媒介/切前结束/切后重建/连续性锚点/STATE-07拆分降级全部明确时，才允许作为多Shot有动机剪辑留在同一Clip。

## Inter-Clip Priority

每个 Clip 必须设计：

- Outgoing Anchor
- Stable End Window
- Tail-Frame Asset：A/B统一为`REF-TAIL-XX｜CLIP-XX尾帧参考`；缺图时仍在参考资产声明列名、用途与“待用户提供/待上传、未确认”，不得冒充已存在图片；C不列`REF-TAIL`
- Tail-Frame Use Mode：A同镜头连续承接 / B新镜头参考型 / C新镜头且无需尾帧
- Tail-Frame Requirement：在同一连续性判定内按当前Clip是否需要严格视觉承接标记`Tail Frame Required = YES / NO`；先判需求、后查资产
- Next Clip Incoming Anchor
- 声音连续锚点（仅对白、环境声、动作声、呼吸、Foley或剧情内声源）
- Direct Cut 降级方案

Continuous Handoff必须自动选择一种尾帧用途：

1. **A｜Direct Start-Frame Handoff｜同镜头连续承接**：上一Clip最后一个镜头在当前Clip继续、目标接近一镜到底时，标记`Tail Frame Required = YES`；【参考资产】列`REF-TAIL`与“同镜头连续承接用途”；【首帧参考】使用固定直接承接句并逐项锁定。
2. **B｜Reference-Only Handoff｜新镜头参考型**：下一Clip另起新镜头重新构图，但仍需上一尾帧锁定站位、朝向、距离、景别、空间、道具或起始构图时，同样标记`Tail Frame Required = YES`；【参考资产】列`REF-TAIL`与“空间/站位/景别参考用途”；【首帧参考】写明另起新镜头、保持项与允许变化，禁止使用A固定句。
3. **C｜Not Required / Not Inherited｜新镜头且无需尾帧**：明确换机位、换景别、反打、特写、俯拍/仰拍或重构图且不依赖上一画面状态时，标记`Tail Frame Required = NO`，不要求截图、不列`REF-TAIL`；依靠Canonical资产、Spatial Blocking与文字规则建立首帧。

A/B无论尾帧是否已上传都必须在参考资产声明列统一`REF-TAIL`名称、对应用途与真实状态；未提供时写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。

系统必须依据边界自行判定，并把连续性意图与资产可用性分开检查：不得把所有尾帧机械地当作参考，不得把待补充尾帧声明冒充已上传/已确认资产；A不得省略固定直接承接句，B不得误用该句，C不得列`REF-TAIL`。
