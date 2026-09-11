# SD Film Regression Scenarios — System

本文件是回归集的一部分；完整范围与其余文件见 `references/regression_scenarios.md` 的 Regression File Index。脚本仍只把本文件当作回归语料的一部分，不构成独立权威。覆盖写作、Runtime、模型适配、FAST、交付校验、美学锁与维护（R24、R27—R35、R48—R52）。

## R24 Screenwriter Module / Writer Intelligence End-to-End

### R24-A Idea — Rainy-night Two-woman Reunion

输入：`调用sd，写一个雨夜双女主重逢短片。`

PASS：Creation Brief进入Screenwriter Module，先以最小充分方式建立双方Want / Objective / Hidden Objective、阻力、关系弧、Dramatic Question、Information Architecture和Setup / Payoff，再生成Production Script Proposal与Writer → Director Handoff；剧本不出现焦段、机位、运镜、SHOT / CLIP或Shot Count。

FAIL：只按氛围生成对白；先写35mm / 特写 / 慢推；或强制用户填写完整WRITER INTENT PACKET。

### R24-B Existing Script — Diagnose Before Rewrite

输入：用户上传完整剧本，没有授权改写。

PASS：先诊断causality、motivation、scene necessity / value change、Writer Beat progression、conflict / stakes、subtext、setup / payoff、information architecture、character / relationship arc与ending payoff，并映射到现有Opportunity Report；停在User Decision Gate，不改正文。

FAIL：自动重写、只做导演镜头分析、跳过Writer Diagnosis或把`下一步`当改写授权。

### R24-C Motivation — Convenience Action Rejected

输入：人物没有前因地“突然坐到对方身边”。

PASS：追溯并要求`Trigger → Character Interpretation → Desire / Intention → Decision → Action → Consequence → New State`；缺任一使动作不成立的核心环节时标记motivation / causality问题，不直接接受剧情便利动作。

FAIL：因为后续剧情需要就保留，或用Camera / 表情装饰掩盖缺失动机。

### R24-D Dialogue — Subtext Opportunity, Not Mechanical Deletion

输入：角色说`我一直很想你`，但既定性格与当场目标不支持直说。

PASS：检查`Dialogue → Surface Meaning → Subtext → Hidden Objective`，指出可通过试探、回避、动作、沉默或道具承载的机会；只在角色与场景逻辑要求时改写，并保留对白可能性。

FAIL：机械删掉所有直白对白，或不检查角色目标就把台词当合格信息说明。

### R24-E Scene — No State Change

输入：一场戏从头到尾没有Information / Relationship / Decision / Power / Emotional / Expectation变化，也无不可替代Setup / Hold / Transition功能。

PASS：标记`weak / replaceable scene`，说明缺失的Value Change并路由到Writer Diagnosis；不靠增加漂亮镜头伪装场景价值。

FAIL：只因场景有气氛或对白就保留，或强制每场必须正负价值翻转而不允许必要Breath / Setup。

### R24-F Setup / Payoff — Timing Survives Production

输入：前场Planted Detail在后场形成Payoff。

PASS：Writer Packet记录Setup / Payoff obligation与信息时机；Scene / Clip / Prompt / Editing保持它，既不遗漏也不提前暴露；Review可追溯到具体义务。

FAIL：Clip边界切断回收、Prompt提前展示真相、Editing交换顺序，或后场重新发明无来源Payoff。

### R24-G Writer Beat Is Not Shot

输入：一个“认出旋律”的Writer Beat。

PASS：Writer只定义Trigger、Interpretation、Decision / Response与New State；Director可用一个Shot、多个Shot或与相邻Beat同处一个长镜头表达，依据观众体验、表演、空间与可执行性决定。

FAIL：Writer强制Shot Count / 特写，或Shot Design无法追溯到Writer Beat / 合法Director Purpose。

### R24-H Prompt — Preserve Both Authorities

输入：已确认Writer Intent与Director Decision的关系场景进入STATE-08。

PASS：最终Prompt保留角色意图、潜台词、Beat order、Setup / Payoff、Information timing与Relationship Delta；Camera仍只来自Director Decision。固定STATE-08 Schema不变，Writer Packet及内部标签不输出。

FAIL：潜台词被压扁成直白台词/表情，Beat顺序改变，Writer越权生成镜头参数，或Director Camera被Writer规则覆盖。

### R24-I Review — Unmotivated Behavior Is Writing Failure

