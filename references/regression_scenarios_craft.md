# SD Film Regression Scenarios — Craft

本文件是回归集的一部分；完整范围与其余文件见 `references/regression_scenarios.md` 的 Regression File Index。脚本仍只把本文件当作回归语料的一部分，不构成独立权威。覆盖 Prompt 编译、表演、视觉阻断、剧本与导演端到端（R15—R23）。

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

PASS：最终Prompt可以保留`岩井俊二式青春电影氛围`；该重要标签首次出现时，在同一`主风格`段紧跟其Project-specific Style Meaning与当前Clip必要的3—5个（或更少）高价值carriers，例如本项目将其定义为柔散自然窗光、低饱和灰绿与米白色关系、克制观察式镜头、人物以停顿/呼吸/同步反应/细微眼神变化表达关系。实际选择服从当前Clip事实，不机械复制全部示例，也不自动加入校园、校服、樱花、海边、夏日奔跑或其他未确认青春场景包。名称完全冗余时允许省略，但具象化后不默认删除。

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

PASS：主体、动作、空间、时间顺序、摄影机路径、道具状态与Handoff优先；风格自动压缩到能直接帮助读懂当前Beat的1—3个或更少高价值carriers，例如稳定的冷灰综合色彩、克制手持和足够景深。一个仍有统一锚定价值的重要标签可以保留并用这些carriers简短解释；完全冗余、无关或冲突的其他标签允许省略，但不存在“具象化后默认删除导演名”的硬规则。固定Template字段仍完整，Generation Budget与Five-Dimensional Matrix不变成最终栏目。

FAIL：为保留风格而删减动作步骤、空间方向、道具状态或Endpoint；同时堆叠多个导演、赛博朋克、黑帮感、广告感、胶片感与器材名；要求风格必须占满3—5项；以压缩为由删除Template字段。

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

## R16 Delta / Budget / Scope / Canon / Authority / Retake

以下案例必须沿用现有STATE-07 Clip Contract、八组Shot-State Memory、Reference Selection / Routing、Execution Ledger、STATE-09 Review与`templates/10_video_prompt.md`固定结构；不得新增主STATE、Clip Registry、平行Project State或最终Prompt字段。

### R16-A Canonical Sources Carry State, Prompt Carries Current Delta

输入：已有Confirmed / Active角色与环境正式资产；当前Clip只发生角色从门边走到桌前、摄影机同轴跟随并停在手触桌面的Endpoint。

PASS：`参考资产`保留正式ID/版本/Primary Role，`人物一致性 / 环境一致性`只作当前状态、风险和不得改变项的最小确认；Prompt主体集中描述行走、摄影机路径、手部接触、时间顺序与稳定Endpoint。模板字段完整但不重复长篇五官、服装、建筑结构与材质。

FAIL：删除正式资产引用；在多个字段重复完整角色/环境设定；因压缩而丢失当前动作、镜头Delta或Endpoint。

### R16-B Generation Budget Allocation

输入：同一候选Clip要求完美身份、复杂奔跑打斗、五人群体、繁忙雨景、环绕运镜、多人对白口型、强FX和变化灯光。

PASS：内部先明确一个Primary Spend（例如双主角身份与核心攻防Beat）、最多一至两个Secondary（例如主空间关系与单一路径跟随），并把群体活动、复杂环绕、非必要口型、额外FX或光色变化写入Economized / Safe Downgrade；Five-Dimensional Matrix只高控制必要未锁定项。若仍超载则返回STATE-07/06拆分。

FAIL：五维全部补满；Primary不唯一；Economized为空；把`Primary Spend / Secondary Spend / Economized`打印成最终Prompt字段。

### R16-C Accepted Take Overrides Planned Transient State

输入：CLIP-03 Planned End为“左手搭手背”，实际Take的Observed End为“右手搭手腕”，用户明确接受该Take；Run、Prompt Revision、Review与接受证据齐全。

PASS：Execution Ledger分别保存Planned与Observed；Accepted Canon State采用“右手搭手腕”。CLIP-04从右手/手腕状态继续，不无过程纠回左手/手背，也不重播接触动作；正式角色/环境/道具资产身份仍不变。

FAIL：未记录Observed；下一Clip强行按原计划恢复左手；把未接受Take写入Canon；因接受动作结果而改变正式资产身份。

### R16-D REF-TAIL Identity Drift Is Not Identity Authority

输入：上一Accepted Take / `REF-TAIL`的脸部略漂移，但Active Character Canonical Reference正确；下一Clip需要继承尾帧姿态、站位与动作阶段。

PASS：角色Canonical Reference声明Identity Authority，`REF-TAIL`声明Transient State Primary Role；下一Clip保持正式角色身份，只从尾帧/Accepted Canon继承姿态、站位、朝向、人物距离与动作阶段，并把脸部漂移列为Continuity Risk。

FAIL：让尾帧覆盖正式脸部身份；完全丢弃尾帧导致站位/动作阶段重置；不写Primary Role / Purpose；把漂移尾帧升级为角色Canonical资产。

