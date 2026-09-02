# SD Film Regression Scenarios

## Purpose

以下场景用于修改Rules、Workflows、Knowledge、Templates或Validator后的生产回归检查。每类至少保留一个PASS和一个FAIL样例。

---

## R00 STATE-01 Optimization Decision Gates

### R00-A Rough Script Reports And Stops

输入：`调用SD + 一份存在开场慢、对白重复和高潮偏弱的普通粗略剧本`。

PASS：先执行`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`；报告逐项覆盖开场钩子、核心冲突进入时机、信息重复、台词效率、动作可视化、人物记忆点、节奏、高潮力度、情绪价值、结尾Hook、时长适配、场景/人物复杂度；结论为B或C档；只说明问题、影响和方向；以“是否执行轻度优化？”或“是否进入结构优化？”结束；`Script Status: Source Material`、STATE-01 `IN_PROGRESS`并停止。

FAIL：同轮输出改写后的剧本正文、替换台词、Adaptation Draft、Screenwriting Optimization结果、Directorial Interpretation结果或Production Script Proposal；自动进入STATE-02。

### R00-B Reject Optimization Locks Original

续接R00-A，用户明确回复“不优化，保留原稿”。

PASS：不修改原稿，不执行Script Adaptation、Screenwriting Optimization或Directorial Interpretation；完成只读Script Analysis；将用户原始版本登记为`Production-Locked`，STATE-01通过Completion Gate后进入STATE-02；报告风险仅作为制作注意项保留。

FAIL：拒绝后仍润色台词、补场、重排、自动改编，或继续等待Production Script Proposal确认。

### R00-C Explicit Optimization Stops At Proposal Confirmation

续接R00-A，用户明确回复“进入优化”。

PASS：A/B类执行`Screenwriting Optimization → Directorial Interpretation → Production Script Proposal`；Class C按必要性先执行`Adaptation Target Detection → Script Adaptation → Adaptation Draft`再进入同一优化链。Proposal输出后写`Script Status: Optimized Proposal`、STATE-01 `IN_PROGRESS`、`Pending Decision: 等待用户确认Production Script Proposal`并再次停止。只有用户随后明确确认Proposal，才Production-Lock并进入STATE-02。

FAIL：把单独“继续 / 下一步 / 好的”当作优化授权或Proposal确认；Proposal输出后直接Production-Lock或进入STATE-02。

---

## R01 Simple Single Shot

单人、简单动作、固定或单一运镜。应为Execution Risk L1，Sequence Planning Not Applicable，边界和稳定结尾仍不得缺失。

## R02 Two-Person Dialogue

检查左右、轴线、说话者/倾听者、Exact Line、自然停顿、误口型和相邻镜眼线。

## R03 Chase / Action Coverage

检查Required Coverage、屏幕方向、动作结果、Camera Class与L3/L4降级，禁止把多视点伪装成一镜。

## R04 FX Lifecycle

检查FX来源、阶段、人物/环境/道具交互、残留后果、光色与声音尾部。

## R05 Multi-Unit Sequence

检查SEQ/BEAT/COV/UNIT命名空间、Entry/Exit Anchor、State Ledger和重试隔离。

## R05A Detailed Shot Design To Clip Production

输入包含连续对话、动作接力、场景断点与不同逐镜时长的Confirmed Detailed Shot Design。检查所有正式Shot按原顺序且仅进入一个CLIP-xxx；每个Clip为4—15秒；连续低复杂度Shot可合并，跨时空/资产断点和超过15秒候选被拆分或返回STATE-06；Clip内保留起始状态、连续动作、空间/道具/摄影机连续性与结尾状态。跨Clip固定执行`上一Clip生成完成 → 判断是否需要严格承接 → 若需要则请求用户截取尾帧 → 上传并命名REF-TAIL → 加入当前Clip参考资产 → 首帧明确引用 → 当前Clip生成 → 当前Clip尾帧限制 → 下一Clip承接`；STATE-08按CLIP→G一对一输出一条连续Prompt，即使Clip包含多个Shot也不拆Prompt；任何Storyboard视觉材料均不得进入参考资产。

## R05B Source Script Label Namespace

