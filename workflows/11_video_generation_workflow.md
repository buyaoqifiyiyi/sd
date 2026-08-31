# Video Generation Workflow

## Purpose

将已经完成的：

- Confirmed Detailed Shot Design
- Confirmed Clip Production Plan
- Sequence Plan（如适用）
- Character Asset
- Environment Asset
- Prop Asset
- Visual Development
- Camera Language
- Composition Language
- Continuity Information

转换为适合Seedance执行的视频生成信息。


本Workflow只负责：

STATE-08 Clip-based Video Prompt / Video Generation。


本Workflow负责：

理解上游镜头。

整理执行信息。

补充时间过程。

补充摄影机行为。

补充人物表演。

补充声音逻辑。

补充剪辑连接。

检查连续性。

完成Seedance适配。

把最终内容交给Video Prompt Template格式化。


本Workflow不负责：

定义最终输出字段名称。

定义最终镜头编号。

把时间码、逐镜时长或按秒动作区间写入最终Prompt；唯一例外是【时长】中的Confirmed Clip平台生成时长（4—15秒）。

定义最终Prompt章节结构。


STATE-08最终输出Schema唯一来源：

templates/10_video_prompt.md


---

# Workflow Boundary

Video Generation是：

生产执行转换阶段。


不是：

重新创作剧情阶段。


不是：

重新设计角色阶段。


不是：

重新设计环境阶段。


不是：

重新进行Clip Production阶段。


不是：

重新进行Shot Design阶段。


进入本Workflow后：

原则上不得改变已经确认的：

剧情事实。

人物身份。

人物关系。

资产设定。

场景。

镜头核心目的。


如果用户明确要求修改：

先判断修改属于：

当前视频执行问题

还是

上游设计问题。


如果属于上游设计问题：

返回对应阶段处理。


---

# STATE-08 Front-Lock Rules

以下规则只约束STATE-08 Prompt编译与最终Template Mapping，不修改主Pipeline、Director Decision Layer、Knowledge Application Reflection、Camera Knowledge、Clip Production或Asset System。

在执行任何Front-Lock、Reference Budget、Knowledge Reflection或Prompt措辞前，必须读取`knowledge/clip_preflight_check.md`并完成STATE-08最终版。先把当前Clip分类为`视觉连续`、`剧情连续`或`主动切场 / 切世界`，再按逐分镜World-State检查角色数量、空间构图、关键道具、适用转场五要素和参考资产资格；其中每个视觉候选必须先通过“这是不是一张实际会被投喂/引用的视觉资产？”检查。只有全部为PASS才可继续；FAIL时先修正Clip设计或按Return Route返回，不得用Prompt润色掩盖。

## Front-Lock Rule

每个Clip Prompt Package在任何风格、人物一致性、环境一致性、音色或分镜描述之前，必须先完成`templates/10_video_prompt.md`定义的全部前置锁定信息，并严格使用该Template的字段、顺序、编号与排版。本Workflow不复制最终骨架。

Voice/Audio Reference不得导致Template中的任何无条件字段被删除；Reference Override时在Template指定位置写明声音身份由Reference锁定且不得文字重定义。每个分镜完整重复Template当前定义的全部分镜字段，不得另增竞争字段；相关边界语义映射到Template指定的结尾状态位置。

参考资产、首帧与尾帧限制等前置锁定语义必须位于Template指定位置，不得降级为备注，也不得由后续文字描述覆盖。

【参考资产】先读取`references/asset_lock_contract.md`，优先引用Asset Registry中Active Version与Canonical References。上一Clip尾帧只能锁定已确认的状态、构图、空间与动作边界，不能覆盖Confirmed Asset的角色身份、服装身份、环境结构、道具结构或Active Version。后续【主风格】【人物一致性】【环境一致性】和逐镜文字只能补充允许变化与执行过程，不得重设前置资产。

视觉条目只允许实际会向模型投喂/引用的已确认视觉文件或受控ID，以及明确需要用户实际补入、写明具体图像对象、投喂用途和`待用户补充/待上传、未确认`状态的视觉图占位。纯文字站位、不可换边、人物距离、同坐一张板凳、道具数量、空间关系、行为约束、禁止项和镜头规则不得成为条目；按语义迁移到现有`空间关系 / 起始状态 / 道具状态 / 首帧参考 / 尾帧限制 / 反向提示词 / Spatial Blocking Rules`。若对象已有真实视觉资产则引用正式ID，例如`PROP-BENCH-01｜双人钢琴凳`；不得使用“板凳参考说明”之类伪资产。既有Voice/Audio Reference继续按独立声音输入合同处理，不受本视觉资格补强改名或删除。

通过资格检查后仍不得全选。必须读取STATE-07的`Clip End-State Record / Next-Clip Carryover`与`Continuity Risks`，按当前Clip生成目标执行Reference Selection / Routing：身份/外观风险选Active Character Canonical References；空间结构风险选Active Environment Canonical References并把Confirmed Spatial Blocking作为文字语义消费；道具造型风险选Active Prop Canonical References；A/B状态锚定选对应`REF-TAIL`并区分用途，C不选旧尾帧；光线、天气或场景状态漂移只有存在真实、已确认且合格的场景视觉基准或合法参考帧时才选图，否则写入现有文字字段。每个入选条目必须对应一项具体风险/目标；Eligible、Registry存在、上一Clip使用过或仍有预算空位都不是充分理由。参考资产按需路由，不是越多越好。

同时必须读取`knowledge/reference_budget.md`并按实际图片文件/帧执行单Clip预算。默认保留原始独立资产，不默认整合：Projected Final Count≤7不整合；8张且无额外帧需求不整合；9张仅在没有尚未计入的连续性图片需求时允许；当前9张且仍需上一Clip尾帧/当前首帧时按10张处理并至少释放1位；>9张必须去重、整合同类非角色信息、仍超限再按优先级裁剪，最终≤9。每个核心角色保留各自独立三视图/角色锁定图，动作/互动图不得替代外貌基准。

## Previous-Clip Continuity Decision Rule

从G02开始，每个Clip在编译【参考资产】与【首帧参考】之前，必须先成对比较`Previous Clip End State → Current Clip Start Requirement`，至少检查：

- 是否同一场景、同一连续时间与同一动作链
- 人物位置、左右关系、身体朝向、视线、距离、情绪与动作阶段
- 摄影机边界、关系轴、道具、环境、光线、综合色彩与持续声音
- 上一Clip已经完成的动作是否会被重播，下一Clip动作是否被提前

先从`视觉连续 / Visual Continuity`、`剧情连续 / Narrative Continuity Only`、`主动切场 / 切世界 / Motivated Scene-or-World Change`中选择一个主分类，再把尾帧使用方式映射为A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】。A/B均标记`Tail Frame Required = YES`，C标记`NO`；需求判定必须先于资产可用性检查，不得因为系统当前没有尾帧图而改变A/B/C。

判定结果只允许以下三类Handoff：

1. `A｜Direct Start-Frame Handoff｜同镜头连续承接`：上一Clip最后一个镜头在当前Clip继续，目标接近一镜到底，必须从上一尾帧的同一空间、动作阶段、构图与镜头几何直接开始。标记`Tail Frame Required = YES`；【参考资产】列`REF-TAIL-XX｜CLIP-XX尾帧参考（同镜头连续承接用途）`；【首帧参考】逐字写`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`并锁定姿态、位置、朝向、距离、动作阶段、构图、景别、机位、环境、光线、天气、道具、情绪与持续声音。
2. `B｜Reference-Only Handoff｜新镜头参考型`：当前Clip另起新镜头重新构图，但仍需上一尾帧精确锁定人物站位、朝向、人物距离、景别衔接、空间关系、道具状态或起始构图。标记`Tail Frame Required = YES`；【参考资产】列`REF-TAIL-XX｜CLIP-XX尾帧参考（用于延续上一镜头结尾的角色站位、朝向、景别与空间关系；空间/站位/景别参考用途）`；【首帧参考】说明参考该尾帧延续上述逻辑，但当前Clip另起新镜头重新构图，并明确允许改变的新机位/景别/视角/构图。不得使用A类固定直接承接句，不得误写成同镜头续拍。
3. `C｜Not Required / No Formal Tail Reference｜新镜头且无需尾帧`：当前镜头明确换机位、换景别、反打、特写、俯拍/仰拍或重构图，且不依赖上一尾帧画面状态。标记`Tail Frame Required = NO`；不得要求用户截图，不在【参考资产】列`REF-TAIL`，只依靠Canonical角色/环境/道具资产、Confirmed Spatial Blocking与文字空间规则建立新首帧并核对仍有效状态。

A/B尾帧尚未提供时，仍必须在【参考资产】直接列出统一`REF-TAIL`名称、对应用途与“待用户提供/待上传、未确认”，同时提示用户从上一Clip最终成片截取并在实际生成前添加；不得伪造路径或声称已上传/已确认。该声明占Projected位但不计入已提交图片数，Prompt可以完整编译和交付。任何`REF-TAIL`条目都必须明确用途类型。

无法唯一判定时使用`Unresolved Handoff`并返回上游成对复核，不得把上一尾帧默认塞入【参考资产】。

## First Frame Reference Rule

【首帧参考】是当前Clip对上一Clip尾帧的承接合同，不是泛化的开场画面描述，也不是任意参考图清单。

G02及以后必须依据Previous-Clip Continuity Decision明确选择“直接继承”“仅作连续性参考”或“不作正式参考资产、文字核对/重建”，并在同一内容中标记`Tail Frame Required = YES / NO`。G01没有上一Clip时，明确写“首段，无上一Clip尾帧；Tail Frame Required = NO”，并从已确认Scene初始状态、开场资产或合法首帧建立。

无论采用哪种模式，【首帧参考】都必须把边界落实为可执行首帧：人物姿态、位置与左右关系、身体朝向与视线、人物间距离、摄影机起始位置与轴线侧、景别、主体构图与前中后景、环境、天气、光线、关键道具状态、动作起始阶段和情绪状态。A Direct不得重新摆位或重播动作并使用固定直接承接句；B Reference-Only必须说明有动机的新机位/景别/视角/构图、与上一尾帧兼容的状态和“另起新镜头重新构图”，且不得使用A的固定句；C从Canonical基础资产、Spatial Blocking与文字End State承接或重建且不列`REF-TAIL`。A/B尾帧尚未上传时明确“REF-TAIL-XX｜CLIP-XX尾帧参考：待用户提供/待上传、未确认”，不得把待补充声明冒充现有图片。跨场景模式不得把旧场景空间、构图或光线带入新场景。

## End Frame Constraint Rule

【尾帧限制】属于同一Package的前置生成边界，必须在【主风格】之前先锁定当前Clip新的最终交付帧。实际生成、提取并确认后，按当前Clip编号登记为`REF-TAIL-XX｜CLIP-XX尾帧参考`；生成前不得把计划名称冒充为已存在参考资产。至少描述：

- 人物最终位置、左右关系、身体朝向、视线、表情/情绪与动作停留点
- 摄影机最终位置、轴线侧、景别、焦点、主体构图与稳定状态
- 关键道具持有者、左右手、位置、方向与状态
- 环境、天气、光线、综合色彩、材质/介质与持续声音的最终状态
- 下一Clip对该尾帧的预计用途：直接作为起始帧、仅作连续性参考、不作正式参考资产仅作连续性核对，或最终收束

当前Clip若使用上一Clip尾帧，本字段仍必须定义本Clip自己的新结束状态；不得沿用上一Clip的`REF-TAIL`名称或状态。尾帧参考只锁定构图、姿态、位置和当前状态，不能替代角色、环境、道具Active Canonical资产。

尾帧必须清楚、可冻结、可继承、主体无遮挡且构图稳定。最后1秒不得开启新的复杂动作、对白、转头、起步、抬手、接触、道具换手、运镜阶段、场景变化或剧情事件；只允许自然呼吸、衣物/竹叶/水流等不改变剧情状态的微小持续运动。若必要动作与稳定尾帧无法同时容纳，先减少次要动作或降低运镜复杂度，仍无法执行时返回STATE-06/07。

## First / End Frame Pair Rule

每个Clip必须形成：

`上一Clip结束状态 → 判定A/B/C与用途 → A/B在参考资产声明REF-TAIL（缺图则标待补充）→ 首帧按Direct或Reference-Only分别说明 → 实际生成前补入尾帧 → 当前Clip生成 → 当前Clip尾帧限制定义新结束状态 → 下一Clip重新判定`

当前Clip的首帧、逐镜“起始状态”、逐镜“镜头结尾状态”和Package【尾帧限制】必须描述同一条可复算状态链。禁止首帧后瞬间跳位，禁止无过程换手/换向/换场，禁止尾帧与下一Clip首帧承接判定互相矛盾。

## Front-Lock Final Prompt Validation Gate

Template Mapping后、交付前必须逐Package检查：

