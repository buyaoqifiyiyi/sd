# SD Film Module Contracts — Auxiliary Modules

本文件是模块接口合同的一部分；Authority Matrix 与 Stable Interface Rules 留在 `references/module_contracts.md`。本文件不拥有归属判定，也不得复制该框架。

## Clip Preflight Check Module Contract

Module Name：`Clip Preflight Check / Clip生成前检查`。

Module Type：STATE-07与STATE-08共享的强制Quality / Continuity Knowledge Gate；同时拥有Visual Blocking Anchor Assessment / Persistence算法，并通过`references/ref_sketch_master.md`消费独立的Sketch Presentation Authority合同；不创建新主STATE、不创建平行Registry、不拥有STATE-08最终字段。

触发：每个STATE-07候选Clip形成执行合同时执行Visual Blocking Risk Pre-Assessment；每个STATE-08 Confirmed Clip在正式Prompt编译与Template Mapping前执行Final Assessment，包括用户指定Clip、说“下一个 / 下一步 / 继续”及批量中的每个Clip。普通资产制作、海报、Storyboard或纯音色任务不独立触发。

Required Inputs及唯一来源：上一Clip End State / Tail-Frame Use、八组`Clip End-State Record / Next-Clip Carryover`、Visual Anchor State、当前Clip Start Requirement与Clip边界由STATE-07 / 当前STATE-08 Checkpoint拥有；逐分镜时空与剧情事实由Script / Scene拥有；资产与Prop State由Asset Registry / STATE-03拥有；Scene Spatial Snapshot、Pose Hierarchy、Relationship Topology、Action PREVIS、Performance Goal / Performance Arc Map与Shot几何由STATE-06拥有；Transition事实由已确认Shot / Transition设计拥有。

Output拥有者：STATE-07检查记录由`templates/20_clip_plan.md`拥有；STATE-08只把通过结果投影到Selected Model对应Template的既有参考字段；`knowledge/clip_preflight_check.md`拥有分类、检查顺序、失败条件与返回路由；`templates/23_visual_blocking_sketch_prompt.md`唯一拥有Technical Visual Blocking Sketch的图像生成输入包与Candidate Evidence Record，不拥有Assessment或最终视频Prompt Schema。

允许读取：Confirmed Clip Production Plan、Detailed Shot Design、Spatial Blocking、Action PREVIS、Asset Registry、Reference Budget、Transition、相邻Clip边界、实际首尾帧、已存在Visual Anchor Revision，以及`references/ref_sketch_master.md`中母版图片的真实注册状态与Presentation合同。允许写入：Clip Plan现有Preflight / Spatial State / Continuity Risks / Reference Budget栏目、当前STATE-08 Checkpoint / Projection / QA，以及绑定单一Clip的Confirmed `REF-SKETCH-XX`。不得新增主STATE、顶级Template字段或Canonical资产类型；不得把母版示例内容写入Current Clip事实。

下游消费者：STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation与STATE-09 Review。

不变量：视觉连续、剧情连续、主动切场/切世界三选一；再在既有判定中明确A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】。A/B标记`Tail Frame Required = YES`并在【参考资产】列统一`REF-TAIL`、分别声明“同镜头连续承接用途”或“空间/站位/景别参考用途”；未提供时写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。A使用固定直接承接句，B明确另起新镜头重新构图且不使用该句。C标记`NO`，不列`REF-TAIL`，用Canonical资产、Spatial Blocking与文字规则重建。逐角色还必须通过Performance / Emotion Check：Inherited Baseline、Trigger、Pre-action / In-action / Post-action Residue、Arc Endpoint、Intentional Hold证据、Next-shot Carryover与多人相对表演层级可复算；静态标签、无刺激重置、固定脸完成动作、全员同强度或全员同脸固定FAIL。每个Clip在STATE-07只标`NONE / POSSIBLE / REQUIRED`草图风险；母版可用性不得改变Assessment。STATE-08每次单Clip Prompt前做Final Assessment。Final=`NONE`直接Prompt；Final=`REQUIRED`先生成 / 验证 / 注册Confirmed `REF-SKETCH-XX`，再完成真实输入绑定：2.0写真实文件/受控ID，2.5与H3 All-Reference写真实`@图片N`并计入预算；任一不可提交时Prompt Pending而不是“加入参考资产”即算完成。生成时遵循`Master Template carries sketch language; Current Clip data carries blocking content.`：真实已注册`REF-SKETCH-MASTER`只拥有Sketch Presentation Authority；当前`REF-SKETCH-XX`才拥有Clip Blocking Authority。母版文件不可用时必须标记Text Contract Fallback，不得声称已使用视觉母版。人物绘制层统一服从`references/ref_sketch_master.md`的`Neutral Mannequin Representation Rule`：S / P / A / Combined使用同一套无性别技术人偶，仅由角色名 / ID、技术颜色与位置标签区分；Character Asset独占性别、脸、发型、服装、年龄感、体型与身份Authority。每张当前草图还须通过Template Content Leakage Check与Character Appearance Leakage Check；明显人物外观或性别化体态泄漏固定判`FAIL = Character Appearance Leakage / Identity Contamination`。普通Prompt Rewrite必须复用原草图；只有Blocking Signature实质改变时允许KEEP / REPLACE / RETIRE / CREATE。当前草图只拥有Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path，不覆盖Character / Environment / Prop Authority。每分镜先锁定World-State，再按`Clip End-State Record`、当前目标与Continuity Risks对Eligible资产执行最小充分Reference Selection / Routing；身份/空间结构/道具造型/Visual Blocking/A-B尾帧/光线场景状态分别使用正确来源，C不选旧尾帧，不因Registry存在或预算空位全选。`REF-SKETCH-MASTER`默认不进入最终视频【参考资产】且不计视频图片预算；跨世界/时空/尺度/形态变化先完成转场五要素；逐镜锁定角色精确数量、空间关系与关键道具状态；Reference Budget最后执行且默认Projected Final Count≤9；只有Seedance 2.5扩展Reference Audit通过时才按已验证上限审计30图 / 10视频 / 10音频 / 合计50及各自30秒时长，且每项有唯一Primary Role。

