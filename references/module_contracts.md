# SD Film Module Contracts

## Module Contract File Index

为控制单次读取成本，模块接口合同按类别拆为四个文件。各文件内部小节保持原有顺序与名称；**归属判定仍以本文件的 Authority Matrix 为准**，类别拆分不改变任何owner。

| File | 覆盖范围 |
|---|---|
| `references/module_contracts.md`（本文件） | Purpose、Authority Matrix、Stable Interface Rules（全局Runtime与生产知识owner清单）、Required Contract For Every New Module、Seedance 2.5 Template Override、Image Model Prompt Template Isolation、Skill Maintenance QA |
| `references/module_contracts_production.md` | 核心生产模块：Screenwriter、STATE-03 Visual Asset Production、Prompt Compilation、Clip Production、Project State And Recovery、Shot Language Router |
| `references/module_contracts_auxiliary.md` | 辅助模块：Clip Preflight Check、MUSIC、AUDIO、Skill Experience、Poster Design、Sequence、Fast Automation Policy |
| `references/module_contracts_knowledge.md` | 知识契约：Camera Composition／Focal Length／Camera Movement Combination／Camera Movement Selection Matrix、Performance Expression、Color、Lighting、Transition、Quality |

## Purpose

本文件定义新增或修改模块与现有生产系统之间的接口合同。Skill维护QA不属于本文件，由`references/maintenance_self_check.md`与其判据真源`references/maintenance_self_check_protocol.md`拥有。

目标是允许SD Film持续扩展，同时避免：

- 重复职责
- 重复Schema
- 非法STATE
- 上游事实被下游覆盖
- 项目数据写入Skill根目录
- 一个模块直接修改另一个模块拥有的输出

## Seedance 2.5 Template Override

本文件中因历史合同而单独提到`templates/10_video_prompt.md`、9图预算或十字段分镜的描述，除非明确写为通用Selected Template，否则只适用于Seedance 2.0。Seedance 2.5一律使用`templates/12_seedance_25_video_prompt.md`：30图 / 10视频 / 10音频 / 合计50项容量审计、多模态参考职责和时间线是其专属最终Schema；MiniMax H3一律使用`templates/13_minimax_h3_video_prompt.md`：官方三段式、`@`参考输入和`非叙事性音乐：N/A`是其专属最终Schema。未来模型必须先建立独立最终Prompt Template，才能接入Model Selection。此覆盖不改变上游事实、资产双确认、A/B/C尾帧、Voice opt-in或无BGM边界。

## Image Model Prompt Template Isolation

图像模型不进入视频Model Selection：`Production Setup Gate`由`modules/image-model-selection.md`拥有项目图像模型默认项与`Image Delivery Mode`的选择，STATE-03由它为当前资产批次继承默认项或处理明确例外，`modules/assets.md`拥有选择后的图像路由。资产类别Template（角色、环境、道具、FX）继续独占资产定义、阶段状态和双确认闭环；每个可选图像模型的Adapter必须声明独立`prompt_output_template`，并由该Template唯一拥有模型专属的最终Prompt正文和参数策略。GPT Image固定使用`templates/24_gpt_image_asset_prompt.md`，Midjourney固定使用`templates/14_midjourney_asset_prompt.md`。未来已验证图像模型若没有自身Adapter与独立最终提示词模板，不得进入模型选择或适配路径，也不得复用现有图像或任一视频模板。模型中立自然语言Prompt仅是未适配外部服务的安全回退，不构成模型Adapter。

---

## Authority Matrix

| Layer | Owns | Must Not Own |
|---|---|---|
| SKILL | 身份、版本、系统角色、主Pipeline、STATE总览、全局优先级、Activation/Reload入口、Workflow路由、外部索引 | 详细行为规则、阶段算法、完整状态Schema、最终输出Schema |
| Config | 运行默认值、资源索引、能力开关 | Pipeline行为、完成门槛、专业方法、最终输出Schema |
| Rules | 行为边界、禁止项、优先级、连续性约束 | 阶段内容生成、最终排版 |
| Workflows | 阶段转换、执行步骤、路由、完成门槛 | 与Template竞争的最终Schema |
| Knowledge | 专业判断、设计方法、内部分析维度 | STATE、项目进度、最终字段 |
| Templates | 对应阶段的字段、顺序、编号与排版 | Pipeline路由、专业判断 |
| References | 状态、项目空间、资产锁与模块接口合同 | 阶段交付格式、专业生成算法 |
| Project Files | 单项目状态、已确认事实、生产交付物；Portable仅持有最小路由镜像 | 通用Skill规则、绕过State Source优先级或静默合并不同Project ID |
| Validators | 可确定的结构、不变量与引用检查 | 审美、剧情质量与导演判断 |

