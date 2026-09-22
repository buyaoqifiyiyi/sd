# SD Film Regression Scenarios — Craft

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是回归集的一部分；完整范围与其余文件见 `references/regression_scenarios.md` 的 Regression File Index，脚本只把本文件当作回归语料的一部分，不构成独立权威。覆盖Prompt编译、表演、视觉阻断、剧本端到端与Writer层工艺（R16—R22、R64—R65、R69、R80—R82、R87、R91、R96）；R15见`references/regression_scenarios_prompt.md`，导演与运镜工艺场景见`references/regression_scenarios_director.md`。

## R16 Delta / Budget / Scope / Canon / Authority / Retake

以下案例必须沿用现有STATE-07 Clip Contract、八组Shot-State Memory、Reference Selection / Routing、Execution Ledger、STATE-09 Review与`templates/10_video_prompt.md`固定结构；不得新增主STATE、Clip Registry、平行Project State或最终Prompt字段。

### R16-A Canonical Sources Carry State, Prompt Carries Current Delta

输入：已有Confirmed / Active角色与环境正式资产；当前Clip只发生角色从门边走到桌前、摄影机同轴跟随并停在手触桌面的Endpoint。

PASS：`参考资产`保留正式ID/版本/Primary Role，`人物一致性 / 环境一致性`只作当前状态、风险和不得改变项的最小确认；Prompt主体集中描述行走、摄影机路径、手部接触、时间顺序与稳定Endpoint。模板字段完整但不重复长篇五官、服装、建筑结构与材质。

FAIL：删除正式资产引用；在多个字段重复完整角色/环境设定；因压缩而丢失当前动作、镜头Delta或Endpoint。

### R16-B Generation Budget Allocation

输入：同一候选Clip要求完美身份、复杂奔跑打斗、五人群体、繁忙雨景、环绕运镜、多人对白口型、强FX和变化灯光。

PASS：内部先明确一个Primary Spend与最多一至两个Secondary，把群体活动、复杂环绕、非必要口型、额外FX与光色变化写入Economized / Safe Downgrade；Five-Dimensional Matrix只高控制必要未锁定项。若仍超载则返回STATE-07/06拆分。

FAIL：五维全部补满；Primary不唯一；Economized为空；把`Primary Spend / Secondary Spend / Economized`写进最终Prompt字段。

### R16-C Accepted Take Overrides Planned Transient State

输入：CLIP-03 Planned End为“左手搭手背”，实际Take的Observed End为“右手搭手腕”，用户明确接受该Take；Run、Prompt Revision、Review与接受证据齐全。

PASS：Execution Ledger分别保存Planned与Observed；Accepted Canon State采用“右手搭手腕”。CLIP-04从该状态继续，不无过程纠回左手/手背，也不重播接触动作；正式资产身份仍不变。

FAIL：未记录Observed；下一Clip强行按原计划恢复左手；把未接受Take写入Canon；因接受动作结果而改变正式资产身份。

### R16-D REF-TAIL Identity Drift Is Not Identity Authority

输入：上一Accepted Take / `REF-TAIL`的脸部略漂移，但Active Character Canonical Reference正确；下一Clip需要继承尾帧姿态、站位与动作阶段。

PASS：角色Canonical Reference声明Identity Authority，`REF-TAIL`声明Transient State Primary Role；下一Clip保持正式角色身份，只从尾帧/Accepted Canon继承姿态、站位、朝向与动作阶段，并把脸部漂移列为Continuity Risk。

FAIL：让尾帧覆盖正式脸部身份；完全丢弃尾帧导致站位/动作阶段重置；不写Primary Role / Purpose；把漂移尾帧升级为角色Canonical资产。

### R16-E Single-Variable Retake For Blocking Error

输入：生成结果只有人物站位错误，身份、动作、镜头、光线、道具与其他连续性均正确。

PASS：Review诊断为Spatial / Blocking并选它为最高影响变量；第一轮只修Affected Clip的空间关系/Blocking与必要相邻边界，保留其他已接受内容；Retake后只比较站位及其边界是否改善。可后期安全修复时路由Editing并说明范围。

FAIL：整段Prompt全部重写；同时更换角色资产、动作、运镜、光线与道具；没有前后Take比较；以“整体感觉”直接REBUILD。

---

## R17 Voice Identity Opt-In And Prompt Isolation

### R17-A No Voice Request

输入：角色有对白，用户只要求继续主Pipeline或输出当前Seedance Clip Prompt，没有提出音色制作或当前视频声音控制要求。

PASS：不进入AUDIO模块；默认外部已有可用角色音色资源；STATE-02/03/08均不阻塞；视频Prompt完全省略`音色特征：`、Voice Profile、Voice/Audio Reference及“已有/缺失/无需音色”状态文字，台词只保留准确文本与必要Dialogue Performance。

FAIL：要求补建Voice Profile；创建Not Applicable；返回STATE-03；输出`No Voice Asset`或无对白占位；把音色描述写进视频Prompt。

### R17-B Explicit Voice Design

输入：`为女主设计音色。`

PASS：Router返回`AUDIO / SEED-AUDIO Voice Asset`，从当前项目阶段独立进入音色模块；输出独立Voice Profile和明确标记为“SD Film为Seed Audio 1.0组织的兼容模板”的Prompt，Prompt内按该模板字段按需输出，并分离稳定Voice Identity与当前Dialogue Performance；不强行并入视频Prompt。

FAIL：继续普通Character Asset；把声音交付塞进STATE-08；冒充官方唯一字段模板；固定要求15秒、八条`No...`声明或无关视觉描述。

### R17-C Confirmed Voice Exists But User Requests Only CLIP-03 Prompt

输入：Active CHAR Version已有Confirmed Voice Profile或Voice Audio Reference；用户只说`输出CLIP-03 Seedance提示词。`

PASS：Confirmed声音资产只作为Source State存在，不投影到CLIP-03视频Prompt；`音色特征：`和Voice/Audio Reference均省略。主流程按STATE-08其他Gate继续。

