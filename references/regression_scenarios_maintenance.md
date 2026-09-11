# SD Film Regression Scenarios — Delivery, Aesthetic And Maintenance

本文件是回归集的一部分，由`references/regression_scenarios.md`的 Regression File Index 统一索引；本文件内部编号保持连续，可按编号直接定位，不整集通读。

覆盖范围：R48—R60 —— 交付物校验、美学决策与试片、维护体系与可达性、媒介剖面、分镜拆解覆盖。

---

## R48 Deliverable Validation, Coverage And Scale Regression

### R48-A Delivery Validator Accepts And Rejects

输入：一个符合`templates/10_video_prompt.md`的`# CLIP-X｜…` Package，以及同一Package的破损版本（字段错序、分镜编号不连续、字段空值、JSON格式、缺少固定无BGM句）。

PASS：`scripts/validate_prompt_package.py <prompt-file> --model seedance-2.0`对合规包返回VALID并以0退出；对每个破损版本返回对应INVALID原因并以1退出。2.5与H3分支分别校验阶段递进无重叠与`非叙事性音乐：N/A`末行。

FAIL：校验器只接受`--skill-root`、无法校验已编译Package；或把`validate_prompt_package.py`写成`validate_sd_film.py`的替代品，或把它列为Skill更新维护QA的执行owner。

### R48-B Unauthorized Voice Field Is Rejected

输入：Package中出现`音色特征：`，但用户未明确要求把声音控制写入当前视频模型Prompt。

PASS：校验器返回INVALID并指明该字段只在显式授权时插入；用户明确要求并追加`--allow-voice-field`时通过。

FAIL：把对白、已有音色资源或Active Voice Profile当成插入该字段的理由。

### R48-C Review Ledger Coverage Is Complete

输入：一次含N个SHOT的Review，其中只有部分SHOT被写入`Shot-Level QA`，或某维度留空。

PASS：每个受审SHOT与每个受审边界各占一行，每一列都有结论；通过写`PASS`或`无风险`，不适用写`N/A`并写明理由；结论为`PASS`时`Problem`写`无`、`Return Route`写`不适用`。

FAIL：只列有问题的SHOT、用一段总体评价替代逐镜记录、任一维度留空，或在该状态下仍作出`PASS`并进入Completion Gate。

### R48-D Shot Count Declaration Matches Shots

输入：一个Seedance 2.0 Clip，`画幅：`声明分镜总数，逐分镜区块数量与之不一致；以及一个模型可能扩写单镜的情形。

PASS：`画幅：`声明的分镜总数与逐分镜实际数量完全一致；存在扩写风险时`反向提示词：`保留与声明一致的数量兜底句，且数量限制不只写在反向提示词。

FAIL：缺少总数声明、虚报数量，或新增独立字段承载数量声明而改变STATE-08固定Schema。

### R48-E Full Shot Scale Contract

输入：大全景中出现人物、门、车辆与建筑。

PASS：按门高、头顶到屋顶余量、人物与车辆的位置关系、建筑层高倍数写出相对比例，并可由现实关系复算。

FAIL：只用“宏大”“电影感构图”描述尺度，人物被缩小、门被放大或层高失真，或把比例错误当成画质/后期问题处理。

### R48-F Character Responds To Environment Light

输入：人物穿过不同光区，或反打镜头改变受光分布。

PASS：面部亮度、色温、方向与反射随位置、遮挡、距离或朝向变化同步改变；面部可读性通过光源关系、反射结果或构图提升。

FAIL：写入与环境无关的固定面部补光或均匀打亮“美颜光”，导致人物像贴在背景上或在镜头间无来源地受光漂移。

### R48-G Reference Provenance And Degradation

输入：同一资产连续多轮图改图，输出出现塑料感、脏高光与细碎噪点。

PASS：先合并修改需求减少迭代；发现劣化时退回原始图或结构图重新生成；只在原图不可用时从最近干净版本分叉并重新合成已确认正确的局部。控制强度按用途选择。