- Markdown Clip标题、`时长：`、`画幅：`、`参考资产：`、`首帧参考：`、`尾帧限制：`是否完整，且后三个前置字段严格位于`主风格：`之前
- 【参考资产】中的每个视觉条目是否逐项通过“这是不是一张实际会被投喂/引用的视觉资产？”检查；真实条目是否引用实际Canonical Asset或其他合法视觉文件/受控ID并写明用途/锁定约束；受控待补视觉图是否写明具体图像对象、实际投喂用途与“待用户补充/待上传、未确认”；A/B待补`REF-TAIL`是否使用统一名称、用途与真实状态；且没有被后续临时文字覆盖
- 站位、不可换边、人物距离、同坐一张板凳、道具数量、空间关系、行为、禁止项与镜头规则等纯文字内容是否已从【参考资产】移出并进入正确既有字段；如果存在真实道具图，是否使用正式资产ID而非“参考说明”
- 是否完成Reference Budget Check：当前Clip无关项已删除、重复项已去除、必需连续性帧已计入、最终图片数≤9；只在超限风险触发后整合同类非角色信息；没有虚构总图/空间关系图/动作关系图；每个核心角色仍有独立外貌基准
- G02及以后是否明确A/B/C并据此标记`Tail Frame Required = YES / NO`；A/B无图时是否在【参考资产】直接列统一`REF-TAIL`、对应用途与“待用户提供/待上传、未确认”，且未声称上传/确认；C是否未列`REF-TAIL`、未要求截图
- 【首帧参考】是否明确A Direct、B Reference-Only或C Not Required；A是否包含固定直接承接句并完整锁定；B是否说明另起新镜头重新构图、保持项和允许变化且未使用该句；C是否写明Canonical资产、Spatial Blocking与文字重建依据
- 【尾帧限制】是否定义当前Clip新的结束状态，包含人物/摄影机/道具/环境最终状态，稳定可冻结，并禁止最后1秒开启新复杂动作；只有实际生成、提取并确认后才登记当前`REF-TAIL-XX｜CLIP-XX尾帧参考`
- Previous Clip End State与Next Clip First Frame Reference是否形成合法连续链或明确断点

若参考资产位于Prompt末尾或【主风格】之后、【首帧参考】缺失、【尾帧限制】缺失、上一尾帧引用模式未判定、跨场景仍把旧尾帧作为正式生成参考，均判定失败。失败时只重排或补齐受影响的前置字段与相邻边界，重新执行Template Mapping和验证后再输出；不得无必要改写分镜内容或返回重做整个Pipeline。


---

# Required Inputs

进入STATE-08前：

优先读取以下信息。

## Confirmed Clip Production Plan

必须读取由`workflows/10_clip_production_workflow.md`与`templates/20_clip_plan.md`生成的Confirmed Clip Production Plan，并以CLIP-001、CLIP-002……作为Prompt编译顺序和最小生成单位。缺失、Planning或验证失败时不得继续。一个Clip即使包含多个Shot，也只编译一条连续Seedance Prompt；不得按Shot拆成多条Prompt。


## Director Decision Notes

必须读取STATE-06为当前Clip所覆盖Scene / Shot Group生成的当前有效`Director Decision Notes`。Notes负责锁定为什么这样拍、Audience Know / Feel / Wait、人物关系与Blocking、镜头总体动/停、功能性色光、表演尺度、声音加强/留白、节奏高潮/余韵、连续性风险和Seedance降级方向。

Notes是内部决策输入，不是最终Prompt栏目。缺失、与Confirmed Detailed Shot Design / Clip Production Plan冲突，或无法明确映射当前Clip时，不得由Knowledge Reflection自由选择方向；返回STATE-06或STATE-07完成最小修订。


## Detailed Shot Design

读取：

镜头目的。

Camera Language Decision（镜头目的、情绪功能、空间功能、人物运动、节奏阶段、推荐主运镜、可选辅助、禁止运镜、Seedance稳定等级、选择理由与原子知识证据）。

景别。

机位。

焦段。

摄影机运动。

人物位置。

人物动作。

情绪功能。

镜头节奏。


Shot Design中的字段：

属于上游生产信息。


不得直接复制为最终Seedance输出格式。


---

## Sequence Plan

项目存在Sequence Plan时读取：

- SEQ ID与Scene Scope
- BEAT顺序
- Required COV与Completion Evidence
- UNIT顺序、Entry Anchor、Exit Anchor与Retry Boundary
- State Ledger与未决风险


Sequence Plan用于检查覆盖完整性和跨生成单元继承。


它不得直接成为最终Prompt栏目，不得用UNIT替代分镜编号，也不得把UNIT或逐镜时长带入最终Prompt；只允许采用Confirmed Clip Production Plan的4—15秒平台生成时长。


---

## Clip Production Semantics

从Confirmed Clip Production Plan及其来源Detailed Shot Design读取执行数据：

Clip Movement Plan，包括主导镜头语言、镜头间运镜变化、视觉高潮镜头、最克制镜头、重复规避与Seedance复杂度控制。

当前Clip对应的Director Decision Notes，以及STATE-07从中综合的主导镜头语言、节奏、调度、视觉高潮/留白、功能性色光与声音方向。

人物空间关系。

构图与空间关系。

视觉重点。

镜头开始状态。

镜头结束状态。

`Clip End-State Record / Next-Clip Carryover`八组语义：Character / Spatial / Prop / Camera / Environment / Performance / Continuity Risks / Next-Clip Carryover；该记录只用于连续性消费，不得变成STATE-08新增字段。

镜头连接类型。

下一镜头衔接意图。

人物面对方向。

重要道具状态。


Clip Production Plan用于：

确认镜头执行逻辑与边界。


不得：

读取、描述或引用Storyboard图片、线稿、分镜板、漫画格、接触表、拼图或任何多画面材料。


【参考资产】只允许使用Canonical Character / Environment / Prop / FX Assets、Voice/Audio Reference、合法首尾帧，以及其他已经明确需要实际投喂的视觉参考图；缺失视觉图只有在写明具体图像对象、实际投喂用途和“待用户补充/待上传、未确认”时才可作受控占位，且不得代替正式Canonical资产的STATE-03确认流程。A/B必需但尚待用户补充的`REF-TAIL`继续以统一名称直接列入并分别标明“同镜头连续承接用途”或“空间/站位/景别参考用途”；未提供时写“待用户提供/待上传、未确认”，不得伪造路径或声称已上传/已确认，Prompt可交付但实际提交生成前补图。C不要求截图、不列`REF-TAIL`，可在【首帧参考】与首镜“起始状态”依靠Canonical资产、Spatial Blocking与文字状态承接或重建。不得使用纯文字参考说明、Storyboard、Detailed Shot Design或Clip Plan截图/渲染图。


---

## Character Asset

读取：

Character Asset ID。

角色身份。

年龄。

脸型。

五官。

发型。

发色。

服装。

身体比例。

角色气质。

当前状态。

Voice Asset Status。

Confirmed Voice Profile及其最终可直接引用的音色描述（适用时）。

Voice Audio Reference Status、Reference ID/受控路径、绑定CHAR Version、授权状态，以及目标模型是否实际使用Audio/Voice Reference。


已有角色资产：

优先级高于临时文字描述。

主要角色或重要配角有对白、旁白、画外音、通话或呼喊时，先执行Voice Reference Override Gate。用户已明确提供当前角色音色参考资产，或目标模型实际使用Active CHAR Version中的Confirmed Voice Audio Reference / Audio Reference / Voice Reference时，Reference是声音身份的唯一锁定来源：STATE-08仍必须保留`音色特征：`，其内容写明声音身份由Reference锁定且不得文字重定义；不得把Confirmed Voice Profile中的音高、声线、音域、共鸣、语速、音色质感写入台词、音效或其他字段。没有适用Reference但已经存在Confirmed Voice Profile时，才把它作为`音色特征：`的文字回退来源；两者都不存在时使用`No Voice Asset`分支，声明未建立独立音色资产且本Clip不创建或推导声音身份，不得自动调用AUDIO模块或返回STATE-03。全段无对白时也保留字段并明确无对白。


---

## Environment Asset

读取：

Environment Asset ID。

地点。

时间。

天气。

空间结构。

道路方向。

建筑位置。

主要灯源。

背景元素。

环境综合色彩。


---

## Prop Asset

存在关键道具时：

读取：

Prop Asset ID。

外观。

持有者。

左右手。

位置。

方向。

状态。


---

## FX Asset

存在正式FX或Inline Effect时读取：

FX Asset ID或Inline Effect标记。

触发与来源。

效果阶段。

运动方向、尺度与强度。

对角色、环境、道具、光线和声音的影响。

结束状态与残留后果。


---

## Visual Development

读取：

综合色彩。

摄影倾向。

光影。

曝光。

景深。

画面质感。

视觉氛围。

导演视觉语言转换结果。

综合色彩必须进一步读取：主/辅/强调色及来源、综合色相结构、饱和度层级、明度/黑位/高光、白平衡/综合色温和偏色、肤色/中性色保护、材质响应与允许变化范围。


---

## Camera Language

根据：

镜头目的。

人物情绪。

空间关系。

动作。

节奏。


选择已经建立的Camera Language知识。


禁止：

为了“电影感”随机加入复杂运镜。


构图、导演模式或情绪镜头名称不得直接作为最终执行描述。


必须拆解为：

- 主体画面位置与景别
- 摄影机位置、角度、焦段和唯一主要运动
- 多运动候选的一镜/多镜分类；若为复合路径，只保留一次同向、有动机、同轴、同平台的延续
- 前景、中景、背景、负空间、内框、遮挡、反射或引导线的真实来源
- 人物左右、视线、距离、路线与轴线
- 构图在动作过程中的变化和稳定终点


---

# Required Resources

执行本Workflow时：

必须使用：

knowledge/quality/shot_qa.md

knowledge/quality/continuity_pair_qa.md

knowledge/quality/execution_risk.md

knowledge/quality/prompt_scorecard.md

用于生成前风险检查、相邻镜验证和Template完成后的内部评分。QA结果不得进入STATE-08最终Schema。

必须使用：

knowledge/11_seedance_adapter.md


用于：

Seedance模型执行适配。


必须使用：

knowledge/director_decision_layer.md


用于：

在Knowledge Application Reflection之前读取并锁定当前Clip的导演意图；它决定“为什么这样拍、观众如何经历、人物关系如何表达”，不选择Knowledge实现策略，也不创建最终字段。


必须使用：

knowledge/knowledge_application_reflection.md


用于：

在读取Confirmed Clip Production Plan与对应Director Decision Notes后、撰写每个Clip最终Prompt之前，执行Knowledge Opportunity Check，筛选1—3项最有价值的实现策略，并把所选知识转译为可执行语义；它不得反向重定义导演意图，该过程默认不向用户输出。


必须使用：

knowledge/prompt_compilation/state08_projection.md


用于：

确认所有Applicable Knowledge已被语义投影到现有Template字段，且没有创建竞争Schema。

必须使用：

knowledge/clip_preflight_check.md

用于：

在Reference Budget和正式Prompt编译前执行STATE-08最终版：区分视觉连续、剧情连续与主动切场 / 切世界；逐分镜锁定World-State、角色精确数量、空间构图、关键道具状态及适用转场五要素；只有PASS才能继续。Preflight结果只进入STATE-07既有计划记录与STATE-08内部Projection / QA，不新增最终字段。

必须使用：

knowledge/reference_budget.md

用于：

在STATE-07预算审计基础上，按STATE-08实际引用文件/帧复核当前Clip最终图片参考数量、资产真实性、重复占位、条件性非角色整合与核心角色独立图硬门槛；预算结果只进入既有`参考资产：`和内部Projection Ledger，不新增最终字段。

必须使用：

knowledge/clip_planning/continuity_and_projection.md

用于核对Clip内逐镜状态链、跨Clip尾帧链和Learned Knowledge到Prompt字段的投影。

必须使用：

knowledge/camera_language/camera_movement/selection_matrix.md

knowledge/camera_language/camera_movement/index.md

以及每个SHOT已确认主运镜对应的原子知识文件；辅助项构成真实物理运镜时也必须读取对应原子文件。

用于核对Camera Language Decision、Clip Movement Plan、运镜叙事功能、稳定等级与基础降级，并把知识转译为可执行摄影描述。只读取索引或沿用通用慢推/横移措辞不算完成本Resource Gate。


必须使用：

templates/10_video_prompt.md


用于：

最终Prompt格式化。


如果当前任务使用首帧、尾帧或图生视频参考：

还必须读取：

templates/11_image_to_video_prompt.md


它只负责整理参考帧Source Data与运动边界。


最终Seedance Schema仍由templates/10_video_prompt.md唯一拥有。


如当前镜头需要：

可调用：

knowledge/camera_language/

所有焦段选择还必须按需读取`knowledge/camera_language/lens_language/focal_length_and_perspective.md`；连续镜头读取`focal_length_continuity.md`。焦段不新增最终字段。


如项目存在已确认视觉风格：

可调用：