FAIL：自动复制Voice Profile；写“由参考音色锁定”；仅因已有声音资产就把Reference列入`参考资产：`；把先前AUDIO授权外推到当前请求。

---

## R18 Spatial / Performance / Action PREVIS Minimal Integration

### R18-A Two-Person Dialogue And Bench Axis Continuity

输入：同一教室连续场景，A与B并排坐在唯一横向长凳上，A始终在观众画面左、B在画面右；先给双人建立镜，再做同一轴线侧的正反打。中段导演有意让A起身绕到B另一侧，并要求越轴后继续对话。

PASS：Scene Spatial Snapshot锁定长凳、门、窗、钢琴等Fixed Environment Anchors、A/B起始位置、Eyeline Axis与camera safe side；普通正反打保持相反眼线与同侧机位。A换位时记录`Start Position → Visible Movement Path → End Position`，镜内明确换位并以固定地标建立新轴线侧，屏幕左右翻转因此合法；Environment Canonical继续锁空间身份，Shot-State Memory记录换位后的局部状态，A/B/C `REF-TAIL`按边界需要选择。

FAIL：下一镜A/B无过程换边；把所有屏幕左右当成场景东/西；只写“创意越轴”而没有可感知过渡；或把合法新轴线一律判错并强迫永不越轴。

### R18-B Restrained Youth Drama Uses Minimal Carriers

输入：4秒青春片反应镜头。角色听见朋友轻声道别，选择不挽留；剧本要求克制，没有崩溃、哭喊或重大揭示。

PASS：路由为Performance-dominant，使用PL1；只选1—2个载体，例如视线停在对方手上后短暂移开、呼吸停半拍再缓慢恢复，并以手指停止动作或肩膀保持不动作为可选支持。保留“想挽留但压住”的公开状态与稳定余韵，不强制完整递进链，不自动加入落泪、吞咽、瞳孔变化或大幅后退。

FAIL：机械输出触发—瞳孔—下颌—吞咽—指尖发白—呼吸粗重—失控哭泣的完整链；或仍只写“她悲伤而复杂地看着对方”。

### R18-C A3 Choreographed Action Has Physical Causality

输入：一段经过剧情授权的复杂格挡—转身—反制动作，起始双方站位、主Action Axis、道具状态与最终“攻击者失衡、主角稳定防守架”结果已确认。

PASS：路由为Action-dominant并选A3；动力链按`knowledge/action_previs.md`只写本例必要链节，不逐条抄全。景别与Coverage让支撑、轨迹、接触和结果可见；结尾把攻击者失衡方向、主角支撑脚与朝向、道具持有与摄影机safe side写入Shot-State Memory，供下一Shot或Accepted Canon继承。

FAIL：只写“主角猛地反击、双方激烈打斗”；接触、受力和结束状态缺失；下一镜双方恢复初始架势；或因为A3自动加入玄幻FX、0.5秒硬撞、机枪式对招和高潮定格。

### R18-D A1 Simple Action Stays Simple And Prompt Stays Clean

输入：角色从桌面拿起一封信，转身看向门口，Clip内没有追逐、对抗、复杂道具、FX或高强度表演。

PASS：路由为Action-dominant或Mixed中的低复杂度动作，选A1，只写右手从桌边起始、沿短路径握住信封、信封离开桌面并稳定保持在右手、角色转头后视线落向门口的Start / Path / End；不添加动力链、精密角度、速度、受力参数或复杂运镜。STATE-08不输出A1、Kinetic Chain、PL等级、Shot Purpose、QA或路由标签，继续按`Source Carries State, Prompt Carries Delta`只保留当前Clip必要Delta。

FAIL：为拿信加入蹬地、腰胯、脊柱传导、空气反馈、接触力数值与多段摄影机；或把内部11环、六阶段和Purpose列表逐项塞进最终Prompt。

---

## R19 Visual Blocking Sketch / Clip Prompt Gate

### R19-A CLIP-04 First Prompt Requires One Confirmed S+P Anchor

输入：CLIP-04中林夏在左、许栀在右，共坐同一张长琴凳，共同面向钢琴 / 窗外；许栀仅允许`Gaze + LIMITED Head`，其余身体锁定；林夏持续弹琴且不转头。用户首次请求`输出CLIP-04提示词`或只说`下一个`。

PASS：STATE-07已记录Visual Blocking Risk Pre-Assessment；STATE-08 Final Assessment判`HIGH / REQUIRED`，本轮先生成中性S+P综合草图，核对role mapping、林夏左 / 许栀右、Side-by-side、Same Bench、Shared Facing、许栀Gaze→林夏、`Head LIMITED`与owner其余Blocking维度。林夏与许栀必须使用同一套无性别技术人偶，只靠蓝 / 红角色标签、姓名和左右位置区分，不以长发 / 短发、裙装 / 裤装或身体曲线区分。通过后注册`REF-SKETCH-04｜CLIP-04空间与姿态调度草图`，说明`草图人物为无性别调度人偶，仅用于空间 / 姿态 / 机位关系，不作为人物外观参考。`加入当前Clip参考资产并更新预算；本轮不输出Prompt，下一次继续且Signature未变时才输出。

FAIL：第一次请求直接输出Prompt；生成草图后未验证或未列入参考资产；把草图当角色 / 环境Canonical；用性别、发型、服装或体型区分林夏 / 许栀；让“许栀看林夏”自动导致全身转向；或认为左右没交换所以Face-to-face不算漂移。

### R19-B Prompt Rewrite Reuses Anchor; Blocking Reconstruction Reassesses

输入：CLIP-04已经有Confirmed `REF-SKETCH-04`。用户连续多次要求压缩措辞、优化主风格、整理反向提示词、调整台词 / 音效，Blocking不变；随后大幅重构为许栀起身走到林夏面前。

PASS：普通改写每次只比较Current Revision与Blocking Signature，结果为KEEP并复用同一草图 / 图片位，不重复生成。起身、移动到面前使Same Bench、Position、Topology与Clip End Blocking实质变化，触发Reassessment并得到`REPLACE with REF-SKETCH-04-v2`或`RETIRE + CREATE`；新草图重新验证后才输出重构Prompt。

