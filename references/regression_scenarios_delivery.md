# SD Film Regression Scenarios — Delivery Validation

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是回归集的一部分；完整范围与其余文件见 `references/regression_scenarios.md` 的 Regression File Index。脚本仍只把本文件当作回归语料的一部分，不构成独立权威。本文件内部编号保持连续，可按编号直接定位，不整集通读。

覆盖范围：R48 —— 交付物校验、覆盖与尺度

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