输入剧本自带“镜头1—镜头5”或“Clip A—Clip E”标题。PASS路径必须先把这些标题登记为Source Script Labels，STATE-05建立SCENE，STATE-06按叙事功能、动作阶段、机位/视点、Coverage与边界创建正式SHOT，STATE-07才根据Confirmed Detailed Shot Design建立CLIP。以下任一情况均为FAIL：在STATE-05或STATE-06完成前创建暂定/占位/正式CLIP；把Source Script Label直接改名或一对一映射为SHOT、UNIT、CLIP或G段；只声明Source Revision但不存在可关联的Confirmed Detailed Shot Design Artifact或Portable Checkpoint。

## R06 Scene / Time Discontinuity

检查Motivated Discontinuity，只重建剧情授权状态，不伪造过渡动作。

## R07 Image-To-Video Reference

检查首/尾帧用途、Asset Active Version、边界冲突和Template 11到Template 10的单向投影。

## R08 Review Revision Loop

PASS允许完成；REVISE/REBUILD保持STATE-09 IN_PROGRESS，记录Affected IDs、Return Route、Accepted Unaffected Artifacts和Recheck Scope。

## R09 STATE-03 Double-Confirmation Closure

以下三个最小案例必须依次通过四个Registry状态，且每个案例在`Prompt Draft`和`Image Generated`各停止一次。示例中的“用户确认”是测试事件，不代表实际项目批准。

### R09-C Character

输入：`CHAR-001 林遥，28岁女气象工程师，短黑发，灰蓝防水工作服，冷静克制；有对白；无剧情状态变体。`

Prompt Draft输出至少包含：

- 角色定义只包含视觉身份与剧情事实；“有对白”不得触发角色音色描述、Voice Profile、Seed Audio Prompt或Voice Reference字段。
- 三视图Prompt：`角色设定表，28岁东亚女性气象工程师林遥，椭圆脸、平直眉、深棕眼、短黑发齐耳并露出双耳，身高约168厘米、匀称偏瘦体型；穿灰蓝色连帽防水工作服、深灰工装裤、黑色防滑短靴，不佩戴首饰。纯浅灰无缝背景，同一画布从左到右为正面全身自然站姿、严格右侧全身、背面全身，三个视图等比例等高度，服装接缝、口袋、拉链、帽型、鞋型与颜色完全一致；柔和中性棚拍光，真实电影角色概念设计，清晰材质与结构，4:3横幅，高分辨率。禁止改变脸型、年龄感、身体比例、发型长度、服装结构与配色；禁止透视夸张、动态姿势、额外人物、文字、水印、拼错肢体。`
- 面部特写Prompt：`林遥面部角色参考，28岁东亚女性，椭圆脸、平直眉、深棕眼、鼻梁自然、薄而清晰的唇形、真实轻微皮肤纹理、短黑发齐耳并露出双耳；正面头肩特写，平静中性表情，视线略高于镜头，浅灰无缝背景，柔和中性棚拍主光加弱填充，肤色准确，真实电影角色概念设计，1:1，高分辨率。严格继承三视图的脸型、年龄感、发际线、发长与发色；禁止美颜塑料皮、夸张妆容、笑容、首饰、额外人物、文字、水印、五官漂移。`
- 状态变体：`Not Required—剧本未确认额外视觉状态。`
- `Visual Production Status: Prompt Draft`与`Awaiting User Confirmation: Image Prompts`；不得生成图片。

模拟用户确认`Prompt Revision: P-v001`后，状态变为`Prompt Confirmed`。生成后仅登记`Candidate References: char-001-turnaround-c01.png; char-001-face-c01.png`，状态为`Image Generated`，不得出现Canonical References或Active。模拟用户确认两张图片后，最终记录必须为`Visual Production Status: Asset Confirmed`、`Status: Active`、`Active Version: v001`，并把两张已批准Candidate References升级为Canonical References；整个案例不创建声音资产，也不因缺少声音资产阻塞。

### R09-E Environment

输入：`ENV-001 海边气象站主控室，近未来但可现实建造，暴雨夜；需要主空间、入口反向视角与控制台关键区域。`

Prompt Draft至少包含：