FAIL：每次措辞优化都重新出图；Prompt改写导致草图版本自身漂移；或大幅Blocking重构仍盲用旧图且不重新评估。

### R19-C Simple Single Person Is NONE

输入：单人原地站立，只做普通转头；固定机位，无共享空间结构、换位、复杂道具、跨轴、复杂前中后景或A2/A3动作。

PASS：每Clip检查仍执行，但Final Assessment=`NONE`；不生成、不预留`REF-SKETCH`，直接编译Prompt。

FAIL：为了流程统一强制生成P-SKETCH或Formal Keyframe。

### R19-D A3 Action May Use A-SKETCH Or Combined Anchor

输入：A3复杂格挡—转身—反制动作，双方起点、主Action Axis、道具、接触 / 近接触、受力方向、恢复终点与Next-action Carryover已确认，但单纯文字仍存在路径 / 接触漂移风险。

PASS：Final Assessment可判`ACTION HIGH / REQUIRED`，选A-SKETCH或S+P+A综合草图；双方使用同一套无性别技术人偶，以箭头、轴线、接触点和受力方向锁定Start / Path / Contact / Force / End / Carryover。只有动作可达性必需的身体比例可以表达，仍不恢复性别、脸、发型与服装身份。通过Sketch Validation与Character Appearance Leakage Check后作为受限Visual Blocking Anchor进入参考资产；角色、环境与道具身份继续由各自Canonical资产控制，Prompt正文只保留当前动作Delta与必要局部约束。

FAIL：A3一律强制多张正式Keyframe；草图带入写实五官、正式服装 / 灯光 / 画风并覆盖Canonical；或把全部动力链和草图标注复制进Prompt。

---

## R20 REF-SKETCH-MASTER Presentation Authority

### R20-A Piano Pair Uses Technical Blocking Sheet Language

输入：CLIP-04仍为林夏左 / 许栀右、Side-by-side、Shared Facing、Same Bench，许栀只有`Gaze + LIMITED Head` Delta；`REF-SKETCH-MASTER`注册为真实可读视觉输入，示例图本身也包含两女与钢琴内容。

PASS：母版只作为Sketch Presentation Authority输入，当前Blocking Signature是内容权威。输出为Technical Director Blocking Sheet，各分区直接证明林夏左 / 许栀右、Side-by-side、Shared Facing、Same Bench、许栀Gaze→林夏和`Head LIMITED`；两人用同一套无性别人偶，只由蓝 / 红标签、姓名与位置区分，不继承母版或角色身份。当前`REF-SKETCH-04`通过验证后进入视频参考资产，母版本身不进入。

FAIL：提示词核心仍是唯美铅笔Storyboard、雨天青春电影或人物插画；以长发 / 短发、裙装、脸或身体曲线区分两人；缺少Topology / Facing / Gaze / Camera证明；或因案例内容与母版相似就把母版当当前Clip Blocking Authority。

### R20-B Three People Around A Table Has No Template Content Leakage

输入：Current Clip是A / B / C三人围圆桌交谈，环境为干燥会议室，无钢琴、长琴凳、窗边雨景或乐谱；需要锁定三人座位、共同视线中心、Camera Safe Side和发言者局部转头。

PASS：继承母版的信息层级和技术标注语言，但Main Blocking与Top-down重新布局为三人环桌Topology；三人使用同一套无性别技术人偶，只靠A / B / C标签、技术颜色和座位位置区分，角色数量、位置、环境锚点和Camera完全来自Current Clip。Template Content Leakage Check与Character Appearance Leakage Check均须通过：母版示例内容与身份化外观都不得出现。

FAIL：复制两个人物、钢琴 / 琴凳、窗户、乐谱、雨线、黑板文字或示例人物造型；用三种发型、服装、性别或体型区分A / B / C；为贴合母版把三人删成两人；或像素级复刻版式导致三人关系不可读。

### R20-C A3 Action Remains Technical Previs

输入：A3武打Clip需要A-SKETCH或S+P+A；Current Clip已确认双方起点、Action Axis、道具路径、接触 / 近接触、受力方向、恢复终点与Next-action Carryover。

PASS：母版只提供Technical Director Blocking Sheet表达，双方使用同一套无性别技术人偶，以Start / Path / Contact / Force / End箭头、轴线、Camera side与动作Permission完成技术预演；布局可为动作路径重新分区，必要身体比例只表达可达性 / 接触 / 受力约束。不出现性别化体态、外貌重绘、海报化定稿或无依据FX，Canonical身份不受影响。

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

PASS：实际视觉检查把`character_appearance_leakage`记录为`true`或无法确认`neutral_mannequin_representation=true`；`scripts/validate_sd_film.py sketch`固定返回`FAIL = Character Appearance Leakage / Identity Contamination`。候选保持`FAILED / REVISE`并沿同一Technical Visual Blocking Sketch route重做，不注册Confirmed、不进入Clip参考资产，也不改Character Asset或Blocking事实迁就草图。

FAIL：因版式与Blocking正确就忽略外观泄漏；用“只是代理”解释后仍注册；或把中性人偶QA扩写进最终Prompt的反向提示词。

---

## R21 Performance Arc / Emotion Preflight

### R21-A Restrained Character Changes Across Shots Without Extra Coverage

输入：同一Scene有三个已确认SHOT。角色先冷静检查异常，第二镜确认目标，第三镜完成处理并恢复克制；剧情、SHOT数量、机位、时长和动作结果均已锁定，不允许加镜头。

PASS：STATE-06建立同一角色的Performance Arc Map：Inherited Baseline为专业冷静；第一镜以视线先移、一次短暂停眼或呼吸变浅表现疑惑；第二镜确认刺激后眼神稳定、下颌或手部张力略增并选择行动；第三镜动作完成后先复核结果、缓慢释放肩颈与呼吸，再回到新的受控Settled State。每镜只承载当前可见段，`Previous Settled State = Current Inherited Baseline`，STATE-07/08 Performance / Emotion Check为PASS，最终只写入既有表演字段语义，不新增SHOT、Clip、STATE或Template字段。

