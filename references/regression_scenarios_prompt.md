# SD Film Regression Scenarios — Prompt Translation

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是回归集的一部分；完整范围与其余文件见 `references/regression_scenarios.md` 的 Regression File Index。脚本仍只把本文件当作回归语料的一部分，不构成独立权威。本文件内部编号保持连续，可按编号直接定位，不整集通读。

覆盖范围：R15 —— Prompt 注意力、文学意图转译与工程级数据压缩

---

## R15 Prompt Attention / Translation / Physical Data

三个案例都必须保持`templates/10_video_prompt.md`固定结构，不新增五维字段，不恢复旧七字段G01；内部执行`Director Intent / Literary Intent → Visual Translation → Physical Anchoring → Prompt Compression → Final Clip Prompt`。

### R15-A Literary Camera Intent

输入：`镜头像终于鼓起勇气一样靠近她。`

PASS：保留“逐渐靠近人物内心、克制而迟疑”的情绪功能，并转译为类似`眼平中近景起镜；人物保持原姿态，摄影机在她短暂停顿后沿单一路径缓慢推进至近景；她在靠近过程中轻微垂眼、呼吸变浅，摄影机减速停住，不横移、不环绕，稳定落在双眼焦点`的可见执行语义。具体动作只能使用上游已确认内容；示例不强制垂眼或呼吸变化。

FAIL：只保留原文学句；机械删除文学意图只剩“慢推”；叠加横移、环绕和变焦；没有人物反应、触发、终点或稳定结尾。

### R15-B Over-Engineered Camera Data

输入：`摄影机1.37m高、距离人物2.43m、以0.137m/s推进，焦距53mm。`

PASS：若小数精度没有用户/模型特定依据且不改变可见结果，压缩为`眼平机位，中景起镜，约5秒沿单一路径缓慢推进至中近景，保持人物双眼对焦与稳定轴线；约50mm等效倾向`或等价可执行关系。内部记录这些数字只表达视觉倾向，不承诺严格测量。

FAIL：原样堆叠全部小数并声称模型会精确执行；删除全部摄影信息导致机位/速度/起止景别丢失；把推进、变焦与焦段变化混为一条互相冲突指令。

### R15-C Canonical Assets Free Prompt Attention

输入：当前Clip已有`CHAR-001@v003`正式角色参考与`ENV-002@v002`正式环境参考，二者真实存在、Confirmed/Active并已列入`参考资产：`；本Clip真正变化的是角色从门边走到桌前、摄影机同轴跟随、最后停在角色手放到桌面的稳定状态。

PASS：`人物一致性`与`环境一致性`只保留资产ID/版本、当前状态、不得改变项及本Clip特有风险的最小确认；不复述整段五官、服装、建筑布局与材质。Prompt注意力集中在起点、行走路径、摄影机跟随距离/轴线、手部动作顺序、桌面接触结果与稳定尾帧；Spatial Blocking、REF-TAIL、Two-Tier与Reference Routing继续按既有合同执行。

FAIL：在全局与每个分镜重复长篇角色外貌和环境结构；因资产已锁定而遗漏动作路径、摄影机行为或结束状态；删除Canonical资产引用；把Five-Dimensional Prompt Control Matrix打印成五个最终大字段。

### R15-D Director Style Label Expansion

输入：`岩井俊二式青春电影氛围。`

PASS：最终Prompt可以保留`岩井俊二式青春电影氛围`；该重要标签首次出现时，在同一`主风格`段紧跟其Project-specific Style Meaning与当前Clip必要的3—5个（或更少）高价值carriers，例如本项目将其定义为柔散自然窗光、低饱和灰绿与米白色关系、克制观察式镜头、人物以停顿/呼吸/同步反应/细微眼神变化表达关系。若处于建立轮（第一个交付Clip / 独立交付 / Style Meaning尚未被正式锁定），还必须按`knowledge/prompt_compilation/state08_projection.md`的`### 主风格 Minimum Content Rule`写足四块，含四项Aesthetic Decision Lock各一次（选择与它排除的可见结果），载体可少但不能只剩一句风格句。实际选择服从当前Clip事实，不机械复制全部示例，也不自动加入校园、校服、樱花、海边、夏日奔跑或其他未确认青春场景包。名称完全冗余时允许省略，但具象化后不默认删除。

FAIL：只写“岩井俊二式青春电影氛围”；解释仍只是“清透、唯美、克制、青春感”等抽象词；把导演名当作精准复现参数；规定carriers足够后必须删除导演名；机械复制整段风格说明；无依据增加校园/樱花/海边/奔跑；风格描述淹没主体、动作、空间、摄影机或状态承接。