- 主参考图Prompt：`近未来海边气象站主控室，长方形单层空间，画面左侧为面向海面的连续抗风玻璃窗，画面右后方为唯一金属气密入口，中央两排低矮控制台沿房间长轴排列，前端大型天气雷达屏，天花暴露式线性灯与检修轨道；湿冷暴雨夜，窗外海浪与远处警示灯可见，室内主要由4000K线性顶灯和青绿色仪表屏照明，灰色防滑地面、哑光铝板墙、深灰橡胶包边。摄影机位于入口内侧约1.6米高度，24mm等效大全景，清楚展示入口—控制台—海窗的可行走动线与尺度；真实电影美术概念图，16:9，高分辨率。锁定窗、入口、两排控制台和雷达屏的相对位置；禁止改变房间骨架、增加楼梯或第二入口、赛博朋克霓虹堆叠、人物、文字、水印。`
- 多视角Prompt：从海窗方向反看入口与两排控制台的完整独立Prompt，保持同一布局、材质、暴雨夜与光源锚点。
- 关键区域Prompt：控制台操作区中景完整独立Prompt，明确按钮、屏幕、椅位、通行宽度与材质。
- `Visual Production Status: Prompt Draft`并等待确认。

模拟Prompt确认、生成`env-001-main-c01.png / env-001-reverse-c01.png / env-001-console-c01.png`、图片确认后，三图才可进入Canonical References；最终必须为`Asset Confirmed + Active`。任一步缺少Prompt确认或图片确认均为FAIL。

### R09-P Prop

输入：`PROP-001 手持风暴数据记录器，掌上工业仪器；正常与屏幕报警两种状态，需要接口细节。`

Prompt Draft至少包含：

- 主参考图Prompt：`手持风暴数据记录器，掌上工业仪器，约18厘米高、8厘米宽、3厘米厚，深灰色防滑橡胶包边，拉丝铝合金正面框，顶部短天线，正面上半部为无品牌矩形屏幕，下半部四枚实体防水按键，右侧橙色密封数据接口盖，背面可拆电池盖与腕带孔；45度三分之四产品展示视角，白灰无缝背景，柔和棚拍主光与轮廓光，真实可制造产品设计，1:1，高分辨率。锁定尺寸比例、天线、屏幕、四按键、橙色接口盖和电池盖位置；禁止品牌文字、额外按键、透明悬浮界面、夸张科幻装饰、人物、水印、结构漂移。`
- 状态Prompt：屏幕由正常数据变为红色报警界面，外壳结构、按键、天线与接口位置完全不变；完整包含同样的构图、光影、背景和限制。
- 细节Prompt：右侧橙色密封接口盖打开的微距结构图，锁定铰链、密封圈与接口尺度；其余结构不改变。
- `Visual Production Status: Prompt Draft`并等待确认。

模拟Prompt确认、生成`prop-001-main-c01.png / prop-001-alarm-c01.png / prop-001-port-c01.png`、图片确认后，三图才可进入Canonical References；最终必须为`Asset Confirmed + Active`。生成图被拒绝时保持Candidate，不能进入Registry确认态。

---

## R10 Canonical Character Appearance / Form Inheritance

项目已有经用户确认的`CHAR-005@v002 孔老板`Active角色资产：孔雀本体、固定冠羽与羽色、真实孔雀躯干和双足结构、无手臂、非人形比例；Canonical References分别锁定Identity、Scale与Costume/Adornment。用户随后只要求制作新的挥翅动作状态图、双人场景示意、Storyboard、电影海报、Detailed Shot Design、Clip和Seedance Prompt，并提供一张构图很好但把孔老板画成人形孔雀头角色的风格参考。

PASS路径必须在所有阶段继续引用`CHAR-005@v002`及适用Canonical References；只继承新参考的构图或镜头关系，不继承其人形结构；动作图只改变挥翅姿势，海报与场景图保持孔雀本体，Shot/Clip/Prompt明确锁定无手臂、孔雀躯干与原羽色，最终视频Review逐项检查物种与身体结构。风格参考、动作参考或新生成结果与Active资产冲突时，Active资产胜出，冲突结果被拒绝或重生。