### R16-E Single-Variable Retake For Blocking Error

输入：生成结果只有人物站位错误，身份、动作、镜头、光线、道具与其他连续性均正确。

PASS：Review诊断为Spatial / Blocking，选择它为最高影响变量；第一轮只修Affected Clip的空间关系/Blocking与必要相邻边界，保留其他已接受内容；Retake后只比较站位及其边界是否改善。若可后期安全修复则路由Editing并说明范围。

FAIL：整段Prompt全部重写；同时更换角色资产、动作、运镜、光线与道具；没有前后Take比较；以“整体感觉”直接REBUILD。

---

## R17 Voice Identity Opt-In And Prompt Isolation

### R17-A No Voice Request

输入：角色有对白，用户只要求继续主Pipeline或输出当前Seedance Clip Prompt，没有提出音色制作或当前视频声音控制要求。

PASS：不进入AUDIO模块；默认外部已有可用角色音色资源；STATE-02/03/08均不阻塞；视频Prompt完全省略`音色特征：`、Voice Profile、Voice/Audio Reference及“已有/缺失/无需音色”等状态文字。台词只保留准确文本与必要Dialogue Performance。

FAIL：要求补建Voice Profile；创建Not Applicable；返回STATE-03；输出`No Voice Asset`或无对白占位；把音色描述写进视频Prompt。

### R17-B Explicit Voice Design

输入：`为女主设计音色。`

PASS：Router返回`AUDIO / SEED-AUDIO Voice Asset`，从当前项目阶段独立进入音色模块；输出独立Voice Profile和明确标记为“SD Film为Seed Audio 1.0组织的兼容模板”的Prompt。Prompt描述speaker，分离稳定Voice Identity与当前Dialogue Performance，并只按需输出Voice Description、Emotional Tone、Delivery / Prosody、Dialogue、Timing、Ambience、Key Sound Effects、Scene Progression和获授权Reference Audio；不强行并入视频Prompt。

FAIL：继续普通Character Asset；把声音交付塞进STATE-08；冒充官方唯一字段模板；固定要求15秒、八条`No...`声明或无关视觉描述。

### R17-C Confirmed Voice Exists But User Requests Only CLIP-03 Prompt

输入：Active CHAR Version已有Confirmed Voice Profile或Voice Audio Reference；用户只说`输出CLIP-03 Seedance提示词。`

PASS：Confirmed声音资产只作为Source State存在，不投影到CLIP-03视频Prompt；`音色特征：`和Voice/Audio Reference均省略。主流程按STATE-08其他Gate继续。

FAIL：自动复制Voice Profile；写“由参考音色锁定”；仅因已有声音资产就把Reference列入`参考资产：`；把先前AUDIO授权外推到当前请求。

---

## R18 Spatial / Performance / Action PREVIS Minimal Integration

### R18-A Two-Person Dialogue And Bench Axis Continuity

输入：同一教室连续场景，A与B并排坐在唯一横向长凳上，A始终在观众画面左、B在画面右；先给双人建立镜，再做同一轴线侧的正反打。中段导演有意让A起身绕到B另一侧，并要求越轴后继续对话。

PASS：Scene Spatial Snapshot锁定长凳、门、窗、钢琴等Fixed Environment Anchors、A/B起始位置、Eyeline Axis与camera safe side；普通正反打保持相反眼线与同侧机位。A换位时记录`Start Position → Visible Movement Path → End Position`，通过角色镜内明确换位并以固定地标建立新轴线侧，随后屏幕左右翻转被判为合法；Environment Canonical继续锁空间身份，不因人物换位重做环境资产。Shot-State Memory记录换位后的局部状态，A/B/C `REF-TAIL`仍按边界需要选择。

FAIL：下一镜A/B无过程换边；把所有屏幕左右当成场景东/西；只写“创意越轴”而没有可感知过渡；或把合法新轴线一律判错并强迫永不越轴。

### R18-B Restrained Youth Drama Uses Minimal Carriers

输入：4秒青春片反应镜头。角色听见朋友轻声道别，选择不挽留；剧本要求克制，没有崩溃、哭喊或重大揭示。

PASS：路由为Performance-dominant，使用PL1；只选择1—2个载体，例如视线停在对方手上后短暂移开、呼吸停半拍再缓慢恢复，并以手指停止动作或肩膀保持不动作为可选支持。保留“想挽留但压住”的公开状态/局部泄漏与稳定余韵，不强制完整递进链，不自动加入落泪、吞咽、瞳孔变化或大幅后退。

FAIL：机械输出触发—瞳孔—下颌—吞咽—指尖发白—呼吸粗重—失控哭泣的完整链；或仍只写“她悲伤而复杂地看着对方”。

### R18-C A3 Choreographed Action Has Physical Causality

输入：一段经过剧情授权的复杂格挡—转身—反制动作，起始双方站位、主Action Axis、道具状态与最终“攻击者失衡、主角稳定防守架”结果已确认。