---

## Required Contract For Every New Module

新增模块必须明确：

1. Module Name与Module Type。
2. 触发条件与不触发条件。
3. 所属STATE或辅助位置。
4. Required Inputs及其唯一来源。
5. Output及其唯一拥有者。
6. 允许读取和允许写入的项目路径。
7. 下游消费者。
8. 禁止修改的上游事实。
9. 与其他模块发生冲突时的返回路由。
10. 可由Validator确定性检查的不变量。

缺少上述合同的模块不得接入Workflow Map。

---

## Stable Interface Rules

### Global Runtime Rule Owners

- Runtime Reload / Workflow Re-entry / Legacy Project Recovery Integrity、Skill Definition Source、Work escalation与Legacy Intent Backfill路由：`rules/runtime_reload.md`
- State Source：`rules/state_source.md`
- Chat Compatibility：`rules/chat_compatibility.md`
- Progression：`rules/progression_rules.md`
- Activation：`rules/activation_rules.md`
- 自动推进策略与FAST资格/Hard Stop：`rules/automation_mode.md`
- Completion Gate：`rules/completion_gate.md`
- Compatibility Mapping：`rules/compatibility_mapping.md`
- Resource Loading：`rules/resource_loading.md`
- Canonical Portable State Schema：`references/project_state_contract.md`
- Skill Update Self-Check / Change Safety Checklist：`references/maintenance_self_check.md`（判据真源：`references/maintenance_self_check_protocol.md`）

其他模块只能引用这些所有者，不得在`SKILL.md`、`config.md`、References、Knowledge、Templates、兼容入口或各Workflow中维护竞争副本。`SKILL.md`可保留激活/重载入口和路由索引，但不得复制完整运行协议。

#### Runtime Recovery Rule Ownership Protection

- Runtime recovery authority只能由`rules/runtime_reload.md`定义；`workflows/18_project_resume_workflow.md`只消费其恢复决定并执行Checkpoint / Retry / Ledger记录。
- STATE Workflow、Screenwriter Module、Director Module、Knowledge与Template不得自行覆盖或重新定义Skill Definition Source、State Source priority、Reload Claim Gate、Work escalation、Legacy Intent Backfill触发或恢复顺序。
- `rules/state_source.md`继续独占Project State Source priority；runtime owner只能调用并记录选定结果，不得维护竞争副本。
- `USER_GUIDE.md`只能说明用户如何调用及可见行为，不是runtime authority，也不得成为恢复、source resolution或Work routing的规范来源。

### Production Knowledge Rule Owners

- Screenwriter Module / Writer Intelligence Layer、WRITER INTENT PACKET、原创故事开发、Writer Diagnosis、Writer → Director Handoff与Directable Screenplay QA：`knowledge/screenplay_development.md`
- Project / Scene / Shot / Clip四层DIRECTOR INTENT PACKET、Director Thinking从STATE-00/01到Scene / Shot / Clip / Prompt / Editing / Review的连续性合同，以及Task Dominance Router：`knowledge/director_decision_layer.md`
- Camera Language Module、Composition / Movement / Lens-Distance / Shot Rhythm四项核心能力和Script→Scene→Shot→Clip→Prompt→Editing→Review映射：`knowledge/camera_language/index.md`；逐Shot固定决策顺序由`knowledge/camera_language/shot_language_router.md`拥有
- Scene Spatial Snapshot、Spatial Blocking Decision、camera safe side与合法越轴空间合同：`knowledge/spatial_blocking_layer.md`
- Visual Blocking Risk Pre-Assessment、Before-Single-Clip-Prompt Gate、Sketch Validation、Visual Anchor State / Blocking Signature与KEEP / REPLACE / RETIRE / CREATE：`knowledge/clip_preflight_check.md`
- Performance Progression Engine、PL1 / PL2 / PL3载体负荷与微表情基础：`knowledge/performance/micro_expression.md`；更细的刺激—评估—控制/泄漏过程由`knowledge/performance/emotion_dynamics.md`拥有
- Action Execution Level A1 / A2 / A3与通用Kinetic Chain：`knowledge/action_previs.md`
- 动作构图模式：`knowledge/camera_language/director_patterns/action_composition.md`；不得复制Action PREVIS动力链
- STATE-08 Field Ownership、State Once、Style / Delta / Negative / Prompt Compression：`knowledge/prompt_compilation/state08_projection.md`；十类Prompt Pollution定义由`rules/03_prompt_rules.md`拥有