knowledge/visual_styles/


人物表演镜头按需调用：

knowledge/performance/


存在对白、环境声、动作声、静默或同期声音衔接时按需调用：

knowledge/sound_language/


存在正式FX或复杂Inline Effect时按需调用：

knowledge/fx/


存在Sequence Plan时按需调用：

knowledge/sequence/


存在综合色彩、调色、综合色温/偏色、饱和度、暗调、霓虹、糖果或清透自然色设计时按需调用：

knowledge/color/


分镜表包含两个及以上分镜、已知下一镜或存在场景/时间切换时必须调用：

knowledge/transitions/


---

# Responsibility Separation

执行时必须保持模块职责分离。


## Workflow

负责：

怎么转换。


## Seedance Adapter

负责：

怎样让视频模型更容易执行。


## Camera Language Knowledge

负责：

怎样使用镜头语言。

当候选设计包含两种以上运动、镜头顺序、多个景别/视点或一镜到底时，读取`knowledge/camera_language/movement_combinations/`，负责判断一镜路径、Coverage拆分、Transition / FX边界与稳定降级；不新增最终字段。

内部分类统一为Single-Move、Low-Complexity Compound Path、Coverage Sequence或Transition / FX Sequence，最终Prompt只保留执行语义。


## Visual Style Knowledge

负责：

怎样把视觉美学转化为摄影语言。


## Color Knowledge

负责：

把已确认资产、光源和材质综合色彩组织为可执行的色相层级、饱和度、明度/对比、白平衡/偏色、肤色保护和跨镜色态；不新增光源或改写资产固有色。


## Performance Knowledge

负责：

把情绪、对白意图和人物关系转换为可观察的表演节拍。


## Sound Language Knowledge

负责：

建立对白、空间声、动作声、静默与跨镜同期声音连续性。背景音乐、配乐、BGM、主题音乐与氛围音乐永久不能进入STATE-08的“音效”或其他字段；用户的音乐要求只能分流至独立MUSIC / SEED-MUSIC模块。

## Transition Knowledge

负责：

先判定Boundary Class，再自动选择一种主要转场技术，建立出镜锚点、切点、入镜锚点与Direct Cut降级；不得改写剧情或新增FX。


## FX Knowledge

负责：

建立效果生命周期、物理交互与跨镜后果。


## Sequence Knowledge

负责：

检查Required Coverage、Generation Unit顺序、重试边界与跨单元State Ledger。


## Template

负责：

最终输出长什么样。


禁止：

Workflow重新创建一套Final Output Schema。


---

# Execution Pipeline

STATE-08执行顺序：

Read Project State

↓

Load Confirmed Assets

↓

Read Sequence Plan If Applicable

↓

Read Detailed Shot Design

↓

Read Confirmed Clip Production Plan

↓

Run Final Clip Preflight Check

↓

Read Director Decision Notes

↓

Lock Director Direction For Current Clip

↓

Run Knowledge Opportunity Check

↓

Select The 1—3 Highest-value Knowledge Strategies

↓

Check Continuity / Complexity / Seedance Stability

↓

Translate Strategies Into Concrete Prompt Language

↓

Verify Camera Language Decision And Clip Movement Plan

↓

Analyze Shot Purpose

↓

Normalize Upstream Information

↓

Build Shot Execution Logic

↓

Design Time Process

↓

Design Camera Execution

↓

Design Color Execution

↓

Design Performance

↓

Design Sound Logic

↓

Design Editing Logic

↓

Apply Seedance Adaptation

↓

Apply Semantic Projection

↓

Run Reference Budget Check

↓

Check Continuity

↓

Prepare Template Data

↓

Apply templates/10_video_prompt.md

↓

Final Validation

↓

Output


其中不可反转的核心编译顺序为：

`Clip Production Result → Director Decision Notes → Knowledge Application Reflection → Seedance Prompt`

Director Decision先决定方向；Knowledge Reflection只从已读取知识中选择1—3个最适合的实现策略。不得先浏览“有哪些技巧”，再用技巧反向主导剧情、人物关系或观众体验。


---

# Step 01

# Read Project State

首先由`references/project_workspace.md`解析项目候选，按`rules/state_source.md`选择并读取唯一State Source，再按`references/project_state_contract.md`验证字段。本Workflow不复制Chat fallback、初始化或Project ID冲突规则；历史聊天中的Skill描述或未验证摘要不得证明项目已经到达STATE-08。


确认：

当前项目。

当前STATE。

已经完成的Workflow。

已确认资产。

当前Visual Style。

已完成Detailed Shot Design。

已完成Clip Production。


如果项目状态尚未达到：

STATE-08


不得假设前置阶段已经完成。


按照Pipeline处理缺失阶段。


---

# Step 02

# Load Confirmed Assets

读取：

asset_registry.md

project_bible.md


确认当前镜头需要使用的：

Character Asset。

Voice Profile（角色有对白或潜在对白需求时）。

Environment Asset。

Prop Asset。


资产优先级：

Confirmed Asset

>

Project Bible

>

Approved Stage Output

>

Current Temporary Description


禁止：

在Video Generation阶段无原因重设计资产。


---

# Step 03

# Read Detailed Shot Design

读取STATE-06已经确认的镜头设计。


存在Sequence Plan时先确认：

- 每个Required COV至少映射到一个SHOT
- 每个SHOT的COV映射与Sequence Plan一致
- 正式SHOT没有被UNIT ID替代
- UNIT顺序没有被STATE-06无原因改变


提取：

镜头功能。

Camera Language Decision全部已确认项与实际读取的原子知识证据。

人物。

场景。

动作。

景别。

焦段。

机位。

摄影机运动。

节奏。

情绪。

空间关系。


注意：

这些属于：

SOURCE DATA。


不是：

FINAL FORMAT。


Camera Language Decision Hard Gate：

- 每个正式SHOT必须具有镜头目的、情绪功能、空间功能、人物运动、节奏阶段、推荐主运镜/Static、可选辅助、禁止运镜、Seedance稳定等级、选择理由与原子知识文件证据。
- 必须实际读取`selection_matrix.md`、Camera Movement Index与被选主运镜原子文件。
- 任一SHOT缺失上述决策时，不得在STATE-08自行补一个“缓慢推进/轻微横移”；返回STATE-06完成Camera Language Decision。


---

# Step 04

# Read Confirmed Clip Production Plan

读取STATE-07 Confirmed Clip Production Plan，并同时读取其来源STATE-06 Detailed Shot Design；禁止读取或引用视觉Storyboard材料。

逐Clip读取其Reference Budget Audit，并在上一Clip尾帧用途判定后重新计算Projected Final Count。STATE-07未记录预算审计、审计使用不存在/未确认资产、核心角色独立图缺失或计划最终图片数>9时，返回STATE-07补齐；需要新建非角色总图时返回对应STATE-03资产Workflow完成确认闭环，不能在STATE-08虚构资产。

随后读取当前Clip所覆盖Scene / Shot Group的`Director Decision Notes`。必须先确认：

- Narrative Objective与Audience Know / Feel / Wait能够明确映射当前Clip
- 人物关系、Blocking、距离、视线、站位和动作变化没有被Clip合并抹平
- Camera总体动/停理由、Composition、Lens / Distance、功能性色光、表演尺度、Sound与Editing / Rhythm方向清楚
- 视觉高潮与最克制/留白位置和Clip Movement Plan一致
- Continuity Risk与Seedance Feasibility / Safe Downgrade已被STATE-07保留

Director Decision Notes Hard Gate：

- 缺失或未覆盖当前Clip：返回STATE-06生成/补齐Notes。
- Notes与Confirmed Detailed Shot Design事实或技术设计冲突：返回STATE-06只修Affected SHOT及相邻边界。
- Notes与Clip边界、主导逻辑、高潮/留白或复杂度编排冲突：返回STATE-07最小调整。
- STATE-08不得用Knowledge Opportunity Check重新决定叙事目标、观众体验、人物关系或总体视听方向。


重点判断：

人物在哪里。

人物朝向哪里。

人物看向哪里。

摄影机位于哪里。

关键道具在哪里。

镜头开始状态。

镜头结束状态。


Clip Production Plan优先帮助解决：

空间。

构图。

位置。

动作。


必须转换为视频过程中可执行、可连续检查的变化，不得把该计划截图后作为视觉参考。


同时读取STATE-06/07已经记录的：

- Transition Class
- Start Boundary
- End-Frame Constraint
- Next-Shot Handoff
- 每个SHOT的Camera Language Decision
- 每个Clip的Clip Movement Plan：主导镜头语言、逐镜运镜变化、视觉高潮镜头、最克制镜头、重复规避、Seedance复杂度控制


如果这些上游边界信息缺失：

只能依据已确认镜头与剧情补齐可验证内容。


不得为了形成连续性而改写剧情、资产、人物站位逻辑或道具状态。


若前后镜头存在无法消解的事实矛盾：

标记为Unresolved Handoff，并返回对应上游阶段修正。


Clip Movement Plan Hard Gate：

- 每个Confirmed Clip必须具有明确主导镜头语言逻辑与逐镜变化链。
- 超过4个Shot时通常至少包含2种不同运镜逻辑；例外必须具有已确认叙事理由。
- 同类主运镜连续3次以上必须有逐镜叙事理由。
- 缺失、与STATE-06决策冲突或复杂度控制不可执行时返回STATE-07；STATE-08不得静默重编排。


## Step 04A｜Final Clip Preflight Check

在分析镜头目的、运行Knowledge Reflection或撰写任何最终Prompt句子前，逐Clip读取STATE-07 Preflight记录，并按实际资产、实际首尾帧与Confirmed Clip Production Plan重跑`knowledge/clip_preflight_check.md`最终版：

1. **Continuity Classification / Tail Frame Requirement**：三选一锁定`视觉连续 / 剧情连续 / 主动切场或切世界`，再明确A【同镜头连续承接】、B【新镜头参考型】或C【新镜头且无需尾帧】。A/B标记`Tail Frame Required = YES`并在【参考资产】列统一`REF-TAIL`、对应用途与真实状态；未提供时写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。C标记`NO`，不列`REF-TAIL`，从Canonical资产、Spatial Blocking、文字End State或当前Scene / World-State / Start Boundary承接或重建。
2. **World-State Check**：逐分镜确认现实、幻想、耳中玉境或其他已确认层，以及Pre/Post Transition阶段。删除未出场、未使用及当前阶段不适用资产。完全在耳中玉境的Clip不得引用现实标准耳勺；只有转换Clip可按阶段使用现实与武器化两种状态。
3. **Character Count Lock**：逐分镜核对`角色 × 精确数量`。唯一角色必须在正向Prompt目标中明确唯一一只/名、前中后景无第二个同类，并准备复制、分身、镜像、背景第二只/名、相似替身的反向限制。
4. **Spatial Composition Lock**：追逐/战斗/对峙/多人镜头逐项核对前后景、左右、朝向、运动轴、摄影机轴线侧、正脸许可与同景深许可。追逐默认后追前逃，禁止双方并排正对镜头、海报式合影和群像站桩。
5. **Prop State Check**：每个关键道具核对当前形态、尺寸、持有者/左右手、位置、方向、是否允许悬浮、转换完成状态与下一镜继承；现实/幻想形态不得跨世界混用或无过程转换。
6. **Transition Check**：现实↔幻想/耳中玉境、地点/时间跳跃、尺度或角色/道具形态变化，必须已有起点状态、转换媒介、运动方向/过程、终点状态和转场后首个稳定构图；缺一不得以“金光一闪 / 突然切换”补写。
7. **Reference Asset Eligibility / Selection / Budget**：前六项通过后才筛选并计数。每个视觉候选先回答“这是不是一张实际会被投喂/引用的视觉资产？”；答案为否的站位、换边、距离、共坐、数量、空间、行为、禁止项或镜头文字规则从【参考资产】删除并迁移到对应既有字段。答案为是的真实资产必须可回查文件/受控ID；待补视觉图必须写具体图像对象、实际投喂用途与`待用户补充/待上传、未确认`，不得绕过正式Canonical资产确认。再依据`Clip End-State Record / Next-Clip Carryover`、当前目标和Continuity Risks逐项路由：身份/外观→Character Canonical；空间结构→Environment Canonical + Spatial Blocking文字语义；道具造型→Prop Canonical；A/B状态锚定→对应用途`REF-TAIL`；C→不选旧尾帧；光线/场景状态→只选实际已确认合格的视觉基准或合法帧，否则写入文字字段。记录每个入选条目解决的风险和Eligible但未选项的理由；漏选、选错或无依据过量引用均FAIL。之后只保留当前World-State实际存在/出场/使用项，核心角色独立图优先，最终≤9，只有超限风险时整合非角色信息。

结果为FAIL时，不得继续Step 05或Template Mapping；按模块Return Route做最小修正并从第1项重跑。结果为PASS时，内部记录Evidence Present，并把通过语义映射到既有Template字段，不输出Preflight标题或检查表。


---