FAIL：在已劣化的衍生图上继续叠加修改；或借本机制把线稿、白模、多格拼图或Storyboard登记为Canonical Reference、STATE-08视频输入。

### R48-H Experience Classification And Coupled Attribution

输入：一条候选经验，来源为同时改变多个变量且无法分离归因的观察。

PASS：候选与确认记录带`Class: P / O / C`；`O`类带`valid_as_of`且到期后转`REVIEW`；`Triggers`、`Procedure`、`Failure Signals`、`Exceptions`、`Counter-examples`齐全；耦合来源记为`coupled_uncharacterized`且不升级为`P`，不据此宣称某一措辞必然有效。

FAIL：只有结论句而缺适用条件、步骤、失效信号或反例的条目入库；把`O`类模型参数写成跨项目原则；用耦合改动宣称某词已获验证。

## R49 Aesthetic Decision Lock Regression

### R49-A Four Dimensions Require Exclusive Choices

输入：一个已完成STATE-03核心资产的短项目进入STATE-04，剧本主题与Director Intent已锁定。

PASS：在写入Project Bible前完成Aesthetic Decision Lock；反差与光比结构、色彩对抗关系、构图主张、视觉母题与变化轨迹四个维度各给出选择、被放弃的选项、事实依据与可观察的可见后果；四项落在既有Overall Visual Style、Color System、Lighting Style、Composition Rules与Continuity区域；视觉母题写明至少三次可出现、变化或反转的轨迹。

FAIL：只写“低饱和、电影感、高级感”等标签或只给色调名；只写选择而没有被放弃的选项；用“为了电影感”充当依据；新增Project Bible竞争区域、平行Schema或STATE-08新字段。

### R49-B Decoration Without Trade-off Is Not A Decision

输入：某项目在四个维度都写了正向描述，但没有说明放弃哪一类常规做法。

PASS：判定Aesthetic Decision Lock未成立，不写入Project Bible，不进入STATE-05；返回STATE-04补齐被放弃的选项与依据。

FAIL：把“统一柔和光比”“自然色调”“标准三分法”这类无取舍的默认做法记为已做出的决定并通过Completion Check。

### R49-C Lock Is Inherited And Audited Downstream

输入：一个已锁定四项决定的项目推进到STATE-06与STATE-08，某个Clip重新引入与锁定构图主张相反的画面组织。

PASS：STATE-06在Composition Strategy中保留已锁定构图主张；STATE-08 Prompt落入已锁定的光比结构、色彩对抗与构图主张；STATE-08 Prompt Scorecard的Hard Gate检查该Clip是否继承并执行Aesthetic Decision Lock，漂移时该项不通过并回到STATE-04或STATE-06。

FAIL：用“更好看”“更有电影感”在STATE-08另起一套临时审美；让Scorecard只按文字华丽程度给摄影与光影两项高分；把Lock写成逐镜参数或在STATE-04提前产出Shot List。

## R50 Aesthetic Decision Lock Projection Regression

### R50-A Lock Reaches The Prompt Compiler

输入：一个已在STATE-04锁定四项美学决定的项目推进到STATE-08，当前Clip只携带1—3条导演优先级。

PASS：STATE-08的Required Resources包含`project_bible.md`的已确认Aesthetic Decision Lock；Prompt Compiler在Global Projection Matrix中按`Aesthetic Decision Lock（STATE-04）→ 主风格；画面描述；环境一致性`投影；`主风格`写出光比程度与色彩对抗关系，逐镜`画面描述`写出本镜相对锁定值的构图与母题Delta。

FAIL：STATE-08只拿到导演优先级而没有美学决策入口；把四项决定写成风格标签；在STATE-08另起一套临时审美。

### R50-B Lock Is Not Erased By Delta Compression

输入：项目风格已由Visual Direction锁定，第二个及之后的连续Clip按`Source Carries State, Prompt Carries Delta`只写差异。

PASS：`主风格`仍保留可核查的光比结构、色彩对抗关系与构图主张锚点；本镜真实发生光比、色彩或构图变化时写明变化；视觉母题在已确认的出现、变化或反转节点上出现，未到节点不重复。