Workflow只负责触发、路由、执行顺序和Completion Gate；Quality只检查这些所有者产生的不变量；Template不复制内部算法。

### Screenwriter Module Contract

Module Type：persistent cross-stage Writer Intelligence Layer；不创建新主STATE、用户问卷、Portable State字段或第二套编剧系统。

Owner：`knowledge/screenplay_development.md`。`knowledge/screenwriting_optimization.md`、`knowledge/script_adaptation.md`与适用genre adapter仅为受控子模块，不得竞争owner。

传递链：`STATE-00 Writer Foundation → STATE-01 Production-Locked Directable Screenplay + WRITER INTENT PACKET → STATE-02/03 Narrative Function → STATE-04 Story / Motif Obligations → STATE-05 Writer Beat / Scene Value Projection → STATE-06 Shot Traceability → STATE-07 Writer Beat Integrity → STATE-08 Writer Intent Preservation → Editing Writer Rhythm Protection → STATE-09 Story Review`。

Authority：Information Architecture、Character Intent / Subtext、关键因果、Writer Beat、Setup / Payoff与Character / Relationship Arc属于Writer；Information Presentation、Performance Direction、Blocking、Mise-en-scène、Composition、Camera Language与Rhythm Presentation属于Director。Writer Beat不等于Shot，Writer不得规定焦段、机位、运镜或Shot Count。

Packet只作内部Source data，按复杂度最小充分维护，不整体展示给用户，也不新增Template字段。下游发现Writer事实冲突返回STATE-01/05；Director如需改变已锁定因果、动机、信息时机或Setup / Payoff义务，必须进入REDIRECT / rewrite反馈链。

### Director Module Contract

Module Type：persistent cross-stage decision layer；不创建新主STATE、用户问卷、Portable State字段或第二套导演系统。

Owner：`knowledge/director_decision_layer.md`。Camera Language核心子能力owner：`knowledge/camera_language/index.md`。STATE-08 Director-to-Prompt Translation owner：`knowledge/prompt_compilation/state08_projection.md`。

传递链：`Writer → Director Handoff → STATE-00/01 Director Baseline / Scene Director Intent → STATE-04 Visual Dramaturgy → STATE-05 Scene Camera Strategy → STATE-06 Director Decision Notes / Camera Language Decision → STATE-07 Dramatic Execution Unit → STATE-08 Director Intent Preservation + Model Translation → Editing / STATE-09 Director's Cut Review`。

不变量：Director Intent先于Knowledge选择；Camera choice是Shot Purpose与Audience Attention的后果；Camera Movement有Trigger / Stop；Packet保持内部；最终Seedance Schema不变；Voice仍opt-in；Spatial Blocking、Pose Hierarchy、Relationship Topology、Delta Blocking、Action PREVIS、Accepted Take Canon、Shot-State Memory、REF-SKETCH与REF-TAIL继续由原owner负责。STATE-04的`Aesthetic Decision Lock`与其可选`Look Frame`由Director层拥有：Look Frame使用`templates/25_look_frame_prompt.md`，属非生产视觉材料，只服务四维度的取舍判断，不登记工件、不写入项目状态、不进入任何下游，也不得作为STATE-08参考资产。

### Additive By Default

优先增加新的辅助信息，不删除或重新解释已有字段。

### Model Execution Lock And Seedance 2.5 Profile Contract

Module Name：`Model Execution Lock` + `Seedance 2.5 Model Profile`。

Module Type：STATE-06完成后的唯一内部Gate与STATE-07/08共用的模型知识Profile；不创建主STATE、项目事实或STATE-08最终字段。

