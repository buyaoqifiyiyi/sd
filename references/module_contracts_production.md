# SD Film Module Contracts — Production Modules

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是模块接口合同的一部分；Authority Matrix 与 Stable Interface Rules 留在 `references/module_contracts.md`。本文件不拥有归属判定，也不得复制该框架。

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

冲突路由：Creation Brief只有在缺失项会实质改变架构或造成品牌/事实风险时请求最小决定；Existing的锁定事实、目标形式、Adaptation Intensity或修改范围不明确时保持STATE-01 IN_PROGRESS并请求用户决定。单独的推进表达不构成Existing优化授权；但在已展示、可核对的Proposal Confirmation Gate时，按`rules/progression_rules.md`确认Proposal。当前请求已明确“直接优化 / 直接改写”时不重复询问同一授权。用户要求修订Proposal时保持Script Development并只修改受影响范围；下游发现剧情事实冲突返回STATE-01，不在资产、镜头或Prompt阶段静默调和。

Validator可检查的不变量：Creation / Existing双入口与互斥判定存在；Creation不要求先提供完整剧本、不输出Opportunity Report、具备十项Directable Screenplay QA且不提前写Shot Design；Existing固定诊断入口、十二项报告维度与A/B/C三档存在；报告前后没有未授权改写，明确“直接优化”不重复询问授权；四种Script Status值合法；Adaptation Draft或Optimized Proposal不能与STATE-01 COMPLETE或STATE-02+并存；C类只有明确授权后经过通用改编；短剧Adapter只按Target Detection加载；B类不被强制改编；No-Revision分支跳过报告和改写但仍执行Script Analysis；拒绝优化锁定原稿；所有Proposal后存在第二次确认；五份Knowledge与所有显式引用存在。

---

## STATE-03 Visual Asset Production Contract

Module Type：STATE-03 Character / Environment / Prop主资产Workflow与正式FX辅助Workflow的共享生产合同，不创建新主STATE。

触发：任何新建或更新的正式视觉资产需要生成或接收角色、环境、道具或FX参考图片。

不触发：纯文字Voice Profile、Seed Audio Voice Sample Prompt、非视觉Audio Reference，以及Asset Discovery中明确标记为Inline Effect且无需正式视觉资产的效果。

所属位置：STATE-03 Asset Development内部，固定顺序为`Asset Design → Image Prompt Generation → 用户确认提示词 → Image Generation → 用户确认图片 → Asset Registry`。

批次交付：STATE-03以批次为默认生产与确认单位，当前批次交付图片还是交付Prompt由`Production Setup Gate`确认的`Image Delivery Mode`经`modules/image-model-selection.md`投影为`Image Delivery Route`决定；批次构成、分批与两轮交付由`rules/02_asset_rules.md`的`Asset Batch Delivery`唯一拥有，同一批次全部图片在同轮提交，不逐张停顿；挑拣退回、整体否决与推进表达的含义由`rules/progression_rules.md`的`Exception-Based Batch Confirmation`拥有。本层只声明不变量：批次不得改变四态生命周期、单项Prompt / Image确认、Canonical绑定或Support的Board ID / Item ID映射，不得让未展示项因用户沉默而确认，也不得让同批其他项的确认掩盖被退回项的Hard Gate。

Two-Tier执行：STATE-02为每个CHAR、ENV、PROP拥有Asset Tiering Decision。Core满足主角/固定角色、跨场景或跨Clip复用、强剧情/角色/品牌识别、高一致性、关键场景或剧情关键道具之一，并在STATE-03独立制作；Support为一次性配角/群演、群体背景角色、同类家具与环境小物、氛围装饰、低频道具等，按同一资产类型与相近用途进入Support Reference Board。该分层是STATE-02/03内部决策，不创建新STATE，不替代Primary / Secondary / Background优先级，也不改变正式FX路由。

Support Board建议4—9个对象，必须具有稳定Board ID与逐项Item ID，统一风格但明确轮廓、服饰/材质、颜色、比例和功能差异；不得跨CHAR / ENV / PROP混板，不得逐项制作完整正式角色资产图或独立资产套图。下游引用使用`<Board Name> / <Board ID> / <Item ID>`。

Required Inputs及唯一来源：资产身份与剧情功能来自STATE-01/02、Project Bible、Active Asset Version和用户明确确认；Visual Direction只能提供项目级风格约束，不得改写资产身份。

Output拥有者：Character、Environment、Prop与FX的最终阶段字段分别由`templates/04_character_asset_prompt.md`、`templates/05_environment_asset_prompt.md`、`templates/06_prop_asset_prompt.md`与`templates/13_fx_asset_prompt.md`拥有；共享Rules与本合同只定义门槛和状态语义。

