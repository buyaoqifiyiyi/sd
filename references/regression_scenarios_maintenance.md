# SD Film Regression Scenarios — Delivery, Aesthetic And Maintenance

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是回归集的一部分，由`references/regression_scenarios.md`的 Regression File Index 统一索引；本文件内部编号保持连续，可按编号直接定位，不整集通读。

覆盖范围：R49—R63、R66—R67 ——R48（交付物校验、覆盖与尺度）是独立可读的子案例合集，已按编号边界拆至 `references/regression_scenarios_delivery.md`。 交付物校验、美学决策与试片、维护体系与可达性、媒介剖面、分镜拆解覆盖、Review审美判断、阶段落点覆盖、FAST不变量与交付收据、交付物完整性打包门、独立调用。

---

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

### R50-C Establishing Round Cannot Collapse Into One Style Sentence

输入：项目第一个交付Clip（或当前Prompt是脱离项目上下文的独立交付），STATE-04已锁定四项美学决定与Visual Grammar Baseline。

PASS：`主风格`按`knowledge/prompt_compilation/state08_projection.md`的`### 主风格 Minimum Content Rule`写出四块：标签或基线 + 项目内含义、Visual Grammar Baseline稳定倾向、四锁各一次（每项含选择与它排除的可见结果）、当前Clip载体；句式可压缩，四项不得缺项，逐镜动作与时间顺序仍留在各自字段。

FAIL：`主风格`只有一句“标签 + 若干可见载体”（例如只写风格名与几个名词），没有四锁、没有可核对基线；或反过来把`主风格`写成第二条时间线、复述逐镜动作与End状态。

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

PASS：`SKILL.md`直接指向短卡`references/maintenance_self_check.md`（检查项、执行链与报告模板齐全），判据真源在`references/maintenance_self_check_protocol.md`；`references/module_contracts.md`只保留模块接口合同与一个指针，已回到复核线以内并从Size Index移除。

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

PASS：`SKILL.md`的`Self-Maintenance`节在前置位置声明本Skill自维护，给出写入前三项判定与写入后的完整自检入口；`references/maintenance_self_check.md`的全部检查项与两个Guard都可由人按文件逐条核对；协议成立与否不引用任何脚本的运行结果。

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

输入：同一对话内的多次正式修改；以及维护者明确确认该批改动定稿。

PASS：对话进行中的改动累积为**一个待发布批次**，不逐任务递增版本号；只有维护者确认该批定稿时才一次性递增`Skill Version`与`Build ID`并使两者继续匹配。递增是纯文本可完成的操作，因此不因换执行者而豁免。

FAIL：每完成一个任务就升一版，把版本号当成进度计数；或在维护者已确认定稿后仍不递增版本，使外部无法判断Skill是否已变更。

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

PASS：STATE-00只登记并写`Medium: Pending`（本阶段不询问）；STATE-01的`Production Setup Gate`在剧本`Production-Locked`后与模型、交付形态、风格基线在同一张确认单里询问一次；媒介确认前不进入STATE-02、不生产媒介相关资产、不加载分化表，也不把它记成已确认真人剧。

FAIL：默认取`live_action`或`2d_anime`并当作已确认事实推进，使下游按错误的剖面展开；或在STATE-00另开一次媒介提问、与`Production Setup`重复索取同一选择。

### R57-D Medium Is Confirmed Before Any Asset, Never After Assets

输入：用户给出一份定稿剧本但从未提及媒介形式，项目正常推进到剧本锁定。

PASS：`Production Setup Proposal`中出现媒介形式（三档候选或用户唯一指定项），与图像模型、交付形态、视频偏好、风格基线同轮确认；回答后写入`project_bible.md`的`Project Information → 媒介形式`。媒介确认发生在**资产制作之前**：STATE-02资产发现与STATE-03资产生产都能读到该值。若用户答的是非`live_action`档，先进STATE-01按`knowledge/medium_profiles.md`的Screenwriter Layer做信息承载复核，再进入STATE-02。

FAIL：让`Medium: Pending`穿过STATE-03资产生产、直到STATE-04的`Medium Profile Gate`才第一次向用户提出媒介问题，使已产出的资产处于可能错档的状态（2D 与实拍的资产结构、材质与光学语言不通用）；或在STATE-04就地问媒介而不按最小修复回STATE-01的`Production Setup Gate`补确认。

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

