# SD Film Module Contracts

## Purpose

本文件定义新增或修改模块与现有生产系统之间的接口合同，并拥有Skill更新后的维护QA。

目标是允许SD Film持续扩展，同时避免：

- 重复职责
- 重复Schema
- 非法STATE
- 上游事实被下游覆盖
- 项目数据写入Skill根目录
- 一个模块直接修改另一个模块拥有的输出

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
- Completion Gate：`rules/completion_gate.md`
- Compatibility Mapping：`rules/compatibility_mapping.md`
- Resource Loading：`rules/resource_loading.md`
- Canonical Portable State Schema：`references/project_state_contract.md`
- Skill Update Self-Check：本文件的`Skill Update Self-Check / Change Safety Checklist`

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

不变量：Director Intent先于Knowledge选择；Camera choice是Shot Purpose与Audience Attention的后果；Camera Movement有Trigger / Stop；Packet保持内部；最终Seedance Schema不变；Voice仍opt-in；Spatial Blocking、Pose Hierarchy、Relationship Topology、Delta Blocking、Action PREVIS、Accepted Take Canon、Shot-State Memory、REF-SKETCH与REF-TAIL继续由原owner负责。

### Additive By Default

优先增加新的辅助信息，不删除或重新解释已有字段。

### Model Execution Lock And Seedance 2.5 Profile Contract

Module Name：`Model Execution Lock` + `Seedance 2.5 Model Profile`。

Module Type：STATE-06完成后的唯一内部Gate与STATE-07/08共用的模型知识Profile；不创建主STATE、项目事实或STATE-08最终字段。

Owner与触发：`workflows/10_clip_production_workflow.md`拥有Lock的询问、写回、切换与返回路由；`knowledge/11_seedance_adapter.md`拥有共通Seedance翻译；`knowledge/seedance_25_profile.md`拥有已证实的2.5能力上限、执行模式及降级策略；`references/project_state_contract.md`拥有状态镜像；`templates/20_clip_plan.md`拥有Confirmed Clip Production Plan中的内部执行Profile字段。STATE-06完成且当前生成批次未锁定目标模型时，Lock必须在Clip候选整合前只询问一次`Seedance 2.0`或`Seedance 2.5`。已锁定时不得重复询问。

Writeback与变更：所选Target Model、Execution Profile、Execution Mode与Effective Gateway Limits写入Project State和Confirmed Clip Production Plan。用户在Clip Plan确认前切换模型时，只使受影响的STATE-07 / STATE-08执行产物失效并重跑；Production-Locked Script、Confirmed Assets、Scene Breakdown与Detailed Shot Design保持已确认状态。最终STATE-08 Prompt不得新增模型、模式、预算或时间轴字段。

Consumers与不变量：STATE-07按Lock选择对应Profile后完成Clip整合；STATE-08只消费已确认Plan并用既有Template编译。2.5能力上限不覆盖实际API/网关限制，Effective Limit取可确认网关限制与Profile上限中的较小值。`REF-TAIL` A/B/C、Canonical Authority、双确认、最小充分参考、Voice opt-in和视频Prompt永久无BGM不因Profile改变。Validator检查Lock/Plan/State一致性、模式合法性、2.0默认回归、2.5模式与条件性时间控制；回归场景由`references/regression_scenarios.md`拥有。

如果必须修改已有Template：

只修改该Template拥有的阶段输出，不把字段传播到无关Template。

### One Owner Per Output

每种最终交付结构只能有一个Template拥有者。

STATE-08最终Seedance Prompt继续只由：

templates/10_video_prompt.md

拥有。

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
- CLIP：STATE-07基于Confirmed Detailed Shot Design生产、供视频模型一次生成的4—15秒执行单元

辅助模块不得占用其他模块的ID命名空间。

### Project Isolation

Work/Codex中的完整项目交付物必须写入Active Project Root；普通Chat不可访问该Root时只在Portable State维护状态摘要与对话中已确认的交付内容。

模块通用知识和Template保留在Skill根目录。

### No Hidden State

辅助模块不得创建新的主STATE。

它可以在当前STATE的Completed Tasks、Pending Tasks或Next Action中记录执行结果。

---

## Screenwriter Module, Adaptation And Analysis Gate Contract

Module Name：`Screenwriter Module / Writer Intelligence Layer + Script Adaptation + Script Optimization Gate`。

Module Type：STATE-01 Script Analysis内部双入口Workflow Gate、原创剧本开发Knowledge、通用改编Knowledge、条件性短剧Adapter与导演化/优化Knowledge，不创建新主STATE。

触发：所有输入先路由。`Creation Brief`是只有创意、题材、品牌需求、人物/世界观设定、情绪/场景或明确剧本创作请求，但没有可逐段诊断的既有剧本/来源叙事正文；它直接触发`Idea / Brief → Screenwriter-led Story Development → Writer → Director Handoff → Directorial Interpretation → Directable Screenplay QA → Production Script Proposal → User Confirmation`。`Existing Script / Material`再分类为A已是制作剧本、B粗略剧本/初稿、C具有既有内容但尚非制作剧本的小说、故事梗概、品牌文案、历史事件、影视桥段或长篇素材；除No Revision / Final Script例外外，先执行`Script Input → Writer Diagnosis → Optimization Opportunity Report → User Decision Gate`。只有C类在报告Adaptation Need且用户明确授权改编/优化后触发Script Adaptation；A/B也必须在明确授权后才进入Script Optimization。

不触发内容改写：用户明确说“不要改剧本”“严格按这个版本制作”“已定稿”或同义表达时，跳过Optimization Opportunity Report、Script Adaptation、短剧Adapter、Screenwriting Optimization与Directorial Interpretation，但仍完整执行原有Script Analysis并按授权锁定。用户在Opportunity Report后拒绝优化/改编时，也跳过全部内容改写，原始版本完成分析后直接Production-Lock。

所属位置：`STATE-01 Script Analysis`内部。Creation Brief的创作请求本身授权生成Proposal，不先输出Optimization Opportunity Report，也不要求用户先在普通Chat完成剧本；只在真正关键缺失时最小澄清。Existing Script / Material默认入口固定为`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`并在没有改写授权时停止。报告只写问题、影响与方向，至少检查开场钩子、核心冲突进入时机、信息重复、台词效率、动作可视化、人物记忆点、节奏、高潮力度、情绪价值、结尾Hook、时长适配、场景/人物复杂度；结论只使用A无明显优化必要、B有轻度优化空间、C有明显结构问题。当前请求已明确“分析并优化 / 直接优化 / 直接改写 / 按指定范围优化”时，报告后不重复询问改写授权；C类继续`Adaptation Target Detection → Script Adaptation → Adaptation Draft → Screenwriting Optimization → Directorial Interpretation → Production Script Proposal → User Confirmation`，A/B从Screenwriting Optimization开始。所有未确认提案不得进入STATE-02。

Adaptation Target Detection：只有目标为短剧、竖屏剧情或1—3分钟剧情视频时加载`knowledge/adaptation/short_form_drama_adapter.md`；其他类型记录Not Applicable，不强制套用短剧规则。

Adaptation Intensity：只允许LEVEL 1 Light Adaptation、LEVEL 2 Structural Adaptation、LEVEL 3 Free Adaptation，并选择最低足够等级。用户明确“基本不要改剧情”时只能LEVEL 1；不可静默升级。

Required Inputs及唯一来源：用户Idea / Brief或原始故事文本、Project Bible中的已确认项目事实、目标形式/时长/平台/受众、用户明确的创作/改编/优化范围与锁定要求。世界观、角色身份、核心创意、主题、名场面、关键设定与品牌要求只由用户或已确认项目事实拥有。

Output拥有者：`templates/02_script_analysis_prompt.md`独占STATE-01用户可见字段、顺序与排版；`workflows/02_script_analysis_workflow.md`拥有入口识别、分类、目标检测、路由、确认门槛与状态转换；`knowledge/screenplay_development.md`是唯一Screenwriter owner，拥有WRITER INTENT PACKET、原创故事开发、Writer Diagnosis、Writer → Director Handoff与Directable Screenplay QA；`knowledge/script_adaptation.md`拥有通用六层改编方法；`knowledge/adaptation/short_form_drama_adapter.md`只拥有适用短剧规则；`knowledge/screenwriting_optimization.md`与`knowledge/directorial_interpretation.md`只拥有各自专业子方法。

允许读取：Selected State Source、Active Project Root中的project_bible.md、用户Idea / Brief、剧本/Source Material/设定与已确认约束。允许写入：Active Project Root的STATE-01 Screenplay / Script Analysis Artifact、适用的Optimization Opportunity Report、获得合法授权后的Adaptation Draft和Production Script Proposal，以及随确认版本传递的轻量Scene Director Intent source data；并写Selected State Source中的Script Status / Pending Decision / Checkpoint。不得写入Skill根目录项目兼容入口。

Script Status继续只允许`Source Material / Adaptation Draft / Optimized Proposal / Production-Locked`，不为原创分支新增状态。Creation Brief生成前为Source Material，Proposal输出后为Optimized Proposal，确认后为Production-Locked；Existing的Opportunity Report与User Decision Gate期间保持Source Material，C类获准路径为`Source Material → Adaptation Draft → Optimized Proposal → Production-Locked`，A/B获准路径跳过Adaptation Draft，拒绝优化路径为`Source Material → Production-Locked`。只有Production-Locked允许STATE-01 COMPLETE。

