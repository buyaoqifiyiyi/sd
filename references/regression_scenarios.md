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

输入包含连续对话、动作接力、场景断点与不同逐镜时长的Confirmed Detailed Shot Design。检查所有正式Shot按原顺序且仅进入一个CLIP-xxx；每个Clip为4—15秒；连续低复杂度Shot可合并，跨时空/资产断点和超过15秒候选被拆分或返回STATE-06；Clip内保留起始状态、连续动作、空间/道具/摄影机连续性与结尾状态，Clip末保存`[Gxx尾帧]`；STATE-08按CLIP→G一对一输出一条连续Prompt，即使Clip包含多个Shot也不拆Prompt；任何Storyboard视觉材料均不得进入参考资产。

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

- 角色定义与角色音色描述：中低音域、清晰克制、自然语速、短停顿后再强调关键词。
- 三视图Prompt：`角色设定表，28岁东亚女性气象工程师林遥，椭圆脸、平直眉、深棕眼、短黑发齐耳并露出双耳，身高约168厘米、匀称偏瘦体型；穿灰蓝色连帽防水工作服、深灰工装裤、黑色防滑短靴，不佩戴首饰。纯浅灰无缝背景，同一画布从左到右为正面全身自然站姿、严格右侧全身、背面全身，三个视图等比例等高度，服装接缝、口袋、拉链、帽型、鞋型与颜色完全一致；柔和中性棚拍光，真实电影角色概念设计，清晰材质与结构，4:3横幅，高分辨率。禁止改变脸型、年龄感、身体比例、发型长度、服装结构与配色；禁止透视夸张、动态姿势、额外人物、文字、水印、拼错肢体。`
- 面部特写Prompt：`林遥面部角色参考，28岁东亚女性，椭圆脸、平直眉、深棕眼、鼻梁自然、薄而清晰的唇形、真实轻微皮肤纹理、短黑发齐耳并露出双耳；正面头肩特写，平静中性表情，视线略高于镜头，浅灰无缝背景，柔和中性棚拍主光加弱填充，肤色准确，真实电影角色概念设计，1:1，高分辨率。严格继承三视图的脸型、年龄感、发际线、发长与发色；禁止美颜塑料皮、夸张妆容、笑容、首饰、额外人物、文字、水印、五官漂移。`
- 状态变体：`Not Required—剧本未确认额外视觉状态。`
- `Visual Production Status: Prompt Draft`与`Awaiting User Confirmation: Image Prompts`；不得生成图片。

模拟用户确认`Prompt Revision: P-v001`后，状态变为`Prompt Confirmed`。生成后仅登记`Candidate References: char-001-turnaround-c01.png; char-001-face-c01.png`，状态为`Image Generated`，不得出现Canonical References或Active。模拟用户确认两张图片后，最终记录必须为`Visual Production Status: Asset Confirmed`、`Status: Active`、`Active Version: v001`，并把两张已批准Candidate References升级为Canonical References。

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

所有案例先删除非当前Clip出场角色、未使用环境/道具/动作图并去重，再把Direct / Reference-Only确定需要的首尾帧计入Projected Final Count。最终`参考资产：`只能列真实存在且已确认的资产/帧，图片总数必须≤9；整合只允许在超限风险触发后作用于非角色信息。

### R11-A Seven Candidates

当前Clip有7张真实、独立、相关参考图，无额外连续性帧需求。PASS：不整合，最终7张。FAIL：为了“统一”或因为已有总设定图而主动替换/合并独立图。

### R11-B Eight Candidates Without Reservation

当前Clip有8张真实、独立、相关参考图，已确认不需要上一Clip尾帧、当前首帧或其他额外图片位。PASS：不整合，最终8张。FAIL：默认整合或无依据预留导致丢失高精度独立图。

### R11-C Nine Candidates Plus Previous Tail

当前Clip已有9张候选，Previous-Clip Continuity Decision为Direct或Reference-Only，必须再加入上一`[Gxx尾帧]`。PASS：Projected Final Count按10张计算，主动去重/整合同类非角色信息或裁剪低优先项，至少释放1位，保留必需尾帧并最终≤9。FAIL：仍声称9张通过、遗漏必需尾帧、超过9张，或合并核心角色图。

### R11-D Twelve Candidates

当前Clip有12张真实候选。PASS：删除无关项、去重；仅在仍超限时用真实已确认的环境多视角/道具组/空间或动作关系总图替代完整覆盖的零散图；仍超限按保留优先级裁剪，最终≤9。FAIL：默认全部合并、虚构不存在的总图，或最终仍>9。