### R58-E Reaching The Line Triggers Slimming, Not Relocation

输入：一个回归文件到达 51200 B 阈值。做法一：把其中一族案例整体搬到一个新文件，文件数由五个变六个、语料总量增加。做法二：把与`references/recovery_guards.md`固定基线逐项重合的九个案例退休、原位只留指针，总量下降并回到五个文件。

PASS：按`references/context_budget.md`的`### 瘦身优先序`，**到达**阈值触发一次瘦身优化：先退休与唯一 owner 重合的内容，再合并，再压缩；判据是**总量下降**。搬迁与拆分不是瘦身。瘦身后仍越线才拆分。不得为凑阈值删除已确认的规则、字段归属或回归场景。

FAIL：把到达阈值当成"违规"只做拆分 / 搬迁；或为了立刻回到线下而删除回归案例、规则正文或字段归属；或把"文件回到线下"当作瘦身完成的证据而不看语料总量。
## R59 Shot Breakdown Coverage Regression

### R59-A Shot Size Has One Owner And The Inline List Matches It

输入：STATE-06需要为新镜头选择景别，Agent就近读取`workflows/09_shot_design_workflow.md`的Step 3。

PASS：Step 3列出与`knowledge/camera_language/lens_language/framing_and_scale.md`一致的规范景别（含中近景与大特写）加局部镜头、细节插入镜头，并显式指向该owner；Required Knowledge在焦段路由旁给出景别路由；该owner已在`references/module_contracts_knowledge.md`登记合同。

FAIL：内联清单短于规范景别，导致中近景与大特写选不出来，而下游`knowledge/camera_language/lens_language/framing_and_scale.md`（该owner本身）与`director_patterns/emotional_patterns.md`（EMO-08固定中近景、EMO-15大特写/局部）仍在消费这两档。

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

### R59-E Stage Work Must Have A Named Landing Field In The Prompt

输入：一个已完成STATE-05到STATE-08全部前置的项目编译CLIP-001；Scene Directing Brief已有Audience Start → End、Reveal Timing与Rhythm Intent，STATE-06已有Director Decision Notes，STATE-01已有Writer Intent Packet。

PASS：`knowledge/prompt_compilation/state08_projection.md`的Global / Per-Shot Projection Matrix为本Clip涉及的上游来源各给出一行落点（Writer Intent、Director Intent / Director Decision Notes、Scene Directing Brief、STATE-04 Aesthetic Decision Lock、STATE-02/03资产、STATE-07 Clip事实），转换规则只引用Writer Gate与Director Pass，不复制其正文；交付前Loss Check逐项核对Scene节奏与信息时机、Writer Beat与Scene Value、Audience Attention与Camera Trigger / Stop是否能从既有字段读出。

FAIL：某阶段确认过的设计在任何矩阵行里都没有落点，只能靠"下游会自然继承"假定其进入Prompt；或为了补落点新增Prompt字段、复制Writer / Director协议正文、把SCENE / BEAT编号或`Pending`写进交付。

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

---

## R61 Aesthetic Judgement At Review Regression

### R61-A The Criteria Live In Exactly One Place

输入：审美判据需要同时服务STATE-08的Prompt评分与STATE-09的成片Review。

PASS：判据、合格与不合格的分界、判定纪律唯一由`knowledge/quality/aesthetic_judgement.md`拥有；`prompt_scorecard.md`与`workflows/13_review_workflow.md`只引用它，两处都不复制其判据正文（Review清单写"按该文件的六条判据"，不重新列举条目名）。两处对象不同——一处审Prompt文本、一处审成片——因此不合并。

FAIL：在两个消费点各留一份完整判据副本，使改动只同步一处；或因对象不同就分别发明两套判据。

### R61-B Review Can Finally Say The Decision Was Wrong

输入：成片的美学方向本身不成立——不是没执行Aesthetic Decision Lock，而是当初那个决定选错了。

PASS：`Director QA`下的`Aesthetic Judgement`作出判断后，`Director QA Return Route`提供返回STATE-04重做该维度的路径，可选择性重跑Look Frame；只复核依赖该决定的STATE-05至STATE-08产物。审美不合格按根因分流——决定错记DIRECTING FAILURE、没做到记GENERATION FAILURE、素材可救记EDITING FAILURE——**不新增Failure Class**。