下游消费者：STATE-02 Asset Discovery及所有后续剧情事实消费者只能读取Production-Locked Script；Adaptation Draft与Optimized Proposal都不是已确认事实。

禁止修改：用户未授权范围、世界观、角色身份、品牌要求、核心创意、关键设定、主Pipeline、资产确认闭环、Spatial Blocking Layer、Director Decision Layer、Knowledge Reflection、Clip-centric逻辑与STATE-08 Seedance Schema。

与Director Decision Layer边界：Screenwriter拥有故事/人物逻辑、Information Architecture、Subtext、Writer Beat与Setup / Payoff，只把Character Performance Intent交给Director，不创建SCENE、SHOT、CLIP、焦段、机位、运镜或Director Decision Notes。Director拥有Information Presentation、Performance Direction、Blocking、Composition、Camera Language与Rhythm Presentation，不擅自改变Writer锁定事实。STATE-05投影两层意图，STATE-06决定Scene / Shot Group的视听执行方向；需要改动故事时走REDIRECT / rewrite反馈链。

冲突路由：Creation Brief只有在缺失项会实质改变架构或造成品牌/事实风险时请求最小决定；Existing的锁定事实、目标形式、Adaptation Intensity或修改范围不明确时保持STATE-01 IN_PROGRESS并请求用户决定。单独“继续 / 下一步 / 好的”既不构成Existing优化授权，也不构成Proposal确认；当前请求已明确“直接优化 / 直接改写”时不重复询问同一授权。用户要求修订Proposal时保持Script Development并只修改受影响范围；下游发现剧情事实冲突返回STATE-01，不在资产、镜头或Prompt阶段静默调和。

Validator可检查的不变量：Creation / Existing双入口与互斥判定存在；Creation不要求先提供完整剧本、不输出Opportunity Report、具备十项Directable Screenplay QA且不提前写Shot Design；Existing固定诊断入口、十二项报告维度与A/B/C三档存在；报告前后没有未授权改写，明确“直接优化”不重复询问授权；四种Script Status值合法；Adaptation Draft或Optimized Proposal不能与STATE-01 COMPLETE或STATE-02+并存；C类只有明确授权后经过通用改编；短剧Adapter只按Target Detection加载；B类不被强制改编；No-Revision分支跳过报告和改写但仍执行Script Analysis；拒绝优化锁定原稿；所有Proposal后存在第二次确认；五份Knowledge与所有显式引用存在。

---

## AUDIO / SEED-AUDIO Voice Asset Module Contract

Module Name：`AUDIO / SEED-AUDIO Voice Asset`。

Module Type：显式调用的Optional/Auxiliary Workflow + Knowledge + 独立Template，不创建新主STATE，不属于STATE-03 Character Asset Workflow的默认步骤。

触发：只有用户当前请求明确要求创建、设计、生成、修改或更新“音色提示词、音色制作、角色声音、Seed Audio / SeedAudio、配音音色、声音资产 / Voice Asset、Voice Profile、角色音色样本Prompt或Audio Reference”时触发。必须记录可核对的`Explicit Trigger Evidence`。

不触发：角色仅仅存在对白、旁白、画外音、通话、呼喊或潜在对白；普通视频制作、角色分析、Character Asset、Detailed Shot Design、Clip Production、STATE-08视频/Seedance Prompt；“继续视频制作”“输出Clip B视频提示词”“下一个Clip”“下一步”“继续”“下一个”；背景音乐、环境声、Foley、音效、歌曲、正式整段配音或多人音频场景。下游缺少Voice Profile也不得自动触发。

所属位置：不绑定主STATE的独立辅助位置。项目存在时可把明确请求的结果绑定到同一CHAR-ID与Version；项目不存在时可直接根据用户当前提供的角色事实交付，不强制初始化影视Pipeline。

Required Inputs及唯一来源：角色年龄、性别、身份、性格、对白功能、情绪基调与可观察说话行为来自用户当前明确输入、已确认Script Analysis、Project Bible或Active CHAR Version；不得从外貌、导演标签、题材或竹雀示例反推。必要事实不足时保持Pending或请求最小必要输入。

Router与Output拥有者：`workflows/audio_router.md`独占显式触发判定与`AUDIO / ORIGINAL WORKFLOW`路由；`workflows/20_seed_audio_voice_asset_workflow.md`只在Positive Route后拥有执行、完成与返回调用前Checkpoint；`templates/21_seed_audio_voice_asset.md`独占Voice Profile、Seed Audio兼容Prompt与Reference Audio Handoff的最终字段、顺序和排版；`knowledge/sound_language/voice_generation.md`只拥有官方能力边界、声音身份推导、Dialogue Performance分离、按需字段选择与Reference Audio方法。`templates/04_character_asset_prompt.md`与`templates/10_video_prompt.md`不得替代本模块Schema。

允许读取：用户当前输入、Active Project Root中的`project_bible.md`、`asset_registry.md`、相关已确认剧本/分析交付物与角色对白证据。允许写入：独立交付物，以及用户明确要求保存/更新时同一CHAR-ID与Version中的Voice Profile、Voice Sample Prompt及经确认的Voice Audio Reference元数据；不创建独立视觉Asset ID，不把音频自动登记为视觉Canonical Reference。

下游消费者：配音指导、跨集声音一致性与Review可消费已经存在且适用的Confirmed Voice Profile / Voice Reference；STATE-06/07可把它们保留为内部Source State。STATE-08默认不消费或序列化声音身份，只有用户明确要求把声音控制写进当前视频模型Prompt时才最小投影；任何下游消费者都不得因资产缺失而反向启动本模块。

下游交接不变量：`Source Carries State, Prompt Carries Delta`。Confirmed Voice Audio Reference或Voice Profile由声音资源/登记记录携带身份，STATE-08默认不写`音色特征：`、不写资产状态、不作文字回退。只有用户明确要求把声音控制写进当前视频模型Prompt时，才在当前Clip按最小必要Delta引用；两者都不存在时仍直接继续视频流程，不输出任何缺失声明，也不自动生成音色资产。

禁止修改：角色身份、剧本台词事实、Active Version、视觉资产、主Pipeline、STATE-08 Seedance Schema以及未经用户或项目事实确认的口音、方言或病理声音特征。

冲突路由：角色事实冲突返回事实拥有者；台词字数或逐镜表演容量冲突返回STATE-06；音频授权、来源或候选未确认时停在本模块Pending/Candidate，不登记为Confirmed；Router返回Original Workflow时立即返回原路由，不加载声音资产Workflow或创建Not Applicable记录。

Validator可检查的不变量：所有声音身份Intent先进入唯一`workflows/audio_router.md`；只有Positive Route加载声音资产Workflow；具有显式触发证据；输出明确标记为SD Film为Seed Audio组织的兼容模板而非官方唯一字段格式；描述speaker并分离稳定Voice Identity与当前Dialogue Performance；只输出适用字段；Reference Audio有授权依据；无无意义精密参数、否定词堆砌或视觉Prompt复制；A/B/C路由样例分别为触发/不触发/不触发。

项目专属Voice Bible不得成为全局默认人设、音色模板或试听文本。

---

## MUSIC / SEED-MUSIC Score Module Contract

Module Name：`MUSIC / SEED-MUSIC Score`。

Module Type：用户显式调用的Optional/Auxiliary Workflow + 独立Knowledge目录 + 独立Template，不创建新主STATE，不是STATE-08、STATE-09或Editing的默认步骤。

触发：只有用户当前请求明确要求创建、规划、设计、生成、修改或输出配乐规划、Music Spotting、Cue Sheet、主题动机、场景 / 转场音乐、SeedMusic / Seed-Music提示词、纯音乐提示词、歌词歌曲或已有音乐Cue的续写 / 风格迁移时触发。必须记录可核对的`Explicit Trigger Evidence`，并先经过`workflows/music_router.md`。

不触发：普通视频、Shot、Clip、Storyboard、Seedance视频Prompt、Review、Editing、项目推进命令；项目资料、题材、情绪或导演参考中出现音乐词汇；缺少配乐计划；用户仅声明视频不生成BGM；对白、音效、Foley、剧情内声源、音色或配音请求。Router返回Original Workflow时不得加载本模块依赖或创建Music Artifact。

所属位置：不绑定主STATE的独立辅助位置。项目存在时绑定当前Project ID和已确认Scene / Sequence / Shot / Clip Artifact；项目不存在时可根据用户当前提供且足够的时间线直接交付。完成后返回调用前Checkpoint，不自动推进主Pipeline。

Required Inputs及唯一来源：用户当前音乐目标、禁用项与明确模式；用户或Production-Locked Script拥有的剧情事实；Confirmed Scene / Sequence / Detailed Shot Design / Clip Production Plan拥有的顺序、边界和时长；用户提供且已授权的Audio Reference或乐谱。模块不得修改这些上游事实。时间线未锁定时只可输出`PROVISIONAL` Spotting，不得伪造精确秒点。

Router与Output拥有者：`workflows/music_router.md`独占显式触发与`ROUTE: MUSIC / SEED-MUSIC Score` / `ROUTE: ORIGINAL WORKFLOW`路由；`workflows/21_seed_music_score_workflow.md`拥有Spotting、Music Bible、Cue架构、SeedMusic编译、完成门槛与返回路由；`knowledge/music_score/`拥有专业判断方法；`templates/22_seed_music_score.md`独占Music Package最终字段、顺序和排版。`templates/10_video_prompt.md`、`templates/08_shot_design_prompt.md`、`knowledge/sound_language/`与Editing Template不得替代本模块Schema。