允许读取：Selected State Source、Active Project Root中的project_bible.md、asset_registry.md、Script/Asset Discovery交付物与当前资产依赖。允许写入：同一Asset ID和Version的Asset Tier、Board ID、Item ID、Image Prompts、Prompt Confirmation、Candidate References、Image Confirmation、Canonical References、Visual Production Status及其Prompt / Image / Confirmed状态投影；完整项目文件只写Active Project Root。

下游消费者：STATE-04 Visual Development、STATE-05 Scene Breakdown、STATE-06 Detailed Shot Design、STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation与Review。

交付包：已确认生产物的分类打包、资产图片稳定文件名与最终视频Prompt参考条目的一一对应，由`references/asset_package.md`唯一拥有。打包是STATE-03资产确认与STATE-07 Clip表确认之后的交付动作，不是新STATE，也不进Registry字段或最终Prompt字段。

不变量：`Visual Production Status`只使用`Prompt Draft`、`Prompt Confirmed`、`Image Generated`、`Asset Confirmed`；Prompt确认与图片确认独立；Prompt Draft不得调用图片生成；Image Generated只登记Candidate References；Asset Confirmed必须有图片批准依据，才可Active并登记Canonical References；工具不可用不把文字设定升级为confirmed asset。`Prompt Status / Image Status / Confirmed Status`必须与该生命周期严格映射；任何Core Asset、Support Board或Support Item在图片确认前都不得confirmed。Support必须有唯一Board ID / Item ID映射和Canonical Board Reference区域/标签对应关系。

禁止修改：主Pipeline、导演决策层、知识应用思考层、Clip-centric逻辑、STATE-08 Seedance Schema、已确认剧情事实和未获批准的Active Asset Version。

冲突路由：资产身份或设计冲突返回对应STATE-03 Asset Workflow；项目级风格冲突返回STATE-04；Prompt执行性问题留在当前资产Workflow；工具不可用保持STATE-03 IN_PROGRESS并等待外部图片或工具恢复。

Validator可检查的不变量：四个状态合法；Prompt Confirmed及以后具有Prompt Revision与Prompt Confirmation；Image Generated具有Candidate References但不为Active；Asset Confirmed具有Image Confirmation、Canonical References与Status Active；三个主资产Template均具有阶段化输出与双确认Checkpoint；CHAR / ENV / PROP均有Core或Support分层，Core的Board / Item为Not Applicable，Support的Board / Item映射唯一且不跨类型；三项状态投影与Visual Production Status一致。

---

## Prompt Compilation Module Contract

Module Type：STATE-08语义投影Knowledge。

触发：所有Video Prompt与Seedance Prompt撰写。

输入拥有者：项目文件、已确认阶段输出与适用Knowledge模块。

输出拥有者：Selected Model对应的唯一STATE-08 Template。

下游消费者：STATE-08 Final Validation与STATE-09 Review。

必须：

- 为每项Applicable Knowledge保留现有字段中的具体语义证据
- 只映射适用模块，不制造填充内容
- 保留信息但不保留内部知识结构
- 在冲突时返回事实拥有者，不用Prompt文案静默调和
- 按Confirmed Clip Production Plan一对一创建`# CLIP-X｜标题 Seedance视频提示词`独立Package；每个Package包含该Clip的1个或多个`分镜X`，但整个Clip只生成一条连续Prompt，不按Shot拆分，并拥有完整结尾帧、尾帧用途判定与反向提示词
- 多Clip项目默认每轮只交付当前一个Clip；“下一个 / 下一步 / 继续”只推进一个Checkpoint。只有用户在当前请求中明确要求全部、一次性、批量或连续输出多个Clip时，才允许同轮输出多个独立Package
- 每个Clip在任何最终Prompt句子之前执行Before-Single-Clip-Prompt Gate；Final=`REQUIRED`且尚无匹配Confirmed Visual Anchor时，本轮按`references/ref_sketch_master.md`路由真实已注册母版或明确Text Contract Fallback，先用Neutral Mannequin Representation Rule生成Technical Director Blocking Sheet、执行Template Content Leakage Check、Character Appearance Leakage Check与完整Sketch Validation并注册当前`REF-SKETCH-XX`；随后必须按`Required Sketch Submission Binding`将可访问的真实图片绑定到兼容Adapter输入，才可输出Prompt。普通Prompt Rewrite不得重触发草图；`REF-SKETCH-MASTER`不得自动进入最终视频参考资产
- 每个Clip必须服从锁定模型的用户选择时长；2.5的16—30秒须严格预检PASS；Clip内分镜保持原顺序、逐镜字段和显式状态链
- 跨Clip在既有Handoff内明确A/B/C：A/B均列统一`REF-TAIL`、用途与真实状态，缺图时标待补充；A直接承接，B另起新镜头重新构图且不使用Direct固定句；C不列`REF-TAIL`，以Canonical资产、Spatial Blocking与文字状态重建
- 每个Clip的`参考资产：`（或对应模型的参考字段）为每个实际投喂的视觉条目写出`references/asset_package.md`锁定的稳定引用名`<Asset ID>｜<资产名>`（环境View补View Code）；条目与包内文件必须一对一可核验，不得虚构引用名、引用未确认或未打包图片，也不得把同一文件列为两个不同资产
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

