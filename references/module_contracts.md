# SD Film Module Contracts

## Purpose

本文件定义新增模块与现有生产系统之间的接口合同。

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

- Runtime Reload：`rules/runtime_reload.md`
- State Source：`rules/state_source.md`
- Chat Compatibility：`rules/chat_compatibility.md`
- Progression：`rules/progression_rules.md`
- Activation：`rules/activation_rules.md`
- Completion Gate：`rules/completion_gate.md`
- Compatibility Mapping：`rules/compatibility_mapping.md`
- Resource Loading：`rules/resource_loading.md`
- Canonical Portable State Schema：`references/project_state_contract.md`

其他模块只能引用这些所有者，不得在`SKILL.md`、`config.md`、References、Knowledge、Templates、兼容入口或各Workflow中维护竞争副本。`SKILL.md`可保留激活/重载入口和路由索引，但不得复制完整运行协议。

### Additive By Default

优先增加新的辅助信息，不删除或重新解释已有字段。

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

## Script Adaptation And Optimization Gate Module Contract

Module Name：`Script Adaptation Module + Script Optimization Gate`。

Module Type：STATE-01 Script Analysis内部Workflow Gate、通用改编Knowledge、条件性短剧Adapter与两份优化Knowledge，不创建新主STATE。

触发：所有输入先分类。A为已是制作剧本；B为粗略剧本/初稿；C为小说、故事梗概、品牌文案、历史事件、影视桥段、长篇素材或概念。除No Revision / Final Script例外外，所有分类统一先执行`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`。只有C类在报告Adaptation Need且用户明确授权改编/优化后触发Script Adaptation；A/B也必须在明确授权后才进入Script Optimization。

不触发内容改写：用户明确说“不要改剧本”“严格按这个版本制作”“已定稿”或同义表达时，跳过Optimization Opportunity Report、Script Adaptation、短剧Adapter、Screenwriting Optimization与Directorial Interpretation，但仍完整执行原有Script Analysis并按授权锁定。用户在Opportunity Report后拒绝优化/改编时，也跳过全部内容改写，原始版本完成分析后直接Production-Lock。

所属位置：`STATE-01 Script Analysis`内部。默认入口固定为`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`并停止。报告只写问题、影响与方向，至少检查开场钩子、核心冲突进入时机、信息重复、台词效率、动作可视化、人物记忆点、节奏、高潮力度、情绪价值、结尾Hook、时长适配、场景/人物复杂度；结论只使用A无明显优化必要、B有轻度优化空间、C有明显结构问题。用户明确授权后，C类继续`Adaptation Target Detection → Script Adaptation → Adaptation Draft → Screenwriting Optimization → Directorial Interpretation → Production Script Proposal → User Confirmation`；A/B从Screenwriting Optimization开始。未确认提案不得进入STATE-02。

Adaptation Target Detection：只有目标为短剧、竖屏剧情或1—3分钟剧情视频时加载`knowledge/adaptation/short_form_drama_adapter.md`；其他类型记录Not Applicable，不强制套用短剧规则。

Adaptation Intensity：只允许LEVEL 1 Light Adaptation、LEVEL 2 Structural Adaptation、LEVEL 3 Free Adaptation，并选择最低足够等级。用户明确“基本不要改剧情”时只能LEVEL 1；不可静默升级。

Required Inputs及唯一来源：用户原始故事文本、Project Bible中的已确认项目事实、目标形式/时长/平台/受众、用户明确的改编/优化范围与锁定要求。世界观、角色身份、核心创意、主题、名场面、关键设定与品牌要求只由用户或已确认项目事实拥有。

Output拥有者：`templates/02_script_analysis_prompt.md`独占STATE-01用户可见字段、顺序与排版；`workflows/02_script_analysis_workflow.md`拥有分类、目标检测、路由、确认门槛与状态转换；`knowledge/script_adaptation.md`拥有通用六层改编方法；`knowledge/adaptation/short_form_drama_adapter.md`只拥有适用短剧规则；`knowledge/screenwriting_optimization.md`与`knowledge/directorial_interpretation.md`只拥有各自专业分析方法。

