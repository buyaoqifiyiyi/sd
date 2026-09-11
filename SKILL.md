---
name: sd-film
description: "调用sd、调用SD、用SD Film、重新调用sd、恢复旧项目、继续之前的项目：AI影视虚拟制片生产系统。处理剧本、导演转译、资产、镜头、Clip、视频 Prompt、Seedance 和项目恢复；AUDIO/MUSIC仅在明确请求时调用，视频 Prompt 永久禁止非剧情内配乐。"
---

# SD Film

Skill Version: 2026.09.11-r53

Build ID: sd-film-2026.09.11-r53

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

STATE-00先确认项目级图像模型默认项与视频模型偏好；STATE-03直接复用图像默认项，STATE-06确认后只对视频偏好进行按Clip能力复核并形成唯一Adapter Execution Profile，不重复索取同一选择。STATE-07先保护Natural Unit的剧情、空间、动作与导演事实，再用已验证Adapter将它整合为模型可执行的Execution Clip。Adapter只能控制模型能力、时长、Timeline、真实参考输入与安全降级，不能改写Script、Writer/Director Intent、Confirmed Blocking、Canonical Asset或Template。

- `adapters/seedance-2.0.md`：4–15 秒。
- `adapters/seedance-2.5.md`：4–30 秒；23 秒通过长时长预检保持单 Clip，34 秒才拆分；按需使用时间戳式 Timeline，并审计 30 图 / 10 视频 / 10 音频、合计最多 50 个参考输入。Dreamina 网页端专有能力必须显式选择该入口，不能误报为方舟 API。
- `adapters/minimax-h3.md`：4–15 秒；支持首/尾帧、全能多模态参考和已有视频编辑，按官方三段式提示词编译；不继承 Seedance 专属的时码式 Targeted Edit 或长时长能力。
- `adapters/other-models.md`：未验证模型不继承 Seedance 能力。

资产创作的图像路由不属于视频Adapter：STATE-00由`modules/image-model-selection.md`一次确认项目图像模型默认项，STATE-03在每个资产批次直接继承；仅用户明确要求例外模型、默认项不可用或当前批次需改用模型时才重新确认。当前可选Built-in Image（`adapters/built-in-image.md` + `templates/24_builtin_image_asset_prompt.md`）或Midjourney（`adapters/midjourney.md` + `templates/14_midjourney_asset_prompt.md`）；未来模型必须先有独立Adapter和最终提示词模板。它不影响视频模型偏好、STATE-07 Clip或STATE-08视频 Prompt。

## Global invariants

- 不跳过 STATE；后续阶段必须有可验证的前置工件与 Completion Gate 证据。
- Writer 只拥有故事、人物、因果、Writer Beat、Setup/Payoff；Director 只拥有观众体验、表演、场面调度、空间、镜头语言。模型限制不得污染二者。
- `REF-SKETCH` 只用无性别技术调度人偶，且只控制空间/姿态/机位关系；不得成为角色外观或 Canonical Asset。
- A/B/C 尾帧、资产双确认、连续性、Voice opt-in 与视频 Prompt 永久无 BGM 继续由各自现有 owner 执行。
- Runtime Reload：`rules/runtime_reload.md`；State Source：`rules/state_source.md`；推进：`rules/progression_rules.md`；激活：`rules/activation_rules.md`；资源按需读取：`rules/resource_loading.md`。
- 自动推进：只有用户明确启用时读取`rules/automation_mode.md`；它只压缩可逆、可追溯的确认，不跳过主STATE、事实锁或硬性风险边界。
- 固定且连续性敏感的环境在STATE-03按需读取`knowledge/environment_multi_view_reconstruction.md`：它扩展既有Environment Asset与Canonical Lock，不创建新STATE；STATE-06/07/08只继承已锁定的空间事实和按风险选择的环境参考。

每次正式修改同步递增 Version / Build，并执行 `references/maintenance_self_check.md` 的15项Self-Check与两个Guard（判据真源：`references/maintenance_self_check_protocol.md`）。