PASS：路由为Action-dominant并选择A3；Action PREVIS写清Trigger、Preparation、Weight Shift、Ground / Foot Drive、Hip / Torso Transfer、Limb / Prop Trajectory、Contact / Near-contact、Force Response、Follow-through、Recovery / End State与Next-action Carryover中的必要链节。景别与Coverage让支撑、轨迹、接触和结果可见；结尾把攻击者失衡方向、主角支撑脚/朝向、道具持有与摄影机safe side写入Shot-State Memory，供下一Shot或Accepted Canon继承。

FAIL：只写“主角猛地反击、双方激烈打斗”；接触、受力和结束状态缺失；下一镜双方恢复初始架势；或因为A3自动加入玄幻FX、0.5秒硬撞、机枪式对招和高潮定格。

### R18-D A1 Simple Action Stays Simple And Prompt Stays Clean

输入：角色从桌面拿起一封信，转身看向门口，Clip内没有追逐、对抗、复杂道具、FX或高强度表演。

PASS：路由为Action-dominant或Mixed中的低复杂度动作，选择A1，只写右手从桌边起始、沿短路径握住信封、信封离开桌面并稳定保持在右手、角色转头后视线落向门口的Start / Path / End；不添加完整动力链、精密角度、速度、受力参数或复杂运镜。STATE-08不输出A1、Kinetic Chain、PL等级、Shot Purpose、QA或路由标签，继续按`Source Carries State, Prompt Carries Delta`只保留当前Clip必要Delta。

FAIL：为拿信加入蹬地、腰胯、脊柱传导、空气反馈、接触力数值与多段摄影机；或把内部11环、六阶段和Purpose列表逐项塞进最终Prompt。

---

## R19 Visual Blocking Sketch / Clip Prompt Gate

### R19-A CLIP-04 First Prompt Requires One Confirmed S+P Anchor

输入：CLIP-04中林夏在左、许栀在右，共坐同一张长琴凳，共同面向钢琴 / 窗外；许栀仅允许`Gaze + LIMITED Head`，Position / Torso / Shoulder / Distance锁定；林夏持续弹琴且不转头。用户首次请求`输出CLIP-04提示词`或只说`下一个`。

PASS：STATE-07已记录Visual Blocking Risk Pre-Assessment；STATE-08 Final Assessment判`HIGH / REQUIRED`，本轮先生成中性S+P综合草图，核对role mapping、林夏左 / 许栀右、Side-by-side、Same Bench、Shared Facing、许栀Gaze→林夏、`Head LIMITED`、Pose Hierarchy、Eyeline Axis与Camera Safe Side。林夏与许栀必须使用同一套无性别技术人偶，只靠蓝 / 红角色标签、姓名和左右位置区分，不以长发 / 短发、裙装 / 裤装或身体曲线区分。通过后注册`REF-SKETCH-04｜CLIP-04空间与姿态调度草图`，说明`草图人物为无性别调度人偶，仅用于空间 / 姿态 / 机位关系，不作为人物外观参考。`加入当前Clip参考资产并更新预算，本轮不输出Prompt。用户下一次继续且Signature未变时才输出Prompt。即使A/B左右未换，Side-by-side漂成Face-to-face仍判Blocking Drift。

FAIL：第一次请求直接输出Prompt；生成草图后未验证或未列入参考资产；把草图当角色 / 环境Canonical；用性别、发型、服装或体型区分林夏 / 许栀；让“许栀看林夏”自动导致全身转向；或认为左右没交换所以Face-to-face不算漂移。

### R19-B Prompt Rewrite Reuses Anchor; Blocking Reconstruction Reassesses

输入：CLIP-04已经有Confirmed `REF-SKETCH-04`。用户连续多次要求压缩措辞、优化主风格、整理反向提示词、调整台词 / 音效，Blocking不变；随后大幅重构为许栀起身走到林夏面前。

PASS：普通改写每次只比较Current Revision与Blocking Signature，结果为KEEP并复用同一草图 / 图片位，不重复生成。起身、移动到面前使Same Bench、Position、Topology、Distance、Movement Path与Clip End Blocking实质变化，触发Reassessment并得到`REPLACE with REF-SKETCH-04-v2`或`RETIRE + CREATE`；新草图重新验证后才输出重构Prompt。

FAIL：每次措辞优化都重新出图；Prompt改写导致草图版本自身漂移；或大幅Blocking重构仍盲用旧图且不重新评估。

### R19-C Simple Single Person Is NONE

输入：单人原地站立，只做普通转头；固定机位，无共享空间结构、换位、复杂道具、跨轴、复杂前中后景或A2/A3动作。

PASS：每Clip检查仍执行，但Final Assessment=`NONE`；不生成、不预留`REF-SKETCH`，直接编译Prompt。

FAIL：为了流程统一强制生成P-SKETCH或Formal Keyframe。

### R19-D A3 Action May Use A-SKETCH Or Combined Anchor

输入：A3复杂格挡—转身—反制动作，双方起点、主Action Axis、道具、接触 / 近接触、受力方向、恢复终点与Next-action Carryover已确认，但单纯文字仍存在路径 / 接触漂移风险。

