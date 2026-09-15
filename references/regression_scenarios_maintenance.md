# SD Film Regression Scenarios — Delivery, Aesthetic And Maintenance

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是回归集的一部分，由`references/regression_scenarios.md`的 Regression File Index 统一索引；本文件内部编号保持连续，可按编号直接定位，不整集通读。

覆盖范围：R48—R63 —— 交付物校验、美学决策与试片、维护体系与可达性、媒介剖面、分镜拆解覆盖、Review审美判断、阶段落点覆盖、FAST不变量与交付收据。

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

### R48-I Package File Names Never Enter The Prompt Reference Name

输入：一份已交付的Seedance 2.5 Package，其`多模态参考资产：`写成`- @图片6：PROP-001｜Identity.png；用途：未点亮花灯造型基准`与`- @图片7：PROP-001｜State.png；用途：点亮后状态基准`；同一项目另有`- @图片1：CHAR-001`（缺资产名与分隔符）。

PASS：`scripts/validate_prompt_package.py`逐条报出——携带文件扩展名（包内文件名不进入引用名）、同一Asset ID出现多次却未补View Code或Purpose、以及缺少`<资产ID>｜<资产名>`形态；改写为`PROP-001｜花灯_Identity` / `PROP-001｜花灯_State` / `CHAR-001｜阿蘅角色身份图`后同一Package通过。`REF-SKETCH-01｜CLIP-01草图.png`、色卡与用户提供的首尾帧沿用登记名，保持豁免。

FAIL：把`PROP-001｜Identity.png`判为合规；或为通过检查给`REF-*`、色卡、用户素材强加Asset ID；或只保留结构断言、把这条形态要求留给"人工注意"。

### R48-J Style Field Carries No Generic Negative List

输入：一份Package的`主风格：`写成`…镜头如压住呼吸般平稳，人物表演内收，不做破败恐怖、灵异、鬼火或脏乱惊悚感。`，同一Package末尾`反向提示词`已列出同一批禁止项；另一个H3 Package把`避免快摇`写在`核心创意`的第二行。

PASS：校验器报出`主风格`出现`不做`（同义负向约束按`禁止 / 不要 / 避免 / 不做 / 拒绝 / 不得`判定），要求改写为正向边界或移入末尾唯一`反向提示词`；H3只检查`主风格：`那一行，第二行的主体与运镜描述不在射程内。Aesthetic Decision Lock里"排除了什么可见结果"属于必需内容，不得被这条断言误伤。

FAIL：把`拒绝…` / `不做…`当风格描述放过并同时保留末尾同义清单；或反向地要求删除四锁的"排除"内容，使Aesthetic Decision Lock被压缩成只剩选择。

### R48-K A Style Field Without Lock Dimension Names Warns

输入：一份Seedance 2.5 Package的`主风格：`只写"墨焰式新中式。冷灰与黑漆构成干净层次；旧花灯是唯一暖色，暖光只短暂掠过侧脸。"，没有出现任何Aesthetic Decision Lock维度名；另一份把四个维度名各写一行、每行含选择与排除项。

PASS：校验器对前者给出`WARNING`（"未出现四项Aesthetic Decision Lock维度名…本条只提示，不阻断交付"）且`errors`为空、退出码为0；对后者无该提示。四锁的"排除了什么可见结果"照旧属于必需内容，不因这条提示被要求删除；部分覆盖与措辞正确性仍由Output QA人工判定。

FAIL：把该缺口做成硬阻断，使合法的后续Delta Clip无法交付；或反向地因为"校验器通过"就认为四块已经写足。

### R48-L A One-Take Time Line May Not Be One Uniform Drift

输入一：一份30秒Seedance 2.5 Package的五个阶段分别写"平稳低速向后退 / 极小的右前弧移 / 连续低降再缓慢回升 / 极小幅靠近 / 极慢后移"，没有任何一段写明静止、停驻、反向或幅度变化。输入二：其余相同，但第一段写成"摄影机固定不动"。输入三：只有两个阶段的短Clip。

PASS：输入一得到`WARNING`（"运镜语汇同质…一镜到底只约束不切，不约束镜头内运动层次"）且`errors`为空、退出码为0；输入二与输入三无该提示（静置段构成可指认差异；两段以内不在射程内）。真实成片回放与此一致：提示词五段皆小幅缓动时，生成结果等于一个固定双人全景，t=6s与t=18s的机位、高度、距离、背景结构完全同位。