# Step 05

# Analyze Shot Purpose

每个镜头必须判断：

为什么存在。

本步骤只验证逐镜功能是否服务当前Clip的Director Decision Notes，不重新决定Scene / Shot Group的主叙事目的、Audience Experience或人物关系方向。


常见镜头功能包括：

环境建立。

人物进入。

信息发现。

人物反应。

关系建立。

关系变化。

动作推进。

情绪确认。

情绪高潮。

动作结果。

环境余韵。

结尾。


如果无法回答：

“这个镜头推动了什么？”


说明：

镜头可能存在冗余。


不得：

只因为镜头看起来漂亮就保留。


---

# Step 06

# Normalize Upstream Information

这是STATE-08的重要转换步骤。


上游可能包含：

景别。

焦段。

运镜。

速度。

光影。

色调。

情绪。

动作节奏。

人物状态。

镜头描述。


这些信息必须：

保留语义。


但不得：

保留上游格式。


执行原则：

Preserve Information.

Do Not Preserve Input Format.


即：

保留内容。

重新组织信息。


最终如何命名字段：

由：

templates/10_video_prompt.md


决定。


本步骤必须读取并应用：

knowledge/prompt_compilation/state08_projection.md


先逐Clip、再逐镜建立内部Applicable Knowledge Set，判断资产、Camera、Composition、Movement Combination、Focal Length、Lighting、Color、Performance、Sound、FX、Sequence、Transition与连续性中哪些模块实际适用。Lighting适用时必须读取knowledge/lighting/index.md并保留可执行语义，不把内部模式ID变成最终字段；人物表情适用时读取knowledge/performance/，把情绪名称拆成注意、面部/身体动作、控制/泄漏、行动选择与稳定状态，不输出PEX/AU编号。Clip表的Knowledge Projection Ledger必须逐项落入Template现有字段。


禁止为了让每个模块“看起来被使用”而增加不存在的内容；但任何已确认且适用的模块都不得在Template Mapping时丢失。


## Knowledge Application Reflection Layer

读取Clip Production Result与当前Clip对应Director Decision Notes后、继续字段组织或撰写任何最终Prompt语句之前，必须逐Clip调用`knowledge/knowledge_application_reflection.md`。强制顺序为：`Clip Production Result → Director Decision Notes → Knowledge Opportunity Check → 筛选最有价值的1—3个知识策略 → 检查连续性 / 复杂度 / Seedance稳定性 → 转译为具体提示词语言 → 生成最终Clip Prompt`。

1. 从Director Decision Notes读取并锁定当前Clip唯一主叙事目标、Audience Know / Feel / Wait、人物关系与总体视听方向；不得在Reflection中重新发明或替换目标。
2. 执行Knowledge Opportunity Check，至少扫描Camera Language、Composition、Color / Tone、Lighting、Performance、Sound、Editing Rhythm、Director Style、Continuity与Seedance Stability。
3. 选择1—3项对当前Clip增益最高、彼此兼容的候选；不是所有Knowledge都必须使用，禁止为了凑数而知识堆砌。若增加技巧没有收益，允许把保持静止、少动、单一路径或不增加额外色彩变化作为有明确价值的克制策略。
4. 检查所选候选是否会造成炫技、重复、复杂度过高、资产/风格漂移、轴线/边界破坏、连续性冲突或Seedance执行不稳；不通过即Reject或降级。
5. 把所选策略转译成摄影机起点/路径/触发/终点、构图空间来源与前中后景关系、综合色彩来源与层级、光源与受光、可见表演节拍、具体声源与尾部、节奏/切点/继承或稳定降级等可执行描述，再映射到Template现有字段。

STATE-07的Knowledge Opportunity Notes只能作为线索，不能替代本步骤的重新判断；Director Decision Notes则是不可被候选Knowledge反向改写的方向约束。最终Prompt禁止只写“使用Side Tracking”“使用某导演风格”“压迫构图”“电影感光线”等知识名称或抽象标签；必须写出模型能观察、执行和验证的具体行为。

禁止只根据剧情平铺直叙生成Prompt。禁止在没有当前Clip叙事理由与上游决策依据时，默认退化为“缓慢推进 + 轻微横移 + 低饱和冷暖对比”的单一安全写法。必须逐Clip判断色调、运镜、构图、表演、声音与剪辑节奏中哪些维度能真正服务当前段落；最合适的导演决策也可以是克制、静止、简单、少动，但必须把这种克制写成可执行的空间、表演、声音与稳定结尾约束。

Reflection Record只进入内部执行上下文或既有Projection / QA记录，不成为Template Data。除非用户明确要求查看，否则不得输出Opportunity Check、候选、拒绝理由、选择表或内部分析过程。


---

# Step 07

# Build Shot Execution Logic

把每个静态镜头设计：

转换成时间中的视频事件。


必须理解：

镜头开始时：

人物和摄影机是什么状态。


↓

镜头过程中：

发生什么变化。


↓

镜头结束时：

人物、道具、摄影机停在哪里。


每个镜头都应该具备：

Start State

↓

Change

↓

End State


并且必须额外建立：

Boundary Source

↓

End-Frame Constraint

↓

Next-Shot Handoff


这些是Workflow内部执行语义。


最终字段名称仍由templates/10_video_prompt.md决定。


例如：

Shot Design：

人物发现对方。


Video Execution：

人物原本正常前行。

↓

视线捕捉远处人物。

↓

脚步逐渐变慢。

↓

人物停下。

↓

视线固定在对方身上。


禁止：

只使用：

“发现对方。”


---

# Step 08

# Clip And Shot Quantity Check


本步骤必须沿用Confirmed Clip Production Plan的4—15秒目标时长，并只把每个Clip的单一平台生成时长写入对应【时长】；不得写逐镜时长或时间码。

本步骤核对正式分镜数量与Clip覆盖关系，不在STATE-08重新分组。进入Template Mapping后执行：一个Confirmed Clip = 一个独立G生成段Prompt Package；每个Package包含Clip表指定的全部相邻分镜。无论剧本是一分钟还是更长，都不得绕过Clip表把整张分镜压缩成一条Prompt。

优先尊重：

STATE-06已经确认的镜头设计。


存在Sequence Plan时同时尊重Required COV和UNIT边界。


减少镜头不得导致Required Coverage丢失；增加镜头不得引入未确认剧情。


不得：

进入STATE-08后无原因重新拆大量镜头。


但如果发现：

单镜头存在模型无法稳定执行的动作密度。


允许：

提出执行性拆分。


参考：

5秒以内：

通常1-3个简单视觉事件。


5-15秒：

根据动作复杂度合理安排。


15-30秒：

允许多个连续镜头。


30秒以上：

按照完整剪辑逻辑处理。


重点不是：

镜头越多越专业。


重点是：

每个镜头能够稳定执行。


---

# Step 09

# Internal Timing And Density Planning


本步骤只进行内部检查。


Confirmed Clip的4—15秒平台生成时长必须进入【时长】。总片时长、单分镜时长、时间码、逐秒动作区间、帧率或帧数不得进入Template Data或最终Prompt。

如果：

Detailed Shot Design与Confirmed Clip Production Plan已经提供时长。


优先使用已有时长。


如果：

用户提供了视频总时长。


检查：

所有镜头时间总和。


需要保证：

时间连续。

动作能够完成。

情绪停顿有足够空间。

每镜最后的低动作稳定窗口已经计入该镜头时长。


禁止：

5秒镜头同时安排：

发现。

认出。

穿越街道。

拥抱。

哭泣。

离开。


如果动作过多：

优先减少动作。

必要时再拆镜头。


不得在用户已确认总时长之外额外追加结尾停留。


如果必要动作与结尾稳定窗口无法同时容纳：

先减少次要动作或降低运镜复杂度。


仍无法执行时返回Shot Design调整，不得让动作瞬间完成。


内部检查完成后：

只保留动作先后、因果、容量和稳定收尾语义。


删除所有精确时间轴表达后再进入Template Mapping。


---

# Step 10

# Motion Design

人物动作必须具有：

因果。

顺序。

速度。

结果。


重要动作分析：

开始状态。

动作启动。

动作过程。

动作变化。

结束状态。


例如：

错误：

她抱住对方。


执行逻辑：

她保持原地短暂停顿。

↓

向前迈出一步。

↓

伸手接近对方。

↓

另一人短暂僵住。

↓

双方完成拥抱。

↓

动作保持。


复杂动作不得：

瞬间完成。


---

# Step 11

# Performance Design

按需读取：

knowledge/performance/


先建立：

Baseline → Stimulus → Attention Shift → Appraisal → Impulse → Control / Leakage → Visible Response → Action Choice → Settled State。


再从`facial_action_language.md`中选择最少的可见通道：

- 明确视线目标、路径、速度与保持/移开
- 眉眼、眼睑、嘴角、唇部或下颌的一项主要变化
- 呼吸、肩颈、手部、重心或距离的一项支持变化
- 泪水、脸红、颤抖等条件性结果及其形成过程（只有上游成立时）
- 结束时可继承的注意目标、面部/身体张力与恢复程度


对白场景还必须区分：

说话者、倾听者、说话前动作、说话过程、倾听反应和说话后停顿。


多人镜头必须确定：

Primary Performer、Secondary Reactor、背景保持者和反应顺序。

人物表演优先使用：

微表情。

眼神。

呼吸。

停顿。

手部动作。

肩部状态。

身体距离。

步伐。


复杂、压抑或混合情绪必须说明公开状态与一处泄漏的先后，不同时输出两套完整冲突表情。微表情短暂出现后必须被压回、发展或回落，不能作为整镜静态面具。


根据角色与剧情决定：

表演强度。


默认优先：

自然。

克制。

真实电影演员感。


除非剧本明确要求：

避免自动增加：

大哭。

尖叫。

瞪眼。

夸张张嘴。

突然奔跑。

猛烈拥抱。

舞台式动作。

瞳孔地震、固定露齿数、自动脸红、瞬间落泪、全身随机颤抖和“眼神温柔/冰冷/坚定”裸标签。


表演结束状态必须进入镜头边界检查，不得在下一镜无原因重置情绪、呼吸、视线或身体张力。
泪液/泪痕、红肿、妆容变化、颤抖和哭笑后的呼吸负荷同样必须继承。


---

# Step 12

# Spatial Design

多人镜头：

必须分析空间关系。


需要确认：

人物A的位置。

人物B的位置。

左右关系。

面对方向。

视线方向。

人物距离。

行进方向。

摄影机位于人物轴线哪一侧。


尤其是：

相向行走。

擦肩。

回头。

对话。

对峙。

战斗。

拥抱。

追逐。


必须保持：

可理解的180度轴线关系。


禁止：

人物应该面对彼此，

却同时正面对摄影机。


---

# Step 13

# Camera Execution

摄影机设计根据：

Shot Design。

已确认的Camera Language Decision。

已确认的Clip Movement Plan。

Camera Language。

人物动作。

情绪。

空间。


共同决定。


先读取并保持上游确认的：

- 本镜主运镜或Static / Locked-Off
- 该运镜承担的镜头目的、情绪功能、空间功能与节奏功能
- 可选辅助与禁止运镜
- Seedance稳定等级、复杂度峰值与安全降级
- 本镜在Clip主导逻辑中的位置：建立、跟随、揭示、靠近、高潮、克制、释放或收束

然后把运镜知识转译成具体可执行摄影描述。不得只复制“Push In / Side Tracking / Handheld”等术语；至少明确：

1. 摄影机从哪里开始，以及位于人物前/后/左/右/哪一肩；
2. 唯一主要路径、物理运动方向、速度和幅度；
3. 哪个人物动作、视线、信息或节奏变化触发摄影机运动；
4. 摄影机如何与人物速度、距离、轴线、前后景视差和对焦配合；
5. 摄影机在哪里减速/停住，结束景别、构图和下一镜继承锚点是什么；
6. 明确禁止的换侧、反向、叠加、越轴或高风险运动。

这些语义映射到`templates/10_video_prompt.md`已有字段：主要路径进入“镜头/机位”，同步视觉过程进入“画面描述”，轴线/方向进入“空间关系”，摄影机终点与边界/下一镜承接语义共同进入“镜头结尾状态”。不得输出Camera Language Decision、Clip Movement Plan、S1-S4等内部字段，也不得新增“与下一镜衔接”字段。


需要确定：

摄影机起点。

摄影机观察对象。

运动方式。

运动方向。

运动速度。

摄影机终点。


焦段执行还必须确定：

- 画幅已确认时的焦段，或未确认时的约XXmm全画幅等效倾向
- 与景别配套的摄影机距离，而不是把焦段与景别混为一谈
- 前后尺度、背景叠合/分离、边缘安全与视差的可见结果
- 对焦对象、焦点行为和必要景深；不把浅景深归因于焦段单独作用
- 广角边缘速度/脸形风险或长焦抖动/跟焦风险及降级方案
- 结尾和下一镜需要继承的摄影距离、脸部几何、背景尺度和焦点状态