FAIL：三镜都只写“角色始终冷静从容”；每镜从默认脸重新开始；为了补情绪增加无必要特写/反应镜；或在STATE-08用“更有情绪、更生动”形容词替代上游表演链。

### R21-B Ensemble Uses Relative Amplitude And Reaction Order

输入：同一Clip含克制处理者、受惊逃跑者、刚解除痛苦的委托者与旁观者。剧情要求处理者始终最克制，受惊者最外放；委托者只在确认危险解除后放松，旁观者延迟反应。

PASS：每个Beat只有一个清楚Primary Performer；受惊者可用Open / Heightened并承担大幅逃跑，处理者用PL1/PL2眼神、呼吸或动作后停顿承接，委托者从谨慎倾听到确认安静再肩膀放松，旁观者作为Listener / Background Holder先保持低幅、收到共享刺激后才升级。视觉重点交接由刺激、视线或动作结果触发，四个角色各有不同Arc Endpoint和Next-shot Carryover。

FAIL：所有人同时瞪眼、张嘴、后退；所有人都用同一`紧张→放松`模板；为保持主角“高冷”让处理者完全无注意/呼吸/停顿变化；或让背景人物无刺激抢走视觉重点。

### R21-C Intentional Hold Is Active, Not Frozen

输入：4秒近景中角色必须保持面无表情以隐藏真实反应，只听完一句关键信息，不说话、不移动位置。

PASS：表演被定义为Intentional Hold：视线先停在说话者、关键字后眨眼短暂停止或呼吸轻微受抑，手部原动作停住，延迟一拍后恢复控制但视线未完全放松；Post-action Residue进入镜头结尾，动作与口型容量不被无关微表情堆满。

FAIL：只写“全程面无表情”；或为了避免面瘫同时加入挑眉、瞪眼、吞咽、握拳、后退、落泪和转身。

---

## R22 Screenplay Creation / Existing Script Dual Entry

### R22-A Idea Enters Screenplay Generation

输入：`调用sd，写一个雨夜双女主重逢短片。`

PASS：STATE-00登记`Creation Brief`，STATE-01进入Director-first Screenplay Development；不要求先提供完整剧本，不对尚不存在的文本输出Optimization Opportunity Report。Proposal按owner具备视觉动作、信息层次与AIGC Directability等可拍摄要素，并在用户确认Gate停止。

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

PASS：剧本通过`knowledge/writer/screenplay_development.md`的`## Directable Screenplay QA`十四项内部QA（含开场钩子、高潮兑现与结尾兑现）；最终文本是可独立阅读的剧本，没有35mm、特写、推镜、摇镜、机位、SHOT / CLIP或分镜表字段。

FAIL：只写说明性对白和内心独白；把QA清单机械输出成剧本正文；或在STATE-01预先锁定摄影机。

### R22-G Existing Diagnosis Regression

输入：Class B初稿，无明确改写授权。

PASS：原有A/B/C分级、十二项Optimization Opportunity Report、User Decision Gate、No Revision、Optimization Rejected、Adaptation Draft与第二次Proposal确认全部仍可用。

FAIL：因新增Creation route而自动改写Existing Script，或取消既有保护Gate。

### R22-H Downstream Isolation Regression

输入：运行Skill静态与定向回归。

PASS：主Pipeline仍只有STATE-00至STATE-09；Storyboard仍Optional/Auxiliary；Voice仍Explicit-only；视频Prompt仍永久禁配乐；REF-SKETCH、Prompt Compiler、STATE-02至09及四种Script Status保持原合同。Director Intent从STATE-00/01开始，Scene Director Intent经STATE-05投影、在STATE-06具体化为Director Decision Notes、在STATE-07/08消费，但不成为最终Prompt字段。

FAIL：新增主STATE、让Storyboard进入主路由、自动触发Voice/Music、改变STATE-08 Schema，或让内部Director Intent污染剧本/Prompt。

### R22-I Poster And Cover Trigger Regression

输入：STATE-04后用户请求“给短剧设计一张平台竖屏封面”；另一会话未请求任何海报或封面。

PASS：显式封面请求进入`workflows/17_poster_design_workflow.md`封面系Lane；渠道尺寸、安全区与导出格式来自官方规范或用户规格，缺失记待确认；大字标题缩略图可读；沿用已确认资产不重设计；输出仍由`templates/15_poster_design_package.md`拥有。未请求时不追加海报或封面交付，主Pipeline推进权不变。

FAIL：未请求时自动加海报或封面；凭记忆硬编码平台像素；把封面做成与影片内容无关的通用营销图；或电影海报系Lane混入电视剧宣传图、广告KV气质。

---

## R64 Prompt Discipline And Reference Intake Regression

### R64-A An External Prompt Is Decompiled, Never Copied

输入：用户丢来一份他很喜欢的外部视频提示词（他人教程或收集的成品Prompt）并说"照这个风格做"。

PASS：系统按`knowledge/visual_styles/index.md`的`### External Prompt Reference Gate`把它当作与截图同级的风格研究来源：先按`Reference-To-System Evidence Gate`分为可观察证据 / Project Proposal / Unknown-Not Transferable，再把可观察部分反编译为STATE-04四项`Aesthetic Decision Lock`；原文、句式、字段名与排版不进入`主风格：`或任何最终Prompt字段；具名作品、器材型号与模型能力数值不因"参考里有"而继承。

FAIL：把外部Prompt的句子、字段名或结构直接搬进最终Prompt；或凭它改动Production-Locked Script、Canonical资产、Director Intent、媒介形式与无BGM边界；或把参考里的模型参数当成当前Target Model的已证能力。

### R64-B Dialogue Is A Closed Set

输入：某Clip的已确认剧本只固定了三句台词；另一Clip确认本Clip无对白。