允许读取：用户当前输入、Selected State Source、Active Project Root中相关已确认剧本、Scene、Sequence、Detailed Shot Design、Clip Plan、生成结果、Review证据及经授权音乐参考。允许写入：独立Music Package、Spotting Map、Music Bible、Cue Sheet与SeedMusic Prompt Artifact；如项目运行时支持，可在Artifact Registry登记，但不得写入Skill根目录项目兼容入口，不得修改视频Prompt Artifact。

下游消费者：用户的独立后期配乐制作、音乐生成与剪辑混音流程；STATE-09可在用户明确提交Music Artifact参与复核时读取它，但不得因缺失而自动启动本模块。STATE-08永远不是本模块输出消费者。

默认模式：Positive Route默认`INSTRUMENTAL`，即纯音乐。Lyrics、演唱、说唱、合唱、哼唱、吟唱、Vocalise、Spoken Word或其他人声纹理只有用户当前另行明确要求时才允许。普通剧情对白不得转成歌词授权。

专业Spotting不变量：激活后系统必须审阅完整请求范围，专业决定音乐进入、退出、Carry-over与`SILENCE / PRODUCTION SOUND ONLY`，不得要求用户逐Clip指定，也不得把“全片配乐”解释为持续全片铺音乐。每个交付至少在请求范围内或相邻Cue边界明确一处留白；留白条目保留同期声音承载说明，但不生成SeedMusic Prompt。

SeedMusic不变量：默认纯音乐执行块只包含`style`与`structure`；省略Lyrics输入；`structure`使用官方示例的`[Verse] / [Chorus] / [Bridge] / [Outro]`绝对秒点，首个秒点为`0s`、后续严格递增。Cue标题与`Related Clip(s)`位于执行块外，只作为追踪元数据；不得把CLIP-ID或生产说明写入`style` / `structure`。

视频隔离不变量：STATE-08任何Clip均永久执行固定背景音乐禁令。即使用户要求配乐，也只能拆分为独立Music Package；不得对明确Clip、批量Clip或任何模型开放视频Prompt音乐例外。

禁止修改：剧情、台词、Clip顺序和时长、镜头设计、同期声音设计、视觉资产、主Pipeline、STATE-08 Seedance Schema与用户未授权的人声 / 歌词模式。不得模仿特定在世艺术家或复刻受版权保护歌曲，应转译为高层音乐特征。

冲突路由：剧情或时间线冲突返回事实拥有者；时长未确认标记`PROVISIONAL`；用户要求把配乐写进视频Prompt时强制拆分路由；Audio Reference缺失或未授权时停用Reference模式；本模块与AUDIO / SEED-AUDIO Voice Asset分别路由、分别使用Template。

Validator可检查的不变量：Positive Route和显式触发证据存在；默认Generation Mode为INSTRUMENTAL；Spotting Map覆盖请求范围且至少允许Music与Designed Silence两类专业判断；Cue ID唯一；已知Clip使用`Related Clip(s)`；默认Prompt含纯音乐与人声排除；执行块存在且只有`style + structure`；结构从`0s`开始并严格递增；留白行没有Prompt；STATE-08固定禁令存在且无任何背景音乐例外参数。

---

## STATE-03 Visual Asset Production Contract

Module Type：STATE-03 Character / Environment / Prop主资产Workflow与正式FX辅助Workflow的共享生产合同，不创建新主STATE。

触发：任何新建或更新的正式视觉资产需要生成或接收角色、环境、道具或FX参考图片。

不触发：纯文字Voice Profile、Seed Audio Voice Sample Prompt、非视觉Audio Reference，以及Asset Discovery中明确标记为Inline Effect且无需正式视觉资产的效果。

所属位置：STATE-03 Asset Development内部，固定顺序为`Asset Design → Image Prompt Generation → 用户确认提示词 → Image Generation → 用户确认图片 → Asset Registry`。

Two-Tier执行：STATE-02为每个CHAR、ENV、PROP拥有Asset Tiering Decision。Core满足主角/固定角色、跨场景或跨Clip复用、强剧情/角色/品牌识别、高一致性、关键场景或剧情关键道具之一，并在STATE-03独立制作；Support为一次性配角/群演、群体背景角色、同类家具与环境小物、氛围装饰、低频道具等，按同一资产类型与相近用途进入Support Reference Board。该分层是STATE-02/03内部决策，不创建新STATE，不替代Primary / Secondary / Background优先级，也不改变正式FX路由。

Support Board建议4—9个对象，必须具有稳定Board ID与逐项Item ID，统一风格但明确轮廓、服饰/材质、颜色、比例和功能差异；不得跨CHAR / ENV / PROP混板，不得逐项制作完整三视图或独立资产套图。下游引用使用`<Board Name> / <Board ID> / <Item ID>`。

Required Inputs及唯一来源：资产身份与剧情功能来自STATE-01/02、Project Bible、Active Asset Version和用户明确确认；Visual Direction只能提供项目级风格约束，不得改写资产身份。

Output拥有者：Character、Environment、Prop与FX的最终阶段字段分别由`templates/04_character_asset_prompt.md`、`templates/05_environment_asset_prompt.md`、`templates/06_prop_asset_prompt.md`与`templates/13_fx_asset_prompt.md`拥有；共享Rules与本合同只定义门槛和状态语义。

允许读取：Selected State Source、Active Project Root中的project_bible.md、asset_registry.md、Script/Asset Discovery交付物与当前资产依赖。允许写入：同一Asset ID和Version的Asset Tier、Board ID、Item ID、Image Prompts、Prompt Confirmation、Candidate References、Image Confirmation、Canonical References、Visual Production Status及其Prompt / Image / Confirmed状态投影；完整项目文件只写Active Project Root。

下游消费者：STATE-04 Visual Development、STATE-05 Scene Breakdown、STATE-06 Detailed Shot Design、STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation与Review。

不变量：`Visual Production Status`只使用`Prompt Draft`、`Prompt Confirmed`、`Image Generated`、`Asset Confirmed`；Prompt确认与图片确认独立；Prompt Draft不得调用图片生成；Image Generated只登记Candidate References；Asset Confirmed必须有图片批准依据，才可Active并登记Canonical References；工具不可用不把文字设定升级为confirmed asset。`Prompt Status / Image Status / Confirmed Status`必须与该生命周期严格映射；任何Core Asset、Support Board或Support Item在图片确认前都不得confirmed。Support必须有唯一Board ID / Item ID映射和Canonical Board Reference区域/标签对应关系。

禁止修改：主Pipeline、导演决策层、知识应用思考层、Clip-centric逻辑、STATE-08 Seedance Schema、已确认剧情事实和未获批准的Active Asset Version。

冲突路由：资产身份或设计冲突返回对应STATE-03 Asset Workflow；项目级风格冲突返回STATE-04；Prompt执行性问题留在当前资产Workflow；工具不可用保持STATE-03 IN_PROGRESS并等待外部图片或工具恢复。

Validator可检查的不变量：四个状态合法；Prompt Confirmed及以后具有Prompt Revision与Prompt Confirmation；Image Generated具有Candidate References但不为Active；Asset Confirmed具有Image Confirmation、Canonical References与Status Active；三个主资产Template均具有阶段化输出与双确认Checkpoint；CHAR / ENV / PROP均有Core或Support分层，Core的Board / Item为Not Applicable，Support的Board / Item映射唯一且不跨类型；三项状态投影与Visual Production Status一致。

---

## Skill Experience Module Contract

Module Name：`Skill Experience Module`。

Module Type：跨项目持久Knowledge层，以及Review / 失败复盘后的候选确认机制；不创建新主STATE。

Owner：`knowledge/skill_experience.md`；存储、确认、应用、项目迭代与失效边界由`references/skill_experience_contract.md`拥有。

触发：STATE-09 Review完成、REVISE / REBUILD返回、生成失败复盘，或用户明确要求总结/记录技能经验。

不触发：普通项目状态读取、单次Prompt润色、项目专属事实整理、未完成推理，以及用户未确认的自动Skill写入。

输入唯一来源：实际Review结果、Generation Attempts / Failure Pattern、用户明确反馈、重复验证案例与当前Skill规则；不得把单一项目事实直接当作跨项目经验。

输出：`Experience Candidate`可在Review / 复盘后自动提出，但必须保持`PENDING`直到用户明确确认；确认后写入Skill经验库并递增Skill版本。已确认经验在相关产出和项目迭代前按需读取，作为只读建议。

应用边界：经验只能投影到当前Template允许的语义，不能新增最终字段、覆盖用户指令、项目事实、Rules、Workflow、Template或既有Owner。项目迭代必须通过对应事实/设计Owner和用户确认，并按项目Revision规则落盘。

允许写入：Skill根目录的经验知识库；禁止写入Project Root、Project State、Portable State、项目兼容入口或任何已确认项目Artifact。

冲突路由：与硬规则、用户当前指令或已确认项目事实冲突时标记`CONFLICT / REVIEW`并暂停应用，返回对应Owner；不静默改写或删除历史证据。

Validator不变量：候选未确认不得入库；经验不占用现有实体ID命名空间；经验不出现在主Pipeline STATE列表；经验应用不绕过Completion Gate；每次经验入库触发完整Skill Update Self-Check。