### R11-E Multi-Core-Character Independence

多角色场景中有多个当前Clip核心角色。PASS：每个核心角色各自保留独立三视图/角色锁定图；动作/互动图只负责动作关系；非角色信息承担必要的整合压力。FAIL：把多个核心角色合并成角色总表、共用一个角色位，或用动作图替代任一角色外貌基准。

### R11 Retention Priority

整合后仍需裁剪时，从高到低保留：当前Clip出场核心角色独立图 > 当前主要环境 > 当前关键道具 > 当前关键动作/互动关系 > 上一Clip尾帧/当前首帧连续性参考 > 特殊一次性道具/次要角色。已经判定为Direct / Reference-Only的连续性帧属于硬需求，必须先释放其他位置，不得静默删除后仍声明连续继承。

---

## R12 Runtime Skill Reload / Hot Reload

三个案例均以用户在已工作的旧对话中输入“调用SD，按当前安装最新版Skill继续当前项目”为触发。

### R12-A Stale Conversation Pipeline vs Current Installed Pipeline

输入：旧对话缓存声称`STATE-07`对应`Storyboard`，磁盘当前`SKILL.md`却声明`STATE-07 Clip Production`并包含更新的Skill Version / Build ID。

PASS：按`rules/runtime_reload.md`重新完整读取当前安装`SKILL.md`，记录`Reload Status: RELOADED`及磁盘版Skill Version / Build ID；当前安装Pipeline覆盖旧对话的Skill描述；再读取config、适用Rules、状态References、映射后Workflow与其依赖。

FAIL：继续把Storyboard当作固定STATE-07；用历史摘要覆盖磁盘Skill；未实际重读却声称`RELOADED`；强制用户新建对话或项目。

### R12-B Preserve Progress And Map To Current Workflow

输入：旧项目停在标注为`Storyboard`的`STATE-07`，已有Confirmed Detailed Shot Design，无Confirmed Clip Production Plan，并有可验证Last Successful Checkpoint。

PASS：按`Active Project Root/project_status.md > portable_project_status.md > 当前可验证Project Context`选择状态；如使用第三级则先规范化为Portable State；把项目映射到当前`STATE-07 Clip Production`和`10_clip_production_workflow.md`；保留Detailed Shot Design、Checkpoint、已完成States与Storyboard Optional Artifact；只继续尚未完成的Clip Production。

FAIL：回退STATE-00；重做已确认Detailed Shot Design；将旧Storyboard作为STATE-08参考资产；仅按旧STATE编号硬复制而不检查Artifact / Completion Gate。

### R12-C Preserve Production Lock And Confirmed Assets

输入：项目已有`Script Status: Production-Locked`、Confirmed Core / Support Assets、Active Versions、Canonical References、已接受Artifact Revision与用户明确的“不改剧本、不改角色外观”约束。

PASS：Reload后上述项目事实全部保留；只更新Skill Definition和必要路由标签；后续Workflow仍从Active / Canonical资产与Production-Locked Script读取真源。

FAIL：把Script Status降回Source Material；丢失Confirmed Assets、Active Version或Canonical References；因Skill重载重新要求用户确认已接受结果；忽略用户锁定约束。

---

## Deterministic Expectations

- Skill、Registry、Project、Asset、Artifact、Execution、Sequence、Clip、Poster、STATE-08和Review Validator通过合法样例。
- 缺字段、重复ID、非法时间轴、背景音乐、内部模式ID泄漏、无Return Route和第三次盲重试被拒绝。
- 主Pipeline仍只有STATE-00至STATE-09。
- STATE-08最终Schema仍只由templates/10_video_prompt.md拥有。
- R09-C/E/P均验证`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`，且Prompt确认前不出图、图片确认前不Active/Canonical。
- R10验证Canonical Character Appearance And Form Lock从Asset、Visual Development、Storyboard/Poster、Shot Design、Clip、Prompt Generation、Final Video到Review的全阶段继承，并覆盖非人角色禁止未授权拟人化。
- R11-A至R11-E验证条件性整合阈值、9张加必需尾帧的真实计数、12张自动压缩到≤9、实际资产存在性和多核心角色独立图硬门槛。
- R12-A至R12-C验证旧对话缓存不能覆盖当前安装Skill、旧STATE按当前Artifact / Completion Gate映射，并且Production-Locked Script、Confirmed Assets、Checkpoint、Accepted Artifacts与用户约束在Reload后不丢失。