PASS：`台词`字段逐句列出该三句，并声明不得增补、改写、复述或生成集合外的对白（含画外音、旁白、无人称语音与背景人声）；无对白Clip写出明确的无对白边界，不留空、不省略字段。

FAIL：Prompt出现集合外的对白、旁白或背景人声；或把无对白Clip的`台词`留空当作"没有要求"。

### R64-C A Wrong Reading Is Re-Specified Positively

输入：某节拍确认"人物持械静立、只做呼吸起伏"，其最可能的失败是被生成成大幅挥砍；另一节拍确认"定格凝视"，最可能失败是夸张瞪眼。

PASS：按`### Positive Specification And Negative Prompt Placement`在`画面与镜头` / `人物动作与情绪`写出可枚举的小载体（姿态稳定、真实呼吸起伏、发丝与衣物自然摆动、视线缓慢移动）；该风险的负向部分按失败**类别**归位——属该节拍内容的留在其所属字段，真正跨阶段的部分才进入末尾唯一`反向提示词：`。

FAIL：只在末尾写"不要大幅挥砍 / 不要夸张瞪眼"而没有正向载体；或在逐镜字段保留否定句、把风险实例逐条罗列成清单。

### R64-D A Sketch Line Disclaims Its Own Markers

输入：当前Clip的`REF-SKETCH`含占位人偶、朝向标记与追踪色块，并作为真实`@图片N`提交。

PASS：`多模态参考资产：`的该行除用途与`锁定 / 保持`维度外，写明它是技术参考而非画面内容——占位标记不是额外人物、道具或装饰，草图线条、分区、标注与追踪色不进入最终画面。

FAIL：只写"草图参考"或只写文件名；或最终画面出现草图的边框、分区、标注、追踪色，或把人偶当成角色。

### R64-E A Long Take Advances By Micro-Beats Without New Phases

输入：一个23秒连续长镜头Clip，Timeline只有三个阶段，其中一段同时承载提械、转脸与定格三个节奏节点。

PASS：该阶段按微节拍逐点写清机位状态、主体动作、眼与脸、空间与道具变化，密度约0.3—1.2秒一个节点（该秒数只作内部判据、不写入Prompt）；阶段总数声明与实际阶段数保持一致，不新增阶段、不新增字段。

FAIL：把多个节奏节点压成"随后继续动作"式概括；或为提高密度新增时间线阶段、改动阶段总数声明，或把时间戳能力扩散到2.0 / H3。

### R64-F The Discipline Self-Check Points At Owners And Does Not Gate

输入：一次交付前运行`knowledge/quality/prompt_scorecard.md`的`## Discipline Self-Check｜六条执行自检`。

PASS：六条逐条指向既有唯一owner、只给可观察证据；未通过的条目作为剩余风险写入Review，不单独判FAIL、不改变既有Hard Gate、不成为最终Prompt字段。

FAIL：把六条复制成第二套规则正文；或把它们升格为新Hard Gate使原本通过的Prompt判FAIL；或把自检标签写进最终Prompt。

### R64-G The Receipt Carries The Discipline Self-Check

输入：一个FAST项目在STATE-08交付轮的收据只有"阶段 → 工件 → 状态"，缺`Prompt纪律自检`条目；另一轮把该自检升成Hard Gate，使一条`不过`把原本可交付的提示词判FAIL；第三轮把六条自检文字写进了最终Prompt末尾。

PASS：按`rules/automation_mode.md`的`### Delivery Receipt｜交付收据`，该轮收据必须含`Prompt纪律自检`条目，逐条写`过` / `不过` / `不适用`并附一句可观察证据，`不过`项同时进入该轮剩余风险；它只提高可见性——不改变该轮能否判完成、不升为Hard Gate、不新增Project State字段、不进入最终Prompt正文。

FAIL：收据缺该条目；或把它升为Hard Gate而改变既有pass/fail；或让它承担状态写回职责、长成第二套Completion Gate判据；或把自检文字写进最终Prompt。

### R64-H An Association Failure Is Attributed To Its Owner, Not Restated

输入：用户带回一条已生成Clip并指出"画面里出现了剧本里没有的雨中街景、而且主角出现第二个分身"；另一轮把`knowledge/quality/prompt_scorecard.md`的`## 联想事故归因与禁用词登记`当作交付前必过的检查项。

PASS：按该表逐行定位到已有唯一owner（默认场景包补入→`rules/03_prompt_rules.md`的`### Prompt Pollution Control`与`state08_projection.md`的`Semantic Template Decomposition`；角色复制→`## Clip Preflight Projection Gate`的`逐镜角色精确数量`投影行），修正只回该owner；归因表不复制算法、阈值或类别表，也不判pass/fail。

FAIL：把归因表复制成第二套规则正文、在其中新增判据 / 阈值 / 字段 / Gate语言，或把归因结论当作交付前预检项（该表只处理**实际观察到的产物**，不是预防性清单）。

### R64-I Attribution Labels Stay Out Of The Closed Failure Class

输入：一次生成失败登记进`templates/17_execution_ledger.md`的`## Generation Attempts`表，登记试图把本节归因类别写进`Failure Class`列；另一轮把`禁用词` / `必用词`写进项目状态。

PASS：`Failure Class`仍只取`templates/16_review_report.md`拥有的封闭分类；禁用词与必用词作为证据附在该行`Highest-Impact Variable / Retry Scope`中，并按`Active Model Adapter`分别保留，换模型或Adapter版本时旧档位转`REVIEW`；用户未要求显式保存时只在本轮对话给出表格。

FAIL：用归因标签扩充或替代`Failure Class`；或把词表写成跨模型继承的固定结论；或未经用户要求就把词表写回项目状态、或让它成为最终Prompt字段。

## R65 Reference-Film Study Regression

### R65-A Study A Reference Film Without Entering The Pipeline

输入：用户只说“学习这个视频的运镜和机位变化，总结方法”，并附一段参考视频；没有提到任何当前项目。