输入：技术画面正确、导演呈现合理，但人物行为没有动机。

PASS：Story Review判`WRITING FAILURE`并返回STATE-01 Screenwriter Module；不判Prompt / Generation failure，不要求只重写Prompt。

FAIL：因画面和导演层通过而KEEP，或把缺失动机路由到STATE-08。

### R24-J Genre — No Universal Conflict Formula

输入：分别运行动作片、商业短剧与青春文艺片案例。

PASS：动作片优先物理目标/阻力与动作因果；商业短剧可按已识别目标加载可选hook / escalation adapter；青春文艺片允许克制、信息不对称与关系压力。三者不共享强制冲突密度、对白密度、固定Beat数或三幕百分比。

FAIL：全局套用短剧爽点、固定15 Beat、强制每场反转，或用青春微表演规则压制动作可读性。

### R24-K Runtime — Continue / Reload / Re-entry Preserved

输入：已验证Project Context后分别说`下一步`、`继续`与`重新调用sd / 按当前Skill继续`。

PASS：普通继续沿合法Checkpoint推进且保留Writer / Director Packet、Confirmed Assets、Accepted Take Canon与Shot-State Memory；显式Reload按现有合同重读Skill Version / Build ID和owner，不重建已确认剧本。

FAIL：新增STATE、普通继续触发全量重载、丢失Writer Packet、跳过确认Gate，或显式Reload沿用旧owner定义。

---

## R27 Clip Execution Mode Acceptance

### R27-A Unmotivated Camera Jump Fails

输入：两个相邻Shot被标记为`多Shot有动机剪辑`，但只有“切到近景”或无动机机位跳变，没有叙事功能、切点、视觉媒介或切后重建。

PASS：STATE-07 Clip Preflight判`FAIL`，不得把随机跳变包装成导演剪辑；返回拆分或补齐上游Director Decision。

FAIL：仅因总时长合格就把两个Shot合进同一Clip。

### R27-B Mid-Take Axis Change Fails

输入：`多Shot连续生成`在无可感知越轴过程、角色换位或隔离镜头的情况下中途换轴。

PASS：连续生成判`FAIL`；维持同一轴线，或改为已确认的有动机剪辑并在新机位稳定重建。

FAIL：把“连续长镜头”当作可任意跳转摄影机的许可。

### R27-C Ear-Mirror Match Cut Passes

输入：现实中角色举起耳镜；耳镜玉光占满画面，作为明确切点与视觉媒介；切后在玉境中重新建立角色、环境、道具、摄影机与稳定构图。耳镜玉光和抬手是保留锚点，世界与机位是允许改变锚点。

PASS：Director确认“揭示耳中玉境”的叙事功能后，可标为`多Shot有动机剪辑`；既有`起始状态 / 画面描述 / 镜头结尾状态`承载切前、切点和切后信息，不新增STATE或STATE-08字段。

FAIL：没有玉光遮幅、切前结束或切后稳定构图就直接换到玉境。

### R27-D Incomplete Motivated Cut Fails

输入：Clip声明`多Shot有动机剪辑`，但缺少切点/视觉媒介，或切后没有新世界、角色、环境、道具、摄影机与稳定构图的重建状态。

PASS：Validator与Clip Preflight失败，并要求补齐既有生成合同内的切镜合同。

FAIL：以“导演意图”或“有电影感”代替可执行切镜信息。

### R27-E Capacity Downgrade Returns STATE-07

输入：一个已具备有动机切镜合同的Clip同时要求高身份保真、复杂多角色动作、口型、FX、世界切换和摄影机重建，模型容量不支持。

PASS：不编译STATE-08，`Return Route = STATE-07 / 拆分Clip`；保留已确认剧情与导演意图，在多个Clip中重建边界。

FAIL：继续生成、删除必要故事信息，或用无原因跳变掩盖容量不足。

---

## R28 Seedance 2.5 Compatibility Regression

Compatibility marker: R20-D A3 Action Remains Technical Previs is not a distinct execution rule; its technical-previs coverage belongs to R20-C, while R20-D remains the simple-head-turn case.

### R28-1 Seedance 2.0 Default Short Clip

输入：当前批次锁定`Seedance 2.0`，未选择其他模式。

PASS：仅一次Lock后使用4—15秒Standard Clip、≤9图片预算、既有A/B/C `REF-TAIL`和固定STATE-08模板；不出现2.5字段、时间码或额外Prompt栏目。