FAIL：只能发现"没执行已确认的决定"、无法发现"决定本身错了"，逼用户在Prompt层反复补救；或为审美单独新增一个Failure Class，使既有正交分类分叉。

### R61-C The System Never Judges Beauty

输入：六条判据全部通过，Agent考虑直接给出`PASS`。

PASS：系统只输出观察结论与可观察证据；审美结论必须由用户给出。未获得时记`PENDING_USER`，此时即使其余检查全部通过，Overall Result也不得判为`PASS`；系统不得代填该项，也不得把六条结论当作该项的替代。**"六条全过"不等于"好看"。**

FAIL：由系统自行判定审美并给出PASS；或用"判据全部通过"充当用户审美结论。

### R61-D The Look Frame Becomes The Review Baseline

输入：STATE-04曾执行`Look Frame`，STATE-09要判断成片是不是当初看到的那一种。

PASS：`templates/25_look_frame_prompt.md`保留"不得进入STATE-05至STATE-08任何阶段"的禁令，同时开出唯一例外——STATE-09 Review可以把试片帧作为**当初美学决定的对照参照**读取；该例外只授权读取比对，不得据此重新生成资产、改写已确认事实或用作任何生成输入。

FAIL：让试片帧成为常规下游输入、被登记为资产、或反过来用成片去改写当初的美学基线。

## R62 Stage-To-Prompt Landing Coverage Regression

### R62-A Every Main Stage Is Named Inside The Projection Matrices

输入：`knowledge/prompt_compilation/state08_projection.md`的Global / Per-Shot Projection Matrix被改动：有人为重排表格删掉一行来源标注，有人把某行改成只剩"见上游"。

PASS：`scripts/validate_sd_film.py`的`check_stage_landing_coverage`要求矩阵区内STATE-00至STATE-07各自被标识（`STATE-00/01/04`这类紧凑写法按run展开，不得只算第一个）、矩阵行数不低于下限、Writer / Director / Scene三行落点仍在。任一缺失即FAIL并指出缺哪个STATE或哪一行。

FAIL：矩阵区不再出现某个主STATE却仍然通过；或为通过检查删掉落点行、把来源标注并进正文、把行数压到下限以下——删行不能买覆盖。

### R62-B A New Stage Artifact Gets Its Landing Row In The Same Change

输入：某次修改给STATE-05新增了一项已确认的场景级设计（例如新的节奏维度），或给STATE-06新增了一个会成为生成输入的字段。

PASS：同一次变更内在投影矩阵补上"来源阶段 → 固定目标字段 → 必须保留的语义"一行，转换规则只引用既有Gate / Pass，不新增Prompt字段、不复制别家协议正文；Loss Check同步加一项可核对的判据。

FAIL：新增设计只在Workflow、Knowledge或Template里被记录，投影矩阵没有任何落点，靠"下游会自然继承"假定它进入Prompt；或为补落点新增最终字段、把内部ID / `Pending`写进交付。

## R63 FAST Invariant And Receipt Guard Regression

### R63-A The Auto-Confirm Invariant Lives In Every Home

输入：一次文案整理把`rules/automation_mode.md`的`## Purpose And Owner`里那句"FAST只自动确认，不减少流程与产物"删掉，只留下"模式只改变确认方式"；另一轮把`USER_GUIDE.md`里用户侧的同一口径删掉。

PASS：`scripts/validate_sd_film.py`的`check_fast_invariant_and_receipt`逐处验证不变量与收据文本仍在位——`rules/automation_mode.md`（Purpose / 连续链 / 聚合包 / 收据三状态）、`rules/05_output_rules.md`（清单不因FAST改变 + 指向收据）、`references/project_state_contract.md`（`COMPLETE`必须有实际产出证据）、`references/module_contracts_auxiliary.md`（"自动接受的是确认，不是工件"）、`USER_GUIDE.md`（用户侧口径）；任一丢失即FAIL并指出缺哪个文件哪句。

FAIL：只看`automation_mode.md`一处就算通过，使"自动模式可以少做几步"的读法在别的入口重新长出来；或反向地因为不变量在位就认定某次交付照做了（是否照做是运行时行为，由R32-D / R32-E覆盖）。

### R63-B The Receipt Cannot Be Reduced To A Receipt Label

输入：有人把`### Delivery Receipt｜交付收据`改成一句话"交付时列出阶段即可"，删掉`本轮完整输出` / `已在Accepted Artifact` / `待交付`三种状态；另有人把收据写成新的Project State字段。