## Sequence Module Contract

Module Type：STATE-05辅助Workflow。

触发：长故事、多Scene连续段、密集剧情、蒙太奇、多个生成单元、需要覆盖检查或续接计划。

不触发：单一简单Scene、单镜头明确、无需跨生成单元管理。

输入拥有者：Scene Breakdown、Project Bible、Asset Registry、Visual Direction。

输出拥有者：templates/14_sequence_plan.md。

项目输出路径：`<active-project-root>/sequences/`。

下游消费者：STATE-06 Detailed Shot Design、STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation、STATE-09 Review。

禁止：

- 创建正式SHOT ID
- 替代Scene Breakdown
- 决定最终Seedance字段
- 把内部生成单元时长写入STATE-08 Prompt
- 为提高覆盖度新增剧情事实

正式SHOT只能由STATE-06创建，并通过COV ID回填覆盖关系。

---

## Poster Design Module Contract

Module Type：STATE-04条件性辅助Workflow与Knowledge。

触发：用户明确请求电影海报、Key Art、One-sheet、先导/正式/角色海报、Poster Prompt或标题字设计。

不触发：普通视频Prompt、Storyboard、分镜、镜头设计、普通社交媒体封面；未请求时不得成为每个项目的默认步骤。

输入拥有者：STATE-01的影片事实与人物关系、STATE-03已确认资产、STATE-04 Visual Direction，以及用户或项目资料确认的投放渠道、准确文案、credits、logo和参考授权状态。

输出拥有者：`templates/15_poster_design_package.md`。

允许读取：Active Project Root中的`project_status.md`、`project_bible.md`、`asset_registry.md`及已确认资产文件。

允许写入：`<active-project-root>/poster_design/`与当前STATE的Completed Tasks / Pending Tasks记录。

下游消费者：海报生成、平面合成、宣传物料派生与Review；不得反向改写Shot Design或STATE-08。

不变量：

- 每张海报只有一个一级视觉母题
- 只有一个Primary Composition Model，Supporting Model不超过一个
- 画幅由投放渠道决定，不固定为9:16
- 精确片名、日期、credits与法务信息必须进入Exact Copy Ledger并使用可控、可编辑、已授权的文字层
- 分层职责至少区分base、type、composite、delivery与layout-spec
- 参考图按Composition / Palette / Lighting / Typography / Texture / Narrative Device之一分配主要角色，并记录必须重新设计的维度
- 未确认信息保持待确认，不虚构主创、片商、标识、电影节、奖项、媒体引语或发行事实

禁止：

- 复制参考海报的可识别人物关系、动作、场景骨架、标题位置、字形、标志性道具组合与完整配色
- 用图像模型的乱码或错字替代准确片名和法务信息
- 为了海报效果重新设计角色、环境、道具或FX资产
- 创建新的主STATE、海报专用资产ID命名空间或STATE-08最终字段

冲突时：剧情和关系返回STATE-01；资产身份返回STATE-03；项目级视觉体系返回STATE-04；准确文案和授权保持Pending并请求项目确认。

---

## Camera Composition Knowledge Contract

Module Type：STATE-06至STATE-08辅助Knowledge。

触发：镜头需要构图、视点、空间层次、人物关系、动作路线或氛围组织。

输入拥有者：Shot Purpose、Scene、已确认资产、Visual Development、Performance、FX与空间连续性。

输出拥有者：STATE-06由对应Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

禁止：

- 把图片“适配情节”当成剧情事实
- 用构图模式新增枪火、爆炸、人物关系或环境事件
- 与Camera Angle、Movement、Perspective、Lens、FX或Performance建立重复原子定义
- 创建新的最终Prompt字段

---

## Focal Length Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-09辅助Camera Knowledge。

触发：需要确定焦段倾向、摄影机距离、同景别透视、景深/对焦、边缘安全、长焦叠层或焦段连续性。

输入拥有者：Visual Direction、Shot Purpose、Shot Scale、Camera Position / Movement、Composition、Blocking、Lighting、Performance与空间连续性。

输出拥有者：STATE-04由Project Bible摄影方向拥有；STATE-06由Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部焦段模式只使用FLN-01至FLN-07，最终Prompt不得输出FLN编号
- 未确认画幅时，毫米数只作为全画幅等效倾向，不作为硬件事实
- 焦段选择必须与摄影机距离、景别、空间效果、对焦/景深和运动约束共同定义
- 透视由摄影机位置决定；虚化由多项变量共同决定；焦段不自动提升质感
- 焦段语义映射到现有Template字段，不创建Lens或Focal Length最终字段

禁止：

- 把焦段当作景别、情绪、透视、压缩、虚化或电影感的单一原因
- 为匹配附件示例新增人物、地点、动作、情绪或器材事实
- 与Camera Movement、Composition、Lighting、Performance或Optical Zoom重复定义
- 用随机焦段变化破坏脸部几何、背景尺度、眼线、轴线和连续性

冲突时：项目级焦段体系返回STATE-04；逐镜景别、机位、运动、对焦或动作容量返回STATE-06；资产或空间事实返回其拥有者。

---

## Camera Movement Combination Knowledge Contract

Module Type：STATE-06至STATE-08辅助Camera / Coverage Knowledge。

触发：镜头描述包含两种以上摄影机运动、多个景别/机位/视点、“镜头顺序”、一镜到底、动作Coverage或跨时空组合。

输入拥有者：Shot Purpose、Coverage Requirement、Camera原子、Blocking、Performance、Lens、FX、Sequence与Transition Boundary。

输出拥有者：STATE-06由Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。

不变量：

- 内部模式只使用CMG-01至CMG-16，最终Prompt不得输出CMG编号
- 先判定Single-Move、Low-Complexity Compound Path、Coverage Sequence或Transition / FX Sequence
- 每个正式SHOT默认只有一个主要摄影机路径；复合路径最多包含一次同向、有动机、同轴、同平台的延续
- 多景别、多视点、新刺激—反应节拍、换侧/越轴、时空变化或不同FX阶段必须拆镜
- 组合语义映射到现有Template字段，不创建Movement Combination最终字段

禁止：

- 把景别、机位、视点、对焦、慢动作、FX或剪辑全部命名为运镜
- 为套用附件模式新增人物关系、情绪、武器、法术、泪水、光源、地点或时间变化
- 把普通摄影机运动直接当作转场，或把多个正式SHOT伪装成一个短镜头
- 牺牲Required Coverage、表演可读性、轴线、焦段连续性或稳定终点

冲突时：Coverage返回Sequence / STATE-06；Camera原子返回对应Camera Knowledge；边界返回Transition；FX和Performance返回其事实拥有者。

---

## Camera Movement Selection Matrix Knowledge Contract

Module Type：STATE-06至STATE-09辅助Camera Knowledge，不创建新STATE。

触发：所有正式SHOT的Camera Language Decision、所有Clip Movement Plan、STATE-08运镜语义投影与STATE-09 Camera Language QA。

不触发：不独立改写剧情、资产、导演风格、Shot Purpose、SHOT / CLIP顺序或Seedance最终Schema。

输入拥有者：Shot Purpose、情绪/表演、人物运动、Blocking / Relational Screen Geometry、空间任务、节奏阶段、Visual Direction、模型复杂度与边界合同分别由对应上游事实和设计拥有者提供。

输出拥有者：STATE-06由`templates/08_shot_design_prompt.md`拥有；STATE-07由`templates/20_clip_plan.md`拥有；STATE-08仍只由`templates/10_video_prompt.md`拥有。

允许读取：`knowledge/camera_language/camera_movement/selection_matrix.md`、Camera Movement Index、被选主/辅助运镜原子文件，以及适用的Movement Combination / Advanced Camera Movement。允许写入：当前阶段拥有者管理的Detailed Shot Design、Clip Production Plan与内部Projection / QA结果。

下游消费者：STATE-06 Detailed Shot Design、STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation与STATE-09 Review。

不变量：每SHOT先做Camera Language Decision；每Clip有主导镜头语言与重复/复杂度控制；超过4个Shot时通常至少2种运镜逻辑；同类主运镜连续3次以上需要逐镜叙事理由；不强制每镜不同；基础稳定运镜优先；复杂Orbit / 360、穿墙、无人机和多段一镜到底受叙事必要性、模型容量与降级门控。

禁止：未检索就默认“缓慢推进/轻微横移”；随机堆叠运镜；把稳定等级、Decision或Clip Movement Plan变成STATE-08新字段；用运镜选择静默修改轴线、剧情、资产或Shot Purpose。

冲突时：逐镜目的、Blocking、轴线、动作容量或主运镜返回STATE-06；Clip编排返回STATE-07；仅执行转译问题留在STATE-08；资产或剧情事实返回其拥有者。

---

## Performance Expression Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-09辅助Knowledge。

触发：镜头包含人物注意、反应、情绪变化、对白倾听、压抑/伪装、哭笑、群体反应、身体状态影响表演，或Scene / Shot Group / Clip需要核对跨镜Performance Arc与相对表演层级。

输入拥有者：Script / Scene事实、Character Asset与基线、人物关系、Shot Purpose、Action / Blocking、Dialogue / Sound、Camera / Composition、Lighting与边界状态。