禁止修改：剧情、世界观、Active Asset Version、角色身份、Shot目的/顺序、Spatial Blocking、主Pipeline、STATE-08 Schema。禁止用Preflight为补救错误而新增转场媒介、角色、道具、FX或剧情事件。

冲突路由：剧情/世界事实返回事实拥有者；资产/道具形态返回STATE-03；Shot / Blocking /转场设计返回STATE-06；Clip边界、预算或执行合同返回STATE-07；仅最终文案投影错误留在STATE-08。

Validator可检查的不变量：两条Workflow Resource Gate均显式引用本模块；STATE-07 Template存在Preflight记录、Performance / Emotion Check与PASS / Return Route；STATE-08 Template没有新增Preflight字段；Five Global High-Priority Rules、十三个Acceptance Scenarios、Before-Single-Clip-Prompt Gate、Blocking Signature、四种Reassessment结果、母版注册状态、两级Authority、七项Layout Validation、Template Content Leakage Check与Character Appearance Leakage Check存在；所有显式文件引用有效。`Asset Status=REGISTERED`时真实相对文件必须存在；`UNAVAILABLE`时不得出现已注册路径声明。Candidate Evidence必须由`scripts/validate_sd_film.py sketch`拒绝单幅电影插画、缺失版式项、Blocking不匹配、模板内容泄漏、人物外观 / 身份污染或Confirmed前图片不可读。

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

Validator不变量：候选未确认不得入库；经验不占用现有实体ID命名空间；经验不出现在主Pipeline STATE列表；经验应用不绕过Completion Gate；每次经验入库触发完整Skill Update Self-Check。每个候选与确认记录必须带`Class: P / O / C`；`O`类必须带`valid_as_of`；`Triggers`、`Procedure`、`Failure Signals`、`Exceptions`、`Counter-examples`缺任一字段不得入库；`coupled_uncharacterized`来源不得升级为`P`，也不得据此宣称某一措辞必然有效。

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

## Fast Automation Policy Contract

Module Type：显式opt-in的Rule；不创建主STATE、项目事实、独立确认状态、Template字段或外部权限。

Owner：`rules/automation_mode.md`。触发只能来自用户当前明确的自动推进指令；状态合同只镜像`Automation Policy`。`rules/progression_rules.md`消费其已确认的Eligible Work，`rules/completion_gate.md`只在本合同允许的范围内接受自动接受证据。

FAST可以压缩已继承项目Built-in Image默认项的当前Prompt确认与内置图片生成批次、STATE-06/07的已通过QA设计工件与同轮Visual Blocking Anchor完成真实输入绑定后的Prompt编译；它不得锁定Production Script Proposal、自动确认Candidate Image、首次确认或更改项目图像/视频模型、调用外部服务或写Review PASS。任何自动接受都必须保留Artifact / Version History证据，并在冲突时返回当前事实owner。

允许读取：当前用户指令、Selected State Source、当前Workflow、已确认上游事实和既有QA。允许写入：状态合同中的`Automation Policy`及既有Artifact / Version History中的自动接受证据。不得改写Production-Locked Script、Canonical Asset、用户确认、主Pipeline、最终Template Schema或外部授权。

Validator不变量：只允许`STANDARD / FAST`；旧状态缺失值迁移为`STANDARD`；FAST不改变Hard Stop，Candidate Image和Production Script Proposal仍要求用户批准；任何文件引用都指向本Rule owner。