PASS：三种状态标签是必备内容，缺一即FAIL；收据只做交付核对，不新增状态字段、不替代Template、不改变Completion Gate判据。`待交付`阶段不得写`State Status: COMPLETE`，下一次普通推进先续交完整工件。

FAIL：把收据简化成没有状态区分的清单（无法区分"已输出"与"只说了完成"）；或让收据承担状态写回职责，使状态合同与Completion Gate出现第二套判据。


## R66 Delivered Artifact Completeness Guard Regression

### R66-A The Completeness Rule Has A Consumer On The Packaging Path

输入：一次真实交付把会话里的摘要直接当工件落盘——`05_shots` 是 202 字节的一行一句清单、`04_scenes` 是两条 bullet、`06_clips` 是一句话——然后按目录结构打包。三个 Template 里"保存为文件时必须运行`scripts/validate_delivery_artifacts.py`，未通过不得交付"当时已经写着，包的目录、命名、清单也全部合规；另一份包相同，但三个源工件是完整 Template 形态。

PASS：`scripts/build_asset_package.py` 在写包之前对 `04_scenes` / `05_shots` / `06_clips` 的源工件运行该 owner 的对应`--kind`检查（**导入该 owner，不复制判据**），摘要形态判`BLOCKED`并逐条报出"哪一类 / 哪个文件 / 缺什么"，**不创建包目录、不生成zip**——避免"半个包"被当成已交付；完整形态的包正常通过这一门。文件名、目录结构与`00_MANIFEST.md`正确**不构成**工件完整的证据。

FAIL：规则只写在 Template 里、打包路径上没有任何消费者，靠执行者自觉运行校验器（于是摘要照样进包并被当作已交付）；或反向地把该门做成WARNING / 事后报告，让不合格的包先生成再说；或在校验器不可读时静默跳过该检查。


## R67 Standalone Invocation Regression

### R67-A A Standalone Run Never Counts As Progress

输入一：用户说"只重做 STATE-06 分镜表，别推进后面的阶段"，项目当时停在 STATE-04；同一次运行给出完整分镜表、用户确认，系统把 `Current State` 写成 STATE-06、`Next Workflow` 指向 Clip Production。输入二：同一请求，但这次只登记 `Active Artifacts` 与 Revision，`Completed States`、`Current State`、`Next Workflow` 都不变，`Pending Decision` 写明"独立调用交付，未计入主Pipeline进度"。输入三：用户说"只调用 Storyboard 模块"，系统把它登记成 `Completed States` 里的一项。

PASS：输入一被判为违规——独立调用不是顺序豁免，产出工件不等于走过该阶段；输入二通过，且该阶段将来被主Pipeline合法走到时按"已确认工件不重做"沿用这份工件而不重做；输入三同样违规——辅助模块不进入 `Completed States`，它最多登记为 Optional/Auxiliary Artifact。三种情形下 `scripts/validate_sd_film.py` 的 `check_standalone_invocation` 都要求"被调用单元仍满足自己的 Entry Gate"与"不计入项目进度"两句话仍在各自的 owner 里。

FAIL：把独立调用当成本节通道之外的捷径——用它跳过中间 STATE、把产物当成阶段完成、把辅助模块写进主路由，或反向地因为"不计入进度"就把独立交付降级成草稿 / 临时产物 / `Not Applicable`（它是正式 Confirmed Artifact，只是不改变主Pipeline进度）。

## R79 Skill Entry Frontmatter Integrity Regression

### R79-A The Discovery Entry Survives A YAML Parse

输入：`SKILL.md` 的`description`用全角引号包裹，并在内部出现引号（当前发布形态）。

PASS：frontmatter 可被 YAML 解析，`name`为`sd-film`，六个启动别名全部保留，`agents/openai.yaml`的`allow_implicit_invocation`为`true`；宿主能登记该 Skill。

FAIL：内层引号写成 ASCII 直引号，标量在第一个内层引号处提前结束，宿主解析失败后**静默丢弃**整个 Skill；而"`name: sd-film` 与六个别名仍是文件子串"使名字、别名与重复入口三项子串检查全部保持绿色——没有报错可读，Skill 只是消失。

### R79-B Judgements Anchor To Structure, Not To Substrings

输入：把`templates/04_character_asset_prompt.md`的 2D 小节标题删掉，但正文里三处反引号引用仍然保留。