允许读取：Selected State Source、Active Project Root中的project_bible.md、用户剧本/Source Material/设定与已确认约束。允许写入：Active Project Root的STATE-01 Script Analysis Artifact、Optimization Opportunity Report，以及获得明确授权后的Adaptation Draft和Production Script Proposal；并写Selected State Source中的Script Status / Pending Decision / Checkpoint。不得写入Skill根目录项目兼容入口。

Script Status只允许`Source Material / Adaptation Draft / Optimized Proposal / Production-Locked`。Opportunity Report与User Decision Gate期间保持Source Material；C类获准路径为`Source Material → Adaptation Draft → Optimized Proposal → Production-Locked`；A/B获准路径跳过Adaptation Draft；拒绝优化路径为`Source Material → Production-Locked`。只有Production-Locked允许STATE-01 COMPLETE。

下游消费者：STATE-02 Asset Discovery及所有后续剧情事实消费者只能读取Production-Locked Script；Adaptation Draft与Optimized Proposal都不是已确认事实。

禁止修改：用户未授权范围、世界观、角色身份、品牌要求、核心创意、关键设定、主Pipeline、资产确认闭环、Spatial Blocking Layer、Director Decision Layer、Knowledge Reflection、Clip-centric逻辑与STATE-08 Seedance Schema。

与Director Decision Layer边界：STATE-01 Script Adaptation与Directorial Interpretation只把来源素材转换为可视、可听、可表演的制作版叙事，不创建SCENE、SHOT、CLIP、焦段、机位或Director Decision Notes；STATE-06 Director Decision Layer只读取已确认Professional Detailed Shot Script决定Scene / Shot Group的视听执行方向，不回到STATE-01改写剧情。

冲突路由：锁定事实、目标形式、Adaptation Intensity或修改范围不明确时保持STATE-01 IN_PROGRESS并请求用户决定；单独“继续 / 下一步 / 好的”既不构成优化授权，也不构成Proposal确认；用户要求修订Proposal时只修改受影响范围；下游发现剧情事实冲突返回STATE-01，不在资产、镜头或Prompt阶段静默调和。

Validator可检查的不变量：固定入口、十二项报告维度与A/B/C三档存在；报告前后没有自动改写；四种Script Status值合法；Adaptation Draft或Optimized Proposal不能与STATE-01 COMPLETE或STATE-02+并存；C类只有明确授权后经过通用改编；短剧Adapter只按Target Detection加载；B类不被强制改编；No-Revision分支跳过报告和改写但仍执行Script Analysis；拒绝优化锁定原稿；Proposal后存在第二次确认；四份Knowledge与所有显式引用存在。

---

## AUDIO / SEED-AUDIO Voice Asset Module Contract

Module Name：`AUDIO / SEED-AUDIO Voice Asset`。

Module Type：显式调用的Optional/Auxiliary Workflow + Knowledge + 独立Template，不创建新主STATE，不属于STATE-03 Character Asset Workflow的默认步骤。

触发：只有用户当前请求明确要求创建、设计、生成、修改或更新“音色提示词、音色制作、角色声音、Seed Audio / SeedAudio、配音音色、声音资产 / Voice Asset、Voice Profile、角色音色样本Prompt或Audio Reference”时触发。必须记录可核对的`Explicit Trigger Evidence`。

不触发：角色仅仅存在对白、旁白、画外音、通话、呼喊或潜在对白；普通视频制作、角色分析、Character Asset、Detailed Shot Design、Clip Production、STATE-08视频/Seedance Prompt；“继续视频制作”“输出Clip B视频提示词”“下一个Clip”“下一步”“继续”“下一个”；背景音乐、环境声、Foley、音效、歌曲、正式整段配音或多人音频场景。下游缺少Voice Profile也不得自动触发。

所属位置：不绑定主STATE的独立辅助位置。项目存在时可把明确请求的结果绑定到同一CHAR-ID与Version；项目不存在时可直接根据用户当前提供的角色事实交付，不强制初始化影视Pipeline。

Required Inputs及唯一来源：角色年龄、性别、身份、性格、对白功能、情绪基调与可观察说话行为来自用户当前明确输入、已确认Script Analysis、Project Bible或Active CHAR Version；不得从外貌、导演标签、题材或竹雀示例反推。必要事实不足时保持Pending或请求最小必要输入。