Owner与触发：`workflows/02_script_analysis_workflow.md`的`Production Setup Gate`在Script `Production-Locked`后拥有项目图像默认项、图像交付形态、视频模型偏好与`Project Style Baseline`的单次确认；`modules/model-selection.md`在STATE-06后拥有按Clip能力复核、Adapter路由与不兼容返回路径；`knowledge/11_seedance_adapter.md`拥有共通Seedance翻译和唯一Model Template Router；`knowledge/prompt_compilation/seedance_20_compilation.md`与`seedance_25_compilation.md`各自拥有对应模型的内部编译语义，后者连同`knowledge/seedance_25_profile.md`消费已证实的2.5能力上限、执行模式及降级策略；`references/project_state_contract.md`拥有状态镜像；`templates/20_clip_plan.md`拥有Confirmed Clip Production Plan中的内部执行Profile字段。已确认偏好且覆盖当前Clip时不得重复询问；不兼容时只提出最小的模型/执行模式替代选择。

Writeback与变更：所选Target Model、唯一匹配的Model Compilation Template、Execution Profile、Execution Mode、Long-duration Route与Effective Gateway Limits写入Project State和Confirmed Clip Production Plan。Seedance 2.5的16—30秒由用户目标时长自动触发内部严格预检，不是用户需额外选择的Execution Mode；用户可在模型窗口内选择时长，未知网关状态不得预先压缩为15秒，实际平台拒绝才作为STATE-07最小调整的触发。用户在Clip Plan确认前切换模型时，只使受影响的STATE-07 / STATE-08执行产物失效并重跑；Production-Locked Script、Confirmed Assets、Scene Breakdown与Detailed Shot Design保持已确认状态。最终STATE-08 Prompt不得新增模型、Compiler、模式、预算或时间轴字段。

Consumers与不变量：STATE-07按Lock选择对应Profile后完成Clip整合；STATE-08只消费已确认Plan并用既有Template编译。模型上限定义可选择时长窗口；外部平台观察信息不作为时长预检。`REF-TAIL` A/B/C、Canonical Authority、双确认、最小充分参考、Voice opt-in和视频Prompt永久无BGM不因Profile改变。Validator检查Lock/Plan/State一致性、模式合法性、2.0默认回归、2.5模式与条件性时间控制；回归场景由`references/regression_scenarios.md`拥有。

如果必须修改已有Template：

只修改该Template拥有的阶段输出，不把字段传播到无关Template。

### One Owner Per Output

每种最终交付结构只能有一个Template拥有者。

STATE-08最终Prompt按Selected Model由唯一Template拥有：

- `templates/10_video_prompt.md`：Seedance 2.0 Prompt；
- `templates/12_seedance_25_video_prompt.md`：Seedance 2.5多模态时间线Prompt；
- `templates/13_minimax_h3_video_prompt.md`：MiniMax H3三段式Prompt。

二者不得交叉复制字段或共同拥有同一模型的输出Schema。

### Upstream Facts Are Read-only Downstream

下游可以补充执行细节，但不能静默修改：剧情事实、资产身份、已确认Visual Direction、Scene目的、镜头目的与边界合同。

发现冲突时返回事实拥有者修正。

### ID Namespace Isolation

不同实体使用不同命名空间：

- CHAR：角色
- ENV：环境
- PROP：道具
- FX：效果
- SCENE：场景
- SEQ：长序列
- BEAT：叙事节拍
- COV：覆盖需求
- UNIT：生成单元
- SHOT：正式镜头
- CLIP：STATE-07基于Confirmed Detailed Shot Design生产、供视频模型一次生成的模型适用执行单元：Seedance 2.0为4—15秒；Seedance 2.5为4—30秒，16—30秒须严格预检PASS且网关确认允许

辅助模块不得占用其他模块的ID命名空间。

### Project Isolation

Work/Codex中的完整项目交付物必须写入Active Project Root；普通Chat不可访问该Root时只在Portable State维护状态摘要与对话中已确认的交付内容。

模块通用知识和Template保留在Skill根目录。

### No Hidden State

辅助模块不得创建新的主STATE。

它可以在当前STATE的Completed Tasks、Pending Tasks或Next Action中记录执行结果。

---

## Skill Maintenance QA

本文件只拥有模块接口合同。Skill维护QA已迁出，其执行入口与必读清单为`references/maintenance_self_check.md`，判据真源为`references/maintenance_self_check_protocol.md`。

模块接口合同发生变化时，仍须按该入口执行完整Skill Update Self-Check / Change Safety Checklist。