以下任一情况均为FAIL：孔老板出现人形躯干、手臂、人类身高比例或半人形站姿；冠羽、羽色、体型、服装/装饰基础无授权变化；因动作、机位、构图、风格或模型适配重新设计外貌；把Storyboard、海报或漂移生成结果登记为新角色Canonical Reference；把两套外貌混合折中；未走STATE-03 Candidate Version与用户批准就改变Active角色资产。

---

## R11 Reference Budget / 参考资产预算控制

所有案例先执行Visual Input Eligibility、删除非当前Clip出场角色、未使用环境/道具/动作图并去重，再判定A/B/C。A/B标记`Tail Frame Required = YES`，尾帧无论是否已上传都预留1个Projected位，并在`参考资产：`直接列统一`REF-TAIL`名称、对应用途与真实状态；未上传时写“待用户提供/待上传、未确认”，不计入已提交图片，Prompt可交付但实际提交生成前补图。C标记`NO`，不列或预留上一尾帧。真实视觉条目必须存在且已确认；其他已经确定需要用户实际补入的视觉参考图必须写明具体图像对象、实际投喂用途与“待用户补充/待上传、未确认”，计Projected位但不冒充已提交图片，也不得绕过正式Canonical资产确认。Projected Final Count与已提交图片数均≤9；整合只允许在超限风险触发后作用于非角色信息。

### R11-A Seven Candidates

当前Clip有7张真实、独立、相关参考图，无额外连续性帧需求。PASS：不整合，最终7张。FAIL：为了“统一”或因为已有总设定图而主动替换/合并独立图。

### R11-B Eight Candidates Without Reservation

当前Clip有8张真实、独立、相关参考图，已确认不需要上一Clip尾帧、当前首帧或其他额外图片位。PASS：不整合，最终8张。FAIL：默认整合或无依据预留导致丢失高精度独立图。

### R11-C Nine Candidates Plus Previous Tail

当前Clip已有9张候选，Previous-Clip Continuity Decision为A Direct或B Reference-Only，因此`Tail Frame Required = YES`。无论上一实际尾帧图是否已经上传，Projected Final Count均按10张计算并至少释放1位；【参考资产】必须以`REF-TAIL-XX｜CLIP-XX尾帧参考`列出尾帧，A标“同镜头连续承接用途”，B标“空间/站位/景别参考用途”。若尚未提供，PASS必须标记“待用户提供/待上传、未确认”，不计入已提交图片；Prompt可交付但实际提交生成前补图。FAIL：因尾帧暂缺把需求改为NO、遗漏`REF-TAIL`声明、声称待补充资产已上传/已确认、B误用A固定直接承接句、仍声称9张通过、超过9张或合并核心角色图。

### R11-D Twelve Candidates

当前Clip有12张真实候选。PASS：删除无关项、去重；仅在仍超限时用真实已确认的环境多视角/道具组/空间或动作关系总图替代完整覆盖的零散图；仍超限按保留优先级裁剪，最终≤9。FAIL：默认全部合并、虚构不存在的总图，或最终仍>9。

### R11-E Multi-Core-Character Independence

多角色场景中有多个当前Clip核心角色。PASS：每个核心角色各自保留独立三视图/角色锁定图；动作/互动图只负责动作关系；非角色信息承担必要的整合压力。FAIL：把多个核心角色合并成角色总表、共用一个角色位，或用动作图替代任一角色外貌基准。

### R11 Retention Priority

整合后仍需裁剪时，从高到低保留：当前Clip出场核心角色独立图 > 当前主要环境 > 当前关键道具 > 当前关键动作/互动关系 > 上一Clip尾帧/当前首帧连续性参考 > 特殊一次性道具/次要角色。已经判定为Direct / Reference-Only且实际存在、可访问、已确认的连续性帧属于硬需求，必须先释放其他位置，不得静默删除后仍声明连续继承。

---

## R12 Runtime Skill Reload / Workflow Re-entry

以下案例覆盖新Chat、旧对话、重复Reload、Workflow Re-entry、资源不可访问、非Reload推进和Work边界。Reload / Re-entry成功判定只服从`rules/runtime_reload.md`；这些案例不创建新的测试协议。

### R12-A Stale Conversation Pipeline vs Current Installed Pipeline

