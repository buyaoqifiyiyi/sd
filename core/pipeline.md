# Core Pipeline

SD Film 的主生产顺序唯一为：

`STATE-00 Project Setup → STATE-01 Script Analysis → STATE-02 Asset Discovery → STATE-03 Asset Development → STATE-04 Visual Development → STATE-05 Scene Breakdown → STATE-06 Detailed Shot Design → STATE-07 Clip Production → STATE-08 Model Adaptation and Video Prompt / Generation → STATE-09 Review`

Storyboard、Audio、Music、Sequence、Poster、Editing 与 Series 是按需辅助能力，不创建 STATE，也不改变下一个主 STATE。现有 Verified Artifact 与 Completion Gate 是进入后续阶段的唯一证据；用户目标词、旧对话或模型名称不是跳阶段证据。

## Responsibility boundary

- STATE-01：Screenwriter 产生并锁定故事事实与 WRITER INTENT PACKET。
- STATE-04—06：Director 将锁定事实转成视觉叙事、空间调度及正式 Shot，不根据视频模型重写创作意图。
- STATE-06 后：Model Selection 选择唯一 Adapter；只取得执行能力，不改写创作事实。
- STATE-07：先形成 Natural Unit，再按选定模型将其整合为 Execution Clip、边界、连续性、参考预算和目标时长。
- STATE-08：以确认的 Execution Clip 编译最终 Prompt；Adapter 仅适配执行，不改写上游事实。
- STATE-09：仅 PASS 完成；REVISE / REBUILD 返回最小受影响 owner。

`下一步`、`继续`等纯推进命令按 `core/runtime-state.md`、当前 Completion Gate 和这个顺序路由；已确认且未受影响的交付物不得重做。