PASS：Final Assessment可判`ACTION HIGH / REQUIRED`，选择A-SKETCH或S+P+A综合草图；双方使用同一套无性别技术人偶，以箭头、轴线、接触点和受力方向锁定Start / Path / Contact / Force / End / Carryover。只有动作可达性必需的身体比例可以表达，仍不恢复性别、脸、发型、服装或角色体型身份。通过Sketch Validation与Character Appearance Leakage Check后作为受限Visual Blocking Anchor进入参考资产。角色、环境与道具身份继续由各自Canonical资产控制；Prompt正文只保留当前动作Delta与必要局部约束。

FAIL：A3一律强制多张正式Keyframe；草图带入写实五官、正式服装 / 灯光 / 画风并覆盖Canonical；或把全部动力链和草图标注复制进Prompt。

---

## R20 REF-SKETCH-MASTER Presentation Authority

### R20-A Piano Pair Uses Technical Blocking Sheet Language

输入：CLIP-04仍为林夏左 / 许栀右、Side-by-side、Shared Facing、Same Bench，许栀只有`Gaze + LIMITED Head` Delta；`REF-SKETCH-MASTER`注册为真实可读视觉输入，示例图本身也包含两女与钢琴内容。

PASS：Final=`REQUIRED`时把母版只作为Sketch Presentation Authority输入，当前Blocking Signature作为内容权威。输出是自适应Technical Director Blocking Sheet，Main Blocking、Spatial / Top-down、Camera Information、Permission与Usage区能直接证明林夏左 / 许栀右、Side-by-side、Shared Facing、Same Bench、许栀Gaze→林夏和`Head LIMITED`；两人使用同一套无性别人偶，只由蓝 / 红角色标签、姓名与位置区分，不继承母版或Character Asset中的性别、发型、服装、体型。当前`REF-SKETCH-04`通过验证后进入视频参考资产；母版本身不进入。

FAIL：提示词核心仍是唯美铅笔Storyboard、雨天青春电影或人物插画；以长发 / 短发、裙装、脸或身体曲线区分两人；缺少Topology / Facing / Gaze / Camera证明；或因为案例内容与母版相似就把母版本身当当前Clip Blocking Authority。

### R20-B Three People Around A Table Has No Template Content Leakage

输入：Current Clip是A / B / C三人围圆桌交谈，环境为干燥会议室，无钢琴、长琴凳、窗边雨景或乐谱；需要锁定三人座位、共同视线中心、Camera Safe Side和发言者局部转头。

PASS：继承母版的信息层级和技术标注语言，但Main Blocking与Top-down重新布局为三人环桌Topology；三人使用同一套无性别技术人偶，只靠A / B / C角色标签、技术颜色和座位位置区分；角色数量、位置、环境锚点和Camera完全来自Current Clip。Template Content Leakage Check确认没有两女、钢琴、琴凳、窗户、乐谱、雨景、母版文字、示例发型 / 服装或示例光色；Character Appearance Leakage Check确认没有任何身份化外观。

FAIL：复制两个人物、钢琴 / 琴凳、窗户、乐谱、雨线、黑板文字或示例人物造型；用三种发型、服装、性别或体型区分A / B / C；为贴合母版把三人删成两人；或像素级复刻版式导致三人关系不可读。

### R20-C A3 Action Remains Technical Previs

输入：A3武打Clip需要A-SKETCH或S+P+A；Current Clip已确认双方起点、Action Axis、道具路径、接触 / 近接触、受力方向、恢复终点与Next-action Carryover。

PASS：母版只提供Technical Director Blocking Sheet表达，双方使用同一套无性别技术人偶，以Start / Path / Contact / Force / End箭头、轴线、Camera side与动作Permission完成技术预演；布局可为动作路径重新分区，必要身体比例只表达可达性 / 接触 / 受力约束。没有性别化体态、角色外貌重绘、高燃海报、能量爆炸、姿势美术定稿、电影光效或无依据FX；Canonical角色 / 环境 / 道具身份不受影响。

FAIL：生成高燃概念插画、武打海报或动作Key Art；根据Character Asset恢复双方脸、发型、服装、性别或体型身份；用母版的静态双人并排版式压扁动作路径；或把技术颜色标记当最终服装 / 光色设计。

### R20-D Simple Head Turn Still Returns NONE

输入：单人固定位置、固定机位，只做普通转头；母版文件已经注册且可读。

PASS：母版可用性不改变Assessment；Final=`NONE`，不调用母版、不生成 / 预留`REF-SKETCH`，直接进入Prompt编译。

FAIL：因为母版已安装就强制生成P-SKETCH、把母版列入视频参考资产或占用图片预算。

### R20-E Prompt Rewrite Reuses Current Sketch Without Recalling Master

输入：当前Clip已有经母版辅助生成并确认的`REF-SKETCH-04`，Blocking Signature不变；用户只要求压缩措辞、调整主风格或整理反向提示词。