输入：旧对话缓存声称`STATE-07`对应`Storyboard`，磁盘当前`SKILL.md`却声明`STATE-07 Clip Production`并包含更新的Skill Version / Build ID。

PASS：按`rules/runtime_reload.md`重新解析当前runtime可访问资源，重新完整读取Current Skill `SKILL.md`，记录`Reload Status: RELOADED`、Loaded Source、Skill Version / Build ID与Owner Files Resolved；当前Skill Pipeline覆盖旧对话的Skill描述；再只读取状态owner、映射后Workflow与其适用依赖。

FAIL：继续把Storyboard当作固定STATE-07；用历史摘要覆盖磁盘Skill；未实际重读却声称`RELOADED`；强制用户新建对话或项目。

### R12-B Preserve Progress And Map To Current Workflow

输入：旧项目停在标注为`Storyboard`的`STATE-07`，已有Confirmed Detailed Shot Design，无Confirmed Clip Production Plan，并有可验证Last Successful Checkpoint。

PASS：按`Active Project Root/project_status.md > portable_project_status.md > 当前可验证Project Context`选择状态；如使用第三级则先规范化为Portable State；把项目映射到当前`STATE-07 Clip Production`和`10_clip_production_workflow.md`；保留Detailed Shot Design、Checkpoint、已完成States与Storyboard Optional Artifact；只继续尚未完成的Clip Production。

FAIL：回退STATE-00；重做已确认Detailed Shot Design；将旧Storyboard作为STATE-08参考资产；仅按旧STATE编号硬复制而不检查Artifact / Completion Gate。

### R12-C Preserve Production Lock And Confirmed Assets

输入：项目已有`Script Status: Production-Locked`、Confirmed Core / Support Assets、Active Versions、Canonical References、已接受Artifact Revision与用户明确的“不改剧本、不改角色外观”约束。

PASS：Reload后上述项目事实全部保留；只更新Skill Definition和必要路由标签；后续Workflow仍从Active / Canonical资产与Production-Locked Script读取真源。

FAIL：把Script Status降回Source Material；丢失Confirmed Assets、Active Version或Canonical References；因Skill重载重新要求用户确认已接受结果；忽略用户锁定约束。

### R12-D New / Ordinary Chat Uses Current Accessible Skill Resources

输入：新普通Chat中用户说“调用sd”，当前runtime能读取exposed / installed SD Film resources，但不能访问Windows本机路径。

PASS：先从当前Chat runtime可访问资源重读`SKILL.md`与基础路由owner，记录真实Loaded Source并继续State Source / Workflow路由；不要求Work，不要求用户上传本机Skill目录。

FAIL：仅因`C:\Users\Lenovo\.codex\skills\sd`不可读就停止、声称BLOCKED、要求切Work，或未读取当前资源便声称严格按当前Skill。

### R12-E Repeated Reload, Current Owner And Re-entry Evidence

输入：Skill更新后，用户再次说“重新调用sd”；上一轮已有Reload Evidence与Project Context。

PASS：生成新的Invocation Marker / Load Timestamp（运行时可提供时），重新读取当前Loaded Source，核对当前Skill Version / Build ID与Owner Files Resolved；版本、来源或owner变更时证据随之变化，未变化时也能证明本轮发生实际读取；Project Context保持；重新确认Current STATE / Workflow / Object，并从当前owner入口执行到合法Checkpoint后才报告已重进Workflow。

FAIL：复用上一轮Evidence、只回显缓存版本、继续使用更新前owner、未实际读取却称已重新加载/已重进，或把Reload当作项目重置。

### R12-F Current Skill Unavailable Uses Truthful Fallback

输入：用户显式“重新加载SD”，但当前Skill入口或必需owner实际不可访问；存在有效Portable State或可验证Project Context。

PASS：记录`Reload Status: UNAVAILABLE`、失败资源/原因和实际Fallback Source；保留项目并继续fallback合同允许的安全工作，不声称`RELOADED`、最新安装版或严格按当前Skill，不因本机路径不可见默认切Work。

FAIL：用旧对话Skill摘要冒充Current Skill、隐瞒fallback、清空项目，或仅因路径不可见报告项目BLOCKED。

### R12-G Plain Continue Does Not Force Full Reload