FAIL：把“已由视觉开发锁定”当作省略理由，导致后续Clip的`主风格`只剩风格标签、`画面描述`只剩动作；或每镜机械重复整段项目Visual Bible。

## R51 Skill Context Budget Regression

### R51-A Oversized File Needs A Read Entry, Not A Penalty

输入：一次变更使某个Workflow、Rule或Knowledge文件继续增长，越过复核线（单文件 50 KB）。

PASS：复核“使用它的时候会读到全部吗”——用不到全部就拆分它或给出读取入口，并把入口登记进`references/context_budget.md`的Size Index。越过复核线本身**不阻断提交**，也不产生债务。

FAIL：让文件静默增长到没人说得清该怎么读；或反过来，为了压数值删掉已确认的规则、字段归属、Template字段或回归场景。

### R51-B Shrunk File Must Be Unregistered

输入：某文件经拆分或压缩后降到复核线以下，但Size Index仍保留其条目。

PASS：同一次变更中移除该条目，Validator随即通过。

FAIL：保留已达标条目，使索引退化为一份固定名单，下一次增长不再触发任何检查。

### R51-C Ceiling Is Not Waivable

输入：某文件达到或超过Ceiling阈值。

PASS：判定为结构性失控，先拆分为多个单一职责文件，同步更新全部引用与路由后再提交；拆分后重新核对文件引用完整性。

FAIL：在Size Index中登记后照常提交；或以“本轮只改文案、与超长无关”为由延期。

### R51-D Size Never Justifies New Files

输入：一次优化中发现多个文件越过复核线，考虑通过新增文件降低单文件体量。

PASS：先按`Rule Ownership Check`确认现有权威位置；只有拆分确实需要新的单一职责载体时才新增，并同步更新所有引用、路由与回归。

FAIL：以“降低体量”为由新增平行规则文件，形成第二套并行检查规范或竞争owner。

## R52 Maintenance Self-Check Extraction Regression

### R52-A Must-Read Path Stops Being A Long File

输入：一次维护优化需要修改Skill，按`SKILL.md`入口执行维护自检。

PASS：`SKILL.md`直接指向短卡`references/maintenance_self_check.md`（15项检查项、执行链与报告模板齐全），判据真源在`references/maintenance_self_check_protocol.md`；`references/module_contracts.md`只保留模块接口合同与一个指针，已回到复核线以内并从Size Index移除。

FAIL：维护自检仍只能通过通读一个超长合同文件才能找到；或抽取后`module_contracts.md`同时保留一份可执行的并行副本。

### R52-B Module Contracts Does Not Re-Grow The Checklist

输入：后续修改在`references/module_contracts.md`中再次写入检查维度、维护链或报告模板。

PASS：判定为Duplicate Rule，保留单一权威来源；`scripts/validate_sd_film.py`检测到合同文件重新出现维护自检标题即失败。

FAIL：允许合同文件与维护QA文件并行维护同一套检查。

### R52-C Non-Runtime Documents Are Not Runtime Authority

输入：某个Workflow或规则需要引用用户用法说明。

PASS：`USER_GUIDE.md`顶部声明自身为非运行时文件；运行时读取按`rules/resource_loading.md`的Read Budget执行，用户说明只用于确认用户可见行为。

FAIL：把`USER_GUIDE.md`当作规则、恢复、路由或Schema来源；或为让它“更权威”而把内部规则复制进用户文档。

### R52-D Capability Numbers Have One Owner

输入：模型时长窗口或参考预算发生变化。

PASS：只修改对应Adapter的能力数值；知识层不再复述原始窗口，只引用Adapter的`duration`并说明超出稳定窗口时的预检条件。

FAIL：知识层保留一份独立的窗口数值，使一次能力变更必须在多个文件同步。

## R53 Size Metric And Corpus Split Regression

### R53-A Size Is Measured In Bytes

输入：一次维护需要判断哪个文件最该处理。

