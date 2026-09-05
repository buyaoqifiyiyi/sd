# Clip Planning Module

Owner：STATE-07 `workflows/10_clip_production_workflow.md`；前置能力 owner：`modules/model-selection.md`；专业方法：`knowledge/clip_planning/`、`knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`。

## Natural Clip first

先按剧情连续性、动作完整性、场景/时间变化、机位突变、情绪节奏、镜头连续性、Writer Beat、Director Intent、Spatial Blocking、道具状态和参考边界形成 Natural Unit。记录自然时长为正式 Shot 时长之和；随后才以已选模型的 Adapter 约束整合为 Execution Clip。

Natural Unit 可以是 23 秒、34 秒或其他导演上成立的时长。它必须保持 Shot 顺序、End-State、A/B/C 尾帧用途和连续性；不改写剧本、资产或 Director Intent。Execution Clip 才可因目标模型上限拆分：2.0 的 23 秒必须拆分；2.5 的 23 秒经预检 PASS 保持单 Clip。

## Handoff

确认 Execution Clip Plan 时，写入 Selected Model、自然时长、模型适配结果和 Adapter handoff。STATE-08 只编译已确认的 Execution Clip；模型不得把 Natural Unit 当作失败，或改写其剧情、空间和导演事实。