### R28-2 Seedance 2.5 Standard Clip

输入：Lock=`Seedance 2.5`，目标时长10秒，未作任何Long-form选择。

PASS：默认仍使用4—15秒Standard Clip、最小充分参考与既有连续性风险降级；30秒不是默认时长。

### R28-3 Seedance 2.5 Long-form Clip

输入：Lock=`Seedance 2.5`，用户选择目标时长20秒；镜头链、空间关系、表演和动作密度均通过严格预检，网关状态未知。

PASS：无需用户额外选择Long-form，计划自动使用16—30秒内部路由；仅严格预检失败时才重跑STATE-07拆分为短Clip，不回退已确认Detailed Shot Design。未知网关状态不触发15秒限制；实际平台拒绝才触发最小调整。

### R28-4 Seedance 2.5 Video Extension

输入：Lock=`Seedance 2.5`，用户选择Video Extension并提供实际上一段成片。

PASS：将该成片登记为受控`REF-VIDEO`，同时保留Canonical资产、首/尾帧、End-State与A/B/C规则；不得以视频输入替代它们。

### R28-5 Seedance 2.5 Targeted Edit

输入：Lock=`Seedance 2.5`，用户明确要求修改既有视频的一段内容。

PASS：只在既有分镜正文的适当字段写受控时间段语义；不新增时间轴/目标模型字段。非Targeted Edit仍拒绝时间码、逐秒分段和帧率描述。

### R28-6 Clay Render Authority Isolation

输入：一个已验证、无性别`REF-SKETCH`作为2.5 Clay Render / 白模空间调度参考。

PASS：只消费位置、朝向、距离、拓扑、机位、姿态、视线和动作路径；Character外观/服装/年龄、Environment材质、灯光、色彩和最终画风仍由Canonical Authority控制。

### R28-7 High Reference Capability Uses Minimal Sufficiency

输入：2.5网关可确认支持高于9张图片、视频或音频参考。

PASS：先按当前Clip风险筛选最小充分集合，只有超过实际有效上限才整合/裁剪；不机械填满30图、10视频或10音频；音频仍须当前用户明确opt-in。

### R28-8 Lock Before Clip Integration

输入：STATE-06已完成，Project State没有Target Video Model。

PASS：在任何STATE-07 Clip整合之前询问一次2.0/2.5；不得等到STATE-08最终Prompt才问。

### R28-9 Locked Model Does Not Re-prompt

输入：Project State和Confirmed Clip Plan均为同一LOCKED模型与执行Profile。

PASS：STATE-07/08直接消费该Profile，不重复询问。

### R28-10 Pre-confirmation Model Switch Scope

输入：Clip Plan确认前用户从2.0切换到2.5或反向切换。

PASS：只使受影响STATE-07/08执行产物重跑；Production-Locked Script、Confirmed Assets、Scene Breakdown和Detailed Shot Design保持Accepted。

### R28-11 MiniMax H3 Standard Clip

输入：Lock=`MiniMax H3`，目标时长12秒，当前Clip有两个实际已确认角色参考图，用户要求中文对白与口型一致。

PASS：只选择`adapters/minimax-h3.md`，保持12秒单Clip并按最小充分原则使用真实参考图；将准确台词和最小口型/中文语义写入既有`台词：`字段，保留当前Clip风险的简洁负面提示词、永久无BGM禁令及`非叙事性音乐：N/A`；不写Seedance Video Extension、Seedance时码式Targeted Edit或未验证的上传上限。

FAIL：把Seedance 2.5的30秒、Video Extension、Clay Render或时码式Targeted Edit移植给H3；忽略H3支持的首/尾帧、全能参考或已有视频编辑；把未上传的图片写成已投喂；仅因存在对白就自动写入音色身份。

## R29 Model Compilation Template Router Regression

### R29-1 Seedance 2.0 Stable Compiler

输入：Lock=`Seedance 2.0`，已确认一个10秒Clip。

PASS：内部Profile选择且只选择`Seedance 2.0 Stable Compiler`，沿用短Clip、≤9图片和既有连续性合同；不要求2.5参考映射或任务语义，最终Template无模型/Compiler字段。

### R29-2 Seedance 2.5 Native Compiler

输入：Lock=`Seedance 2.5`，Clip使用已确认的参考素材。

