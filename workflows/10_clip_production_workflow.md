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
- `knowledge/clip_planning/`、`knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`
- `knowledge/spatial_blocking_layer.md`、适用的 Camera / Performance / Transition knowledge
- 当前Clip使用Spatial Lock环境时：`knowledge/environment_multi_view_reconstruction.md`
- `templates/20_clip_plan.md`

## Procedure

1. 核验 STATE-06 已确认、Revision 匹配、正式 SHOT 完整、空间 Blocking 与资产事实可读；失败回最小 owner。
2. 按 Shot 原顺序形成 Natural Unit：先消费当前Director Decision Notes，投影Clip Dramatic Function、Start → End Dramatic State、Critical Performance / Blocking、Rhythm与Information Timing Requirement；再保护 Writer Beat、Director Intent、动作完整性、时空/轴线、道具、情绪和 End-State。Natural Unit时长等于其Shot时长之和；不得把多个阶段默认压成同一观察角度或同一路径跟随，只有明确的连续长镜理由才允许保持该摄影机逻辑。
3. 使用已选 Adapter 将 Natural Unit 整合为 Execution Clip。仅在时长或模型可执行性要求时拆分，并为每段保留动作、空间、尾帧、连续性与 Return Route。
4. 按唯一 Selected Adapter 的时长、连续生成、Timeline 与安全降级规则整合。Seedance 2.0、Seedance 2.5 与 MiniMax H3 的具体窗口和条件只由各自 Adapter 拥有；不得将任一模型能力复制给另一模型。
5. 每 Clip 执行连续性、World-State、角色数量、空间构图、表演、道具、转场、Reference Budget 和 A/B/C 尾帧用途检查；光色漂移风险按`rules/02_asset_rules.md`决定是否条件性选择已确认的`Project Color Reference`，它不成为资产。Spatial Lock环境按当前Camera Direction、景别、活动区、背景结构和风险，从已确认View Set预选最相关2–4张环境Canonical图并记录Primary Responsibility；不是机械加入全套View。`REF-SKETCH` 仅在 STATE-08 Gate 生成。
6. 将 Selected Model、Adapter Profile、Execution Mode、时长、Preflight、End-State、Next-Clip Carryover 与受影响范围写入 State Contract 和 Clip Plan。

## Completion

所有正式 Shot 原序且仅一次分配；每个 Execution Clip 有可验证输入、时长、连续性、尾帧用途和预算；Execution Clip Plan Confirmed 后完成 STATE-07。`Automation Policy: FAST`只在模型已锁定、所有Preflight PASS和状态写回成功时，按`rules/automation_mode.md`自动接受该Plan并记录依据；模型更换仅使受影响的 STATE-07/08 产物失效。