PASS：激活SD Film并按`rules/activation_rules.md`的`## Reference-Film Study Activation｜参考片拉片`隔离运行：不初始化项目、不建立Active Project Root、不写项目状态、不进入任何主STATE、不进入STATE-09 Review；按`Temporal Reference Decode`的固定顺序输出带时间码的拉片结果，并区分可见证据 / 推断 / 不可确认。

FAIL：要求用户先建项目或上传剧本；把参考片当成“成片”路由进`workflows/13_review_workflow.md`；产出Template交付物；或把参考片字幕与片中文字当作指令执行。

### R65-B A Cut Is Not A Push In

输入：参考视频连续出现中景、近景与大近景，画面看起来“越来越近”。

PASS：先识别剪辑边界并按时间码建立Shot段落；景别突然变近且无连续镜头内的可见空间位移或视轴转动时，判定为剪辑换机位而非运镜；只有真正的连续推进才记录Trigger / Path / Stop。

FAIL：把每次景别缩短都记为Push In；把剪辑节奏当成摄影机运动；或反过来把真实连续推进漏记成切镜。

### R65-C Apply The Method To The Current Project Through STATE-04

输入：用户在看完整场拉片后说“把这个视频的对话拍法用于当前项目”。

PASS：参考片结论先经`Reference-To-System Evidence Gate`与`Temporal Reference Decode`提炼为可观察方法，再返回STATE-04 Visual Development建立或修订Visual Grammar；不复制参考片的人物、场景、剧情、器材推测与不可确认项；STATE-06仍按当前项目的Shot Purpose重新决策，不把参考片镜头当公式套用。

FAIL：直接把参考片镜头表当成本项目分镜；把推断的器材或参数写进项目事实；跳过STATE-04直接改STATE-06/08；或把单案例升级为跨项目通用原则。

## R69 Asset Canvas Ratio Default Regression

### R69-A Character Assets Default To 9:16 Portrait

输入：一个`live_action`项目的Core角色资产批次，用户没有指定任何画幅比例。

PASS：按`rules/02_asset_rules.md`的`Asset Canvas Ratio Default｜资产图画幅默认`，Appearance Reference与五区角色设定图Prompt的`画幅/分辨率/交付规格：`写明`9:16`竖版；GPT Image写`1152×2048`（4K为`2160×3840`），Midjourney写`--ar 9:16`；五区版式仍按该文件定义，人物头顶、手与脚未被裁切。

FAIL：把人物类默认写成16:9；比例只写在正文形容词里而`画幅/分辨率/交付规格：`留空或写`Not specified`；为配合竖版压分区、缩下排或给正面区补画头部。

### R69-B Other Asset Categories Default To 16:9 Landscape

输入：同一项目的环境（含多视角）、道具（`1×4`）、正式FX与Support Board批次，用户没有指定任何画幅比例。

PASS：四类Prompt都按owner取其他类`16:9`横版（GPT Image写`2048×1152`，Midjourney写`--ar 16:9`）；环境每View一张画布、道具保持`1×4`等宽、Board横版排布；同一批次内画幅一致并进入`Shared Style Lock`。

FAIL：环境View改竖版或把多视角塞进一张画布；道具四格改成纵向排列或不等宽；Board用9:16排到对象互相遮挡；任一类继续沿用没有画幅的旧空字段。

### R69-C User Exception Wins And A Reference Image Never Sets The Canvas

输入一：用户明确说“这一批角色资产图我要横版16:9”。输入二：用户给了一张竖版参考图但没有提比例。输入三：项目已确认交付规格写明本项目全部资产图16:9。

PASS：输入一按用户当前明确例外取16:9并在当前批次记录该例外；输入二仍取人物类默认9:16，且不把参考图的宽高比当作画幅依据（判据见`Reference Provenance And Degradation`）；输入三以已确认交付规格为准，覆盖类别默认。

FAIL：把参考图的宽高比当成新资产图的画幅；用“参考图是竖的”替代用户指令；把一次例外扩散到其他批次或其他类别而不记录；或让三处输入互相矛盾却仍判PASS。

### R69-D The Ratio Never Reshapes The Layout And Out-Of-Boundary Ratios Are Refused

输入一：人物五区设定图在9:16下被要求“上下排都放大”。输入二：道具图被要求写成`4:1`。

PASS：五区在竖版下仍保持区域分工，不为放大而裁切、改分区数或拆成多张图；`4:1`超出现行图像模型可交付边界（`adapters/gpt-image.md`的`gpt-image-2`为比例≤3:1）时据实说明并回到合法比例或改选模型，不写成已交付。

FAIL：为满足宽比例把`1×4`道具图拆成两张或四张独立图；把超边界比例写成可交付参数；或版式已随比例漂移而Image QA仍判PASS。

## R80 Genre Profile Regression

### R80-A Genre Knowledge Loads Only From A Registered Genre

输入一：项目登记`类型：悬疑`。输入二：项目未登记类型，素材里只有平台标签"悬疑向"，媒介确认为`2d_anime`。输入三：用户给了一段参考片，未说明本项目类型。

PASS：输入一在STATE-04按`knowledge/genre/index.md`的`## Loading Rule`只读命中类型文件（带次类型时最多两个），把类型承诺落进`Visual Grammar Baseline`；输入二与输入三记`Genre Profile: PENDING`，不加载类型文件，也不从媒介档、平台、标签、画风或参考片推定类型。

FAIL：因媒介是`2d_anime`、平台是短剧或参考片是惊悚片就推定类型并加载；为"全面"整目录读取六个类型文件；类型未登记却写出`Genre Profile`结论。

### R80-B A Genre Is A Conditional Candidate, Never A Formula

输入一：悬疑项目的某场次在已确认剧本里信息透明，没有未知可保留。输入二：用户要求喜剧段落"每分钟来一个笑点"。输入三：恐怖场次被要求"这里加个跳吓"。

PASS：三处都按类型文件的成立条件判定——条件不满足时不使用该倾向并记录让位依据；类型倾向与Writer / Director Intent、已确认项目事实冲突时一律让位；不写固定节拍模型、不写冲突公式、不把单项目做法升级为通用原则，也不改写Production-Locked Script、Canonical资产或已确认Blocking。