输入：当前runtime已有一次成功loaded Skill Definition和有效Project Context，用户只说“下一步”。

PASS：复用当前loaded definition，按需读取当前Workflow与依赖并推进一个合法Checkpoint；不全量重读Skill，不产生新的Reload Evidence，也不把“下一步”当作显式Reload。

FAIL：每一步无意义重读全部Rules / Workflows / Knowledge，或伪称本轮再次RELOADED。

### R12-H Work Is Only For Local File Operations

输入A：普通制作请求“调用sd，继续CLIP-003”；输入B：用户要求修改本机`C:\Users\Lenovo\.codex\skills\sd`文件。

PASS：A先使用当前Chat可访问Skill资源并正常路由，不默认Work；B进入具备本地文件能力的Work/Codex并遵守Skill维护流程。

FAIL：A强制切Work，或B在无法直接操作本地文件的环境中伪称已经修改。

### R12-I Old Prompt Does Not Bypass STATE-08 Entry

输入：旧对话含CLIP-04旧Prompt、旧Skill摘要与上一次未验证结论；Project Context中已有Confirmed Clip Plan、Current Clip与已确认资产。用户说“重新调用sd，重写CLIP-04”。

PASS：重新读取Current Skill并保留Project Context，重新确认STATE-08与`workflows/11_video_generation_workflow.md`，从Workflow入口依次执行Reference Selection / Routing、Final Visual Blocking Anchor Assessment、Prompt Compiler与Final QA；旧Prompt只作为待比较/修改对象，不成为Gate证据或唯一编译输入。

FAIL：直接润色旧Prompt、沿用旧Skill摘要、跳过Reference Routing / Visual Blocking Gate / Final QA，或因重载清空Confirmed Project Context。

### R12-J Confirmed Sketch Survives Re-entry When Blocking Is Stable

输入：CLIP-04已有与当前Blocking Signature匹配的Confirmed `REF-SKETCH-04`；用户显式重新调用并只要求压缩措辞或优化Prompt，Blocking未实质变化。

PASS：re-entry重新执行Final Assessment并得到`KEEP existing sketch`，复用同一草图、Revision与图片位，不重新生成草图；随后从Prompt Compiler与Final QA产生当前CLIP-04结果。

FAIL：把re-entry解释为重置草图、重复生成`REF-SKETCH`、调用母版替换已确认Anchor，或跳过Assessment直接假设旧图有效。

### R12-K Material Blocking Change Forces Reassessment

输入：CLIP-04原为双人并排共坐，已有Confirmed `REF-SKETCH-04`；用户显式重新调用并把Blocking改为一人起身走到另一人面前，改变Topology、Position与Movement Path。

PASS：保留旧草图Revision追溯，但re-entry重新执行Visual Blocking Anchor Reassessment并只得到`REPLACE / RETIRE / CREATE`中的适用结果；Final=`REQUIRED`且新Anchor尚未确认时停在草图Checkpoint，不沿用旧图或直接输出Prompt。

FAIL：因旧图已存在而`KEEP`、只改Prompt文字掩盖Blocking冲突、跳过草图验证，或删除旧Revision追溯。

---

## R13 Cross-Clip End-State And Reference Routing

以下三例均先从上一Clip的Entry / 内部状态链 / Exit / Handoff归并八组`Clip End-State Record / Next-Clip Carryover`，再按当前Clip目标与Continuity Risks路由最小充分参考资产；不得把整个Registry、上一Clip全部资产或所有Eligible条目机械复制到下一Clip。

### R13-A Same-Shot Direct Continuation

上一Clip结束时：林夏坐在钢琴凳画左、身体朝右前方，右手压住乐谱；许栀坐画右、与林夏肩距约20厘米；两人位于同一关系轴北侧，摄影机C1在轴线南侧中景，雨天窗光从画右进入。下一Clip继续同一镜头、同一动作阶段。

