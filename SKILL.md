---
name: sd-film
description: AI影视虚拟制片生产系统。处理剧本、导演转译、资产、镜头、Clip、视频 Prompt、Seedance 和项目恢复；AUDIO/MUSIC仅在明确请求时调用，视频 Prompt 永久禁止非剧情内配乐。
---

# SD Film

Skill Version: 2026.09.05-r13

Build ID: sd-film-2026.09.05-r13

## Core

先读 `core/runtime-state.md`、`core/pipeline.md`、`core/rule-priority.md`。它们决定当前 STATE、合法推进、恢复、确认和冲突优先级。`references/project_state_contract.md` 是状态 Schema 与持久化唯一 owner；`templates/` 是最终输出格式唯一 owner。

主流程：STATE-00 Project Setup → STATE-01 Script → STATE-02 Asset Discovery → STATE-03 Asset Development → STATE-04 Visual Development → STATE-05 Scene Breakdown → STATE-06 Detailed Shot Design → Model Selection（内部）→ STATE-07 Clip Production → STATE-08 Video Prompt / Generation → STATE-09 Review。

已确认且未受影响的工件不得重做；用户的“下一步/继续/重做/返回/重新调用”由 Runtime State 和当前 Completion Gate 路由。Storyboard、Audio、Music、Sequence、Poster、Editing、Series 是辅助能力，不创建主 STATE。

## Modules

| Concern | Owner entry |
|---|---|
| Story, Writer Intent | `modules/screenwriter.md` |
| Director Intent and camera | `modules/director.md` |
| Assets and Canonical references | `modules/assets.md` |
| Optional storyboard | `modules/storyboard.md` |
| Spatial relations / neutral-mannequin blocking | `modules/spatial-blocking.md` |
| Natural Unit and Execution Clip planning | `modules/clip-planning.md` |
| Model choice and applicability | `modules/model-selection.md` |
| Final Prompt compilation | `modules/prompt-generation.md` |

## Model adapters

在 STATE-06 确认后、STATE-07 前选择一个 Adapter。STATE-07 先保护 Natural Unit 的剧情、空间、动作与导演事实，再用 Adapter 将它整合为模型可执行的 Execution Clip。Adapter 只能控制模型能力、时长、Timeline、参考输入与安全降级，不能改写 Script、Writer/Director Intent、Confirmed Blocking、Canonical Asset 或 Template。

- `adapters/seedance-2.0.md`：4–15 秒。
- `adapters/seedance-2.5.md`：4–30 秒；23 秒通过长时长预检保持单 Clip，34 秒才拆分；Timeline 按需使用。
- `adapters/other-models.md`：未验证模型不继承 Seedance 能力。

资产创作的图像路由不属于上述视频 Model Selection：默认由`modules/assets.md`使用内置 Image 输出；用户在STATE-03明确指定 Midjourney 时才读取`adapters/midjourney.md`，只交付 Midjourney Prompt，不调用内置图片生成。它不影响STATE-06后的模型选择、STATE-07 Clip或STATE-08视频 Prompt。

## Global invariants

- 不跳过 STATE；后续阶段必须有可验证的前置工件与 Completion Gate 证据。
- Writer 只拥有故事、人物、因果、Writer Beat、Setup/Payoff；Director 只拥有观众体验、表演、场面调度、空间、镜头语言。模型限制不得污染二者。
- `REF-SKETCH` 只用无性别技术调度人偶，且只控制空间/姿态/机位关系；不得成为角色外观或 Canonical Asset。
- A/B/C 尾帧、资产双确认、连续性、Voice opt-in 与视频 Prompt 永久无 BGM 继续由各自现有 owner 执行。
- Runtime Reload：`rules/runtime_reload.md`；State Source：`rules/state_source.md`；推进：`rules/progression_rules.md`；激活：`rules/activation_rules.md`；资源按需读取：`rules/resource_loading.md`。

每次正式修改同步递增 Version / Build，并执行 `references/module_contracts.md` 的 Change Safety Checklist、Standalone Skill Discovery Guard 与 Runtime Startup / Recovery Guard。