PASS：内部Profile选择且只选择`Seedance 2.5 Native Compiler`并读取2.5 Profile；素材映射只在内部记录来源、用途与Authority，最终Template字段、顺序和排版保持不变。

### R29-3 Native Reference And Frame Semantics Do Not Leak

输入：2.5 Clip使用合法首/尾帧、Clay Render空间草图和实际`REF-VIDEO`延展输入。

PASS：内部语义分别保留首尾帧、草图Authority和延展输入，仍不取代Canonical / REF-TAIL / End-State；最终Prompt不出现上传顺序、内部角色、API字段、Target Model、Execution Mode或Compiler字段。

### R29-4 Targeted Edit Is Conditional

输入：2.5用户明确编辑既有视频，随后另给一个Standard Clip。

PASS：前者只在既有分镜正文表达受控编辑范围与保持项，后者不含时间码或逐秒区间；两者共用固定最终Schema。

---

## R30 FAST Continuous Chain Regression

### R30-A Explicit Low-Confirmation Language Enables FAST Only

输入：项目已有合法State Source，用户说“尽量少确认，只在关键节点停，自动完成可逆步骤”。

PASS：写入`Automation Policy: FAST`并读取唯一owner `rules/automation_mode.md`；不新建模式、STATE或Schema。表达不锁定Production Script Proposal、不选择模型、不批准Candidate Image、不提交外部服务，也不构成Review PASS。

FAIL：把用户的低确认偏好解释为全部授权，或因为措辞未包含“Fast Mode”而仍强制STANDARD。

### R30-B FAST Carries Verified Internal Work Through Prompt Delivery

输入：STATE-04起的事实、资产、视频模型和Execution Profile均已锁定；STATE-04/05/06/07的QA均通过；三个Execution Clip均Confirmed，其中CLIP-02需要`REF-SKETCH`。

PASS：连续推进STATE-04→05→06→07→08，自动接受Detailed Shot与Clip Plan；CLIP-02的草图验证、注册后同轮编译Prompt；三个完整Prompt按顺序交付，单轮容量不足时仅在完整Clip之间分批，下一次普通推进直接续交。每一阶段仍完成既有QA、预算、无BGM和状态写回。

FAIL：要求用户在STATE之间逐次确认、草图后额外等待、仅因多Clip就停止在第一个Prompt，或跳过QA / Completion Gate。

### R30-C FAST Stops At Non-Reversible Boundaries

输入：FAST项目在资产图像模型未选、外部Midjourney Prompt已编译、Candidate Image已回传、或准备提交视频生成时继续推进。

PASS：首次/变更模型时请求选择；已锁定Midjourney批次只自动交付外部提交包；回传Candidate后停在批次审阅，用户批准后才Active / Canonical；外部视频生成由用户显式提交；未实际查看视频不得Review PASS。

FAIL：替用户选择模型、代投Midjourney或视频服务、把Prompt写成生成结果，或自动把Candidate升级Canonical。

---

## R31 Candidate Output Triage And Cleanup Regression

### R31-A Asset Run Keeps One Valid Candidate And Removes Extras

输入：CHAR-001正式资产Prompt预期一张五区角色设定图；本次GPT Image 生成返回三张：C01正确、C02为重复画布、C03是错误角色且带水印。三个未确认输出均位于当前运行可验证的临时目录。

PASS：视觉核验后只将C01登记并展示为`KEEP` Candidate，报告“保留 C01，仍待图片确认”；C02 / C03标为`DISCARD`、报告最短原因、从Candidate References / Registry / 下游参考移除并删除其已核验临时文件。不得要求用户从错误或重复图中选择，C01也不得因此自动Canonical / Active。

FAIL：把三张都显示为候选、只说“有错误”却不指明保留项、把C02 / C03计入预算，或删除C01 / 已确认资产。

### R31-B Valid Aesthetic Alternatives Need One User Choice

输入：ENV-001回传两张均满足当前Prompt、资产ID和空间结构的单图候选，差异仅是同等可用的阴天光照细微倾向，系统没有客观依据判断哪张更符合用户偏好。

PASS：只展示这两张`NEEDS_USER_SELECTION`候选，标明ID与可见差异；不删除任一项，不将其自动升级Canonical / Active，等待用户的图片选择与批准。

FAIL：用FAST替用户做审美选择、把两张都登记为Active，或将未确认的合格图直接删除。

### R31-C Sketch Failure Is Removed Before Registration