摄影机运动必须：

能够与人物动作同时执行。

如包含第二阶段运动，还必须确认它与主要路径同向、同轴、同平台、同主体、同目的，并由一次明确事件触发；否则拆为下一个正式SHOT。


构图执行必须同时确定：

- 主体在画面左、中、右及前、中、后景的位置
- 主构图原子或一个可降级导演模式
- 前景、背景、遮挡、反射、引导线、负空间或色光区域的真实空间来源
- 视觉焦点如何随人物动作、摄影机运动或一次光学变化转移
- 镜头结束时的稳定构图、焦点与空间锚点


模式名称只用于内部选择。进入最终Prompt时必须拆解到“景别”“镜头/机位”“画面描述”“空间关系”“镜头结尾状态”等现有字段，不得只写模式标签。


例如：

角色缓慢靠近。

摄影机可以：

固定。

缓慢后退。

轻微侧向跟随。


不应无理由：

同时推。

摇。

环绕。

变焦。

快速升降。


---

# Camera Simplicity Rule

视频模型执行稳定性：

高于摄影炫技。


优先：

一个主要摄影运动。


必要时：

增加一次轻微、同向、有动机的路径延续；焦点修正或手持呼吸不得升级为第二个主要运动。


禁止：

一个短镜头堆叠大量复杂运镜。

禁止把多个景别、机位、视点、观察对象、时空或FX阶段用箭头串成一个分镜。此类组合必须先按`knowledge/camera_language/movement_combinations/decision_engine.md`拆镜。

简单不等于单一模板。禁止把“缓慢推进”“轻微横移”“稳定中景”作为未检索时的默认答案；只有它与本镜已确认的叙事功能、起止路径和Clip重复规避一致时才可使用。


---

# Camera Language Selection

本节只是快速候选提示。正式选择必须优先服从已确认的Camera Language Decision与Clip Movement Plan，并实际读取`knowledge/camera_language/camera_movement/selection_matrix.md`、Camera Movement Index和被选原子知识文件；不得根据下列例子重新自由选镜。


## 环境建立

可以考虑：

Wide Shot。

Slow Push。

Slow Pull Out。

Static Wide。


---

## 人物进入

可以考虑：

Tracking。

Side Tracking。

Follow Shot。


---

## 发现

可以考虑：

Slow Dolly In。

Over-the-Shoulder。

Reflection。

Rack Focus。


---

## 情绪反应

可以考虑：

Medium Close-Up。

Close-Up。

Slow Push。


---

## 紧张

可以考虑：

Handheld。

Blocked Composition。

Tracking。


---

## 关系变化

可以考虑：

Two Shot。

Side Two Shot。

Over-the-Shoulder。

Slow Push。


---

## 情绪高潮

可以考虑：

Close Two Shot。

Slow Orbit。

Long Take。


复杂Camera Language：

必须有明确叙事目的。

复杂Orbit / 360、穿墙、无人机和多段一镜到底还必须证明基础运镜无法等价完成、模型复杂度允许，并保留Static / Push In / Pull Out / Tracking / Side Tracking / Pan / Crane / Shoulder Follow / Dolly Tracking等基础降级；否则禁止进入最终Prompt。


---

# Step 14

# Lighting Execution

光线必须延续：

Visual Development。

Environment Asset。

时间。

天气。


并从knowledge/lighting/中按需编译：

- 已确认光源/环境依据与空间锚点
- 光线方向、光质、强度/曝光、光比、综合色温关系与衰减
- 雾烟尘雨水等介质、遮挡、材质与反射
- 人物、面部、道具与环境的可见受光结果
- 起始光态、本镜唯一必要变化、稳定结束光态与下一镜边界


需要判断：

人物移动之后：

受光是否变化。


例如：

人物从街道进入便利店屋檐：

可以产生：

冷色环境光

↓

暖黄色侧光增加。


这种变化必须：

具有真实空间依据。


低调光是明暗/光比策略，散射光是光质，体积光需要参与介质，反射补光需要真实反射面。浅景深、运镜、构图、调色、FX与情绪表演继续由各自模块负责。


禁止：

无理由改变综合色温。

无理由增加新光源。

无理由改变夜晚为白天。


## Color Execution

综合色彩设计必须按`knowledge/color/index.md`从已确认事实编译：

- 资产固有色、环境/实用光源、时间天气、FX和材质提供的颜色来源
- 主色、辅助色、强调色的面积、空间位置和叙事优先级
- 人物、背景与强调色的饱和度层级
- 整体明度、黑位、高光、局部对比和表演/动作可读区
- 白平衡/综合色温、绿色—品红偏色，以及肤色/中性色/关键资产颜色保护
- 材质、玻璃、金属、水面、湿地、烟雾等综合色彩响应
- 起始色态、本镜唯一必要变化、稳定结束色态与下一镜继承

冷暖、饱和度、暗调、霓虹、糖果或清透色不能直接替代执行说明。霓虹必须绑定已确认光源；暗调必须保留阴影细节和关键可读区；高饱和优先选择性增强；低饱和保留身份色；色调不自动代表人物情绪。

禁止无理由整帧滤镜跳变、肤色漂移、综合色彩闪变、通道溢出、死黑/过曝、白平衡抽动或资产换色。


---

# Step 15

# Prop Execution

关键道具：

必须按照真实物理逻辑变化。


例如雨伞：

持有。

↓

倾斜。

↓

移动。

↓

松手。

↓

落地。


禁止：

直接：

持有

↓

消失。


道具变化必须：

存在动作过程。


---

# Step 16

# Sound Logic

按需读取：

knowledge/sound_language/

为镜头设计：

声音逻辑。


根据剧情判断：

环境声。

动作声。

对白。

呼吸、衣料、脚步、道具与其他同期Foley。

剧情内真实播放源或现场声。


角色有对白、旁白、画外音、通话或呼喊时：

- 先从asset_registry.md的Active CHAR Version读取`Voice Asset Status`、Confirmed Voice Profile、`Voice Audio Reference Status`与Reference元数据，并检查用户是否已明确提供当前Voice Reference。
- 如果用户已明确提供当前Voice Reference，或目标模型实际使用同一Active CHAR Version的Confirmed Voice Audio Reference / Audio Reference / Voice Reference：在`参考资产：`标明角色与Reference ID/受控路径及“只锁定声音身份，不作为视觉参考”；保留`音色特征：`并写明由该Reference锁定声音身份、不得文字重定义；不得把Voice Profile或任何Voice characteristics、音高、声线、音域、共鸣、语速、音色质感写入视频Prompt其他字段。
- Reference Override分支中的“台词”只写准确台词和必要轻量表演指令，例如“轻声说”“无奈地说”“短暂停顿后说”；“音效”可以记录对白/口型同步、声源位置、距离、遮挡与同期空间，但不得借这些字段重新定义音色。
- 只有没有适用Voice/Audio Reference、但已经存在Confirmed Voice Profile时，才由`音色特征：`忠实引用其“最终可直接引用的音色描述”，并让“台词”与“音效”遵守其基础音色、音域倾向、语速、咬字/发音、力度、停顿与呼吸特征。
- 不得用通用的“低沉磁性、温柔清亮、播音腔”等套话覆盖已确认Profile，不得无依据添加口音、方言、地域发音、疾病嗓音或声带损伤。
- 主要角色/重要配角有对白但Voice Profile不存在或仍为Pending时，进入`No Voice Asset`分支：保留固定`音色特征：`并写明未建立独立音色资产、本Clip不创建或推导声音身份；继续当前STATE-08，不得返回STATE-03、不得调用AUDIO模块、不得临时把推测写成已确认音色资产。
- 本步骤不生成音频、不调用TTS、不创建配音文件。


声音必须服务：

空间。

动作。

情绪。


例如雨夜：

环境声可以包括：

雨声。

轮胎压水。

远处城市底噪。

雨滴击打伞面。


人物靠近时：

可以逐渐突出：

呼吸。

脚步。

衣料摩擦。


默认禁止：

在“音效”字段中写背景音乐、配乐、BGM、歌曲、电影配乐、主题音乐、氛围音乐、节拍或“无配乐”等音乐说明。

要求Seedance生成任何背景音乐、配乐、BGM、主题音乐、氛围音乐或歌曲。该禁令没有用户指定Clip例外；任何后期配乐要求都必须另行进入显式MUSIC / SEED-MUSIC模块。


每个镜头必须确认一个主要声音重点，并区分：

- Persistent Ambience
- Local Source / Foley
- Dialogue / Voice-over
- Intended Silence


镜头边界还需记录声音尾部以及Bridge、Cut、Fade或Unresolved状态。


同一时空中持续的底噪、声源位置、对白状态和FX声音不得在切镜时无原因重置。

正向声音硬门槛：

- 每镜必须写出具体环境底声/空间底噪；有意静默也必须说明理由并保留可听见的自然底声
- 每镜至少写出一个与画面同步的前景层：动作声、Foley、呼吸、对白或剧情内声源
- “无”“静音”“无音效”“有效内容”以及只写“禁止背景音乐”均视为声音缺失
- 固定背景音乐禁令只进入【反向提示词】，不得挤占“音效”字段；所有Clip无例外执行


---

# Step 17

# Editing Logic

必须读取：

knowledge/transitions/index.md

并依序应用其Decision Engine、Pattern Library与Continuity Ledger。

每个分镜边界需要先按照rules/04_consistency_rules.md判定连接类型，并区分同一Clip内部边界与跨Clip边界：

- Continuous Handoff
- Motivated Discontinuity
- Unresolved Handoff


然后明确：

如何与前一个镜头或前一个Clip连接。

当前动作在哪里结束。

下一镜头从哪里开始。


对于Continuous Handoff：

上一镜头最后状态必须成为下一镜头起始状态，且下一镜动作不得在上一镜结尾提前发生。


对于Motivated Discontinuity：

场景切换、时间跳跃、硬切、蒙太奇、闪回或故意跳切必须明确断点和新的时空锚点，不得伪造不存在的过渡动作。


对于Unresolved Handoff：

下一镜未知或资料矛盾时，不得猜测；保留当前镜头安全稳定的结尾，并标记待下一镜确定后成对复核。


先检查动作、视线、反应、构图、方向、尺度、同期声、完整遮挡、光态与FX是否存在真实锚点。没有充分依据时使用Direct Cut；下一镜未知时保持Unresolved Handoff。

每个边界只选择一种主要视觉转场。同期Sound Bridge可作为辅助，但不得使用背景音乐、配乐或歌曲。

推、拉、摇、移、跟、升降、环绕、甩镜、俯冲、贴地推进与变焦本身不是转场。只有存在明确切点与兼容下一镜锚点时，才构成跨镜连接。

大多数转场在后期完成；STATE-08负责生成兼容的出镜/入镜把手。只有真实遮挡、已确认光态/介质/FX或明确奇幻规则存在时，才设计In-camera或FX转场；否则降级为Direct Cut。


复杂转场：

必须有叙事目的。


---

# Step 18

# Memory And Flashback

如果剧情存在：

回忆。

闪回。

幻觉。

记忆碎片。


必须确认：

是否已经在Shot Design中建立。


如果没有：

STATE-08不得无原因增加。


已经确认的Flashback：

必须明确：

进入点。

视觉差异。

时间差异。

退出点。


禁止：

现实与回忆无提示混合。


---

# Step 19

# Apply Seedance Adapter

完成镜头执行逻辑后：

调用：

knowledge/11_seedance_adapter.md


用于检查：

动作密度。

时间过程。

人物方向。

摄影机复杂度。

空间关系。

道具连续。

角色稳定。

环境连续。


Seedance Adapter：

可以帮助简化：

模型不容易执行的复杂动作。


但不得：

改变剧情。

改变人物关系。

改变镜头核心目的。


Seedance Adapter内部的：

Scene。

Character。

Action。

Composition。

Camera。

Lighting。

Sound。

Editing。


只作为：

内部分析维度。


不得：

直接成为最终输出结构。


---

# Step 20

# Continuity Check

所有镜头完成执行转换后：

统一检查连续性。


---

## Character Continuity

检查：

角色身份。

脸型。

五官。

年龄。

发型。

服装。

身体比例。


---

## Character State Continuity

检查：

湿润程度。

伤痕。

污渍。

妆容。

呼吸状态。

情绪状态。


---

## Environment Continuity

检查：

地点。

时间。

天气。

道路。

建筑。

灯光方向。

雨量。

背景。


---

## Spatial Continuity

检查：

人物左右关系。

面对方向。

行走方向。

视线。

距离。

180度轴线。


---

## Action Continuity

检查：

上一镜头结束动作。

下一镜头开始动作。


例如：

G02结束：

人物刚停下。


G03开始：

应该从停下后的状态继续。


而不是：

重新开始走路。


---

## Prop Continuity

检查：

道具持有者。

左右手。

位置。

方向。

状态。


---

## Camera Continuity

检查：

摄影机位置变化是否合理。

景别变化是否具有逻辑。