FAIL：把刻意静止的合法长镜判为不合格或做成硬阻断；或反向地因为提示词写了五种运镜名就认为成片有运镜层次——写入词表不等于画面可达。

### R48-M Scene Breakdown And Storyboard Stubs Are Rejected

输入一：Scene Breakdown交成两条bullet（`SCENE-001：雨天教学楼走廊，女孩离开；CHAR-001 / ENV-001。`）。输入二：分镜表交成一行一句的`SHOT-001 女孩窗边按灭手机；SHOT-002 她走向楼梯；…`。输入三：某行分镜的`画面表达`留空，且镜号从SHOT-001跳到SHOT-003。输入四：Clip表只写"已确认CLIP-001，规划完成"。

PASS：`scripts/validate_delivery_artifacts.py --kind scene-breakdown | shot-design | clip-plan`分别报出缺少Template区块与Scene Directing Brief子项、缺少默认5列表（"一行一句的分镜清单不是Template交付物"）、空单元格与编号断档、缺少默认6列表；改用逐场Brief + 七个区块、默认5列表、默认6列表后全部通过。完整十八列专业分镜（用户明确要求"完整版专业分镜"时）同样被接受。

FAIL：把bullet清单或一行一句当成交付物放过；或反向地要求默认分镜表逐格展示十八个内部字段（`templates/08_shot_design_prompt.md`的`## Default User-facing Delivery`已覆盖该读法）；或要求Clip表展示Preflight、参考预算等内部账本。

### R48-N Category Manifests Stay Readable One Row Per File

输入一：某包有两套环境资产、各四张视角图，类别清单把同一Asset ID的四张图挤进一个`文件名`单元格（`ENV-001｜Layout_ENV-01.png、…_ENV-04.png`）。输入二：用户照着包内文件找Prompt里的`ENV-001｜教学楼走廊_ENV-03`，清单里没有资产名也没有视角角色可读。

PASS：`02_assets/<KIND>/_MANIFEST.md`一行一个文件，列`文件名｜Asset ID｜资产名｜Purpose｜View角色｜Active Version｜Status｜Approval Basis｜Prompt引用名`；`View角色`把View Code译成Master Establishing / Reverse / Lateral / Top-Down / EXT，非环境视角写`Not Applicable`；`Prompt引用名`写出`ENV-001｜教学楼走廊_ENV-03`形态，使包内文件与Prompt参考条目逐行对应；`00_MANIFEST.md`明细同样带`资产名`与`Purpose / View角色`。**文件名本身不变**，已确认资产不被追溯改名。

FAIL：把同一Asset ID的多张Canonical图合并成一行；只列`Layout_ENV-03`而不给视角角色与资产名，逼用户去背View Code表；或反向地为了可读而改名已确认资产图片（那会使已交付Prompt的参考条目失效）。

### R48-O A Cutting Clip May Not Cite Only The Master Environment View

输入：一份30秒Seedance 2.5 Package含切场（`由湿地倒影自然切到校门内侧`）并跨两个空间，`多模态参考资产`只列 `ENV-001｜教学楼走廊_ENV-01` 与 `ENV-002｜校门与操场_ENV-01`；包里当时实际有每套空间四张View。另一份Clip只有一个空间、无切场、轴线稳定，同样只列 `_ENV-01`。

PASS：前者得到非阻断`WARNING`（"环境参考只出现母参考（`_ENV-01`），没有反向或侧向视图…请按路由覆盖不变量确认是否需要补 `_ENV-02` / `_ENV-03`"）且`errors`为空；后者无该提示。真实成片回放与此一致：只列Master时，成片出现外套敞开→立领合襟的服装状态漂移与空间背景不一致——图在包里，但没有被路由进Prompt。

FAIL：把只列Master一律判为不合格或硬阻断（单空间稳定Clip是合法的）；或反向地因为"包里有四张View"就认为Prompt已经覆盖——包内存在不等于已路由。

### R48-P Fixed Structures Are Never Penetrated And Never Duplicated In Reflection