FAIL：为凑类型给透明场次加入反转或保留信息；按分钟数安排笑点；用无因果跳吓充当恐怖结构；以"类型需要"为由改写剧情事实、冲突强度或结局形态。

## R81 Drawn-Medium Language Regression

### R81-A 2d_anime Reads Equivalents, Not Optics

输入：媒介确认为`2d_anime`的项目进入STATE-06。

PASS：按`knowledge/camera_language/index.md`的`## Medium Branch｜媒介分支`，该档不读光学原子，改读`knowledge/anime_language/index.md`的等效词汇——版面占比即景别、版面放大代替推、版面平移代替摇（地平线与消失点不变）、关键帧密度与冲击帧代替帧率与运动模糊；实拍专有量（焦段毫米数、光比比值、光圈、真实景深、稳定器、胶片型号）一律不写。

FAIL：照抄实拍光学原子并把焦段、光比或器材写进该档Prompt；或把"是2D"当作放宽镜头必要性、资产确认或Reference Budget的理由。

### R81-B The 2D Asset Form Is A Structure, Not A Negation

输入：`2d_anime`项目的 Core 角色资产批次。

PASS：按`templates/04_character_asset_prompt.md`的`#### 2D Character Asset Sheet Prompt｜设定集与画风锚`输出三区块——角色设定区（三区全身，**均完整含头部、面部与发型**）、表情区（仅表情不同）、画风与色指定区（线宽层级、上色法、阴影层数与色块关系）；Image QA 按设定集核对，**不得**要求五区版式，**不得**把上排正面区含头部与面部判为失败。

FAIL：把"五区不适用"当成结构定义；套用五区版式并给正面区挖空头部；把上排含头部判为出图失败并"补齐"；色指定写出用户未提供的Hex、RGB或LUT。

## R82 Delivery Aspect Framing Regression

### R82-A Vertical Layouts And Safe Areas Are Concrete

输入：交付画幅确认为竖屏的双人对话场次。

PASS：按`knowledge/camera_language/composition_language/vertical_framing.md`取三种布局之一（过肩前后错位 / 上下错位 / 纵深分离），一次只用一种；横向长距离运动改纵向或朝向镜头；面部、关键道具与字幕避开顶部与底部安全边带，平台未确认时**不虚构数值**；同项目不同Clip不混用画幅。

FAIL：把横向并列构图直接塞进竖屏导致两侧被裁；横向大幅移动撞出画外；关键信息落在平台界面覆盖区；为平台安全区编造具体比例。

### R82-B Delivery Aspect Is Confirmed, Never Inferred Or Cropped

输入一：平台是短视频、目标是短剧、素材是竖屏参考，但未声明交付画幅。输入二：已确认横屏素材需要竖屏交付。

PASS：输入一不推定交付画幅，横屏项目不加载该原子；输入二据实说明横竖构图的信息分配不同，**不得用裁切转换**，需要竖屏时按竖屏重新构图；交付画幅是**交付**量，与相机成像画幅（全画幅等效倾向）不得互相推断。

FAIL：从平台、目标形式或参考图比例推定交付画幅；把裁切后的画面当作竖屏交付；用资产图比例反推成片画幅。

## R87 Reference-Film Study Measurement Regression

本节只补上拉片的**测量层**：切点、时长与运动量从哪来，判断怎么被对账，以及无工具时的降级线。不得新增主STATE，不得让拉片产物获得Artifact ID或Canonical身份。

### R87-A Boundaries And Duration Are Measured, Never Eyeballed

输入：用户给出一条成片并要求拉片，本机有node与ffmpeg。

PASS：按`workflows/22_reference_film_study_workflow.md`的Step 2执行测量，汇报给出片长、帧率、切点数与合并后镜头数；模型只判景别、类别、运镜、画面、节奏，**不报时间**。阈值不合适的依据是"平均镜长与镜头数"这一行输出，不是观感。

FAIL：凭目测写出"这个镜头大约3秒"并把它当读数；手改`start` / `end` / `seconds` / `motion` / `seedCuts` / `meta`；缺少`node`或`ffmpeg`时仍声称有实测数值。

### R87-B No Tooling Means A Manual Pass, Stated As Such

输入：运行环境没有`node`或`ffmpeg`。

PASS：按`knowledge/visual_styles/index.md`的`#### Measured Boundary And Motion｜边界与运动量实测`末段执行一次纯人工拉片，结论仍按三层证据写出，并在汇报中**明确说明本次未实测、没有任何实测数值**；声称大动却看不出画面位移的一律降级为不可确认。

FAIL：因为无法实测就把"看起来像推镜"写成推镜；或反过来以"没有工具"为由跳过拉片、跳过运镜验收或降低结论分层要求。

### R87-C A Claimed Strong Move Must Survive The Motion Gate

输入：某镜实测帧间变化中位数为0.7，模型填了`push-in`（`strong`档）。

PASS：`validate`的运镜实测对账拦下该镜并**返回退出码1**，提示"写的是「推」，实测帧间变化只有0.7（< 1.5）——这一镜画面没动，重看一遍"；逐条修完重跑直到通过才交付报告。按退出码判定，不按输出末尾观感判定。

FAIL：跳过`validate`直接出报告；把退出码1当作已通过；只在文字里加一句"可能是主体在动"而不回看画面改写运镜。**注意反向那一向不属FAIL**：声称固定而实测偏高只出提示，它是需要人回看的地方，不是错误。

### R87-D A Skipped Gate Is Not A Passed Gate

输入：本轮未提供`--track`、未建`cast`，或关键帧目录不存在。

PASS：跳过的门在报告里**逐条列出并写明跳过原因**，汇报中明说"跳过不是通过"；关键帧确实没抽出来时明说缺哪几张。

FAIL：把`⊘ 跳过（视为通过）`汇报成"质量门全绿"；用占位图或挪用其他帧来凑"关键帧齐全"。

### R87-E Windows Redirect And Filtergraph Path Are Handled At The Right Layer