PASS：`check_anime_language` 报 FAIL 并指名该标题缺失；花名册类判据只读花名册表（标题锚定行首），索引正文里的原子路径不被当成第二次登记，`# Read Scope` 表里反引号写出的节名也不会让登记项读成缺失。

FAIL：只做子串匹配，于是删掉真标题仍命中正文引用而报 PASS；或整文件扫描，于是正文提及被当成重复登记而报 FAIL。

## R83 Delivery Spec Ownership Regression

### R83-A The Overriding Authority Has One Owner And One Record

输入一：用户在请求里写明交付画幅为竖屏。输入二：项目材料未提任何交付画幅。

PASS：输入一把画幅、比例与平台写入`templates/01_project_bible_template.md`的`## Delivery Spec｜交付规格`并标`SELECTED`；输入二保持`UNSELECTED`，资产图按`rules/02_asset_rules.md`的`Asset Canvas Ratio Default｜资产图画幅默认`取类别默认——**默认值路径行为不变，只是原本不可达的覆盖分支被接通**。

FAIL：`项目已确认交付规格`被十余处引用为覆盖性权威，却既无定义也无记录位置；或从参考图宽高比、平台标签、目标形式、素材比例反推交付规格。

### R83-B Consumers Route To The Owner

输入：新增或修改消费方后复核路由。

PASS：`rules/02_asset_rules.md`的`Asset Canvas Ratio Default`、`knowledge/camera_language/composition_language/vertical_framing.md`的触发、`rules/resource_loading.md`范围门的判定依据三处都指向`templates/01`的该节；确定性射程由`check_delivery_spec`承担。

FAIL：消费方各写一套解释；或声称该检查能判断交付规格的内容是否正确（它只验证 owner 与路由在位）。

## R84 Period And Place Regression

### R84-A Every Era Claim Lands In One Of Three Evidence Classes

输入一：用户给出"1990年代中国北方县城"。输入二：需要一处无法从已确认材料核对的年号与机构名。

PASS：输入一的可观察约束（技术可用性、服装形制、文字与标识、照明与交通通讯条件）写成项目事实；输入二的年号、真实机构、真实事件与真实品牌按**不可确认**处理，改为不指向真实的等价物；由已确认时代推出的细节标为**合理推断**。**不得把常识当史实。**

FAIL：把推断写成史实；为求精确虚构年号、机构与型号；或因"时代需要"放宽真实人物、机构、事件与品牌的一等禁项。

### R84-B Technology Boundary And Lighting Conditions Decide The Night Scene

输入：一个尚无电照明的时代，剧本要求夜景。

PASS：夜景由火光、月光、天光与窗光构成，明暗对比大、色温偏低；该时代没有城市底噪光，也没有电流声与引擎声，`光线`、`环境一致性`与声音字段同步体现。

FAIL：写入该时代尚不存在的技术类别、现代字体标识或包装；或用"风格化"解释技术类别错误。

## R85 Branded Content Regression

### R85-A One Attention Chain, And No Invented Commercial Facts

输入一：已确认品牌诉求包含三个卖点。输入二：缺口包含真实价格与功效表述。

PASS：输入一把三个卖点排序成**一条注意焦点链**，被降级的卖点改由背景或道具承担或明确不做；产品按主角型 / 使能型 / 背景型之一进入画面；输入二按一等禁项与`workflows/03_asset_discovery_workflow.md`的`## Commercial Fact Triage`记为Pending Decision，**不由制作补齐**。

FAIL：多个卖点并列争第一注意目标；利益点靠台词或字幕宣布；用"看起来专业"的画面替代缺失的价格与功效。

### R85-B Text-Accurate Elements Go To Post, And The Project Is Never Presumed Commercial

输入一：需要可读的长文案、价签与精确 Logo。输入二：一个时长短、平台是短视频、画面里出现商标的普通叙事项目。

PASS：输入一按"优先后期叠加"处理，不写成模型生成承诺；输入二**不加载**本域，也不得从时长、平台、题材或道具品牌推定其为商业片。商业片不豁免资产双确认、Completion Gate、Reference Budget 与无BGM规则。

FAIL：把文字级正确的元素写成模型生成承诺；把普通叙事项目改造成商业片；以"客户要快"为由绕过任何 Gate。

## R86 Audience And Non-Fiction Regression