镜头方向是否破坏空间认知。


---

## Lighting Continuity

检查：

- 光源身份、空间锚点与方向
- 光质、强度/曝光、光比、综合色温关系与衰减
- 人物、面部、道具与环境受光
- 遮挡、阴影、轮廓、材质与反射
- 雾、烟、尘、雨、水等介质状态
- 动态实用光源的有限变化与结束状态
- 上一镜结束光态是否能直接成为下一镜起始光态，或是否存在已确认断点

禁止无理由光源换边、曝光泵动、随机闪烁、反射漂移、介质密度跳变或夜景突然变亮。


## Color Continuity

检查：

- 主/辅/强调色及其空间来源和画面占比
- 人物、背景、道具与FX的饱和度层级
- 明度、黑位、高光、局部对比和关键可读区
- 白平衡/综合色温与绿色—品红偏色
- 肤色、中性色、服装、道具和环境固有色
- 材质、湿地、玻璃、金属、水面与介质综合色彩响应
- 上一镜结束色态是否成为下一镜起始色态，或是否存在已确认断点

禁止全局综合色彩滤镜随机切换、肤色青绿/橙红漂移、饱和度泵动、黑位压死、高光综合色彩溢出、霓虹换边或资产颜色被重绘。


---

## Emotional Continuity

检查：

情绪是否自然递进。


禁止：

无剧情原因：

克制

↓

突然崩溃。


---

## Shot Boundary Continuity


逐对检查：

- 每镜起始边界来源是否明确
- 每镜最后一帧是否形成稳定、可验证的结束状态
- 每镜是否说明与下一镜直接继承、经断点重建或暂定未决
- 连续继承是否保持人物位置、左右关系、朝向、视线、动作阶段、情绪、道具、环境、摄影机与持续声音
- 场景/时间/剪辑断点是否只改变已获剧情授权的状态
- 是否存在为衔接而新增剧情或提前执行下一镜动作
- 跨Clip时是否先判定A/B/C；A/B是否标记`Tail Frame Required = YES`并把前一段`REF-TAIL`列入【参考资产】、声明对应的同镜头连续承接用途或空间/站位/景别参考用途，缺图时写待补充状态；A是否直接承接，B是否另起新镜头重新构图；C是否标记`NO`、不列尾帧并以Canonical资产、Spatial Blocking与文字End State承接或重建
- Motivated Discontinuity时，后一G段是否明确不继承前一尾帧、说明重建原因并只保留已确认锚点


如果逐个Clip分批输出：

下一Clip尚未确定时，上一Clip末镜只输出暂定安全衔接。


下一镜确定后，必须先复核并在必要时最小修改上一镜的结尾限制与衔接说明，再输出下一镜。


---

## Sequence And Unit Continuity


存在Sequence Plan时逐UNIT检查：

- Required COV是否在对应SHOT中得到可见完成证据
- UNIT Entry是否来自已确认上一UNIT Exit或Motivated Break
- State Ledger中的人物、环境、道具、FX、声音与故事认知是否被继承
- UNIT重试边界是否不会修改已接受的前序素材
- 是否存在Required Coverage遗漏、重复或被Optional内容挤压


Coverage遗漏返回Sequence Planning或Shot Design，不在STATE-08临时创造镜头目的。


---

# Step 21

# Clip Independence And Shot Integrity Check

每个Clip必须：

作为独立的视频生成单元和独立Prompt Package可以被理解、复制与提交；Clip内每个正式分镜仍保留完整逐镜字段。


“相对独立”只表示本Clip指令自足、单一空间与单一连续时间段可执行。


它不表示：

跨镜头人物、环境、道具、动作或情绪可以重新初始化。

硬性Package Gate：

- 为Confirmed Clip按顺序使用CLIP-001、CLIP-002、CLIP-003……
- 每个`# CLIP-X｜标题 Seedance视频提示词`区块只对应一个CLIP-xxx，并包含该Clip列出的1个或多个`分镜X`；单镜Clip独立执行，多镜Clip作为同一次连续长镜头的执行阶段且不在Clip内部硬切
- Clip区块总数不得大于正式分镜总数，允许相等；单分镜Clip是合法输入，不得为了减少Clip区块数量强行合并
- 每个区块在Markdown标题中写明正式CLIP-xxx与人类可读标题，在`时长：`写明4—15秒平台生成时长；不得输出独立“CLIP标题”字段或方头括号章节
- 该时长必须逐字取自Confirmed Clip Production Plan的目标时长，并与Clip Detail中的逐镜求和、合计和平台生成时长一致；禁止重新估算
- 每个Clip区块重复完整全局锁定字段，并拥有自己的前置`首帧参考：`、`尾帧限制：`与末尾`反向提示词：`
- 禁止跨Clip合并、遗漏、重排或重复分镜
- 同一Clip内非末分镜通过“同一Clip连续生成”逐项继承；末分镜负责跨Clip衔接与尾帧
- A Direct Start-Frame Handoff的G02及以后标记`Tail Frame Required = YES`；【参考资产】列统一`REF-TAIL`名称与“同镜头连续承接用途”，【首帧参考】逐字写固定直接承接句并从该帧逐项继续；未提供时同一条目写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图
- B Reference-Only Handoff的G02及以后同样标记`Tail Frame Required = YES`；【参考资产】列统一`REF-TAIL`名称与“空间/站位/景别参考用途”，【首帧参考】说明延续空间逻辑但另起新镜头重新构图，禁止使用A的固定直接承接句；未提供时同样列待补充状态
- C新镜头且无需尾帧标记`Tail Frame Required = NO`，不要求用户截图、不把上一尾帧列入【参考资产】；在【首帧参考】明确Canonical资产、Spatial Blocking、文字核对/重建原因与保留锚点

默认交付模式是Single-Clip Checkpoint：多Clip项目本轮只输出当前待处理的一个Clip及其G段，完成该Package全部章节后停止，等待用户审核、修改或确认。用户只说“下一个”“下一步”或“继续”时，只推进并输出下一个尚未交付Clip，不得倾倒剩余全部Clip；完整视频提示词是项目最终目标，不是本轮批量交付授权。

只有用户在当前请求中明确要求“全部输出”“一次性输出”“批量输出”或“连续输出多个Clip”时，才切换为Explicit Batch Override并连续列出多个独立完整Clip区块。该覆盖只改变本轮Package数量；每段仍必须完全自足、逐段通过Final Validation并保持独立Checkpoint语义。不得从用户的最终目标、项目规模或此前曾要求完整视频推定批量授权。不得因为批量而压缩、共享、合并、删减或改名字段；如果完整内容超出单次回复容量，自动按完整Clip分批，批次边界不得拆开单个Clip。


一个镜头内不得同时存在：

无法连续执行的多个空间。

多个时间点。

无转场的现实与回忆。

互相矛盾的摄影运动。

互相矛盾的人物位置。


如果存在：

优先降低复杂度。


必要时：

返回Shot Design重新拆分。


---

# Step 22

# Prepare Template Data

完成内容设计后：

把信息整理成：

Template需要的数据。


按Clip分别准备内容；每个Package包括：

当前镜头所需的全局视觉信息副本。

已通过的Clip Preflight语义副本：连续性三选一主分类；逐分镜World-State；角色精确数量与唯一性；追逐/战斗/多人空间构图；关键道具形态/尺寸/持有/悬浮/转换状态；适用转场五要素。该副本只用于把语义映射到现有字段，不成为新栏目。

`参考资产：`清单：先读取`Clip End-State Record / Next-Clip Carryover`与当前Continuity Risks，按身份/外观、空间结构、道具造型、A/B状态锚定、光线/场景状态等实际风险路由最小充分资产，再显式列出本Clip实际使用的Canonical Character / Environment / Prop / FX Assets、Voice/Audio Reference、合法首尾帧与其他确定需要实际投喂的视觉参考图，并逐项写明用途、所解决风险和锁定约束；不得把整个Registry或所有Eligible资产机械复制进来。已确认资产不得被临时文字描述覆盖。每个视觉条目序列化前必须通过Visual Input Eligibility；纯文字约束移到对应既有字段，受控待补视觉图写具体图像对象、实际投喂用途与未确认状态。上一Clip尾帧先由Previous-Clip Continuity Decision中的A/B/C决定：A/B均以`REF-TAIL-XX｜CLIP-XX尾帧参考`直接列入本字段并分别标明“同镜头连续承接用途”或“空间/站位/景别参考用途”；缺图时同一条目写“待用户提供/待上传、未确认”，不得声称已上传/已确认。C不要求截图且不列旧尾帧。

在序列化该清单前，先执行Visual Input Eligibility并记录文字伪资产迁移，再按Preflight逐分镜World-State删除非当前Clip出场角色、未使用环境/道具/动作图及当前阶段不适用资产；A/B无论尾帧是否已上传都预留1个Projected位并列出待补充声明，只有实际尾帧图存在、可访问、已确认时才计入已提交图片数；C不预留旧尾帧。其他受控待补视觉图同样只计Projected位且必须说明具体图像与实际投喂用途。再按`knowledge/reference_budget.md`复算：≤7直接保留独立图；8张且无额外帧需求直接保留；9张确认无待加入连续性图片后才保留；>9才整合同类非角色信息，仍超限按优先级裁剪。已有9张且新增或待上传上一尾帧时按10计算并至少释放1位。Projected Final Count与已提交图片数均≤9；真实图片参考必须存在且已确认；每个核心角色各自独立三视图/角色锁定图不可合并或由动作图替代。

`首帧参考：`写明A/B/C、`Tail Frame Required = YES / NO`与当前Clip可执行首帧。A引用对应`REF-TAIL`并逐字写固定直接承接句；B引用对应`REF-TAIL`并说明延续站位/朝向/距离/景别/空间/道具或构图逻辑，但当前Clip另起新镜头重新构图，禁止使用A固定句；A/B未提供尾帧时明确“待用户提供/待上传、未确认”，不得声称图片存在，Prompt可交付但实际提交生成前补图。C不列`REF-TAIL`，用Canonical基础资产、Spatial Blocking与文字End State承接或重建。无论哪种模式都逐项描述人物姿态、位置、朝向、视线、人物间距离、摄影机起始位置、景别、主体构图、环境、天气、道具、动作起始状态、光线与情绪状态。

`尾帧限制：`在分镜之前前置锁定当前Clip新的最终交付状态，逐项描述人物最终位置/动作/视线/情绪、摄影机最终状态、道具和环境最终状态，以及下一Clip预计如何使用；必须可冻结、可继承，最后1秒不得开启新复杂动作。实际生成、提取并确认后才按当前Clip编号登记为新的`REF-TAIL-XX｜CLIP-XX尾帧参考`；不得沿用上一Clip尾帧名。

角色锁定信息。

环境锁定信息。

道具锁定信息。

当前Clip内全部分镜的视觉事件，以及它们作为同一次长镜头连续阶段的执行顺序。

每个镜头的空间信息。

每个镜头的摄影信息。

每个镜头的光线信息。

每个镜头的综合色彩信息与稳定结束色态。

每个镜头的人物表演。

每个镜头的声音。

每个有对白角色的Voice Reference Override判定。使用适用Reference时准备Reference ID/受控路径、准确台词、轻量表演指令和同期声空间，并为固定`音色特征：`准备“由Reference锁定声音身份、不得文字重定义”的非空内容；无适用Reference但已有Confirmed Voice Profile时准备其最终可直接引用的音色描述及当前镜头允许的状态变化；两者都不存在时准备`No Voice Asset`声明，不推导、不补齐。全段无对白时也准备固定字段内容。

每个镜头的剪辑。

每个镜头的起始边界来源。

每个镜头第一帧的来源或要求；连续动作/连续转场直接继承上一结尾，不重新初始化人物站位、动作、环境、道具、摄影机边界或轴线。

每个镜头的最后一帧稳定限制。

每个镜头的尾帧接口状态：默认低动作、清楚可读、主体无遮挡、构图稳定且可继承；除非剧情明确要求，不得停在高速运动、动作未完成、主体严重遮挡或构图不可读状态。

当前分镜的连接类型与下一镜衔接说明，并写入固定字段“镜头结尾状态”，不得新增字段。

跨Clip时明确判定A“同镜头连续承接”（Direct）、B“新镜头参考型”（Reference-Only）或C“新镜头且无需尾帧”（Not Required）；A/B分别声明尾帧用途，C说明不继承、重建原因与保留锚点。

当前段的新尾帧结束状态，以及实际生成、提取并确认后的资产名`REF-TAIL-XX｜CLIP-XX尾帧参考`；按下一Clip的A/B/C标记`Tail Frame Required = YES / NO`，再记录用途为同镜头连续承接、空间/站位/景别参考、待用户提供/待上传且未确认、不使用尾帧并以Canonical资产/Spatial Blocking/文字规则重建，或最终收束。

当前段独立`反向提示词：`；首个非空内容行永久固定逐字为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”，不得省略、改写或后移。

连续性约束。

