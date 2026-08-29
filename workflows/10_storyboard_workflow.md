# Optional / Auxiliary Storyboard Workflow

## Status And Trigger

本 Workflow 是可选辅助流程，不绑定任何固定 STATE，不属于主 Pipeline。

只在用户明确要求 Storyboard、分镜板、故事板、九宫格或其他视觉预演时调用。未明确请求时不得自动执行，也不得阻塞 `STATE-06 Detailed Shot Design → STATE-07 Clip Production`。

## Inputs

- 已确认 Detailed Shot Design
- 已确认 Character / Environment / Prop / FX Assets
- Visual Direction
- 需要视觉化的 Shot ID、画格数量、比例与用途

## Responsibilities

- 将已确认 Shot 视觉化为辅助预演，不新增或改写剧情、Shot、资产、动作结果或连续性事实
- 每格保留 Shot ID、构图、人物/空间关系、关键动作状态和必要边界注记
- 输出使用 `templates/09_storyboard_prompt.md`
- 产物登记为 Auxiliary Storyboard Artifact，不改变 Current State、Next Workflow 或主流程 Completion Gate

## Isolation Rules

- Storyboard 不是 STATE-07 交付物，也不是进入 STATE-08 的前置条件
- Storyboard 不参与 Clip 划分；Clip Production 只读取 Detailed Shot Design 与已确认生产事实
- Storyboard 图片、线稿、多格拼图、接触表及其截图不得登记为 Canonical Asset，不得进入 STATE-08【参考资产】
- STATE-08 不从 Storyboard 反推人物、环境、道具、动作、镜头或 Prompt

## Completion

完成后只在Selected State Source的 Completed Tasks / Active Artifacts 中记录 `Optional Storyboard Complete` 与产物 Revision；保持原 Current State 和 Next Workflow 不变，并按`references/project_state_contract.md`同步或输出完整Portable State，执行其`Portable Required Field Writeback`。普通Chat本机Root不可读时不得因Storyboard记录而停止主Pipeline。