PASS：体量按UTF-8字节数判定，不按行数；`references/context_budget.md`的Metric节写明理由，`scripts/validate_sd_film.py`以字节阈值执行。改变阈值或度量必须同步Metric节、Ledger与测试。

FAIL：用行数排名决定优先级——本库空行占比31%–57%，会把段落密集的大文件排到后面，把空行多的中等文件排到前面（实测曾把33 KB的文件判为最大、把57 KB的文件漏在20名之外）。

### R53-B Composite Files Get Split, Integral Files Do Not

输入：某文件超过单文件Target。

PASS：先判定类别。并列独立小节组成的`COMPOSITE`必须拆分，并由原文件提供Index；一条连贯链条的`INTEGRAL`允许保留，但必须在Ledger写明按章节读的入口，且明确“拆分会让单次使用读取更多文件”时不拆。

FAIL：只按体量机械拆分，把`INTEGRAL`文件切断成互相依赖的碎片；或对`COMPOSITE`长期挂账不拆。

### R53-C Ceiling Is Not Waivable And Was Actually Enforced

输入：某文件达到Ceiling（100 KB）。

PASS：Validator失败，必须先拆分再提交。历史遗留的132.7 KB回归集即因此被拆为四个文件，而不是登记后放行。

FAIL：先把超Ceiling文件登记进Ledger再照常提交，使Ceiling退化为软约束。

### R53-D Split Preserves Identifiers And Index

输入：一个文件被拆为多个文件。

PASS：编号／命名空间保持连续，原文件保留原名并提供Regression File Index；所有引用方更新到新文件；回归断言改为对整个语料集求值，不因再次拆分而失效。

FAIL：拆分后出现断号、同名两处可执行副本，或引用方仍指向已移走的小节。

## R54 Long-Term Context Budget Maintenance Regression

### R54-A Prevent Layer Blocks Growth Before It Lands

输入：一次优化需要在某个已接近Target的文件里补写内容。

PASS：先判定归属，默认补进既有owner；如果补写会使文件越过复核线，就在同一次变更内给出它的读取入口或先拆分；新建Markdown不超过30 KB。

FAIL：先把内容写进去，再登记进Size Index把问题推给下一次。

### R54-B Composite Debt Is Queued, Not Shelved

输入：某`COMPOSITE`文件超Target并已登记。

PASS：它被当作待拆队列；连续两次复审仍未拆分即按未处理技术债上报。历史遗留的132.7 KB回归集与72.8 KB模块合同集均在本类规则下被拆，拆后按其体量自动摘牌。

FAIL：以“已登记”为理由长期不拆，使Ledger变成永久豁免名单。

### R54-C Audit Runs On A Cadence And Detects Drift

输入：固定的周期性体检。

PASS：运行`scripts/validate_sd_film.py --skill-root <skill-root> --report`，输出字节排名、越过复核线项及其类别、读取入口与复审日期；Size Index登记的`Size`与实测差异超过20%即判为索引过期，并使Validator失败。

FAIL：把体检当作唯一防线，或让Ledger记录的体量长期与实测脱节。

### R54-D Enforce Layer Is Independent Of Discipline

输入：一次正式修改。

PASS：字节阈值、文件类别合法性、Ledger一致性、`NON_RUNTIME`自证全部由`scripts/validate_sd_film.py`确定性执行，不依赖维护者是否记得读规则。

FAIL：把体量约束只写成文档要求而不落进Validator，使是否遵守取决于自觉。

### R54-E Subtraction Channel Is Exercised, Not Just Declared

输入：一次正式修改新增了规则或机制。

PASS：`Duplicate Rule Check`除查重复外，还显式判定是否存在可合并或可退役的既有规则，并写明依据；结论为“无”时同样记录判断依据。`merge_existing`与`deprecate/remove`是可用且被评估过的变更分类。

FAIL：把`Additive By Default`解释成规则总量只增不减；连续多个周期只出现`optimize_existing`与`add_new`，却从未评估过任何一条既有规则是否已被覆盖、吸收或不再有触发条件。历史上51个提交的内容型变更增删比在6:1至190:1之间、全部deletions都是搬家或重写，即属本项FAIL的实测样本。