Router与Output拥有者：`workflows/audio_router.md`独占显式触发判定与`AUDIO / ORIGINAL WORKFLOW`路由；`workflows/20_seed_audio_voice_asset_workflow.md`只在Positive Route后拥有执行、完成与返回调用前Checkpoint；`templates/21_seed_audio_voice_asset.md`独占Voice Profile、Seed Audio Voice Sample Prompt与Voice Audio Reference Handoff的最终字段、顺序和排版；`knowledge/sound_language/voice_generation.md`只拥有声学推导、试听覆盖、喜剧节奏与Audio Reference选择方法。`templates/04_character_asset_prompt.md`与`templates/10_video_prompt.md`不得替代本模块Schema。

允许读取：用户当前输入、Active Project Root中的`project_bible.md`、`asset_registry.md`、相关已确认剧本/分析交付物与角色对白证据。允许写入：独立交付物，以及用户明确要求保存/更新时同一CHAR-ID与Version中的Voice Profile、Voice Sample Prompt及经确认的Voice Audio Reference元数据；不创建独立视觉Asset ID，不把音频自动登记为视觉Canonical Reference。

下游消费者：STATE-06/07/08可消费已经存在且适用的Confirmed Voice Profile / Voice Reference，配音指导、跨集声音一致性与Review也可消费；任何下游消费者都不得因资产缺失而反向启动本模块。

下游交接不变量：存在适用Confirmed Voice Audio Reference时，STATE-08只引用该Reference锁定声音身份并保留固定`音色特征：`声明不得文字重定义；没有Reference但已有Confirmed Voice Profile时允许文字回退；两者都不存在时写明“未建立独立音色资产，本Clip不创建或推导声音身份”，继续视频流程，不自动生成音色资产。

禁止修改：角色身份、剧本台词事实、Active Version、视觉资产、主Pipeline、STATE-08 Seedance Schema以及未经用户或项目事实确认的口音、方言或病理声音特征。

冲突路由：角色事实冲突返回事实拥有者；台词字数或逐镜表演容量冲突返回STATE-06；音频授权、来源或候选未确认时停在本模块Pending/Candidate，不登记为Confirmed；Router返回Original Workflow时立即返回原路由，不加载声音资产Workflow或创建Not Applicable记录。

Validator可检查的不变量：所有声音身份Intent先进入唯一`workflows/audio_router.md`；只有Positive Route加载声音资产Workflow；具有显式触发证据；默认包含`Generate speech only.`、`Target duration`、两条录音声明、八条禁止音频类型声明，以及`Speaker → Voice characteristics → Speaking rhythm（需要时）→ Performance style → Avoid → Read naturally`顺序；唯一Template引用正确；Audio Reference元数据绑定同一CHAR Version并记录来源与授权；A/B/C路由样例分别为触发/不触发/不触发。

竹雀的孔老板、老板娘、吴御史、诸葛亮只作为项目Voice Bible示例，不是全局默认人设或音色模板。

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

触发：镜头包含人物注意、反应、情绪变化、对白倾听、压抑/伪装、哭笑、群体反应或身体状态影响表演。

输入拥有者：Script / Scene事实、Character Asset与基线、人物关系、Shot Purpose、Action / Blocking、Dialogue / Sound、Camera / Composition、Lighting与边界状态。

输出拥有者：STATE-04由Project Bible表演字段拥有；STATE-06由Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部表演模式只使用PEX-01至PEX-36，最终Prompt不得输出PEX或AU编号
- 每个情绪变化必须有已确认刺激、注意变化、至少一项可见反应、行动选择与稳定结束状态
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
- 每个Clip拥有包含Shot清单、Entry、连续动作、摄影机/空间关系、道具连续性、内部逐镜状态链、稳定Exit、`[Gxx尾帧]`与下一Clip Handoff
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

Module Type：STATE-07与STATE-08共享的强制Quality / Continuity Knowledge Gate；不创建新主STATE、不创建新ID命名空间、不拥有STATE-08最终字段。

触发：每个STATE-07候选Clip形成执行合同时执行前置版；每个STATE-08 Confirmed Clip在正式Prompt编译与Template Mapping前执行最终版。普通资产制作、海报、Storyboard或纯音色任务不独立触发。