PASS：结果为KEEP，复用现有`REF-SKETCH-04`与同一图片位，不重新调用母版、不重新生成草图；最终视频`参考资产：`只列当前草图及其他实际视频输入，不列`REF-SKETCH-MASTER`。只有Blocking-affecting Revision才执行KEEP / REPLACE / RETIRE / CREATE，REPLACE / CREATE时才重新按注册状态使用母版或Text Contract Fallback。

FAIL：每次Prompt Rewrite都重新读取母版并生成新草图；母版成为持续视频参考；或Blocking重构后仍盲用旧草图。

### R20-F Character Appearance Leakage Is A Hard Failure

输入：候选S-SKETCH / P-SKETCH / A-SKETCH版式、标签、箭头、Camera和Blocking均正确，但任一人物出现写实五官、具体长短发、具体服装设计、明显胸腰臀性别体态、年龄 / 美貌 / 气质身份，或根据Character Asset重画外观。

PASS：实际视觉检查把`character_appearance_leakage`记录为`true`或无法确认`neutral_mannequin_representation=true`；`scripts/validate_sd_film.py sketch`固定返回`FAIL = Character Appearance Leakage / Identity Contamination`。候选保持`FAILED / REVISE`并沿同一Technical Visual Blocking Sketch route重做，不注册Confirmed、不进入Clip参考资产，也不通过修改Character Asset或Blocking事实迁就草图。

FAIL：因为版式与Blocking正确就忽略人物外观泄漏；用“只是代理”解释后仍注册；或把中性人偶QA扩写进最终Seedance Prompt的反向提示词。

---

## R21 Performance Arc / Emotion Preflight

### R21-A Restrained Character Changes Across Shots Without Extra Coverage

输入：同一Scene有三个已确认SHOT。角色先冷静检查异常，第二镜确认目标，第三镜完成处理并恢复克制；剧情、SHOT数量、机位、时长和动作结果均已锁定，不允许加镜头。

PASS：STATE-06建立同一角色的Performance Arc Map：Inherited Baseline为专业冷静；第一镜通过视线先移、一次短暂停眼或呼吸变浅表现疑惑；第二镜在确认刺激后眼神稳定、下颌或手部张力略增并选择行动；第三镜动作完成后先复核结果、缓慢释放肩颈/呼吸，再回到新的受控Settled State。每镜只承载当前可见段，`Previous Settled State = Current Inherited Baseline`，STATE-07/08 Performance / Emotion Check为PASS，最终只写入既有`人物动作 / 人物动作与情绪 / 镜头结尾状态 / Performance State`语义，不新增SHOT、Clip、STATE或Template字段。

FAIL：三镜都只写“角色始终冷静从容”；每镜从默认脸重新开始；为了补情绪增加无必要特写/反应镜；或在STATE-08用“更有情绪、更生动”形容词替代上游表演链。

### R21-B Ensemble Uses Relative Amplitude And Reaction Order

输入：同一Clip含克制处理者、受惊逃跑者、刚解除痛苦的委托者与旁观者。剧情要求处理者始终最克制，受惊者最外放；委托者只在确认危险解除后放松，旁观者延迟反应。

PASS：每个Beat只有一个清楚Primary Performer；受惊者可使用Open / Heightened并承担大幅逃跑，处理者用PL1/PL2眼神、呼吸或动作后停顿承接，委托者从谨慎倾听到确认安静再肩膀放松，旁观者作为Listener / Background Holder先保持低幅、收到共享刺激后才升级。视觉重点交接由刺激、视线或动作结果触发，四个角色各有不同Arc Endpoint和Next-shot Carryover。

FAIL：所有人同时瞪眼、张嘴、后退；所有人都用同一`紧张→放松`模板；为保持主角“高冷”让处理者完全无注意/呼吸/停顿变化；或让背景人物无刺激抢走视觉重点。

### R21-C Intentional Hold Is Active, Not Frozen

输入：4秒近景中角色必须保持面无表情以隐藏真实反应，只听完一句关键信息，不说话、不移动位置。

PASS：表演被定义为Intentional Hold：视线先停在说话者、关键字后眨眼短暂停止或呼吸轻微受抑，手部原动作停住，延迟一拍后恢复控制但视线未完全放松；Post-action Residue进入镜头结尾。动作/口型容量没有被无关微表情堆满。

FAIL：只写“全程面无表情”；或为了避免面瘫同时加入挑眉、瞪眼、吞咽、握拳、后退、落泪和转身。

---

## R22 Screenplay Creation / Existing Script Dual Entry

### R22-A Idea Enters Screenplay Generation

输入：`调用sd，写一个雨夜双女主重逢短片。`

PASS：STATE-00登记`Creation Brief`，STATE-01进入Director-first Screenplay Development；不要求先提供完整剧本，不对尚不存在的文本输出Optimization Opportunity Report。Proposal具有视觉动作、关系变化、信息层次、表演机会、空间潜力与AIGC Directability，并在用户确认Gate停止。

FAIL：把创意归为Existing Class C后要求先批准改编；要求去普通Chat写完剧本；或直接进入Shot Design。

### R22-B Uploaded Script Enters Diagnosis Without Rewrite

输入：用户上传完整剧本并说`调用sd`，没有允许修改。