Sequence、Coverage与UNIT信息只作为内部来源关系和执行检查。

生成限制。


在交给Template之前，必须按knowledge/prompt_compilation/state08_projection.md建立一次性内部Projection Ledger：

- Applicable Source
- Confirmed Fact / Design
- Target Existing Field(s)
- Evidence Present
- Conflict / Return Route

Ledger建立前先完成Director Direction Projection Check：确认Narrative Objective、Audience Experience、关系/Blocking、Camera动/停、构图与距离、功能性色光、表演尺度、声音加强/留白、节奏高潮/余韵及稳定降级都已由STATE-07保留，并将其中可执行结果投影到Template现有字段；不得把Director Decision Notes本身、十三维度标题或内部问答写入Template Data。

Movement Applicable时，Ledger还必须逐SHOT核对：Camera Language Decision与Clip Movement Plan来源、主运镜原子知识证据、叙事功能、具体起点/路径/触发/速度/终点/限制、重复规避、稳定降级和目标既有字段。不得只把运镜名称或“电影感”写入字段。


Ledger只用于防止语义丢失，禁止原样输出。

建立Ledger前必须确认本Clip已完成Knowledge Application Reflection：所选1—3项策略各自具有具体Prompt Evidence与目标既有字段；被拒绝候选没有以术语、导演名、模式ID或重复修饰词泄漏进最终文案。若存在明显可用且能提升Clip、又不破坏一致性与稳定性的Knowledge，却因沿用默认模板而完全未评估或未投影，返回本Workflow的Reflection步骤补齐。

同时必须确认Knowledge Reflection只实现Director Decision Notes，没有把知识库候选反向升级为新的剧情目标、人物关系、Blocking、视觉高潮、色光转折、表演爆发或声音事件。


每项Applicable Knowledge必须至少在一个主要目标字段中出现具体执行证据；不得只出现模块名、模式ID、“电影感”或其他抽象标签。

焦段Applicable时，Ledger必须确认“焦段倾向 + 摄影机距离 + 景别 + 空间结果 + 对焦/景深 + 运动约束”已投影到现有字段；不得只保留毫米数，也不得输出FLN编号。

Color Applicable时，Ledger必须确认“颜色来源 + 主辅强调色层级 + 饱和度 + 明度/对比 + 白平衡/偏色 + 肤色/中性色保护 + 材质响应 + 结束/继承色态”已投影到现有字段；不得只保留色调名称，也不得输出CLR编号。


不得准备或传递到Template的内容：

- 时间码或起止时间戳
- 总片时长、单分镜时长或Clip内部逐镜时长；保留Confirmed Clip的单一4—15秒平台生成时长
- 按秒动作区间
- 帧率、帧数或帧区间


这里：

只整理信息。


不得：

自己决定最终字段名称。


不得：

自己决定镜头编号格式。


不得：

自己决定最终排版。


---

# Step 23

# Template Handoff

所有执行信息准备完成后：

必须调用：

templates/10_video_prompt.md


Template负责：

`# CLIP-X｜标题 Seedance视频提示词`与Confirmed Clip Production Plan的一对一编号，以及每个Clip包含的正式Shot列表。

最终字段名称。

最终字段顺序。

每个独立Clip区块内的全局锁定排版。

镜头排版。

Seedance总控补充。

负面限制。


Template还必须执行Clip Duration / No-Timeline过滤：

镜头标题只保留`分镜X`，不使用方头括号、不附加任何时间码或逐镜时长；Clip时长只在`时长：`写一次。

写入前必须交叉核对Confirmed Clip Production Plan：标题中的CLIP-xxx与计划一对一、Shot列表一致、平台生成时长一致且位于4—15秒。

Template还必须执行Package完整性过滤：每个Clip按Template当前顺序完成全部全局字段、Clip表列出的全部正式分镜、每镜全部字段与段末限制。不得出现旧章节、独立竞争标题字段、条件字段删除或额外分镜字段。


Workflow不得覆盖：

Template最终Schema。


---

# Template Ownership Rule

STATE-08的最终格式：

只有一个真源：

templates/10_video_prompt.md


如果Workflow内部术语与Template不同：

最终输出：

使用Template。


如果Shot Design字段与Template不同：

最终输出：

使用Template。


如果Seedance Adapter内部维度与Template不同：

最终输出：

使用Template。


原则：

Internal Structure ≠ Final Structure.


---

# Upstream Format Isolation

禁止：

直接复制Shot Design字段成为最终输出。


例如：

上游可以存在：

景别。

焦段。

运镜。

速度。

光影。

情绪。


这些内容：

必须被重新组织。


最终如何命名：

由Template决定。


---

# Knowledge Format Isolation

禁止：

把Seedance Adapter内部：

Scene。

Character。

Action。

Composition。

Camera。

Lighting。

Sound。

Editing。


直接作为最终栏目。


这些只是：

Knowledge Dimensions。


---

# No Workflow Schema Rule

本Workflow中：

不得维护：

另一套固定Seedance输出字段。


不得维护：

另一套镜头编号。


不得维护：

任何最终Prompt时间轴Schema。


不得维护：

另一套Final Output Example。


如果需要修改最终Seedance输出结构：

只修改：

templates/10_video_prompt.md


不要同时修改：

本Workflow。


---

# Step 24

# Final Validation

Template完成格式化后：

执行最终内容检查。


注意：

这里检查：

内容是否合法。


Schema字段完整性：

按照：

templates/10_video_prompt.md


检查。

逐Clip执行两遍固定结构校验：Template Mapping后一次，交付前一次。逐项核对`templates/10_video_prompt.md`当前定义的标题、全局字段、正式分镜、每镜字段、段末限制、顺序、非空性和字段唯一性；不得出现旧章节、竞争标题或字段、条件删除、“同上/沿用前文/略”或跨Clip共享。批量输出仍逐Clip独立校验；过长时在完整Clip之间自动分批。任一项失败不得输出，必须修正后重新校验。


---

## Stage Check

是否确实处于：

STATE-08。


---

## Story Check

是否：

没有改变剧情核心。


---

## Asset Check

是否：

角色。

环境。

道具。


使用正确资产。

`参考资产：`是否逐项列出当前Clip实际使用的Canonical角色、环境、道具、FX、Voice/Audio Reference、合法首尾帧与其他确定会实际投喂的视觉参考图，并写明用途、状态和锁定约束；是否以已确认资产优先于临时文字描述。每个视觉条目是否能肯定回答“这是不是一张实际会被投喂/引用的视觉资产？”；答案为否是否已移出并归类到正确字段。A/B所需`REF-TAIL`缺图时必须作为“待用户提供/待上传、未确认”的受控声明列出且注明用途，不得因尚未上传而省略；其他受控待补视觉图必须说明具体图像对象与实际投喂用途。未参与实际输入的说明、普通缺失占位或伪资产不得输出。

是否已按`Clip End-State Record / Next-Clip Carryover`、当前目标与Continuity Risks完成Reference Selection / Routing；每个入选条目能否说明所解决风险；身份/外观、空间结构、道具造型、A/B尾帧与光线/场景状态是否选择正确来源；C是否未选旧尾帧；是否不存在必需资产漏选、用途选错、无风险依据的过量条目或把Spatial Blocking Map当视觉参考。

是否通过`knowledge/reference_budget.md`：最终图片参考≤9；无非当前Clip角色/环境/道具/动作图；无重复占位；无未实际存在或未确认的总图、空间关系图、动作关系图；每个核心角色各自保留独立三视图/角色锁定图；≤7没有整合、8张无额外帧需求没有整合、9张已确认无额外连续性需求、>9已经执行非角色整合/优先级裁剪。失败时不得输出。

---

## Clip Preflight Check

是否已按`knowledge/clip_preflight_check.md`执行STATE-08最终版并为PASS：

- Continuity Classification是否在视觉连续、剧情连续、主动切场/切世界中三选一，并明确A/B/C；A/B是否标记`Tail Frame Required = YES`并在【参考资产】列统一`REF-TAIL`、用途与真实状态，缺图时是否写“待用户提供/待上传、未确认”且未冒充已提交图片；A/B的首帧句式是否正确区分；C是否标记`NO`、不列`REF-TAIL`并采用Canonical资产、Spatial Blocking与文字重建。
- 每个分镜是否明确World-State；参考资产是否只含当前阶段实际存在/出场/使用项；完全位于耳中玉境等转换后世界的Clip是否排除现实阶段环境/道具。
- 每个视觉条目是否通过Visual Input Eligibility；站位、不可换边、人物距离、同坐一张板凳、道具数量、空间关系、行为约束、禁止项或镜头规则是否没有伪装成资产，并已迁移到`空间关系 / 起始状态 / 道具状态 / 首帧参考 / 尾帧限制 / 反向提示词 / Spatial Blocking Rules`；真实道具图是否使用正式ID。
- 每个分镜是否锁定角色精确数量；唯一角色是否在正向字段明确唯一一只/名和前中后景无第二个同类，并在反向提示词禁止复制、分身、镜像重复、背景第二个与相似替身。
- 追逐/战斗/对峙/多人镜头是否锁定前后景、左右、朝向、关系轴、运动方向、正脸许可与同景深许可；追逐是否默认后追前逃并禁止双方并排正对镜头、海报式合影和群像站桩。
- 每个关键道具是否明确当前形态、尺寸、持有者/左右手、位置、是否允许悬浮、转换完成状态与下一镜继承；现实与武器化等不同世界状态是否没有混用。
- 现实↔幻想/耳中玉境、地点/时间、尺度或角色/道具形态转换是否完整定义起点状态、转换媒介、运动方向/过程、终点状态与转场后首个稳定构图；是否没有用含糊闪光替代过程。
- Reference Budget是否只在前述检查通过后执行，最终≤9且只在信息超限风险时整合非角色资产。

任一项失败不得交付；先按Preflight Return Route最小修正Affected Clip / Shot / Asset，再从Continuity Classification重跑。

---

## First-Frame Check

是否每个分镜的“起始状态”明确首帧来源或首帧要求。A是否从上一Clip`REF-TAIL`直接继续并使用固定直接承接句；B是否参考上一`REF-TAIL`但明确另起新镜头重新构图且不使用该句；A/B未上传时是否明确待补充而未声称图片存在；C是否从Canonical资产、Spatial Blocking、文字End State、当前Scene或合法新首帧继续且不列`REF-TAIL`；是否没有无依据重新初始化人物站位、动作阶段、环境、道具、摄影机边界或轴线。

---

## End-Frame Interface Check

是否每个分镜“镜头结尾状态”与Package前置`尾帧限制：`都形成稳定、清楚可读、主体无遮挡、构图稳定且可继承的尾帧接口。除非剧情明确授权，是否排除高速运动、动作未完成、主体严重遮挡与构图不可读；是否明确最后1秒不启动新复杂动作。

---

## Cross-Clip Continuity Check

是否每个分镜都明确与下一镜/Clip的Boundary Class。跨Clip是否读取上一Clip八组`Clip End-State Record / Next-Clip Carryover`并逐项形成当前首帧；是否明确选择A同镜头连续承接、B新镜头参考型或C新镜头且无需尾帧；A/B是否声明不同用途并使用正确首帧句式，C是否写明不使用尾帧、重建原因与保留锚点；是否不存在无说明的状态断裂、人物/道具重置、相机轴线跳变或连续性丢失。


---

## Character Check

是否：

人物身份稳定。

脸部稳定。

发型稳定。

服装稳定。


---

## Spatial Check

是否：

人物方向。

视线。

轴线。

距离。


合理。


---

## Motion Check

是否：

动作存在过程。

没有瞬移。

没有复杂动作突然完成。


---

## Director Direction Check

是否已读取当前Clip对应Director Decision Notes，并在Knowledge Reflection之前锁定其方向。

是否：

- 最终执行语义具有明确叙事目的，并使观众的知道 / 感受 / 等待关系可成立
- 人物距离、视线、站位、动作先后与变化表达了已确认关系
- 镜头运动或保持静止均有导演理由，没有纯炫技，也没有无选择的平铺直叙
- 色彩/灯光只在具有剧情与真实光源依据时发生功能性变化；不变化时保持了必要稳定
- 表演外放/克制、声音加强/留白、节奏高潮/余韵均按Notes实现
- Knowledge Reflection只选择实现策略，没有反向修改导演意图
- 最终Prompt没有出现Director Decision Notes标题、十三维度、内部问答、候选/拒绝理由或元说明

任一方向性冲突按Director Decision Notes Hard Gate返回STATE-06/07；仅策略转译或泄漏问题留在STATE-08最小修订。


---

## Camera Check

是否：

摄影机运动能够执行。

没有无意义炫技。

每个SHOT的Camera Language Decision和所属Clip Movement Plan均已读取并保持，未被通用慢推/轻微横移模板覆盖。

每项主运镜都已转译为摄影机起点、人物侧位、单一路径、方向、速度/幅度、触发、人物配合、终点、轴线与稳定限制，而不是只保留术语。