Required Inputs及唯一来源：上一Clip End State / Tail-Frame Use、当前Clip Start Requirement与Clip边界由STATE-07拥有；逐分镜时空与剧情事实由Script / Scene拥有；资产与Prop State由Asset Registry / STATE-03拥有；Spatial Blocking与Shot几何由STATE-06拥有；Transition事实由已确认Shot / Transition设计拥有。

Output拥有者：STATE-07检查记录由`templates/20_clip_plan.md`拥有；STATE-08只把通过结果投影到`templates/10_video_prompt.md`既有字段；`knowledge/clip_preflight_check.md`只拥有分类、检查顺序、失败条件与返回路由。

允许读取：Confirmed Clip Production Plan、Detailed Shot Design、Spatial Blocking、Asset Registry、Reference Budget、Transition、相邻Clip边界与实际首尾帧。允许写入：Clip Plan中的Preflight记录、既有预算/连续性/风险栏目及STATE-08内部Projection / QA记录。

下游消费者：STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation与STATE-09 Review。

不变量：视觉连续、剧情连续、主动切场/切世界三选一；只有视觉连续强制正式引用上一尾帧；每分镜先锁定World-State再筛选资产；跨世界/时空/尺度/形态变化先完成转场五要素；逐镜锁定角色精确数量、空间关系与关键道具状态；Reference Budget最后执行且最终≤9；任一适用项失败不得确认Clip Plan或输出STATE-08 Prompt。

禁止修改：剧情、世界观、Active Asset Version、角色身份、Shot目的/顺序、Spatial Blocking、主Pipeline、STATE-08 Schema。禁止用Preflight为补救错误而新增转场媒介、角色、道具、FX或剧情事件。

冲突路由：剧情/世界事实返回事实拥有者；资产/道具形态返回STATE-03；Shot / Blocking /转场设计返回STATE-06；Clip边界、预算或执行合同返回STATE-07；仅最终文案投影错误留在STATE-08。

Validator可检查的不变量：两条Workflow Resource Gate均显式引用本模块；STATE-07 Template存在Preflight记录与PASS / Return Route；STATE-08 Template没有新增Preflight字段；五个Acceptance Scenarios和三条高优先级规则存在；所有显式文件引用有效。

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
- 每个Clip必须为4—15秒；Clip内分镜保持原顺序、逐镜字段和显式状态链
- Continuous Handoff通过上一段`[Gxx尾帧]`建立下一段首帧引用；Motivated Discontinuity明确不继承及重建原因
- 每个Clip交付前强制验证【参考资产】、首帧来源/要求、稳定尾帧接口和前后Clip连续性关系；缺任一项不得输出
- 先执行Voice Reference Override Gate：固定字段`音色特征：`始终保留；有适用Voice/Audio Reference时写明Reference锁定且不得文字重定义，并删除其他字段中的全部文字音色描述；无适用Reference但已有Confirmed Voice Profile时以其填充；两者都不存在时使用`No Voice Asset`声明且不得自动触发AUDIO模块；无对白时明确无对白

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
- 投影到上一G段前置【尾帧限制】、下一G段【首帧参考】、按空间/动作连续性条件决定的【参考资产】正式引用，以及“镜头结尾状态”“与下一镜衔接”和下一镜“起始状态”；跨场景时上一尾帧通常不进入下一段【参考资产】，只作人物与视觉连续性核对
- 同期声音桥只使用对白、环境声、动作声、呼吸、Foley或剧情内声源
- 同一Clip内使用逐镜状态链；跨Clip Continuous Handoff使用`[Gxx尾帧]`连接独立Prompt Package；Motivated Discontinuity保留明确不继承声明

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

必须从可验证Checkpoint继续，保持Accepted Unaffected Artifacts，不创建新主STATE。State Source只按`rules/state_source.md`选择；本模块不得复制优先级或Chat fallback细节。禁止把历史聊天文本当作状态、选择最近项目、静默合并不同Project ID、重写成功Checkpoint之前内容，或在第三次同类失败后继续盲重试。

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

## Change Safety Checklist

模块接入完成前检查：

- 主Pipeline仍只包含STATE-00至STATE-09
- 原有Template仍拥有原有阶段Schema
- 新ID命名空间没有冲突
- 新Workflow有明确触发与Not Applicable路径
- 新输出保存在Active Project Root
- 所有显式内部文件引用均存在
- 正常样例通过Validator
- 缺字段、重复ID或越权ID样例被拒绝