## R55 Tool-Independent Self-Maintenance Regression

### R55-A The Rule Lives In The Skill, Not In The Environment

输入：把SD Film Skill交给另一个Agent、另一台机器，或一个没有Python、没有`scripts/`、没有定时任务的环境。

PASS：`SKILL.md`的`Self-Maintenance`节在前置位置声明本Skill自维护，给出写入前三项判定与写入后的完整自检入口；`references/maintenance_self_check.md`的15项与两个Guard全部可由人按文件逐条核对；协议成立与否不引用任何脚本的运行结果。

FAIL：把自检仅实现为`scripts/validate_sd_film.py`、周期性任务或某个宿主的功能，使换环境后Skill退化为无约束的文档；或在判据中把“运行脚本”写成必要条件。

### R55-B Writing Is Guarded Before, Not Only Audited After

输入：一次新增或写入Skill内容的操作。

PASS：动手前先完成归属／体量／减法三项判定；越界在同一次变更内处理；写入后再执行完整自检。

FAIL：只做事后审计——内容先落盘，靠事后报告发现问题。

### R55-C Missing Tooling Never Lowers The Bar

输入：当前环境没有Python、没有`scripts/`或没有网络。

PASS：按`references/maintenance_self_check.md`的Required Verification左列，逐项人工执行结构、引用、体量与两个Guard，结论与有工具时同强度。

FAIL：以“本机没有验证器”为由跳过固定基线，或把未验证的变更标成`PASS`。

### R55-D Version Discipline Is Portable

输入：一次正式修改。

PASS：同步递增`Skill Version`与`Build ID`。这是纯文本可完成的操作，因此不因换执行者而豁免。

FAIL：改动内容但不递增版本，使外部无法判断Skill是否已变更。

### R55-E Identity Survives The Move

输入：维护自检体系从一个文件搬到另一个文件，或换了入口节名。

PASS：原名称`Skill Update Self-Check / Change Safety Checklist`在owner清单、报告模板与执行入口中保持可检索；新的入口节显式声明自己**只是入口、不构成第二套体系**；全库只有一个检查体系入口。

FAIL：搬家或改名后旧名不再被提及，且没有任何地方声明新旧是同一体系——读者会以为出现了两套并行检查，或以为原有检测层已被替换。

## R56 Maintenance System Consolidation Regression

### R56-A Each Rule Body Has Exactly One Owner

输入：一次维护改动同时涉及`SKILL.md`、执行清单、判据真源与体量文件。

PASS：每一条规则正文只有一处完整定义。“写入前的判定”只在执行清单的`Before You Write`完整描述；`SKILL.md`只列不变量并给路由；体量文件只拥有阈值与台账，不重述体系框架。

FAIL：同一套判定在两处以上各写一遍完整版本（如体量文件再写一遍Prevent四条的正文），使改动必须多点同步。

### R56-B The Budget File Does Not Own The Maintenance System

输入：需要说明维护体系的层次与节奏。

PASS：层次与节奏由执行清单的`Maintenance System Map`拥有；`context_budget.md`只拥有体量判据与台账，并在需要时引用维护体系，不自己定义Prevent／Enforce／Audit。

FAIL：把体系框架写在体量文件里，使读者从体量文件进入时以为维护体系只有体量一件事。

### R56-C The System Map Exposes One System

输入：读者从任一份维护文件进入。

PASS：执行清单的`Maintenance System Map`列出全部成员文件、各自角色与读取时机，并声明它们是**分层关系、不是并行副本**。

FAIL：成员分散且没有任何一处说明它们的关系，读者需要自己拼出体系全貌。

## R57 Medium Profile Regression

### R57-A Medium Is Orthogonal To Genre

输入：同一题材（如爱情）分别以`live_action`与`2d_anime`建立项目。

PASS：两者的Genre承诺、主Pipeline、Template字段与STATE-08 Schema完全相同；分档差异只出现在编剧信息承载、镜头语言基底与美学词表三张表内。