PASS：八组记录完整保留人物坐姿/朝向/距离、乐谱持有与位置、轴线和C1机位、雨天光态及未完成动作；判定A Direct与`Tail Frame Required = YES`。Reference Selection选择各自身份风险所需Character Canonical、钢琴区域结构风险所需Environment Canonical、乐谱造型风险所需Prop Canonical与`REF-TAIL-XX｜CLIP-XX尾帧参考（同镜头连续承接用途）`；Spatial Blocking仅作文字几何约束，不把Top-down Map当视觉资产。尾帧缺图时条目写“待用户提供/待上传、未确认”，Prompt仍可完整交付但实际提交生成前补图；`首帧参考：`使用固定Direct句并逐项继承，不重置坐姿、不重播压住乐谱动作。

FAIL：缺少任一八组状态导致人物/道具/相机/光态重置；把B/C误判为A；省略REF-TAIL、用途错误、用文字End State冒充图片，或因预算有空位加入不相关角色/道具资产。

### R13-B New Shot With Tail Position Reference

上一Clip具有与R13-A相同End-State，但下一Clip另起OTS新镜头：允许摄影机从C1改为轴线同侧C2、景别改为近景；人物坐姿、左右、朝向、肩距、乐谱位置、雨天窗光方向与钢琴空间关系必须保持。

PASS：八组记录把“必须保持”与“允许改变”分开；判定B Reference-Only与`Tail Frame Required = YES`。Reference Selection保留解决身份/环境结构/乐谱造型风险的对应Canonical资产，并选择`REF-TAIL-XX｜CLIP-XX尾帧参考（空间/站位/景别参考用途）`锁定站位、距离和空间；`首帧参考：`明确另起新镜头重新构图、允许C1→C2与中景→近景，不使用A的固定Direct句。其他已确认但与本Clip无关的资产不选。

FAIL：把新OTS误写为同镜头续拍；使用A固定句；尾帧用途未写或写错；无授权跨轴、左右翻转、人物/道具重置；为了“更稳”把全部Registry资产塞入参考清单。

### R13-C New Shot Without Tail Reference

下一Clip切到同一教室门外的单人门把手特写，人物不入画；新构图不依赖上一尾帧的两人站位，但仍需保持已确认教室门结构、雨天状态和门把手造型。

PASS：八组记录明确上一人物状态暂不进入画面、剧情仍有效但不作视觉首帧锚定；判定C Not Required与`Tail Frame Required = NO`。Reference Selection不列、不预留`REF-TAIL`，只选择门结构风险所需Environment Canonical与门把手造型风险所需Prop Canonical；雨天光态若只有文字场景视觉基准则写入`环境一致性 / 首帧参考 / 起始状态`，只有实际已确认合格的场景状态图存在时才作为视觉参考。Spatial Blocking继续提供文字方向约束，Top-down Map不进入参考资产。

FAIL：机械要求截图或把旧尾帧、两名角色图、钢琴/乐谱等无关资产塞入；把旧人物构图和光线画面强行继承到新特写；遗漏门结构或门把手这一实际风险所需资产。

---

## R14 Reference Asset Eligibility / 参考资产准入

输入清单：

```text
参考资产：
1. 林夏.png｜林夏-基础形象
2. 许栀.png｜许栀-基础形象
3. ENV-02｜窗台钢琴区域教室全景
4. REF-TAIL-02｜CLIP-02尾帧参考｜用途：镜头延续、参考人物坐姿延续、参考人物在同一张板凳上的左右站位、参考肩膀距离、参考手臂搭放位置、参考钢琴与窗户空间关系、参考雨天光线与环境状态
5. 乐谱参考资产｜用途：固定乐谱纸张尺寸、材质、印刷内容与旧化程度；作为本Clip“被风吹落的乐谱”造型依据
6. 板凳参考说明｜用途：锁定两人共坐同一张板凳；不是两把椅子，不是两张琴凳，不允许拆分座位
```

PASS：逐项执行“这是不是一张实际会被投喂/引用的视觉资产？”；1—5号保持不动，6号判定`NOT ELIGIBLE`并从`参考资产：`删除。其正向事实迁移为`空间关系：两人始终共坐同一张双人板凳，林夏在左、许栀在右，保持已确认肩膀距离。`或等价`道具状态`约束；“不得拆成两把椅子/两张琴凳”可在`道具状态`正向锁定并把高风险错误写入`反向提示词`。如果项目实际存在双人钢琴凳视觉图，则以真实`PROP-BENCH-01｜双人钢琴凳`及其文件/受控ID进入参考资产，而不是保留6号文字说明。