### R86-A Audience Is Never Inferred, And Imitation Risk Sets The Scale

输入一：一个动画媒介、少儿频道、画风可爱、时长很短的冒险项目，未声明受众。输入二：儿童向剧本里出现可模仿的危险动作。

PASS：输入一记`Audience Profile: PENDING`、不加载分化表、按既有通用行为继续，也不得登记为已确认的儿童向或家庭向；输入二在同一段落内给出可理解的负面后果，或改为不可模仿的表达。儿童向不等于降智：不得以可理解性为由简化因果或删除冲突；分级条文属**外部事实**，必须由用户提供来源。

FAIL：因"动画片是给孩子看的"或平台是少儿频道就推定受众；用可理解性当理由删掉冲突；虚构分级标准或声称"符合"未确认的分级体系。

### R86-B Non-Fiction Keeps Its Four Gates And Never Fakes Archive

输入一：目标确认为纪实，需要补足一处未记录的现场细节。输入二：需要一段"看起来像史料"的画面。

PASS：输入一按重现处理，可区分并标注依据来源，只补足可核实的事实间隙，不补人物内心、未记录的对话与未发生的动机；输入二使用生成影像时**不得被呈现为档案或真实影像**，不配纪实性字幕、时间码或档案式包装；每条事实陈述可指向可核对来源（来源台账），旁白只讲可核对内容，时间线与事件顺序与来源一致。

FAIL：用无依据的重现填补来源缺口；为叙事顺畅调换事件顺序或制造未记录的前因后果；把生成画面伪装成档案；涉及真实主体却未取得用户提供的授权。

## R95 Platform And Commercial Audience Regression

### R95-A Platform Facts Are Never Invented, And The Profile Only Differentiates Confirmed Facts

输入一：一个动画短剧项目，未声明交付渠道，客户只说"就是发短视频平台"。输入二：交付渠道已确认，`注意窗口`与`结尾动作`由客户给出，但推荐机制与时长上限未提供。

PASS：输入一记`Platform Profile: PENDING`、不加载任何分化层、按既有通用行为继续，也不得登记为已确认的平台剖面——媒介是动画、题材像广告、时长很短、画风像某一站都不构成依据；输入二按已确认的`注意窗口`与`完播语义`执行开场与结尾义务，转化动作由可见行为收束并回答"前面哪个Setup让它可信"，缺失的推荐机制与时长上限记Pending Decision，不猜也不声称符合该平台机制。文字级元素（二维码、价格、免责声明、入口文案）按"优先后期叠加"处理；短剧Hook窗口与五段模型仍由`knowledge/adaptation/short_form_drama_adapter.md`拥有，不新建第二套节拍模型。

FAIL：从媒介、题材、时长、画风或客户行业推定平台；用"这类片子一般是多少秒"代替用户给定的`注意窗口`；虚构平台规则或声称"符合"某平台的推荐机制；把某一平台的常见结构当作通用模板；为平台静默改写Production-Locked Script；用文字落版单独承担转化动作。

### R95-B Commercial Audience And Format Do Not Overwrite The Age Axis Or The Script

输入一：品牌项目要求"给决策者看"，同时受众已声明为儿童向。输入二：品牌项目要求在同一支片子里完成宣传、科普与招商，并需要一段医学结论。

PASS：输入一按`knowledge/branded_content/04_commercial_audience.md`排决策者说服路径（结果与代价落在动作描述与`构图`），但适宜性判据优先——不得为说服力突破`knowledge/audience_profiles.md`的分层表，也不得用恐吓、羞辱或不可解释的威胁制造痛点，两轴冲突时年龄轴优先；输入二先按`01_brand_requirement_translation.md`排序或拆为多条交付，不在单条里并列三套义务；医学结论属**一等禁项**，必须由客户提供，制作不推断、不为可读性简化到失真、不省略必要前提，缺口记Pending Decision。`05_commercial_format.md`的形态只决定"必须让观众看见什么"，不决定段落数或秒数，也不改写已锁定因果、动机与Setup / Payoff义务。

FAIL：用"决策者只关心成本"这类通用假设当项目事实；为说服力加入未成年人不宜内容；一支片子同时承担宣传、科普与招商三套义务；制作自行补写专业结论、数据、剂量或适用范围；为符合形态改写Production-Locked Script、Canonical资产或已确认Blocking；把某一形态的常见段落结构当作通用模板。