PASS：登记`Existing Script / Material + Class A/B`，先输出Optimization Opportunity Report并等待决定；没有改写正文或误进Creation Brief。

FAIL：从零重写、静默优化、跳过诊断，或因题材像创意而误走Creation。

### R22-C Explicit Direct Optimization Does Not Re-ask Authorization

输入：`调用sd，直接优化这个剧本；保持世界观、人物身份和结局。`

PASS：先完成诊断和Opportunity证据，再在同一轮按明确授权进入适用Optimization / Adaptation路径；不重复询问“是否优化”。Production Script Proposal输出后仍等待最终确认。

FAIL：省略诊断证据、重复请求同一改写授权，或把改写授权误当最终Proposal确认。

### R22-D Confirmed Screenplay Advances Without Regeneration

输入：Creation或Existing分支的当前Proposal已被用户明确确认并记录`Script Status: Production-Locked`，用户随后说`下一步`。

PASS：STATE-01 Completion Gate通过后进入STATE-02 Asset Discovery；不重复生成剧本，不停回Proposal Gate。

FAIL：重新写剧本、重新做Opportunity Report，或跳过STATE-02进入资产制作/Shot。

### R22-E Scene Revision Stays In Script Development

输入：当前`Script Status: Optimized Proposal`，用户说`修改这一场：让她不要直接表白。`

PASS：保持STATE-01 IN_PROGRESS，只修指定场与必要相邻因果，重跑受影响Scene Director Intent与Directable Screenplay QA，再次等待Proposal确认。

FAIL：进入STATE-05/06、重写全稿、把`下一步`当确认，或保留旧Proposal为Production-Locked。

### R22-F Director-first But Not Pre-shot

输入：从零生成一支情感短片剧本。

PASS：剧本通过Scene Purpose、Audience Experience、Character Objective / Conflict、Relationship Change、Visual Action、Performance Opportunity、Spatial Dramaturgy、Information Strategy、Rhythm Curve与AIGC Directability十项内部QA；最终文本是可独立阅读的剧本，没有35mm、特写、推镜、摇镜、机位、SHOT / CLIP或分镜表字段。

FAIL：只写说明性对白和内心独白；把十项QA机械输出成剧本正文；或在STATE-01预先锁定摄影机。

### R22-G Existing Diagnosis Regression

输入：Class B初稿，无明确改写授权。

PASS：原有A/B/C分级、十二项Optimization Opportunity Report、User Decision Gate、No Revision、Optimization Rejected、Adaptation Draft与第二次Proposal确认全部仍可用。

FAIL：因新增Creation route而自动改写Existing Script，或取消既有保护Gate。

### R22-H Downstream Isolation Regression

输入：运行Skill静态与定向回归。

PASS：主Pipeline仍只有STATE-00至STATE-09；Storyboard仍Optional/Auxiliary；Voice仍Explicit-only；视频Prompt仍永久禁配乐；REF-SKETCH、Prompt Compiler、STATE-02至09及四种Script Status保持原合同。Director Intent从STATE-00/01开始，Scene Director Intent经STATE-05投影、在STATE-06具体化为Director Decision Notes、在STATE-07/08消费，但不成为最终Prompt字段。

FAIL：新增主STATE、让Storyboard进入主路由、自动触发Voice/Music、改变STATE-08 Schema，或让内部Director Intent污染剧本/Prompt。

---

## R23 Director Module / Camera Language End-to-End

### R23-A Script — Rainy-night Two-woman Reunion

输入：`调用sd，写一个雨夜双女主重逢短片。`

PASS：STATE-00建立最小Project Director Baseline；STATE-01仍走Creation Brief → Idea-to-Screenplay，形成Audience Experience、Information Strategy、Visual Action、Performance Opportunity、Spatial Potential、Rhythm与camera-language opportunity。剧本可以写“先让观众看到她没有回头，随后才意识到另一人一直看她”等可镜头化信息顺序，但最终仍是可独立阅读的剧本，不出现Shot List、35mm、特写、低机位、推拉摇移、SHOT或CLIP字段。

FAIL：只记录平台/画幅；没有观众体验或信息策略；或在剧本阶段直接生成镜头表和摄影参数。

### R23-B Visual Development — Distance, Approach, Restraint

输入：同一双人关系弧为“疏远→靠近→再次克制”。

PASS：STATE-04形成Visual Dramaturgy / Mise-en-scène与Visual Arc：负空间、共享空间、前中后景、人物距离、对比/色光和环境压力先分离、再接近、最后重新保留克制边界；各变化有剧情/空间/真实光源依据。输出投影到现有Project Bible字段。

FAIL：只写“全片低饱和冷色电影感”、每场相同色调，或提前锁定每个Shot的焦段和运镜。

### R23-C Scene Breakdown — 40-second Two-person Scene

输入：40秒双人场景，含重逢、回避、怀疑、确认与再次克制。

