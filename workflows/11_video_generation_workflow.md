# STATE-08 Video Prompt / Generation Workflow

## Contract

Input：Confirmed Execution Clip Plan、Selected Model / Adapter Profile、Confirmed Script、Director Intent、Spatial Blocking、Canonical Assets、首尾帧与状态。Output schema：`templates/10_video_prompt.md`。本 Workflow 不选择模型、不创建或拆分 Clip、不调用旧 Compiler。

## Required reads

- `modules/prompt-generation.md`
- 当前 Selected Adapter
- `knowledge/prompt_compilation/state08_projection.md`
- `knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`
- `templates/10_video_prompt.md`

## Procedure

1. 核验 Execution Clip Plan、Adapter Profile、状态、资产和 Shot/Blocking Revision 一致；缺失或冲突回 STATE-07 或事实 owner。
2. 对当前一个 Confirmed Execution Clip 执行最终 Reference、A/B/C 尾帧、Visual Blocking Anchor、连续性和 Prompt Preflight。不得把 Storyboard、Top-down Map 或文字伪资产作为视频参考。
3. 通过 Projection 将已确认事实写入 Template 既有字段。每个 Clip 独立完整输出；不输出 Adapter、模型、内部账本、时间码或新的 Schema。
4. 不改写剧情、关系、导演意图、Shot 目的、Blocking 或 Canonical Asset。Voice 仅显式 opt-in；Prompt 永久禁止 BGM/配乐。

## Failure and completion

只改当前 Clip 的 Prompt 映射问题留在 STATE-08；Clip 边界、预算、尾帧或连续性组织问题回 STATE-07；Shot/Blocking 回 STATE-06；事实或资产回对应 owner。全部检查 PASS 后交付或生成，随后进入 STATE-09 Review。