## Clip Production Module Contract

Module Type：STATE-07主流程Workflow / Knowledge。

触发：任何已完成STATE-06 Confirmed Detailed Shot Design、准备组织AI视频生成单元的项目。

输入拥有者：Detailed Shot Design正式镜头、目标时长、Shot Boundary、Confirmed Assets、Visual Development、Sequence / Coverage及Applicable Knowledge结果。

输出拥有者：`workflows/10_clip_production_workflow.md`与`templates/20_clip_plan.md`。

下游消费者：STATE-08 Clip-based Video Prompt / Video Generation、Review与生成执行。

不变量：

- 不修改正式SHOT编号与顺序
- 每个正式分镜必须且仅能进入一个CLIP-xxx
- 每个Clip确认时长必须服从锁定模型和用户选择：2.0为4—15秒；2.5为4—30秒，16—30秒须严格预检PASS；单Shot可短于4秒并进入兼容Clip，超过30秒才返回STATE-06拆分
- 只有相邻、时空/资产/边界/轴线/动作/运镜兼容且模型可稳定执行的分镜可以合并
- 每个Clip拥有包含Shot清单、Entry、连续动作、摄影机/空间关系、道具连续性、内部逐镜状态链、稳定Exit、新尾帧限制与下一Clip Handoff；并把这些已有事实归并为`Character / Spatial / Prop / Camera / Environment / Performance / Continuity Risks / Next-Clip Carryover`八组`Clip End-State Record`，不新增STATE或STATE-08字段；实际生成、提取并确认后统一登记为`REF-TAIL-XX｜CLIP-XX尾帧参考`
- Knowledge Projection Ledger只记录可执行语义，最终Prompt仍由`templates/10_video_prompt.md`拥有

禁止：

- 用Clip改写剧情、删减Required Coverage或跨越中间分镜
- 为凑4秒新增无叙事作用的动作
- 未经严格预检就超过锁定模型的时长窗口、跨时空/资产版本或高复杂度强行合并（2.5的16—30秒只有`Long-duration Preflight`PASS才成立）
- 让Planning或验证失败的Clip Production Plan进入STATE-08

冲突时：剧情/场景返回其事实拥有者；镜头、时长、轴线或动作容量返回STATE-06；Clip组织返回STATE-07；资产版本返回STATE-03；Prompt字段返回STATE-08 Template。

---

## Project State And Recovery Contract

Module Type：项目控制Reference与辅助Workflow。

输入拥有者：project_manifest.json、按State Source优先级选定的project_status.md或portable_project_status.md、asset_registry.md和Artifact Ledgers。

输出拥有者：项目状态字段由references/project_state_contract.md拥有；恢复记录由templates/17_execution_ledger.md与templates/18_artifact_revision_ledger.md拥有。

必须从可验证Checkpoint继续，保持Accepted Unaffected Artifacts，不创建新主STATE。Legacy Project Recovery Integrity、Skill Definition Source、Work escalation与Legacy Intent Backfill路由只由`rules/runtime_reload.md`拥有；State Source只按`rules/state_source.md`选择；本模块不得复制优先级或Chat fallback细节。`workflows/18_project_resume_workflow.md`只消费以上owner的结果并执行Checkpoint / Retry / Ledger。禁止把历史聊天里的Skill摘要当作Current Skill或State Source、选择最近项目、静默合并不同Project ID、重写成功Checkpoint之前内容，或在第三次同类失败后继续盲重试。

Legacy Intent Backfill固定是additive compatibility pass：只补当前schema缺失且可从Confirmed Canon可靠推导的Writer / Director intent，保留Production-Locked Screenplay、Confirmed Assets、Blocking Canon / Spatial Snapshot、Confirmed `REF-SKETCH`、Accepted Take / accepted prompt及已确认镜头。它不得回STATE-01重做项目，也不得把Packet变成Portable字段或最终Template Schema。

---

## Shot Language Router Contract

Module Type：STATE-06至STATE-08 Camera Knowledge Router。

输入拥有者：Shot Purpose、Coverage、Blocking、Performance、Space、Assets、Visual Direction与Boundary。

输出拥有者：STATE-06由templates/08_shot_design_prompt.md拥有；STATE-08由Selected Model对应的唯一Template拥有。

必须按Evidence→Scale→Perspective→Position→Lens→Composition→Movement→Risk→Downgrade顺序选择。禁止重复定义Camera原子、用导演标签覆盖空间/证据或把内部Risk等级写入最终Prompt。

---