### R15-E Cinematic Live-action Label Expansion

输入：`电影级真人青春短片质感。`

PASS：最终Prompt可以保留`电影级真人青春短片质感`；首次出现时在同一风格段具体解释为当前Clip最需要的3—5项（或更少），例如真实演员自然肤质与皮肤细节、自然曝光关系和真实暗部层次、浅景深、轻微胶片颗粒、受控高光或克制的镜头动态。选择必须与已确认媒介、资产、光源、动作和Generation Budget一致，不把示例整段固化成模板。

FAIL：只保留“电影级 / 真人感 / 青春感”；用“高级、真实、有质感”等同级抽象词循环解释；堆叠8K、ARRI、award winning等器材/质量词；无依据新增商业布光、黑金配色或广告式摆拍；为了填满维度而制造冲突。

### R15-F Stable Project Style Delta

输入：CLIP-001已在Confirmed Visual Direction / Project Bible与Canonical角色、环境资产中锁定`岩井俊二式潮湿夏日青春氛围`的项目特定含义；CLIP-002为直接连续段，只增加窗外雨势变弱、人物关系由回避变为短暂同步反应，其他项目风格不变。

PASS：CLIP-002按`Source Carries State, Prompt Carries Delta`在`主风格`保留标签或已确认风格锚点，只补“雨势变弱后的柔散窗光保持、两人以一次同步抬眼建立关系”等当前delta与风险；不复制CLIP-001的完整光线、综合色彩、肤质、颗粒、镜头和表演说明。同一标签在本Prompt中不重复解释。若正式Style Source不可访问或含义发生变化，则重新展开受影响部分。

FAIL：每个连续Clip完整复制同一长篇Visual Bible；只因是“后续Clip”就在没有正式Style Source时写裸标签；省略当前Clip真实变化的光态、表演或风险；在主风格和每个分镜反复解释同一标签。

### R15-G Action-Heavy Clip Style Compression

输入：一个动作复杂Clip已经需要锁定双人身份、追逃前后关系、单一摄影机路径、道具换手顺序、环境障碍、动作Endpoint与下一Clip Handoff，同时上游还给出多个导演/流派/情绪标签。

PASS：主体、动作、空间、时间顺序、摄影机路径、道具状态与Handoff优先；风格自动压缩到能直接帮助读懂当前Beat的1—3个或更少高价值carriers，例如稳定的冷灰综合色彩、克制手持和足够景深。压缩的是**表达与载体数量**：已锁定的Aesthetic Decision Lock四项锚点仍按`knowledge/prompt_compilation/state08_projection.md`的`### 主风格 Minimum Content Rule`保留。一个仍有统一锚定价值的重要标签可以保留并用这些carriers简短解释；完全冗余、无关或冲突的其他标签允许省略，但不存在“具象化后默认删除导演名”的硬规则。固定Template字段仍完整，Generation Budget与Five-Dimensional Matrix不变成最终栏目。

FAIL：为保留风格而删减动作步骤、空间方向、道具状态或Endpoint；同时堆叠多个导演、赛博朋克、黑帮感、广告感、胶片感与器材名；要求风格必须占满3—5项；以“压缩”为由删掉四项Aesthetic Decision Lock锚点或把`主风格`压成一句风格句；以压缩为由删除Template字段。

### R15-H Positive Specification And Unified Negative Prompt

输入：`岩井俊二式潮湿夏日青春气质；禁止夸张微笑、甜宠式表演、广告摆拍、MV慢动作与炫技运镜。`

PASS：`主风格：`可以保留并展开`岩井俊二式潮湿夏日青春气质`，但以柔散自然窗光、低饱和灰绿/米白、安静观察式摄影、克制含蓄表演、细小停顿/视线/手部动作与简洁自然镜头调度等当前Clip必要的正向carriers执行；不在正文重复原负向清单。只有仍属当前高风险、正向描述难完全锁定的残余错误经过合并压缩后进入末尾唯一`反向提示词：`。

FAIL：在`主风格 / 人物一致性 / 画面描述 / 人物动作与情绪`继续散布“禁止 / 不要 / 避免”清单；把原句完整复制到多个字段；删除风格标签但没有建立执行carriers；末尾反向段与正文同义重复或比动作/空间/镜头正文更长更抢权重。

### R15-I Multi-Shot Single Final Negative Prompt

输入：一个包含三个分镜的Confirmed Clip，三个分镜共享角色一致性、克制表演和空间轴线风险。

PASS：三个分镜正文分别写清当前动作、空间与连续性正向状态，不重复通用负向清单；整个Clip只有一个`反向提示词：`，位于最后一个分镜全部字段之后，并且是当前Clip最终段落，其后无任何备注或正文。