FAIL：把媒介当作Genre的子类或后缀，使“2D爱情剧”与“真人爱情剧”被判成两个不同题材，或让媒介改变Genre承诺。

### R57-B Drawn Medium Cannot Use Optical Parameters

输入：`2d_anime`项目进入STATE-04定义摄影方向。

PASS：`Camera Style`、`Lens Direction`、`Aperture And Depth`、`Filter And Texture`按绘制媒介的等效表达填写（注意引导、明暗对比、帧感）；不出现焦段毫米数、光比比值、轨道器材或真实景深。

FAIL：为2D项目照搬实拍焦段与光比语言，或把这些参数留空而不给等效表达。

### R57-C Unconfirmed Medium Is Not Silently Live Action

输入：用户只说“动画”，未指明二维或三维。

PASS：STATE-00写`Medium: Pending`并询问一次；后续STATE按`live_action`既有行为继续但登记为`Pending`，不加载分化表，也不把它记成已确认真人剧。

FAIL：默认取`live_action`或`2d_anime`并当作已确认事实推进，使下游按错误的剖面展开。

## R58 Review Line Is A Signal, Not A Quota Regression

### R58-A Crossing The Review Line Is Not A Violation

输入：一次变更把某个运行时文件推到 50 KB 以上，但没有人在同一次变更里登记它。

PASS：该文件出现在`--report`的提示里；Validator仍然通过，因为长度本身不是缺陷。周期性复核时要么拆分它，要么在Size Index写下它的读取入口。

FAIL：因为“超过阈值”就判定提交失败；或反过来，把越线当成不需要处理的事，让文件长到没人说得清该怎么读。

### R58-B Size Index Entry Without A Read Entry Fails

输入：某个越线的`INTEGRAL`文件在Size Index中登记了Class与体量，但`Read Entry`列为空。

PASS：Validator失败，提示该条目必须写明读取入口——索引失去可执行性就等于没有。

FAIL：允许索引只记录体量而不说怎么读，使它退化成一份“哪些文件很大”的名单。

### R58-C Non-Runtime Files Are Outside The Review Line

输入：`USER_GUIDE.md`这类不参与运行时读取的文件越过复核线。

PASS：它不在Size Index中，也不出现在`--report`的待补提示里；判定依据是文件自身声明了“非运行时文件”，而不是默认豁免。

FAIL：把非运行时手册与高频必读文件用同一把尺子量，让它白挂一条不存在的问题；或不加自证地整体豁免。

### R58-D Size Index Never Decays Into A Standing List

输入：某登记文件经拆分降到复核线以下但条目未移除，或条目指向一个已不存在的文件。

PASS：两种漂移都使Validator失败，索引始终只描述当前真实存在的厚文件。

FAIL：保留已达标条目或悬空条目，使索引变成一份越积越长的固定名单。

---

## R59 Shot Breakdown Coverage Regression

### R59-A Shot Size Has One Owner And The Inline List Matches It

输入：STATE-06需要为新镜头选择景别，Agent就近读取`workflows/09_shot_design_workflow.md`的Step 3。

PASS：Step 3列出与`knowledge/camera_language/lens_language/framing_and_scale.md`一致的规范景别（含中近景与大特写）加局部镜头、细节插入镜头，并显式指向该owner；Required Knowledge在焦段路由旁给出景别路由；该owner已在`references/module_contracts_knowledge.md`登记合同。

FAIL：内联清单短于规范景别，导致中近景与大特写选不出来，而下游`camera_language/image_source_coverage.md`与`director_patterns/emotional_patterns.md`（EMO-08固定中近景、EMO-15大特写/局部）仍在消费这两档。

### R59-B Rhythm Intent Has A Recorded Field Before It Has A Consumer

输入：某Scene判定Sequence Planning Required，`workflows/16_sequence_planning_workflow.md`读取“已确认的Rhythm Intent”。