输入一：一份走廊Clip沿窗带行走，`多模态参考资产`只列 `ENV-001｜教学楼走廊_ENV-01`，文字里既没写她在玻璃的哪一侧，也没写反射是否表现。输入二：同一Clip补了 `ENV-001｜教学楼走廊_ENV-03` 侧向View，或写明"人物始终在窗内侧、玻璃只作前景遮挡、不表现反射"。输入三：STATE-09 Technical Review 的固定结构穿透检查项在位。

PASS：输入一得到两条非阻断`WARNING`（环境视图覆盖 + 固定平面与反射未锁定）且`errors`为空；输入二两条都不再出现；技术Review逐项核对"人物/道具没有穿过墙、玻璃、窗、门框、栏杆或幕墙；同一主体没有在反射面里出现第二个副本；窗框、立柱、墙垛在同一帧里只遮挡主体，不与主体互穿；反射只按`环境一致性`锁定的策略出现"。真实成片回放与此一致：只列Master且无平面锁时，8秒处玻璃里出现第二截白袖子与人形剪影（反射副本），10秒处她的躯干嵌进窗框与墙垛、一半在结构这侧一半在另一侧（深度顺序反转）。

FAIL：把`校门内侧`这类地点词当成平面锁（锁必须紧邻平面词，如`窗内侧`）；把提示做成硬阻断；或只检查摄影机穿墙这类S4高风险运镜，而放过"主体穿过固定结构 / 反射里出现第二个副本"这一类失败。

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


## R64 Delivered Artifact Completeness Guard Regression

### R64-A The Completeness Rule Has A Consumer On The Packaging Path

输入：一次真实交付把会话里的摘要直接当工件落盘——`05_shots` 是 202 字节的一行一句清单、`04_scenes` 是两条 bullet、`06_clips` 是一句话——然后按目录结构打包。三个 Template 里"保存为文件时必须运行`scripts/validate_delivery_artifacts.py`，未通过不得交付"当时已经写着，包的目录、命名、清单也全部合规；另一份包相同，但三个源工件是完整 Template 形态。

PASS：`scripts/build_asset_package.py` 在写包之前对 `04_scenes` / `05_shots` / `06_clips` 的源工件运行该 owner 的对应`--kind`检查（**导入该 owner，不复制判据**），摘要形态判`BLOCKED`并逐条报出"哪一类 / 哪个文件 / 缺什么"，**不创建包目录、不生成zip**——避免"半个包"被当成已交付；完整形态的包正常通过这一门。文件名、目录结构与`00_MANIFEST.md`正确**不构成**工件完整的证据。

FAIL：规则只写在 Template 里、打包路径上没有任何消费者，靠执行者自觉运行校验器（于是摘要照样进包并被当作已交付）；或反向地把该门做成WARNING / 事后报告，让不合格的包先生成再说；或在校验器不可读时静默跳过该检查。


## R65 Standalone Invocation Regression

### R65-A A Standalone Run Never Counts As Progress

输入一：用户说"只重做 STATE-06 分镜表，别推进后面的阶段"，项目当时停在 STATE-04；同一次运行给出完整分镜表、用户确认，系统把 `Current State` 写成 STATE-06、`Next Workflow` 指向 Clip Production。输入二：同一请求，但这次只登记 `Active Artifacts` 与 Revision，`Completed States`、`Current State`、`Next Workflow` 都不变，`Pending Decision` 写明"独立调用交付，未计入主Pipeline进度"。输入三：用户说"只调用 Storyboard 模块"，系统把它登记成 `Completed States` 里的一项。

PASS：输入一被判为违规——独立调用不是顺序豁免，产出工件不等于走过该阶段；输入二通过，且该阶段将来被主Pipeline合法走到时按"已确认工件不重做"沿用这份工件而不重做；输入三同样违规——辅助模块不进入 `Completed States`，它最多登记为 Optional/Auxiliary Artifact。三种情形下 `scripts/validate_sd_film.py` 的 `check_standalone_invocation` 都要求"被调用单元仍满足自己的 Entry Gate"与"不计入项目进度"两句话仍在各自的 owner 里。

FAIL：把独立调用当成本节通道之外的捷径——用它跳过中间 STATE、把产物当成阶段完成、把辅助模块写进主路由，或反向地因为"不计入进度"就把独立交付降级成草稿 / 临时产物 / `Not Applicable`（它是正式 Confirmed Artifact，只是不改变主Pipeline进度）。