输入（Windows）：按Workflow执行`seed`并把stdout重定向到`shots.json`；随后合成对照视频。

PASS：重定向写**原始字节**（PowerShell 5.1的`>`会写出UTF-8 BOM，下游JSON解析即失败）；合成走`scripts/reference-film/compose-win.mjs`而不是上游`compose`（Windows的`\`与`:`会被滤镜解析器吃掉，绝对路径必须写成`C\:/…`）；平台差异与实测射程记在`scripts/reference-film/vendor/README.md`，**不改上游vendoring文件**；合成后抽帧确认镜号与面板高亮行一致。

FAIL：把BOM导致的JSON解析失败当成拉片数据错误去改底稿；遇到滤镜路径报错就声称本机不支持合成；直接编辑`scripts/reference-film/vendor/`里的上游文件；不抽帧验收就交付对照视频。

## R91 Directable Screenplay And Craft-Entry Regression

### R91-A A State Change Must Be Pointable, Not Narrated

输入：一个两分钟的家庭短片提案。儿子把父亲的旧手表放回抽屉，父亲没有抬头，只说了一句"放那儿吧"；提案正文里这一场另写了一句"父亲其实已经原谅了他"。
PASS：`## Directable Screenplay Gate｜可失败判定`第1项判定失败——关系变化被写成了叙述，正文里没有承载它的动作或反应用；最小修订为让父亲的一个可见动作承担该变化（把表从抽屉取出上弦，或推到儿子那一侧），然后重新指认。
FAIL：因为"父亲其实已经原谅了他"读起来亲切就放行；用一句解释性台词替代动作并视为已兑现；或声称QA十四项已通过，因此无需本Gate。

### R91-B A Craft Entry Without Its Condition Is Not Applied

输入：一个四分钟的双人关系短片，中段两人对话变成轮流陈述，信息平铺且不再推进。
PASS：取`## Craft Manual｜工艺手册`的`两人对话僵住时引入第三件事`条目，先读其`成立条件`（两人对话变成轮流陈述、或信息交换平铺）——条件成立；按条目引入一件可被争夺、交代或传手的实物作为争斗出口，让关系通过它变化；同时核对`反用场景`（需要正面摊牌的场景不适用），确认本场不是摊牌场。
FAIL：因为"三人对话更高级"而引入一个无关人物；把条目当成硬门，要求所有双人场景都必须有第三件事；或用它替代人物动机的补足，把结构手段当成性格解释。

## R96 Performance Evidence Regression

本节四组验收细则都是既有owner内的知识补足，不新增主STATE、Template字段或Prompt栏目；AU编号与节拍编号仍不得进入最终Prompt。

### R96-A Skin Acceptance Fails Before The Reference Is Locked, And Not For 2D

输入一：`live_action`角色外观参考图，脸被磨成塑料质感，鼻梁与额头连成油亮高光。输入二：`2d_anime`角色资产被指"没有次表面散射"。
PASS：输入一按`rules/02_asset_rules.md`的`### Appearance Reference Acceptance｜外观参考图验收`判第4项「高光分布」与第3项「克制瑕疵」不通过——该图不锁定，返回补足后重新确认，不得登记Candidate / Canonical / Active。输入二判**不适用**（该档对应物是线稿、上色法与网点），验收改走`templates/04_character_asset_prompt.md`的`#### 2D Character Asset Sheet Prompt｜设定集与画风锚`。
FAIL：因五官与服装都对而放行，或记成"画质不够高"、靠下游Prompt加`8K、真人皮肤、电影感`补救；把六项当成要逐条写进Prompt的模板；把实拍词表套到绘制媒介上；或以"不适用"为由跳过该档自己的画风锚与色指定检查。

### R96-B Detail Budget Follows Scale Instead Of Accumulating

输入：全员中景的双人对白Clip，`人物动作与情绪`写了`额头毛孔、鼻翼纹理、唇纹`，却没写地面接触与衣料反光。
PASS：按`knowledge/camera_language/lens_language/framing_and_scale.md`的`## Detail Budget By Scale｜景别细节预算`判越预算——中近景及更远只写整体肤色、皮肤与衣料反光差异与大面积受压受光结果，毛孔与唇纹属近景 / 特写预算；替换为当前景别真正看得见的结果（移动方向、接触点、面部朝向）。
FAIL：认为"写得更细总是更好"；或反向把近景写成`整体肤色`而与上一镜无差别；或借本条新增肤质、湿度与光源事实。

### R96-C A Disfluency Lands On One Hard Word And Reaches Sound, Breath And Mouth

输入：一个争吵场，女主要说"我一直觉得自己挺……"，剧本没写不流畅；导演要她表现出"难以承认自己的付出没被看见"。
PASS：按`knowledge/performance/dialogue_performance.md`的`## Speech Disfluency｜言语不流畅`取`启动失败`——口型已准备但未出声，一次失败吸气后才开口；不流畅落在最难面对的那个词，不平均分布；声音、呼吸与口型三处同步，在`人物动作与情绪 / 台词 / 音效`落成证据。
FAIL：写"她有些犹豫地说话"这类形容词；把不流畅均匀撒在每个字上读成喜剧节奏；或只改台词文本而不改呼吸与口型。

### R96-D Overlap Names Its Entry And The Listener Reacts Only After The Trigger

输入：男主在女主尾词尚未结束时抢入一句话；台词表把两人句子排成先后两行，听者反应被写成"听到这句话后她崩溃"。
PASS：按`knowledge/performance/dialogue_performance.md`的`## Turn-Taking｜话轮`改写——写明重叠入口（在上一句尾词口型尚未结束时进入）、相对时长与音量关系（起音低于被抢话者，被抢话者不突然静音）；听者反应写成只在听到主触发词后出现的信息延迟；台词仍按闭集编译。
FAIL：用绝对秒数（提前0.1秒、重叠0.2秒）替代关系描述；让被抢话者立刻静音；让听者在关键词之前就反应；或忽略重叠仍是高风险项。