输出拥有者：STATE-04由Project Bible表演字段拥有；STATE-06由Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部表演模式只使用PEX-01至PEX-36，最终Prompt不得输出PEX或AU编号
- 每个情绪变化必须有已确认刺激、注意变化、至少一项可见反应、行动选择与稳定结束状态
- 每个相关角色在Scene / Shot Group层使用内部Performance Arc Map核对Inherited Baseline、Trigger、Pre-action / In-action / Post-action Residue、Arc Endpoint与Next-shot Carryover；单SHOT只投影当前可见段，不创建Template字段
- Intentional Hold必须保留注意目标、压制/延迟、呼吸/姿态或行动证据；静态情绪标签与固定脸完成动作不构成有效表演
- 多人场景必须明确Primary Performer、Secondary Reactor / Listener / Background Holder、反应顺序、相对幅度与视觉重点交接；除非剧情授权，不得全员同强度表演或全员同脸冻结
- 连续镜头继承视线目标、呼吸、面部/身体张力、泪液/红肿等可见后果与控制/泄漏状态
- 表演语义映射到现有Template字段，不创建Expression或Performance最终字段

禁止：

- 把喜怒哀乐或模式名称当作完整表演指令
- 把固定脸型、瞳孔、脸红、露齿数、落泪或颤抖当作情绪必然结果
- 用表情新增人物关系、心理诊断、剧情刺激、台词、动作结果、光线或色调
- 与Character Asset、Action / Blocking、Dialogue / Sound、Lighting建立重复原子定义

冲突时：项目表演尺度返回STATE-04；角色身份/基线返回Character Asset拥有者；动作、对白容量、景别或逐镜表演节拍返回STATE-06。

---

## Color Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-09辅助Knowledge。

触发：项目或镜头需要综合色彩体系、主辅强调色、饱和度、明度/对比、白平衡/偏色、肤色/中性色保护、材质综合色彩响应或跨镜色态连续性。

输入拥有者：已确认Character / Environment / Prop / FX Asset、Visual Direction、Lighting、Shot Purpose、时间/天气、材质与边界状态。

输出拥有者：STATE-04由Project Bible Color System拥有；STATE-06由Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部模式只使用CLR-01至CLR-09，最终Prompt不得输出CLR编号
- 每个适用色调必须同时定义综合色彩来源、色相层级、饱和度、明度/对比、白平衡/偏色、肤色/中性色保护和稳定结束色态
- 连续镜头保持资产固有色、肤色、中性色、综合色温、饱和度与材质响应连续
- Color语义映射到现有Template字段，不创建Color或色调最终字段

禁止：

- 把色调名称当作固定情绪、题材、人物状态或完整Prompt
- 用调色新增光源、环境、服装、道具、FX或改变资产固有色
- 把暗调写成欠曝、把高饱和写成全局拉满、把糖果/清透写成过曝磨皮
- 与Lighting、Exposure、Texture、Asset或Performance重复定义原子职责

冲突时：项目级色彩体系返回STATE-04；资产固有色返回对应资产拥有者；光源/曝光返回Lighting；逐镜色态与动作容量返回STATE-06。

---

## Lighting Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-08辅助Knowledge。

触发：时间、天气、环境实用光源、人物受光、明暗关系、光线变化、反射或参与介质影响镜头可见结果。

输入拥有者：Visual Direction、Environment / Character / Prop / FX Asset、Shot Purpose、空间与边界连续性。

输出拥有者：STATE-04由Project Bible对应字段拥有；STATE-06由Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部模式ID只能为LGT-01至LGT-20，最终Prompt不得输出模式ID
- 每个适用光影设计必须有已确认或可由环境成立的光源/介质依据
- 连续镜头保持光源空间锚点、方向、光质、综合色温关系与动态状态连续
- 光影语义必须映射到现有Template字段，不创建Lighting最终字段

禁止：

- 把浅景深、运镜、构图、调色、FX或情绪表演重复定义为灯光原子
- 用“电影感、高级感、压迫感”等抽象标签代替光源、方向与可见结果
- 为套用模式新增灯具、火焰、雾、雨、水、车辆、招牌或剧情反应
- 静默修改时间、天气、环境结构、资产状态或镜头目的

冲突时：项目级光线体系返回STATE-04；环境/实用光源/介质资产返回其事实拥有者；逐镜执行与动作容量返回STATE-06。

---

## Clip Production Module Contract

Module Type：STATE-07主流程Workflow / Knowledge。

触发：任何已完成STATE-06 Confirmed Detailed Shot Design、准备组织AI视频生成单元的项目。

输入拥有者：Detailed Shot Design正式镜头、目标时长、Shot Boundary、Confirmed Assets、Visual Development、Sequence / Coverage及Applicable Knowledge结果。

输出拥有者：`workflows/10_clip_production_workflow.md`与`templates/20_clip_plan.md`。

下游消费者：STATE-08 Clip-based Video Prompt / Video Generation、Review与生成执行。

不变量：

- 不修改正式SHOT编号与顺序
- 每个正式分镜必须且仅能进入一个CLIP-xxx
- 每个Clip确认时长必须为4—15秒；单Shot可短于4秒并进入兼容Clip，超过15秒的Shot返回STATE-06拆分
- 只有相邻、时空/资产/边界/轴线/动作/运镜兼容且模型可稳定执行的分镜可以合并
- 每个Clip拥有包含Shot清单、Entry、连续动作、摄影机/空间关系、道具连续性、内部逐镜状态链、稳定Exit、新尾帧限制与下一Clip Handoff；并把这些已有事实归并为`Character / Spatial / Prop / Camera / Environment / Performance / Continuity Risks / Next-Clip Carryover`八组`Clip End-State Record`，不新增STATE或STATE-08字段；实际生成、提取并确认后统一登记为`REF-TAIL-XX｜CLIP-XX尾帧参考`
- Knowledge Projection Ledger只记录可执行语义，最终Prompt仍由`templates/10_video_prompt.md`拥有

禁止：

- 用Clip改写剧情、删减Required Coverage或跨越中间分镜
- 为凑4秒新增无叙事作用的动作
- 超过15秒、跨时空/资产版本或高复杂度强行合并
- 让Planning或验证失败的Clip Production Plan进入STATE-08

冲突时：剧情/场景返回其事实拥有者；镜头、时长、轴线或动作容量返回STATE-06；Clip组织返回STATE-07；资产版本返回STATE-03；Prompt字段返回STATE-08 Template。

---

## Clip Preflight Check Module Contract

Module Name：`Clip Preflight Check / Clip生成前检查`。

Module Type：STATE-07与STATE-08共享的强制Quality / Continuity Knowledge Gate；同时拥有Visual Blocking Anchor Assessment / Persistence算法，并通过`references/ref_sketch_master.md`消费独立的Sketch Presentation Authority合同；不创建新主STATE、不创建平行Registry、不拥有STATE-08最终字段。

触发：每个STATE-07候选Clip形成执行合同时执行Visual Blocking Risk Pre-Assessment；每个STATE-08 Confirmed Clip在正式Prompt编译与Template Mapping前执行Final Assessment，包括用户指定Clip、说“下一个 / 下一步 / 继续”及批量中的每个Clip。普通资产制作、海报、Storyboard或纯音色任务不独立触发。

Required Inputs及唯一来源：上一Clip End State / Tail-Frame Use、八组`Clip End-State Record / Next-Clip Carryover`、Visual Anchor State、当前Clip Start Requirement与Clip边界由STATE-07 / 当前STATE-08 Checkpoint拥有；逐分镜时空与剧情事实由Script / Scene拥有；资产与Prop State由Asset Registry / STATE-03拥有；Scene Spatial Snapshot、Pose Hierarchy、Relationship Topology、Action PREVIS、Performance Goal / Performance Arc Map与Shot几何由STATE-06拥有；Transition事实由已确认Shot / Transition设计拥有。

Output拥有者：STATE-07检查记录由`templates/20_clip_plan.md`拥有；STATE-08只把通过结果投影到`templates/10_video_prompt.md`既有字段；`knowledge/clip_preflight_check.md`拥有分类、检查顺序、失败条件与返回路由；`templates/23_visual_blocking_sketch_prompt.md`唯一拥有Technical Visual Blocking Sketch的图像生成输入包与Candidate Evidence Record，不拥有Assessment或最终视频Prompt Schema。

允许读取：Confirmed Clip Production Plan、Detailed Shot Design、Spatial Blocking、Action PREVIS、Asset Registry、Reference Budget、Transition、相邻Clip边界、实际首尾帧、已存在Visual Anchor Revision，以及`references/ref_sketch_master.md`中母版图片的真实注册状态与Presentation合同。允许写入：Clip Plan现有Preflight / Spatial State / Continuity Risks / Reference Budget栏目、当前STATE-08 Checkpoint / Projection / QA，以及绑定单一Clip的Confirmed `REF-SKETCH-XX`。不得新增主STATE、顶级Template字段或Canonical资产类型；不得把母版示例内容写入Current Clip事实。

下游消费者：STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation与STATE-09 Review。