FAIL：保留6号；仅因加入“参考说明/用途”就把它算作图片位；删除或重写1—5号视觉条目；把约束迁移到新字段；虚构`PROP-BENCH-01`或其图片路径；把待补正式Canonical道具图当作占位绕过STATE-03。

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

## Deterministic Expectations

- Skill、Registry、Project、Asset、Artifact、Execution、Sequence、Clip、Poster、STATE-08和Review Validator通过合法样例。
- 缺字段、重复ID、非法时间轴、背景音乐、内部模式ID泄漏、无Return Route和第三次盲重试被拒绝。
- 主Pipeline仍只有STATE-00至STATE-09。
- STATE-08最终Schema仍只由templates/10_video_prompt.md拥有。
- R09-C/E/P均验证`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`，且Prompt确认前不出图、图片确认前不Active/Canonical。
- R10验证Canonical Character Appearance And Form Lock从Asset、Visual Development、Storyboard/Poster、Shot Design、Clip、Prompt Generation、Final Video到Review的全阶段继承，并覆盖非人角色禁止未授权拟人化。
- R11-A至R11-E验证条件性整合阈值、9张加必需尾帧的真实计数、12张自动压缩到≤9、实际资产存在性和多核心角色独立图硬门槛。
- R12-A至R12-K验证旧对话缓存不能覆盖Latest Successfully Loaded Current Skill Definition、旧STATE按当前Artifact / Completion Gate映射、Project Context在Reload后不丢失、显式重新调用会从当前Workflow入口重跑而非润色旧Prompt、Confirmed草图按Blocking Signature复用或重评，以及普通Chat优先当前可访问Skill resources、重复Reload产生本轮证据、资源不可访问时诚实报告fallback、“下一步”不强制全量重载、Work只用于本地文件操作。
- R13-A至R13-C验证尾帧需求先于资产可用性判定、严格承接主动请求截图与草案/最终版边界，以及非严格承接不强制截图。
- R14验证纯文字“板凳参考说明”从参考资产删除并迁移到既有空间/道具/反向字段，1—5号视觉资产保持不动，真实双人钢琴凳图只以正式资产ID引用。
- R15-A至R15-L验证文学意图可执行转译、工程级数据按视觉价值压缩、Canonical资产释放Prompt注意力、导演/电影级标签首次出现时的项目特定展开、已锁定项目风格的后续Clip delta压缩、动作复杂Clip中的风格让位、正文正向化、通用负向项末尾唯一收束、局部物理连续性约束保留、CLIP-03字段唯一归属与事故历史式反向段压缩，以及本次调整不破坏Voice opt-in；最终Template结构保持不变。
- R16-A至R16-E验证Canonical来源携带已锁定状态、Generation Budget先于五维、Accepted Observed State覆盖Planned瞬时状态、`REF-TAIL`不越权覆盖身份，以及站位失败优先单变量复拍；全部复用现有Pipeline、Execution Ledger与Template结构。
- R17-A至R17-C验证角色声音身份严格opt-in、常规STATE-08 Prompt完全省略声音身份文字、显式声音设计进入独立Seed Audio兼容模板，以及已有Confirmed Voice Source不会在只请求Clip Prompt时被自动序列化。
- R18-A至R18-D验证Scene Spatial Snapshot与合法越轴、PL1克制表演、A3动作动力因果和A1简洁降级；四类均不得新增主STATE、Template字段或Prompt内部标签。
- R19-A至R19-D验证每Clip必检查但不必出草图、首次Required Clip先草图后Prompt、Pose Hierarchy / Relationship Topology漂移、Confirmed Anchor持久复用、Blocking重构四种Reassessment结果、简单单人NONE与A3综合草图；草图不得覆盖Canonical资产或污染最终Prompt。
- R20-A至R20-F验证母版只拥有Sketch Presentation Authority、Current Clip独占Blocking内容、钢琴双人 / 三人围桌 / A3统一使用无性别技术人偶、任何Character Appearance Leakage硬失败、简单单人NONE不受母版可用性影响、Prompt Rewrite复用当前草图且母版不进入最终视频参考资产或图片预算。