每个Clip保持明确主导运镜逻辑；超过4个Shot时通常至少2种运镜逻辑；同类主运镜连续3次以上具有逐镜叙事理由；没有为了多样而强制每镜不同。

复杂Orbit / 360、穿墙、无人机或多段一镜到底均通过叙事必要性、模型容量与稳定降级门槛。


构图原子、导演模式、焦点、角度与运动是否已经拆成可执行空间语句，而不是只保留专业术语名称。


构图最终状态是否进入镜头结尾限制，复杂模式是否具有降级方案。


---

## Lighting Check

是否：

光线符合环境和Visual Development。


---

## Sound Check

是否：

声音逻辑合理。

有对白的主要角色/重要配角是否先完成Voice Reference Override判定：有适用Voice/Audio Reference时，是否已在`参考资产：`引用、保留非空`音色特征：`并写明声音身份由Reference锁定且不得文字重定义，同时删除其他字段中的Voice characteristics、音高、声线、音域、共鸣、语速、音色质感等全部文字音色重定义；无适用Reference但已有Confirmed Voice Profile时，是否把它转译到`音色特征：`及对白表现语义中；两者都不存在时，是否使用`No Voice Asset`声明且没有自动调用AUDIO模块；全段无对白时是否仍保留字段。

Reference Override分支是否只在台词层保留“轻声说、无奈地说、短暂停顿后说”等必要轻量表演指令，且没有借当前情绪、距离、体力或特殊状态重设声音身份；Profile Fallback分支是否只作剧情授权的临时变化，没有擅自添加口音/方言/疾病嗓音，也没有触发音频或TTS生产。

每镜“音效”只含对白、环境声、动作声、呼吸、Foley与剧情内真实声源，不含背景音乐、配乐、BGM、主题音乐、氛围音乐、歌曲、节拍或“无配乐”等音乐说明；该规则不存在用户指定Clip例外。

每镜“音效”同时具备具体环境底声/有意静默、至少一个同步前景声和声音尾部，不得写“无”“静音”“有效内容”或仅写禁令。

每个Clip的`反向提示词：`首个非空内容行无例外逐字为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”，不得省略、改写或后移。


---

## Editing Check

是否：

镜头之间能够连续。


或在已确认的场景切换、时间跳跃、硬切、蒙太奇、闪回、故意跳切处明确断开继承。


是否：

每镜都在固定字段中提供起始边界、最后一帧限制与下一镜衔接语义，不增加竞争字段。

每个Confirmed Clip都拥有独立完整的固定模板区块；Clip内分镜列表与Clip表完全一致，不存在跨Clip吞并、遗漏、重排或重复。

每个Clip区块的平台生成时长与Confirmed Clip Production Plan目标时长完全相等，并已通过state08 --clip-plan交叉校验。

每个Clip区块均在`主风格：`之前完整输出`首帧参考：`与`尾帧限制：`，无条件输出`音色特征：`，并在末尾输出`反向提示词：`；`尾帧限制：`定义当前Clip新的结束状态，实际生成、提取并确认后才登记为对应`REF-TAIL-XX｜CLIP-XX尾帧参考`。

后一Clip先判定A/B/C，再核验实际尾帧图。A/B在`参考资产：`列统一`REF-TAIL`名称、各自用途与真实状态；未提供时写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。A在`首帧参考：`和首镜“起始状态”使用固定直接承接句并完整继承；B明确另起新镜头重新构图且不使用该句。C不要求截图、不列`REF-TAIL`，可在`首帧参考：`和首镜“起始状态”中依靠Canonical资产、Spatial Blocking与文字状态重建。

已知相邻镜头只使用一种主要转场技术，拥有可验证Outgoing Anchor、Cut Point、Incoming Anchor与Direct Cut降级；普通运镜未被误当转场。


是否：

没有为自动衔接改变剧情、人物站位逻辑、道具状态或提前执行下一镜动作。


---

## Prop Check

是否：

关键道具符合物理连续性。


---

## FX Check

是否：

FX具有触发、来源、过程、交互和结束状态。

跨镜强度、方向、覆盖范围、残留后果和声音尾部保持连续，或存在已确认断点。


---

## Sequence Coverage Check

存在Sequence Plan时确认：

Required COV均由已确认SHOT承担。

UNIT顺序、Entry / Exit Anchor、State Ledger与Retry Boundary没有被改写。

最终Prompt没有出现SEQ、BEAT、COV或UNIT作为新的固定Schema栏目。


---

## Semantic Projection Check

按照knowledge/prompt_compilation/state08_projection.md确认：

- 所有已确认且Applicable的资产、Camera、Focal Length、Composition、Lighting、Color、Performance、Sound、FX、Sequence与连续性语义均进入现有Template字段
- Director Decision Notes中的可执行方向已经进入现有字段，但Notes标题、十三维度、内部问答、风险权衡与推理记录没有成为最终栏目或文案
- 焦段与景别、摄影机距离分别清楚；透视、背景尺度和虚化没有错误归因，FLN编号没有泄漏
- Color拥有真实来源、综合色彩层级、饱和度、明暗/偏色、肤色保护、材质响应和稳定结束色态；没有新增光源、重写资产颜色或泄漏CLR编号
- 未触发模块没有被虚构填充
- 内部知识标题、模式ID与Projection Ledger没有成为最终栏目
- 同一信息没有在多个字段机械重复
- Template格式化没有丢失摄影机终点、构图锚点、表演结果、FX残留、声音尾部或下一镜衔接
- Camera Language Decision与Clip Movement Plan没有成为新字段，但其主导逻辑、逐镜变化、具体运镜路径、重复规避与复杂度降级已进入现有字段


## Knowledge Application Check

逐Clip轻量确认：

- Knowledge Opportunity Check是否发生在`Clip Production Result → Director Decision Notes`之后；所选策略是否只实现已确认导演意图，而没有根据知识库技巧反向改写叙事目的、观众体验、人物关系或总体视听策略。
- 已执行十类Knowledge Opportunity Check：Camera Language、Composition、Color / Tone、Lighting、Performance、Sound、Editing Rhythm、Director Style、Continuity与Seedance Stability；不存在“有明显可用知识却完全未评估/未转译”的默认模板退化。
- 最终采用1—3项高价值策略；没有为了专业感堆砌Camera、Composition、Color / Tone、Lighting、Performance、Sound、Editing Rhythm或Director Style技巧。克制 / 稳定策略具有具体收益，不是占位。
- 每项采用策略均已写成具体可执行描述，没有只留下Side Tracking、Push In、导演名、模式ID或抽象风格词。
- 所选策略不改变剧情、资产、SHOT/CLIP顺序、关系轴、边界与连续性，并通过Seedance动作密度、摄影机复杂度和稳定结尾检查。
- Opportunity Check、选择表、拒绝理由与内部Reflection Record没有进入最终Prompt；用户明确要求查看时也只另行提供决策摘要。


---

## Emotional Check

是否：

人物情绪自然递进。


表演节拍可观察且没有无原因重置。


对白口型容量、说话者与倾听者反应可以执行。


---

## Template Check

最终输出是否：

完全使用：

templates/10_video_prompt.md


规定的当前Schema。


如果不符合：

不得：

在Workflow内创建新的替代格式。


必须：

重新执行Template Mapping。


同时检查最终Prompt：

除【时长】单一4—15秒Clip平台生成时长外，不得出现时间码、时间戳、总片时长、单分镜时长、按秒动作区间、帧率、帧数或帧区间限制。

交付前强制运行：

validate_sd_film.py state08 <video-prompt.md> --clip-plan <confirmed-clip-plan.md>

默认命令只允许当前一个Clip Prompt Package。只有用户在当前请求中明确授权“全部输出 / 一次性输出 / 批量输出 / 连续输出多个Clip”时，才追加`--batch-output`；用户只说“下一个 / 下一步 / 继续”时禁止追加该开关。

未提供Confirmed Clip Production Plan、任一G段时长与Clip表不一致、任一Clip超出4—15秒或任一“音效”缺少正向可听内容时，不得交付。


---

# Prompt Quality Decision

完成Final Validation后，使用knowledge/quality/prompt_scorecard.md执行Hard Gates与100分内部评分。

- 任一Hard Gate失败：不得交付，按Error Routing返回。
- 90–100：Ready for Review。
- 80–89：允许进入Review，但必须把剩余风险写入Review输入。
- 70–79：REVISE，不得提交生成。
- 0–69：REBUILD或返回事实拥有者。

分数、Risk Level和内部QA字段不得进入templates/10_video_prompt.md。

---

# Revision Handling

如果用户指出生成问题：

优先判断问题属于哪一层。


例如：

人物都面向镜头：

属于：

Spatial / Camera问题。


雨伞消失：

属于：

Prop Continuity问题。


人物突然拥抱：

属于：

Motion / Performance问题。


角色换脸：

属于：

Character Consistency问题。


格式不正确：

属于：

Template Mapping问题。


修改时：

只处理对应问题。


禁止：

无必要重新设计全部镜头。


---

# Error Routing

如果问题属于：

角色设计：

返回：

Character Asset Workflow。

角色有对白但Confirmed Voice Profile缺失或Pending时，不返回Character Asset Workflow，也不调用AUDIO模块；使用`No Voice Asset`分支继续STATE-08。只有已经存在的声音资产与Active CHAR Version发生身份冲突时，才停止使用冲突资产并返回其事实/版本拥有者处理；不得留在STATE-08自由推导基础音色。


如果属于：

环境设计：

返回：

Environment Asset Workflow。


如果属于：

场景拆解：

返回：

Scene Breakdown Workflow。


如果属于：

镜头设计：

返回：

Shot Design Workflow。


如果属于：

Sequence Coverage、Generation Unit或State Ledger设计：

返回：

Sequence Planning Workflow。


如果属于：

Clip Production：

返回：

`10_clip_production_workflow.md`。

Reference Budget审计缺失、连续性帧加入后超限或裁剪/整合计划错误属于Clip Production，返回STATE-07；若唯一可行方案需要新建环境/道具/空间/动作总图，则返回对应STATE-03资产Workflow完成真实生成与确认，不能留在STATE-08虚构名称。

`Clip End-State Record / Next-Clip Carryover`缺失、与Exit / Spatial Blocking / Handoff冲突，或Reference Selection / Routing在STATE-07漏选、选错、过量时返回STATE-07只修Affected Clip；若记录与SHOT / Blocking事实冲突返回STATE-06，若资产本身版本/形态错误返回STATE-03。上游选择正确而STATE-08仅序列化遗漏、用途误写或误把未选资产加入`参考资产：`时，留在STATE-08只修Affected Clip Prompt。

Clip Preflight在STATE-07记录缺失、连续性主分类错误、World-State/角色数量/空间构图/道具状态/转场五要素设计不完整或Reference Asset Check失败时，返回STATE-07修正Affected Clip；若根因属于资产形态/版本返回STATE-03，属于Shot / Blocking /转场设计返回STATE-06。只有上游Preflight正确而最终字段转译遗漏时留在STATE-08修正。


如果属于：

视频执行：

留在：

Video Generation Workflow。


如果只属于：

最终格式：

重新调用：

templates/10_video_prompt.md


不重新设计镜头。


---

# Output Responsibility

本Workflow最终交付的是：

经过Seedance适配、按Confirmed Clip一对一组织且保留正式Shot顺序的独立G段视频执行信息。每个Clip只产生一条连续Prompt；Clip内可包含多个Shot，但不得拆成多个Shot Prompt。


最终呈现方式：

由：

templates/10_video_prompt.md


决定。


本Workflow不得：

自行输出另一套结构。

---

# State Update

开始本Workflow时，按照`references/project_state_contract.md`写入Selected State Source并同步或输出Portable State：

- Current State：STATE-08
- State Status：IN_PROGRESS
- Active Workflow：11_video_generation_workflow.md

只有最终Prompt完成Template Mapping、Final Validation并成功落盘后：

- State Status：COMPLETE
- Last Completed Step：STATE-08 Clip-based Video Prompt / Video Generation
- Last Successful Checkpoint：已验证的STATE-08 Prompt Revision
- Active Artifacts：登记Prompt路径与Revision ID
- Next Workflow：13_review_workflow.md

任何检查失败时不得写STATE-08 Complete。应按Error Routing返回对应Workflow，并保留最后一个成功Checkpoint；状态字段、Portable Required Field Writeback与同步只按`references/project_state_contract.md`执行。


---

# Final Principle

STATE-08 Clip-based Video Prompt / Video Generation的核心任务：

不是：

写一个漂亮Prompt。


而是：

把已经完成的电影生产设计：

转换成视频模型能够稳定执行的信息。


核心优先级：

剧情正确

>

资产一致

>

空间清晰

>

动作连续

>

人物表演

>

摄影逻辑

>

光线连续

>

声音与剪辑

>

模型执行稳定性


最终格式：

不属于Workflow。


最终格式唯一来源：

templates/10_video_prompt.md