输入：CLIP-04需要`REF-SKETCH`，生成结果一张通过所有技术验证，另一张含角色发型、服装和电影光效。

PASS：只保留并报告技术合格草图；泄漏图为`DISCARD`，从Candidate Evidence、Confirmed Visual Anchor、参考资产与图片预算移除；临时本地文件归属明确时直接删除，否则说明无法物理删除但不会再引用。合格草图仍须完成原有验证和注册，不成为角色资产。

FAIL：把失败草图也展示或登记、只报告“草图有问题”不说保留哪张、因自动清理而跳过Sketch Validation，或删除已Confirmed草图。

---

## R32 Unified Delivery Package Regression

### R32-A FAST Aggregates Preproduction And Execution Without Flattening Artifacts

输入：核心资产、Production-Locked Script和事实已确认；视频模型/Profile已锁定；STATE-04至STATE-08所需输入完整且所有QA通过。用户启用FAST并要求继续。

PASS：内部按STATE-04→05→06→07→08依序读取、检查、写回；对外以`Preproduction Package`交付可查看的Visual Direction摘要、完整Scene Breakdown与完整Detailed Shot Design，再以`Execution Package`交付完整Clip Plan和每个Clip的完整目标模型Prompt。每个Template原字段、顺序和内容保持完整；不得将多个阶段压为一张新总表或用“同上”替代。每个Clip仍执行预检、参考预算和无BGM边界。

FAIL：把包名写进Project State或最终Prompt字段、跳过中间QA、只交摘要、先输出Prompt后形成Clip Plan，或因聚合改写Script / Director Intent / Canonical资产。

### R32-B Hard Stop Truncates The Package At The Nearest Boundary

输入：FAST项目完成STATE-06，但尚未选择视频模型；另一项目在资产Candidate Image审阅前要求一次性完成全流程。

PASS：前者可以结束`Preproduction Package`，随后只展示首次模型选择；不得虚构Execution Package。后者只交付`Asset Candidate Package`的筛选结果并停在候选图确认，不进入STATE-04。用户要求统一输出不替代模型选择或Candidate / Canonical批准。

FAIL：为了交付完整包默认挑选模型、把候选图升级Canonical、跳过STATE-03，或把外部提交当作包内自动步骤。

### R32-C Standard Mode Aggregates Only Already-Legal Results

输入：STANDARD项目说“按包交付”，但当前Detailed Shot尚未被确认，且没有FAST自动接受资格。

PASS：可以将已经合法完成的相邻成果组合展示，但在当前Detailed Shot确认Checkpoint停止；不得用“按包交付”把未展示Shot或Clip Plan视为确认，更不得提前编译STATE-08 Prompt。

FAIL：因为用户要求合并展示就绕过Confirmation Input Semantics、Completion Gate或Hard Stop。

---

## R33 Model-Specific Main Style Regression

### R33-A Seedance 2.5 Has A Dedicated Main Style Field

输入：Seedance 2.5的CLIP-02继承已确认的低饱和海边Visual Grammar Baseline，当前剧情需要人物在暮色中靠近，且时间线已有动作与镜头设计。

PASS：`尾帧限制：`后、`全局叙事与画面设定：`前存在独立`主风格：`；它写项目特定风格含义与当前Clip必要的少量可见载体，例如真实暮光来源、低饱和灰蓝关系、克制观察机位与表演尺度。`全局叙事与画面设定：`只写主体、地点、事件、主题和核心镜头意图，不重复完整风格段；时间线继续承载当前动作、摄影机与光色变化。

FAIL：把风格只隐含在全局叙事或时间线、在多个字段机械重复，或因新增风格字段删掉多模态参考 / 时间线 / 无BGM边界。

### R33-B H3 Keeps Three-Part Structure With Main Style First In Core Idea

输入：MiniMax H3的CLIP-03使用已确认青春片Visual Grammar Baseline，要求人物在厨房内完成一个克制反应。

PASS：顶级结构仍只有`参考素材说明：`、`核心创意：`、`画面过程说明：`与既有末尾限制；`核心创意：`的第一行固定为`主风格：`，写项目特定含义和最小充分的可见载体，第二行再写主体、地点、事件与必要运镜。不得新增与三段式竞争的顶级风格段。

FAIL：只写孤立风格标签、将风格藏在第二行后、增加H3顶级`主风格：`段、混入Seedance 2.5时间线或删除`非叙事性音乐：N/A`。

---

## R34 Required Sketch Submission Binding Regression