PASS：STATE-05按Dramatic / Relationship / Information / Performance Beat拆解，建立Dramatic Geography、Spatial Evolution、Reveal / Withhold timing与Beat-to-beat rhythm；形成“先观察并隐藏反应→信息泄漏时保持→确认后才允许靠近→结尾压住”的Scene Camera Strategy。没有创建SHOT / CLIP或具体镜头参数。

FAIL：按台词句数机械拆段；只列地点和人物；或把Scene Camera Strategy写成85mm、特写、慢推清单。

### R23-D Shot Design — Glance Beat Is Derived, Not Decorated

输入：同一个“偷看”Beat；人物A保持向前，人物B只以一次视线偏移泄漏在意，A尚未确认。

PASS：STATE-06按`Shot Purpose → Audience Attention → POV / Audience Position → Relationship & Blocking → Composition Strategy → Shot Size → Lens → Camera Position → Camera Movement → Duration / Hold → Cut Motivation`推导。构图先保护共同朝前与A未察觉，B的眼神成为第二注意目标；Camera在泄漏前保持固定，是否在Beat后运动取决于确认/压力功能，并具有Trigger / Stop。可回答删除本Shot后观众会失去“B先泄漏而A未知”的信息差。

FAIL：无论Blocking与信息时序都默认“85mm特写+慢推+浅景深”，或先选技术再补理由。

### R23-E Clip Production — Suspicion To Confirmation Stays Intact

输入：两个相邻Shots共同完成“怀疑→证据→确认”，单独生成会破坏反应积累，合计时长与复杂度仍在4—15秒内。

PASS：STATE-07把它们作为一个Dramatic Execution Unit，保留Start→End dramatic delta、critical performance / blocking、information timing、Camera Continuity / Visual Rhythm与稳定Endpoint；不因技术便利拆开。若合并导致互斥时空、状态重置或模型过载，则返回拆分而不是强行合并。

FAIL：一Shot一Clip机械拆分，或为了情绪连续把超时/过载/跨世界内容强塞进同一Clip。

### R23-F Prompt — Piano Pair Director Intent Preservation

输入：现有双女主钢琴类Clip；两人同坐一张长琴凳、共同朝前，只有一人短暂gaze-only泄漏，另一人延迟反应，信息不能提前确认。

PASS：最终Prompt继续严格使用`templates/10_video_prompt.md`原Schema；先锁共同朝前和关系距离，再以动作顺序、活动幅度、焦点/遮挡建立First Look / Second Look；包含gaze-only leakage、Hold / Pause / Delayed Reaction、Composition Function、Camera Movement Trigger或有理由Static、Information Delay与稳定余韵。遵守Source Carries State, Prompt Carries Delta，不显著变长，不输出Director理论、Packet、dominance、BUILD/HOLD/PEAK/RELEASE、PL等级或未调用Voice Profile。

FAIL：两人同时转头互看、每镜慢推+浅景深、提前确认关系、长篇解释“为什么这样拍”、改变模板字段，或出现`音色特征：`/Voice资产状态。

### R23-G Action Case — Action-dominant Wuxia Clip

输入：武侠格挡—转身—反制Clip，双方起点、Action Axis、武器路径、接触/受力和恢复状态已确认。

PASS：选择Action-dominant + Action PREVIS A3；Camera Language优先脚下支撑、武器/身体轨迹、接触点、力线、受力结果、屏幕方向与空间可读性，复杂运镜在动作负荷前降级。表演只保留影响动作选择或结果的最小信息，不用青春微表演逻辑压制动作。

FAIL：为了情绪特写切碎动作因果，遮挡接触点、越轴、双方并排合影，或把完整微表情链与复杂Camera同时拉满。

### R23-H Review — Technically Correct, Dramatically Early

输入：实际结果身份、道具、Blocking和技术连续性全部正确，但人物在设计的延迟揭示前已经看向对方并暴露确认情绪。

PASS：Technical Review通过相应项，Director's Cut Review判Information Timing / Performance Truth失败；绝不Disposition=`KEEP`。现有素材能通过切点、顺序、Reaction Priority或声音连接恢复时选择`RE-EDIT`；模型没有生成合法延迟表演且上游设计正确时`REGENERATE`；上游导演/Prompt意图本身提前暴露时`REDIRECT`。同时标记Failure Origin，不把所有情况都当生成瑕疵。

FAIL：因技术连续性正确而PASS / KEEP，或不区分generation failure与directing failure。

### R23-I Runtime — Continue Is Not Reload

输入：当前Workflow与Project Context已验证，用户只说`下一步`或`继续`。

PASS：沿当前Checkpoint继续一个合法步骤，按需读取当前Workflow与Director Intent投影；不触发全量Runtime Reload，不清空Packet、Confirmed Assets、Accepted Take Canon或Shot-State Memory。明确`重新调用sd / 按当前Skill继续`时才按既有Reload / Re-entry合同重读当前版本。

FAIL：普通继续每次全量reload、重建导演Packet、重新生成剧本/分镜，或跳过当前确认Gate。

### R23-J Camera Language — Three Shots Have Three Functions

输入：同一场戏需要三个Shot依次完成空间建立、信息隐藏/泄漏、关系确认后的压住/释放。