PASS：STATE-05把它投影为`templates/07_scene_design_prompt.md`的`Scene Directing Brief`字段，并由`knowledge/director_decision_layer.md`声明归属；未确认时写`Pending`，不得由Writer Beat数量反推。

FAIL：消费方读取一个没有任何记录落点的Rhythm Intent（孤儿内容），或让Sequence Planning自行发明节奏意图。

### R59-C Rhythm Projection Never Pre-Commits A Shot Count

输入：STATE-05投影节奏意图时，Agent顺手给出“本场预计8个镜头”。

PASS：节奏段只写节拍结构、必须存在的节奏对比与信息时机关系；镜头数量仍只由STATE-06按Shot Purpose Gate与实际可执行性决定，不在本阶段预定。

FAIL：把预估镜头数写成配额或写进Scene输出，使STATE-06为命中数字增删镜头，退回按Beat机械切分。

### R59-D Storyboard Stays A Side Route, Not An Upgrade Tier

输入：用户只说“给我完整版专业分镜”。

PASS：只展开`templates/08_shot_design_prompt.md`的十八字段内部记录；视觉Storyboard仍由`workflows/10_storyboard_workflow.md`另行显式请求，且不进入STATE-07 / STATE-08参考资产。

FAIL：把Storyboard当作分镜表的更完整版本顺带产出，或让它进入STATE-08参考资产。

---

## R60 Look Frame And Aesthetic Judgement Regression

### R60-A The Aesthetic Lock Is Tried, Not Gambled

输入：某项目在STATE-04形成`Aesthetic Decision Lock`草案四维度，四维度全部只能靠文字描述，尚未看到任何画面。

PASS：允许在锁定之前执行一次可选`Look Frame`——用已确认资产出1—3张试片帧，用户判断后修正草案，再写入Project Bible并进入Step 6。Gate位于`Aesthetic Decision Lock Gate`之后、正式锁定之前；工具不可用或用户不想出图时记录原因跳过，`Aesthetic Decision Lock`仍按原四维度完成。

FAIL：在看不到任何画面的情况下让草案直接成为项目级承诺；或把试片写成STATE-04的必经步骤；或跳过时仍声称做过试片。

### R60-B Look Frame Never Enters The Asset Chain

输入：试片帧生成完成后，Agent考虑把它登记为项目视觉基准，或用作STATE-07首帧参考。

PASS：Look Frame属非生产视觉材料，不登记为Canonical Asset、不写入项目状态、不新增工件ID或STATE、不进入STATE-05之后任何阶段；`rules/05_output_rules.md`的STATE-07与STATE-08输入禁令、以及`rules/03_prompt_rules.md`的参考资产禁令均已显式列入Look Frame试片帧。

FAIL：把试片帧登记为资产、写进Portable State、或让它出现在STATE-08【参考资产】里。

### R60-C Look Frame And REF-SKETCH Stay Separate

输入：某Clip同时存在美学不确定与空间不确定。

PASS：两者分工明确——Look Frame在STATE-04、带已确认资产的真实外观、只验光比/色彩对抗/构图主张/视觉母题；REF-SKETCH在STATE-08、使用无性别技术调度人偶、只验位置/姿态/机位/轴线。两者不共用模板、不互相替代。

FAIL：用试片帧验证空间调度，或用REF-SKETCH验证外观与美学；或让两者共用`templates/09_storyboard_prompt.md`类默认生图指令。

### R60-D Aesthetic Dimensions Ask For Visible Choices

输入：某Clip的Prompt已逐字复述`Aesthetic Decision Lock`的光比结构与色彩对抗关系。

PASS：`prompt_scorecard.md`的两项审美维度按`### Aesthetic Criteria`评分，要求给出可观察证据——视觉重心唯一、明暗有层级、色彩有主从、取舍可见、不平均、景深清晰度有意图；只复述Lock措辞不得满分；未写出可见取舍证据时Hard Gate不通过。评分权重不变，且仍声明不能替代人工审美判断。

FAIL：把"是否执行了Lock"当作审美评分依据，使100分打满而画面依然平均；或把可被文字检验的六条冒充为完整的审美判断。