不变量：视觉连续、剧情连续、主动切场/切世界三选一；再在既有判定中明确A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】。A/B标记`Tail Frame Required = YES`并在【参考资产】列统一`REF-TAIL`、分别声明“同镜头连续承接用途”或“空间/站位/景别参考用途”；未提供时写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。A使用固定直接承接句，B明确另起新镜头重新构图且不使用该句。C标记`NO`，不列`REF-TAIL`，用Canonical资产、Spatial Blocking与文字规则重建。逐角色还必须通过Performance / Emotion Check：Inherited Baseline、Trigger、Pre-action / In-action / Post-action Residue、Arc Endpoint、Intentional Hold证据、Next-shot Carryover与多人相对表演层级可复算；静态标签、无刺激重置、固定脸完成动作、全员同强度或全员同脸固定FAIL。每个Clip在STATE-07只标`NONE / POSSIBLE / REQUIRED`草图风险；母版可用性不得改变Assessment。STATE-08每次单Clip Prompt前做Final Assessment。Final=`NONE`直接Prompt；Final=`REQUIRED`先生成 / 验证 / 注册Confirmed `REF-SKETCH-XX`、加入参考资产并本轮停在草图，下一次继续才Prompt。生成时遵循`Master Template carries sketch language; Current Clip data carries blocking content.`：真实已注册`REF-SKETCH-MASTER`只拥有Sketch Presentation Authority；当前`REF-SKETCH-XX`才拥有Clip Blocking Authority。母版文件不可用时必须标记Text Contract Fallback，不得声称已使用视觉母版。人物绘制层统一服从`references/ref_sketch_master.md`的`Neutral Mannequin Representation Rule`：S / P / A / Combined使用同一套无性别技术人偶，仅由角色名 / ID、技术颜色与位置标签区分；Character Asset独占性别、脸、发型、服装、年龄感、体型与身份Authority。每张当前草图还须通过Template Content Leakage Check与Character Appearance Leakage Check；明显人物外观或性别化体态泄漏固定判`FAIL = Character Appearance Leakage / Identity Contamination`。普通Prompt Rewrite必须复用原草图；只有Blocking Signature实质改变时允许KEEP / REPLACE / RETIRE / CREATE。当前草图只拥有Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path，不覆盖Character / Environment / Prop Authority。每分镜先锁定World-State，再按`Clip End-State Record`、当前目标与Continuity Risks对Eligible资产执行最小充分Reference Selection / Routing；身份/空间结构/道具造型/Visual Blocking/A-B尾帧/光线场景状态分别使用正确来源，C不选旧尾帧，不因Registry存在或预算空位全选。`REF-SKETCH-MASTER`默认不进入最终视频【参考资产】且不计视频图片预算；跨世界/时空/尺度/形态变化先完成转场五要素；逐镜锁定角色精确数量、空间关系与关键道具状态；Reference Budget最后执行且Projected Final Count≤9。

禁止修改：剧情、世界观、Active Asset Version、角色身份、Shot目的/顺序、Spatial Blocking、主Pipeline、STATE-08 Schema。禁止用Preflight为补救错误而新增转场媒介、角色、道具、FX或剧情事件。

冲突路由：剧情/世界事实返回事实拥有者；资产/道具形态返回STATE-03；Shot / Blocking /转场设计返回STATE-06；Clip边界、预算或执行合同返回STATE-07；仅最终文案投影错误留在STATE-08。

Validator可检查的不变量：两条Workflow Resource Gate均显式引用本模块；STATE-07 Template存在Preflight记录、Performance / Emotion Check与PASS / Return Route；STATE-08 Template没有新增Preflight字段；Five Global High-Priority Rules、十三个Acceptance Scenarios、Before-Single-Clip-Prompt Gate、Blocking Signature、四种Reassessment结果、母版注册状态、两级Authority、七项Layout Validation、Template Content Leakage Check与Character Appearance Leakage Check存在；所有显式文件引用有效。`Asset Status=REGISTERED`时真实相对文件必须存在；`UNAVAILABLE`时不得出现已注册路径声明。Candidate Evidence必须由`scripts/validate_sd_film.py sketch`拒绝单幅电影插画、缺失版式项、Blocking不匹配、模板内容泄漏、人物外观 / 身份污染或Confirmed前图片不可读。

---

## Prompt Compilation Module Contract

Module Type：STATE-08语义投影Knowledge。

触发：所有Video Prompt与Seedance Prompt撰写。

输入拥有者：项目文件、已确认阶段输出与适用Knowledge模块。

输出拥有者：`templates/10_video_prompt.md`。

下游消费者：STATE-08 Final Validation与STATE-09 Review。

必须：

- 为每项Applicable Knowledge保留现有字段中的具体语义证据
- 只映射适用模块，不制造填充内容
- 保留信息但不保留内部知识结构
- 在冲突时返回事实拥有者，不用Prompt文案静默调和
- 按Confirmed Clip Production Plan一对一创建`# CLIP-X｜标题 Seedance视频提示词`独立Package；每个Package包含该Clip的1个或多个`分镜X`，但整个Clip只生成一条连续Prompt，不按Shot拆分，并拥有完整结尾帧、尾帧用途判定与反向提示词
- 多Clip项目默认每轮只交付当前一个Clip；“下一个 / 下一步 / 继续”只推进一个Checkpoint。只有用户在当前请求中明确要求全部、一次性、批量或连续输出多个Clip时，才允许同轮输出多个独立Package
- 每个Clip在任何最终Prompt句子之前执行Before-Single-Clip-Prompt Gate；Final=`REQUIRED`且尚无匹配Confirmed Visual Anchor时，本轮按`references/ref_sketch_master.md`路由真实已注册母版或明确Text Contract Fallback，先用Neutral Mannequin Representation Rule生成Technical Director Blocking Sheet、执行Template Content Leakage Check、Character Appearance Leakage Check与完整Sketch Validation、注册当前`REF-SKETCH-XX`、加入参考资产并停止，下一Checkpoint才输出Prompt。普通Prompt Rewrite不得重触发草图；`REF-SKETCH-MASTER`不得自动进入最终视频参考资产
- 每个Clip必须为4—15秒；Clip内分镜保持原顺序、逐镜字段和显式状态链
- 跨Clip在既有Handoff内明确A/B/C：A/B均列统一`REF-TAIL`、用途与真实状态，缺图时标待补充；A直接承接，B另起新镜头重新构图且不使用Direct固定句；C不列`REF-TAIL`，以Canonical资产、Spatial Blocking与文字状态重建
- 每个Clip交付前强制验证【参考资产】、首帧来源/要求、稳定尾帧接口和前后Clip连续性关系；缺任一项不得输出
- 先执行Voice Identity Omission Gate：默认不检查或投影Voice Profile / Voice Audio Reference，不输出`音色特征：`或声音资产状态；只有用户明确要求把声音控制写进当前视频模型Prompt时，才按`Source Carries State, Prompt Carries Delta`输出当前Clip最小必要控制
- 风格标签行为只由`knowledge/prompt_compilation/state08_projection.md`的Style Label Expansion Rule拥有：重要标签可保留，首次出现必须在同一风格段获得项目特定、可执行解释；正式Style Source锁定后的连续Clip只补当前delta；具象化本身不是默认删除标签的理由
- Repetition Pollution只由`knowledge/prompt_compilation/state08_projection.md`的Field Ownership Assignment / State Once Gate处理：每条约束先指定唯一权威字段，其他位置只保留状态变化、边界接口或局部高风险所需的最短Delta；Template字段完整不得被解释为全文重复授权
- Negative Compression只保留固定禁BGM首句与当前Clip少量难以正向锁死的高风险类别；历史事故、其他Clip状态、未来泄漏、未出场资产、正文重复与同义枚举必须删除或合并

禁止：

- 新增或改名最终字段
- 输出内部Projection Ledger
- 把模式ID、SEQ/BEAT/COV/UNIT或知识标题变成固定Schema栏目
- 为显示“专业度”机械重复同一信息
- 绕过Confirmed Clip Production Plan跨Clip合并、遗漏、重排或重复正式Shot，按Shot拆Prompt，或只在整组Prompt末尾输出一次结尾帧与反向提示词

---

## Transition Knowledge Contract

Module Type：跨镜头边界与转场选择Knowledge。

输入拥有者：`rules/04_consistency_rules.md`判定的Boundary Class，以及Detailed Shot Design、Clip Production Plan、Sequence和已确认资产/FX事实。

输出拥有者：Shot Design的边界合同与`templates/10_video_prompt.md`现有字段。

必须：

- 先判定Continuous Handoff、Motivated Discontinuity或Unresolved Handoff，再选择一种主要转场技术
- 记录Outgoing Anchor、Cut Point、Incoming Anchor、继承/重建状态、禁止提前动作与Direct Cut降级
- 投影到上一G段前置【尾帧限制】、下一G段【首帧参考】、按空间/动作连续性条件决定的【参考资产】正式引用，以及上一镜“镜头结尾状态”和下一镜“起始状态”；跨场景时上一尾帧通常不进入下一段【参考资产】，只作人物与视觉连续性核对
- 同期声音桥只使用对白、环境声、动作声、呼吸、Foley或剧情内声源
- 同一Clip内使用逐镜状态链；跨Clip明确A/B/C。A/B在下一Package【参考资产】列统一`REF-TAIL`、对应用途与真实状态，缺图时标“待用户提供/待上传、未确认”，Prompt可交付但生成前补图；A使用Direct固定句，B明确另起新镜头且不使用该句；C不列`REF-TAIL`并使用Canonical资产、Spatial Blocking与文字End State承接或重建

禁止：

- 新增STATE-08“转场”字段或输出TRN内部ID
- 改写Boundary Class、剧情、资产、站位、道具或镜头目的
- 把普通运镜直接命名为转场
- 无依据新增光源、介质、FX、魔法或场景变形
- 使用背景音乐、配乐或歌曲建立STATE-08声音转场

