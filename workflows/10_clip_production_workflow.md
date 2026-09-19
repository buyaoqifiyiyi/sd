# STATE-07 Clip Production Workflow

# Workflow Position

当前阶段：
STATE-07 Clip Production

前置阶段、下一阶段与对应下一 Workflow 的唯一 owner：
`workflows/workflow_map.md`

---

## Contract

Input：Confirmed STATE-06 Detailed Shot Design、WRITER / DIRECTOR INTENT、Confirmed Spatial Blocking、Canonical Assets、Selected Model / Adapter Profile。Output：`templates/20_clip_plan.md` 规定的 Confirmed Execution Clip Plan。Next：STATE-08。

STATE-07 是 Natural Unit 与 Execution Clip 的唯一决策 owner。它不重写 Script、Director Intent、Shot、Blocking、资产身份或最终 Prompt Schema。

## Required reads

- `modules/clip-planning.md`
- `modules/model-selection.md` 与唯一 Selected Adapter
- `knowledge/director_decision_layer.md`（当前Natural Unit覆盖的Director Decision Notes与Clip-level投影）
- `knowledge/clip_planning/index.md`（先据index定位，只读当前Clip相关文件）、`knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`
- `knowledge/spatial_blocking_layer.md`、`knowledge/camera_language/index.md`（Clip Movement Plan / Camera Continuity / Visual Rhythm的执行owner）、适用的 Performance / Transition knowledge
- 当前Clip使用Spatial Lock环境时：`knowledge/environment_multi_view_reconstruction.md`
- `templates/20_clip_plan.md`

## Procedure

**入口硬门**：没有`Selected Model`、`Adapter Revision`与`Model Planning Envelope`时，**不得创建任何 Execution Clip**。三者由 Model Selection 在 STATE-06 后交付并锁定；缺失或与 Adapter 不匹配时返回 Model Selection，不在本阶段猜模型。

本阶段按**三遍**执行，顺序不得颠倒——第一遍不知道模型，第三遍才知道真实数据：

1. **第一遍｜Natural Unit（不套用任何时长切法）**：核验 STATE-06 已确认、Revision 匹配、正式 SHOT 完整、空间 Blocking 与资产事实可读；失败回最小 owner。按 Shot 原顺序形成 Natural Unit：先消费当前Director Decision Notes，投影Clip Dramatic Function、Start → End Dramatic State、Critical Performance / Blocking、Rhythm与Information Timing Requirement；再保护 Writer Beat、Director Intent、动作完整性、时空/轴线、道具、情绪和 End-State。识别完整动作链、情绪因果、回忆与现实之间的匹配关系、道具状态变化、空间连续性与合理叙事断点。**此时不得按旧习惯先切成15秒以下短段**；Natural Unit时长等于其Shot时长之和。不得把多个阶段默认压成同一观察角度或同一路径跟随，只有明确的连续长镜理由才允许保持该摄影机逻辑。
2. **第二遍｜模型适配（在已锁定 Envelope 内）**：使用已锁定 Adapter 的时长、连续生成、Timeline 与安全降级规则处理 Natural Unit，判据只用各自 Adapter 拥有的窗口与条件，不得把任一模型能力复制给另一模型：
   - `≤30秒`且长时严格预检通过：Seedance 2.5 **保留完整单元**；
   - `>30秒`：按导演上成立的拆点拆分，而不是按旧窗口习惯；
   - 参考超限或复杂度过高：先精简参考或拆分，并记录理由；
   - **不得因为"方便重生"而提前切碎完整动作链**。
3. **第三遍｜逐Clip复核（Clip草案形成后）**：此时才计算每Clip的实际时长、实际参考数量、是否真正使用模型独占能力、预计生成费用、安全拆点与重生成风险，并按`modules/model-selection.md`的`## Clip Adequacy Verification｜Clip适用性验证`给出能力使用等级。**这一层是模型适用性验证，不是模型选择**；发现模型确实不兼容时才返回 Model Selection，并重新规划受影响的Clip。
4. **长时能力利用审计｜Long-Duration Capability Utilization**：逐对检查**相邻 Natural Unit 合并后**的结果，满足全部三个条件时**必须评估合并**：①合并后时长落在已锁定 Adapter 的窗口内（Seedance 2.5 为 ≤30秒，16—30秒按长时长严格预检执行）；②两段共享人物、空间、动作链或情绪因果中的至少一项；③合并后仍满足连续性、World-State、角色数量与 Reference Budget。结论逐对记录`合并 / 不合并`与理由，理由必须指向上述三项的具体一项或明确反例。本审计不新建 STATE、不改写 Shot 设计，也不得为了拉长时长而合并互不相关或刻意交叉剪辑的段落。
5. **三个非阻断警告**（只提高可见性，不阻断交付、不自动改 Clip 边界）：
   - `Duration Underutilized`：已锁定 Adapter 的时长窗口上限达到 30 秒（本仓库当前为 Seedance 2.5）但全片没有任何 Clip 进入 16—30 秒区间，即该模型的加长窗口与长时连续能力未被使用；提示存在合并候选与相应的尾帧交接减少。
   - `Continuity Fragmentation`：一个直接连续的完整动作被拆到不同 Clip（A类同镜头连续承接、或动作链跨越 Clip 边界），且拆点不是由模型窗口上限强制造成的；提示该段是可合并候选，同时给出合并的代价（单Clip风险面变大、重生成成本上升、中间控制点消失）。
   - `Continuity Fragmentation`的唯一例外：拆点由**导演上的刻意交叉剪辑**造成（例如现实与回忆的蒙太奇交替、世界切换）。此时拆点是设计特征而非碎片化，警告降级为记录，并写明该拆点服务的蒙太奇意图。
6. 每 Clip 执行连续性、World-State、角色数量、空间构图、表演、道具、转场、Reference Budget 和 A/B/C 尾帧用途检查；光色漂移风险按`rules/02_asset_rules.md`决定是否条件性选择已确认的`Project Color Reference`，它不成为资产。Spatial Lock环境按当前Camera Direction、景别、活动区、背景结构和风险，从已确认View Set预选最相关2–4张环境Canonical图并记录Primary Responsibility；不是机械加入全套View。`REF-SKETCH` 仅在 STATE-08 Gate 生成。
7. 将 Selected Model、**继承的 Model Lock Revision**、Adapter Profile、Execution Mode、时长、Preflight、End-State、Next-Clip Carryover、长时能力利用审计结论与受影响范围写入 State Contract 和 Clip Plan。

# Completion Gate

所有正式 Shot 原序且仅一次分配；每个 Execution Clip 有可验证输入、时长、连续性、尾帧用途和预算；Clip Plan 显式记录所继承的`Model Lock Revision`，且其创建不得早于该 Model Lock；Execution Clip Plan Confirmed 后完成 STATE-07。`Automation Policy: FAST`只在模型已锁定、所有Preflight PASS和状态写回成功时，按`rules/automation_mode.md`自动接受该Plan并记录依据；模型更换仅使受影响的 STATE-07/08 产物失效，Production-Locked Script、Confirmed Assets、Scene Breakdown 与 Detailed Shot Design 保持有效。