FAIL：每个分镜各写一次反向清单；出现两个或更多`反向提示词：`；反向段出现在分镜之间；末尾反向段之后仍有尾帧说明、音色字段、备注或补充正文。

### R15-J Local Physical Continuity Constraint

输入：某分镜要求`左手始终握住伞柄，不能换手`，且换手会破坏上一镜到下一镜的动作连续性。

PASS：在该分镜的`起始状态 / 人物动作与情绪 / 道具状态 / 镜头结尾状态`中适用位置保留最小、指代清楚的连续性约束，优先写成`左手持续握住伞柄，整个动作链与结尾状态均保持左手持有`；不把它扩展成局部通用负向清单。跨镜通用高风险项仍只在末尾唯一反向段收束。

FAIL：为了统一负向位置而把持伞手约束全部移走，导致具体动作链不清；在每个字段重复“不能换手”；把雨伞约束扩展成长串通用负向词；用反向提示词掩盖上游持有者或左右手事实冲突。

### R15-K Voice Omission Survives Negative Placement Change

输入：角色有对白，用户只要求普通Seedance Clip Prompt，没有明确要求当前视频模型使用声音/音色控制。

PASS：本次正向优先与反向段调整不改变Voice opt-in边界；最终Prompt完全省略`音色特征：`、Voice Profile、Voice/Audio Reference和声音资产状态文字；`反向提示词：`仍为最后字段。

FAIL：为了统一字段位置而重新加入`音色特征：`或占位语；把声音资产状态塞到反向提示词之后；把固定禁BGM句误当作声音身份授权。

### R15-L CLIP-03 State Ownership / Negative Compression

输入：真实回归样本CLIP-03《落下的乐谱与四个单音》。已确认两名角色身份、ENV-02旧音乐教室与唯一横向长琴凳、REF-TAIL-02承接、乐谱视觉资产；Clip内发生“从前态调整为共坐正常坐姿 → 乐谱落地但无人拾取 → 两人交替完成四个独立单音”。用户没有显式要求声音身份控制。上游风格锚点包含`岩井俊二式潮湿夏日青春氛围`。

PASS：

- 先建立Ownership Map：`参考资产`只声明真实Source及用途；`首帧参考`权威定义起始左右/姿态/共用长琴凳与Direct承接；`人物一致性`只保留身份/年龄/发型/服装/比例；`环境一致性`只保留教室结构、唯一长琴凳结构与阴雨光态基线；逐镜只写新增动作、状态变化和局部物理关系；`尾帧限制`权威定义结束坐姿、乐谱状态、四音完成状态与carryover。
- “同一张长琴凳 / 林夏左许栀右 / 乐谱不捡 / 四个单音”各有唯一完整定义；其他位置只在状态变化、首尾接口或局部高风险时写`保持该状态 / 乐谱留在地面 / 完成下一次单音`等最短Delta，不在6—9个字段全文重复。
- 正文把座椅、左右、手部和演奏范围写成正向可执行状态；只保留必须贴近动作链的最小局部物理约束。
- 雨声、风声、窗帘、纸张滑落/落地和四个钢琴单音进入各分镜`音效`；最终完全没有`音色特征：`、Voice Profile、Voice/Audio Reference或声音资产状态文字。
- 最终只有一个末尾`反向提示词：`。固定禁BGM首句之后只保留当前Clip少量高风险类别，例如座椅结构分裂/人物左右互换、人物离座或拾取乐谱、肢体异常、演奏范围自动扩展、身份/环境漂移与夸张表演/摄影偏移；相近错误合并，不逐项复述正向状态。
- 删除猫、吉他、手机、磁带等历史事故物、未来Clip事件和当前未出场资产；反向段不成为事故历史清单，也不压过主体、动作、空间、镜头、时间状态与Handoff。
- `岩井俊二式`标签可保留，并在首次出现的同一`主风格`段给出当前项目可执行解释；Style Label Expansion不因去重失效。
- REF-TAIL继续按A Direct用途存在，Reference Asset Eligibility、Accepted Take Canon与Shot-State Memory不被State Once去重削弱；首帧与尾帧仍足以复算连续性。

FAIL：把唯一长琴凳、左右、乐谱和四音规则在参考用途、首尾帧、人物/环境一致性、每个分镜与反向段全文重复；正文仍散布通用`禁止/不得/不要`清单；用`音色特征：`承载雨风纸张或钢琴声；反向段包含事故历史、未来剧情或与当前Clip无关资产；去重后首帧/尾帧不足以复算A Direct连续性；删除或孤立风格标签而不做Style Label Expansion。

---