---

## Project State And Recovery Contract

Module Type：项目控制Reference与辅助Workflow。

输入拥有者：project_manifest.json、按State Source优先级选定的project_status.md或portable_project_status.md、asset_registry.md和Artifact Ledgers。

输出拥有者：项目状态字段由references/project_state_contract.md拥有；恢复记录由templates/17_execution_ledger.md与templates/18_artifact_revision_ledger.md拥有。

必须从可验证Checkpoint继续，保持Accepted Unaffected Artifacts，不创建新主STATE。Legacy Project Recovery Integrity、Skill Definition Source、Work escalation与Legacy Intent Backfill路由只由`rules/runtime_reload.md`拥有；State Source只按`rules/state_source.md`选择；本模块不得复制优先级或Chat fallback细节。`workflows/18_project_resume_workflow.md`只消费以上owner的结果并执行Checkpoint / Retry / Ledger。禁止把历史聊天里的Skill摘要当作Current Skill或State Source、选择最近项目、静默合并不同Project ID、重写成功Checkpoint之前内容，或在第三次同类失败后继续盲重试。

Legacy Intent Backfill固定是additive compatibility pass：只补当前schema缺失且可从Confirmed Canon可靠推导的Writer / Director intent，保留Production-Locked Screenplay、Confirmed Assets、Blocking Canon / Spatial Snapshot、Confirmed `REF-SKETCH`、Accepted Take / accepted prompt及已确认镜头。它不得回STATE-01重做项目，也不得把Packet变成Portable字段或最终Template Schema。

---

## Quality Knowledge Contract

Module Type：STATE-06至STATE-09辅助Knowledge。

输入拥有者：已确认资产、Detailed Shot Design、Clip Production Plan、Prompt、生成结果与边界合同。

输出拥有者：正式Review由templates/16_review_report.md拥有；内部QA可进入Execution Ledger。

必须执行Shot QA、相邻镜QA、Execution Risk和适用的Prompt Scorecard。禁止用分数覆盖Hard Gate、把QA字段写入STATE-08 Prompt或用审美偏好改写剧情事实。

---

## Shot Language Router Contract

Module Type：STATE-06至STATE-08 Camera Knowledge Router。

输入拥有者：Shot Purpose、Coverage、Blocking、Performance、Space、Assets、Visual Direction与Boundary。

输出拥有者：STATE-06由templates/08_shot_design_prompt.md拥有；STATE-08仍由templates/10_video_prompt.md拥有。

必须按Evidence→Scale→Perspective→Position→Lens→Composition→Movement→Risk→Downgrade顺序选择。禁止重复定义Camera原子、用导演标签覆盖空间/证据或把内部Risk等级写入最终Prompt。

---

## Skill Update Self-Check / Change Safety Checklist

本节是所有Skill维护QA的唯一权威来源。它属于Skill维护层，不是影视制作Pipeline的STATE，不写入项目状态，不进入用户视频Prompt，也不得被复制成另一套并行检查规范。

### Trigger And Change Classification

每次对Skill作任何正式修改后都必须执行，包括修改`SKILL.md`、Rules、Workflows、Knowledge、Templates、References、Validator、测试、用户文档、模块增删、Prompt结构、路由、Gate、STATE规则、资产规则、连续性规则、Review规则以及纯拼写修正。轻量语义检查可以与改动风险匹配，但`Standalone Skill Discovery Guard`与`Unconditional Chat Runtime Startup And Recovery Guard`永远不能省略；任何修改都必须运行当前静态Skill Validator、完整测试入口、SD-R1—SD-R5与LR-R1—LR-R10，证明桌面Chat仍能发现、启动、恢复并保持诚实Claim。

开始修改前先搜索当前权威来源和同类机制，完成后把本次变更标记为以下一种：

- `no_change`：现有机制已完整覆盖，未修改文件。
- `optimize_existing`：权威原规则存在但覆盖不完整，在原位置补足。
- `merge_existing`：同类规则零散分布，合并到一个权威来源，其他位置只保留引用或路由。
- `add_new`：确认没有合适权威位置后才新增最小模块或文件。
- `deprecate/remove`：移除已废弃、冲突或被权威来源替代的内容，并清理全部引用。

### Mandatory Maintenance Chain

```text
Read current rules
→ Locate related rules
→ Classify existing coverage
→ Apply minimal change
→ Run Skill Update Self-Check
→ Run Standalone Skill Discovery Guard
→ Run Unconditional Chat Runtime Startup And Recovery Guard
→ Classify and resolve every finding by risk
→ Run targeted regression for the requested change and every repaired finding
→ Sync USER_GUIDE when user-facing behavior changed
→ Final change report
```

### Check Dimensions

1. **Duplicate Rule Check**：搜索语义相同但措辞不同的并行规则，以及本应由单一来源拥有却复制到`SKILL.md`、Rule、Workflow、Knowledge、Template、Reference或Validator的规范。保留一个权威来源，其他位置只保留必要路由、引用或不变量，不复制完整协议或Schema。
2. **Conflict Check**：核对Pipeline、STATE编号、Gate、优先级、默认行为与辅助模块边界。重点排除显式调用与默认必经并存、Storyboard Auxiliary与固定STATE并存、Shot/Clip/Prompt单位关系冲突，以及同一Template字段被不同文件定义。
3. **Terminology Drift Check**：复用当前正式术语与ID，包括Shot、Clip、Prompt、Voice Profile、Accepted Take、Accepted Canon State、Shot-State Memory、Reference Selection / Routing、REF-TAIL、Visual Blocking Anchor、Visual Anchor State与Blocking Signature。新名称只有在代表新概念且不会形成同义命名时才允许。
4. **Rule Ownership Check**：按本文件Authority Matrix检查归属。`SKILL.md`只保留身份、版本、入口、主路由、全局硬规则和索引；详细算法、门槛、知识、Schema与合同分别留在Workflow、Rules、Knowledge、Templates和References。不得为提高可见性而在入口复制细粒度规则或Template字段。
5. **Prompt Pollution Check**：确认新增内部控制不会直接膨胀最终Prompt。检查重复、冲突、抽象语义模板、否定词堆叠、资产重述、无效精密参数、跨镜头残留、风格堆叠与优先级淹没；内部QA、分数、Issue ID、路由说明和维护术语不得进入最终Prompt。
6. **Routing Integrity Check**：确认新模块有正确入口、触发和返回路由；显式调用模块未变为默认必经；Optional/Auxiliary Workflow未写入主Pipeline；Legacy Compatibility未成为新项目主路由；普通“继续”未被误判为Reload、AUDIO或MUSIC授权。
7. **Template Consistency Check**：核对Workflow声明的Output Owner、字段语义与当前Template；废弃字段不得残留。Template继续唯一拥有用户可见字段、顺序、必填性和排版。音色未显式投影时，常规STATE-08输出不得默认保留声音身份或“音色特征”字段。
8. **Reference Integrity Check**：验证所有显式文件、模块、Template、Knowledge与脚本路径真实存在且名称一致；新增资源已被合法路由发现；删除或改名后没有悬空引用。运行`scripts/validate_sd_film.py skill <skill-root>`执行可确定的结构与引用检查。
9. **State / Continuity Compatibility Check**：确认STATE-00至STATE-09、Shot-State Memory、Accepted Take、Accepted Canon State、Reference Selection / Routing、REF-TAIL A Direct / B Reference-Only / C Not Required、Visual Anchor State / Blocking Signature、Spatial Blocking、资产锁、Revision与Checkpoint不被破坏；维护QA不得创建新主STATE或项目事实。
10. **User Guide Sync Check**：如果修改改变用户该如何下指令、默认行为、用户可见输出结构、模块入口、opt-in边界或停止点，必须同步`USER_GUIDE.md`；仅内部知识或实现优化且不改变调用和输出时标记`NOT REQUIRED`，不得为机械同步复制内部规则。
11. **Regression Check**：根据影响范围选择最少但有效的案例，并同时包含适用的正例和反例。路由变更验证正确模块与不触发路径；Prompt变更验证Schema与污染；连续性变更验证REF-TAIL三模式；音色变更验证未调用时省略、显式调用时进入Seed Audio；资产变更验证Core / Support与Reference Asset Eligibility。优先复用`references/regression_scenarios.md`与现有Validator / tests；如果自检同时修复了其他历史问题，必须为每个修复项增加对应的直接回归，不得因为它与原始请求无关而省略验证。
12. **Change Classification Check**：复核最终分类与实际操作一致，并记录为什么不是其他类别；新增文件前必须能说明现有权威位置为何不合适。
13. **Runtime Claim / Legacy Recovery Check**：核对Runtime Skill Reload、Workflow Re-entry与Legacy Project Recovery仍由唯一owner定义；Skill Source / Project State Source独立；历史Skill永不成为Current authority；Claim Gate诚实；Work只在真实必要时escalate；Legacy Intent Backfill只增补不重做；STATE-08从current owner entry重进；普通`下一步`不触发全量恢复。必须运行`references/regression_scenarios.md`中的`Legacy Recovery Regression Matrix (LR-R1—LR-R10)`及现有Validator / tests。
14. **Standalone Skill Discovery Check**：核对当前运行时用户级权威副本位于`$HOME/.codex/skills/sd-film`、同名`sd-film`没有第二份用户级副本、`SKILL.md` frontmatter保留启动别名、`agents/openai.yaml`与Skill名称一致、`policy.allow_implicit_invocation`为`true`，且用户文档只把Codex `$sd-film`作为本机独立Skill的确定性显式入口。在当前用户客户端中，普通Chat的`@`选择器只显示Plugin；不得宣称本机独立Skill可通过`@`加显示名调用，也不得把网页/移动端读取本机Skill误写为受支持能力。