PASS：三个Camera Language Decision分别承担建立、隐藏/泄漏、确认后的压住或释放；景别、构图、机位、距离、运镜/Static和Hold / Cut由功能差异推导。可刻意重复同一摄影逻辑，但必须说明如何累积信息/关系；不得为了多样随机堆运动。

FAIL：三镜都无理由“慢推+浅景深”，或三镜为了不同而随机环绕、升降、甩镜并破坏轴线/表演。

### R23-K Cross-stage Director Consumption — FX, Sequence, Clip And Prompt

输入：一个项目具有已确认Scene Director Intent；其中包含需遮挡Reveal并留下后果的FX、需要跨Scene组织Coverage的Sequence，以及覆盖多个SHOT的Execution Clip。

PASS：STATE-03 FX从当前Director Intent只读取视觉重点、遮挡/Reveal与后果呈现功能，不创建Camera或剧情；条件性Sequence Planning只消费已确认Scene Director Intent、Information Presentation与Rhythm Intent来组织BEAT / COV / UNIT，不创建SHOT或Camera参数；STATE-07将匹配的Director Decision Notes投影为Clip Dramatic Function、关键表演/Blocking、节奏与信息时机；STATE-08在编译前核验当前Clip Director Intent / Notes一致，并只把1—3项已确认导演优先级交给Projection。任一缺失或冲突均返回最小事实owner。

FAIL：FX或Sequence绕过导演呈现约束自行创造镜头/剧情；STATE-07只写笼统“保持导演意图”而不形成Clip投影；或STATE-08仅凭旧Prompt、Adapter或模型偏好重写导演方向。

### R23-L Multi-stage Clip — Observation Hierarchy Is Not Flat Follow

输入：一个Seedance 2.5、20秒的Clip依次承载相遇、共同完成小动作、关系靠近、信息确认与余韵；草案要求“同一台摄影机自然跟随、保持前进方向”，所有阶段都是平视中景和轻微推进，但没有连续长镜的叙事理由。

PASS：STATE-06对不同Shot Purpose / Audience Attention / 关系与信息阶段执行Adjacent Observation Contrast；STATE-07 Long-duration Preflight与Clip Movement Plan记录阶段间的观察层次，或明确连续长镜理由、受保护注意力对象、解除条件与稳定终点。若无法成立，返回STATE-07拆分Clip或使用有动机剪辑；STATE-08仅把已确认层次转为既有字段语义，不输出内部标签；STATE-09能区分“Clip Plan缺设计”与“Plan正确但Prompt / 生成压平”。

FAIL：为了避免单调随机堆叠越轴、环绕、升降、甩镜或强制每镜不同；或把多阶段内容默认写成同一平视跟拍、同一路径前进和无触发的轻微推进。

### R23-M Visual Grammar — Baseline Holds, Scene Delta Serves Drama

输入：一个项目已确认克制、潮湿、低对比的海边小镇视觉世界；同一角色分别进入“等待的站台”“共同生活的厨房”“关系确认的海堤”。草案把三场都写成相同灰蓝色、同一平视中景与同一路径跟随；另一草案为了变化无依据加入红色霓虹与舞台顶光。

PASS：STATE-04先建立不含逐Shot参数的Visual Grammar Baseline，明确可用色谱、强调色的出现条件、真实光源、材质/空间气质和摄影机介入倾向；STATE-05为每场标记空间的戏剧功能与有事实依据的Scene Delta；STATE-06再把当前主信息与关系转成镜头选择；STATE-09既能拒绝把统一机械拍成相同，也能拒绝为变化而破坏Baseline。STATE-08只继承已锁定Baseline与当前delta，不增加最终Prompt Schema。

FAIL：把某位导演、某种题材或“低饱和”固化为所有项目的默认审美；让颜色只因好看出现、改写资产固有色或虚构光源；或在STATE-04以Visual Grammar名义预写逐Shot焦段、机位与运镜。

### R23-N Project Color Reference — Conditional Model Input, Never Asset Authority

输入：用户提供一张可访问的海边小镇色卡，并确认它用于本项目的综合色彩基线；夜景Clip存在暖色强调比重漂移风险，角色、环境、道具与首尾帧均已有更高优先级的Canonical参考。

PASS：STATE-04把色卡作为`Project Color Reference`记录在既有Color System，不注册为CHAR / ENV / PROP / FX或Canonical Asset；STATE-07仅因当前光色漂移风险选入并计入Reference Budget；STATE-08在既有模型参考字段写真实来源、唯一Primary Role与“仅控制综合色相 / 明度 / 饱和度 / 强调色占比”。角色、环境、道具、构图、光源、镜头与最终画风继续服从其原owner。无真实色卡、未确认色卡、没有当前风险或有更具体场景状态参考时，色卡不进入模型输入，只有文字Color System继续生效。

FAIL：把色卡当人物、环境、道具或最终画风资产；让它覆盖Canonical外观/结构、虚构光源、强制每个Clip投喂，或对仅有Hex/文字需求伪造图片输入与确认状态。

---
