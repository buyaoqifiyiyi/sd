# STATE-07 Clip Production Workflow

## Contract

Input：Confirmed STATE-06 Detailed Shot Design、WRITER / DIRECTOR INTENT、Confirmed Spatial Blocking、Canonical Assets、Selected Model / Adapter Profile。Output：`templates/20_clip_plan.md` 规定的 Confirmed Execution Clip Plan。Next：STATE-08。

STATE-07 是 Natural Unit 与 Execution Clip 的唯一决策 owner。它不重写 Script、Director Intent、Shot、Blocking、资产身份或最终 Prompt Schema。

## Required reads

- `modules/clip-planning.md`
- `modules/model-selection.md` 与唯一 Selected Adapter
- `knowledge/clip_planning/`、`knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`
- `knowledge/spatial_blocking_layer.md`、适用的 Camera / Performance / Transition knowledge
- `templates/20_clip_plan.md`

## Procedure

1. 核验 STATE-06 已确认、Revision 匹配、正式 SHOT 完整、空间 Blocking 与资产事实可读；失败回最小 owner。
2. 按 Shot 原顺序形成 Natural Unit：保护 Writer Beat、Director Intent、动作完整性、时空/轴线、道具、情绪和 End-State。Natural Unit 时长等于其 Shot 时长之和。
3. 使用已选 Adapter 将 Natural Unit 整合为 Execution Clip。仅在时长或模型可执行性要求时拆分，并为每段保留动作、空间、尾帧、连续性与 Return Route。
4. 2.0：4–15 秒；23 秒 Unit 必须拆分。2.5：4–30 秒；23 秒经 Long-duration Preflight PASS 保持单 Clip；34 秒拆分。Timeline 只在 Adapter 认为适用时采用。
5. 每 Clip 执行连续性、World-State、角色数量、空间构图、表演、道具、转场、Reference Budget 和 A/B/C 尾帧用途检查。`REF-SKETCH` 仅在 STATE-08 Gate 生成。
6. 将 Selected Model、Adapter Profile、Execution Mode、时长、Preflight、End-State、Next-Clip Carryover 与受影响范围写入 State Contract 和 Clip Plan。

## Completion

所有正式 Shot 原序且仅一次分配；每个 Execution Clip 有可验证输入、时长、连续性、尾帧用途和预算；Execution Clip Plan Confirmed 后完成 STATE-07。模型更换仅使受影响的 STATE-07/08 产物失效。