### Skill-Wide Detection And Risk-Based Repair

- **Detection scope is Skill-wide**：每次完整自检都检查整个Skill在十二个维度上的可见问题，不以本次Diff、修改文件或直接消费者为发现边界。已经发现的问题不得仅因“与本次修改无关”而跳过、隐藏或从报告中删除。
- **Every finding requires disposition**：每个真实发现项必须在本轮标记为`FIXED`或`WARN`，并记录所有者、影响和处理依据；误报必须说明为什么不构成问题，不能用总体`PASS`掩盖单项发现。
- **SAFE_LOCAL**：权威来源明确、影响局部、行为保持不变且可通过确定性检查或直接回归验证的问题，本轮必须修复，即使它是历史遗留或与原始请求无关。例如悬空引用、重复定义、失效索引、确定的术语漂移、版本不一致和无消费者的竞争副本。
- **CONTROLLED_CROSS_MODULE**：涉及多个文件或消费者，但所有者、影响边界和回归路径明确的问题，原则上也在本轮修复；同步更新所有直接消费者并扩展定向回归。文件数量或是否属于原始Diff本身不是延期理由。
- **HIGH_RISK / DECISION_REQUIRED**：可能改变用户已确认的重要行为、主Pipeline、STATE、资产锁、项目事实、最终Schema、外部兼容，或需要无法在本轮可靠验证的大规模迁移时，不得静默修改。标记`WARN`，写明证据、影响、权威所有者、建议修复方案与所需用户决定；若会使本次更新不安全，则在完成前升级为明确阻塞或请求决定。
- 风险分级是为了决定如何处理，不是缩小检查范围。禁止把“不要全面重构”解释成只修本次相关问题；同时也不得把自优化变成无边界重写。优先逐项、可回滚、可验证地清零问题，只有达到`HIGH_RISK / DECISION_REQUIRED`门槛才允许延期。
- 不允许为了“统一”删除用户已确认的重要行为、改变Production-Locked事实、清空Confirmed Assets / Accepted Artifacts，或扩大当前授权范围。
- 语义检查由维护者实际阅读和比较完成；Validator只负责确定性结构、不变量和引用检查。Validator通过不等于全部语义维度自动PASS。

### Targeted Regression Selection

回归选择以所有实际修复项及其直接消费者为边界，而不只看原始请求的Diff：先验证每个修改文件，再验证它引用或被引用的直接模块，最后验证对应关键不变量。若修复横跨多个所有者，分别验证各自Template / Workflow合同；若只改内部说明且无行为变化，不机械运行无关的全生产回归，但不得漏掉自检附带修复的直接回归。

模块接入或路由变更至少继续检查：

- 主Pipeline仍只包含STATE-00至STATE-09。
- 原有Template仍拥有原有阶段Schema。
- 新ID命名空间没有冲突。
- 新Workflow有明确触发、不触发与Not Applicable / Return Route。
- 新输出只写入合法的Active Project Root或对应可移植状态位置。
- 所有显式内部文件引用均存在。
- 正常样例通过Validator；缺字段、重复ID、越权ID或错误路由样例被拒绝。

### Runtime Recovery Regression Protection

`Unconditional Chat Runtime Startup And Recovery Guard`是每次正式Skill修改的固定基线，而不是按Diff选择的可选回归。无论修改任何文件、模块、文案、Template、Knowledge、测试、Validator或仅修正拼写，都必须运行完整`Legacy Recovery Regression Matrix (LR-R1—LR-R10)`，验证普通Chat activation、Current Skill resource解析、双source独立、Claim Gate、Work边界、legacy mapping、intent backfill、STATE-08 re-entry与plain-next隔离；不能以改动小、未触及runtime或“本轮改的不是recovery文件”为由跳过。

以下区域仍视为高风险触发面；命中时除固定基线外，还必须根据直接消费者增加定向恢复案例：

- `SKILL.md` activation / routing
- Runtime Reload / Workflow Re-entry
- State Source / Portable State
- Project Setup / project status schema
- Pipeline / STATE rename、owner或filename变化
- Screenwriter Module / WRITER INTENT PACKET
- Director Module / DIRECTOR INTENT PACKET
- STATE-07 / STATE-08 Current Object、Clip state、Reference / Blocking / Prompt entry
- `USER_GUIDE.md` recovery commands
- ordinary Chat vs Work routing

执行owner固定为`scripts/validate_sd_film.py skill <skill-root>`与`scripts/test_validate_sd_film.py`。这两项验证始终检查LR-R1—LR-R10的静态合同和防篡改用例，因此每次正式修改都必须运行它们；如果未来脚本owner改名或迁移，必须在同一次变更中把本节、`SKILL.md`指针与测试入口一起迁移，不能只删掉检查。语义演练仍由维护者按Matrix逐项核对，脚本通过不替代语义判断。

### Standalone Skill Discovery Guard

本Guard属于现有Skill维护QA，不是Plugin机制、不是主Pipeline STATE，也不建立第二套Runtime Router。它只保护独立Skill在支持本机Skills的ChatGPT桌面应用、Codex CLI与IDE中的发现入口；不得据此声称网页端或移动端能直接读取本机目录。

每次正式修改都必须运行以下固定检查，不允许因“本轮只改Writer / Director / Runtime / Template / 文案”而跳过：

- `SKILL.md` frontmatter的`name`仍为`sd-film`，`description`前置保留`调用sd`、`调用SD`、`用SD Film`、`重新调用sd`、`恢复旧项目`、`继续之前的项目`等高价值启动词；隐式调用只以当前description作发现提示，不以旧对话Skill摘要补位。
- `agents/openai.yaml`存在，`interface.display_name`为`SD Film`，`interface.default_prompt`显式提及`$sd-film`，`policy.allow_implicit_invocation`为`true`；Writer、Director、STATE Workflow和USER_GUIDE不得覆盖该调用策略。
- 当前运行时用户级权威安装采用`$HOME/.codex/skills/sd-film`；不得同时在`$HOME/.agents/skills`或另一用户级Skill目录保留第二份同名`sd-film`。运行时安装根发生迁移时执行一次迁移，不维持双写或两个独立副本。
- Codex中的确定性显式入口是`$sd-film`。在当前用户客户端的普通Chat中，`@`选择器只显示Plugin或Plugin内含能力，本机独立Skill不得承诺以`@`选择显示名的入口；普通Chat只有在宿主实际暴露本机Skills时，才可能通过`description`对`调用sd`作隐式选择。`agents/openai.yaml`的`display_name`与`allow_implicit_invocation`不会把独立Skill注册成Plugin，也不证明普通Chat已有`@`入口。
- Skill变更通常应被Codex自动检测；如果当前Codex会话未刷新元数据，要求重启桌面应用或新建Codex任务后复测。普通Chat的`@`列表没有SD Film时，不得把它误诊为Skill内容错误，也不得为迎合`@`而创建Plugin、复制Skill或弱化Runtime规则。

可执行owner仍为`scripts/validate_sd_film.py skill <skill-root>`与`scripts/test_validate_sd_film.py`；它们必须检查元数据、别名、隐式调用开关、单一用户级权威副本、禁止虚假`@`显式调用声明及`Standalone Skill Discovery Regression Matrix (SD-R1—SD-R5)`。安装位置、普通Chat是否暴露本机Skill以及客户端刷新属于运行环境证据，脚本之外仍需在最终报告中如实记录。

### Required Self-Check Summary

每次正式修改后的最终报告必须简短列出：

```text
Skill Update Self-Check

Change Classification: no_change / optimize_existing / merge_existing / add_new / deprecate/remove
Findings Disposition: FIXED <count> / WARN <count> / FALSE_POSITIVE <count>
Duplicate Rules: PASS / FIXED / WARN
Conflict Rules: PASS / FIXED / WARN
Terminology: PASS / FIXED / WARN
Rule Ownership: PASS / FIXED / WARN
Prompt Pollution: PASS / FIXED / WARN
Routing: PASS / FIXED / WARN
Template Sync: PASS / FIXED / WARN
Reference Integrity: PASS / FIXED / WARN
State / Continuity: PASS / FIXED / WARN
Runtime Claim Integrity: PASS / FIXED / WARN
Legacy Recovery Regression: PASS / FAIL / WARN
Chat Runtime Startup Guard: PASS / FAIL / WARN
Standalone Skill Discovery: PASS / FAIL / WARN
Writer / Director Compatibility: PASS / FIXED / WARN
Regression: PASS / FAIL / WARN
USER_GUIDE Sync: YES / NOT REQUIRED
Warnings: NONE / <concise unresolved warnings>
```

报告同时说明原机制位置、覆盖缺口、实际改动文件、运行过的验证，以及全部发现项的风险等级和处置。只有实际执行过的检查才能标记`PASS`；发现并修复后标记`FIXED`；只有达到`HIGH_RISK / DECISION_REQUIRED`门槛且本轮不能安全解决时才标记`WARN`，并附证据、影响、建议方案和下一步，不能再使用“与本次修改无关”作为延期理由。