### R34-A Project Model Choice Is Early, Clip Capability Is Late-Bound

输入：新项目在STATE-00确认`GPT Image + MiniMax H3`；STATE-03新建角色与环境资产；后续CLIP-04为H3 Start-End模式且Final=`REQUIRED`。

PASS：STATE-03直接继承GPT Image而不逐批重复提问；STATE-06/07复核H3 Start-End无法提交Required草图，只给出改为H3 All-Reference、改选兼容模型或返回上游降低Blocking的最小路径。不得为了兑现项目偏好把`REF-SKETCH`伪装为首/尾帧，也不得重做剧本、资产或导演设计。

### R34-B Required Sketch Is A Real Submitted Input For Every Compatible Model

输入：`REF-SKETCH-04`已验证、Confirmed、Signature匹配且其真实文件/受控ID可访问；CLIP-04的Final=`REQUIRED`，预算仍有一个图片位。

PASS：Seedance 2.0的`参考资产：`列出`REF-SKETCH-04｜真实文件/受控ID｜实际提交图片输入`；Seedance 2.5的`多模态参考资产：`有其真实`@图片N`；MiniMax H3 All-Reference的`参考素材说明：`有其真实`@图片N`。三者都把它计入实际图片预算，且唯一Authority为Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path；Canonical角色、环境、道具、材质、灯光、色彩与最终画风不受草图控制。

### R34-C Missing Or Incompatible Sketch Input Cannot Be Claimed

输入：Final=`REQUIRED`，但`REF-SKETCH-04`文件/受控ID不可访问，或其Signature过期，或2.0/2.5预算已满，或H3仍为Start-End / Video Edit。

PASS：`REF-SKETCH Submission Compatibility=FAIL`，Prompt Pending并给出恢复输入、腾出预算、改H3 All-Reference、改模型或返回Blocking的最小路径。最终文字不得写“已使用 / 已提交草图”，不得作为输入就绪生成包交付。

### R34-D None, Rewrite And Replacement Boundaries

输入：Final=`NONE`的简单Clip；以及一个Signature不变的Prompt Rewrite与一个Blocking重构后的REPLACE。

PASS：NONE没有草图空槽位、占位或图片预算；Rewrite复用同一实际`REF-SKETCH`输入但不重复生成或计数；REPLACE从输入与预算移除旧草图，绑定新的可访问、Signature匹配草图后再编译。

## R35 Declared-Existing Asset Handling Regression

### R35-A Declared Assets Are Listed, Not Solicited

输入：用户在STATE-00 / STATE-02说明“角色和环境资产我这边已经有了”，未提供任何文件或路径；项目仍需判定CHAR / ENV / PROP / FX。

PASS：STATE-02照常输出完整资产清单、Tier判定与Support Board计划，已声明条目标注`已有（用户声明）`、其余标注`待制作`；不要求用户上传、发送、粘贴、提供路径、文件名或自有素材清单，不重复追问，不写BLOCKED，不把停止点放在素材索取上；Registry仍为`Prompt Status: Not Started / Image Status: Not Generated / Confirmed Status: No`。

FAIL：要求用户先交资产或上传参考图；把资产清单变成逐项缺口盘问；因文件未提供或不可读而停住；或在用户未说明前虚构其持有 / 缺失状态。

### R35-B Declaration Is Not Registration

输入：用户声明“角色图已有”后未提供文件，随后要求继续到STATE-03。

PASS：`已有（用户声明）`不满足`Existing Asset Fast Path`触发前提，角色仍走Asset Design → Prompt → Image双确认；只有用户实际提供文件、给出可访问受控ID或明确要求登记时才进入Existing File Check → Candidate Reference Registration → User Confirmation → Canonical Reference / Active Version。

FAIL：把声明当已确认资产直接用于下游Prompt或视频参考；跳过Prompt / Image确认；或以“用户已有”为由跳过Tier判定与Registry状态语义。

### R35-C Missing Items Come From The List Or The User

输入：清单已输出，用户未说明缺失项，也未提供任何补充。

PASS：Skill按清单继续当前可推进步骤，不逐项盘问缺失；只有某缺口会改变当前对象身份或阻断当前制作步骤时，才一次性指出该**具体**缺口并给最小路径。

FAIL：连续追问“哪些没有”“请逐项确认是否已有”“请提供素材清单”；或把未声明资产写成缺失、把用户声明过的资产写成待制作。
