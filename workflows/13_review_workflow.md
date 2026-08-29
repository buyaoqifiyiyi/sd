# SD Film Review Workflow

# AI影视质量审核流程


## Workflow Purpose


本Workflow负责：

对AI生成结果进行影视质量审核。


目标：

确认：

人物。

环境。

道具。

FX。

动作。

表演。

声音。

镜头。

风格。


是否符合项目要求。


---

# Workflow Position


当前阶段：

STATE-09



进入条件：


STATE-08 Clip-based Video Prompt / Video Generation Complete



---

# Core Principle


审核不是简单判断：

“好不好看”。


审核重点：


是否符合：

Project Bible。


是否符合：

Asset Registry。


是否符合：

Shot Design。



---

# Entry Gate


执行前必须确认：

已读取：

- references/project_state_contract.md
- templates/16_review_report.md
- knowledge/quality/index.md
- knowledge/quality/shot_qa.md
- knowledge/quality/continuity_pair_qa.md
- knowledge/quality/execution_risk.md
- knowledge/quality/prompt_scorecard.md（审核STATE-08 Prompt时）
- knowledge/spatial_blocking_layer.md
- knowledge/director_decision_layer.md
- knowledge/knowledge_application_reflection.md
- knowledge/camera_language/camera_movement/selection_matrix.md
- knowledge/camera_language/camera_movement/index.md，以及受审SHOT已确认主运镜对应的原子知识文件


存在：


project_bible.md


project_status.md

这里表示按`references/project_state_contract.md`选定的State Source；普通Chat本机Root不可读时使用Portable State。


asset_registry.md


SHOT设计

Director Decision Notes（按受审Scene / Shot Group）

每个受审Scene的Confirmed Spatial Blocking Result；若Decision为双锁，追加已核对的Top-down Blocking Map，若为Structured Text Fallback则读取其原因与风险


Sequence Plan（如适用）


生成视频结果



---

# Review Pipeline


审核顺序：


视觉一致性

↓

资产一致性

↓

FX连续性

↓

表演与对白执行

↓

声音连续性

↓

Coverage与Generation Unit完成度

↓

动作质量

↓

Spatial Continuity QA

↓

Director QA

↓

镜头质量

↓

项目风格



---

# 01 Character Review


检查角色一致性。



## Identity


检查：


□ 面部一致


□ 年龄一致


□ 发型一致


□ 身体比例一致



---

## Costume


检查：


□ 服装一致


□ 材质一致


□ 配饰一致



---

# Failure Return


如果角色错误：


返回：

Character Asset Workflow



禁止：

仅修改Prompt修复。



---

# 02 Environment Review


检查环境一致性。



包括：


□ 建筑结构


□ 空间关系


□ 时间


□ 天气


□ 光影



---

# Failure Return


环境错误：


返回：

Environment Asset Workflow



---

# 03 Prop Review


检查关键道具。


包括：


□ 外观一致


□ 尺寸合理


□ 使用正确



---

# Failure Return


道具错误：


返回：

Prop Asset Workflow



---

# 04 FX Review


存在FX时检查：


□ 触发、来源与效果阶段正确


□ 方向、强度、尺度与覆盖范围合理


□ 角色、环境、道具和光线交互成立


□ 结束状态、残留后果与下一镜连续


□ 效果声音尾部与画面同步


---

# Failure Return


FX身份或生命周期定义错误：

返回：

FX Asset Workflow。


逐镜效果阶段或复杂度错误：

返回：

Shot Design Workflow或Video Generation Workflow。


局部执行瑕疵：

进入Editing Workflow。


---

# 05 Performance Review


检查：


□ 表演目标与剧情一致


□ 微表情、呼吸、视线与身体动作自然

□ 表演具有刺激、注意转移、局部面部/身体变化、行动选择与稳定结束状态，没有只写喜怒哀乐

□ 表情符合角色基线；瞳孔、脸红、泪液、颤抖等条件性结果没有被机械套用

□ 压抑、伪装与混合情绪的公开状态、短暂泄漏和恢复过程清楚


□ 情绪强度连续，没有无原因重置


□ 多人反应顺序和视觉重点清晰


□ 对白说话者、倾听者与口型可执行

□ 表情、说话、哭笑、吞咽、呼吸和遮脸动作不存在容量冲突


---

# Failure Return


表演目标或节拍设计错误：

返回Shot Design Workflow。


局部表演执行错误：

返回Video Generation Workflow或进入Editing Workflow。


---

# 06 Sound Review


检查：


□ 对白身份、台词、音色与口型匹配


□ 环境声和动作声符合空间与材质


□ STATE-08每镜“音效”不含背景音乐、配乐、BGM、歌曲、节拍或“无配乐”等音乐说明

□ 未触发用户显式背景音乐例外时，STATE-08【反向提示词】首个非空内容行逐字为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”；触发例外时只豁免用户明确指定的Clip

□ 后期阶段如规划配乐，其功能与进入退出点已确认，且没有回写STATE-08音效字段；静默具有明确目的


□ 跨镜声场、Sound Bridge与声音尾部连续

□ Sound Bridge只使用剧情内声音，没有使用背景音乐或配乐替代同期声锚点


---

# Failure Return


声音设计逻辑错误：

返回Video Generation Workflow。


仅需局部混音、同步或后期修正：

进入Editing Workflow或后期流程。


---

# 07 Sequence Coverage Review


存在Sequence Plan时检查：


□ 所有Required COV在最终结果中拥有可见完成证据


□ 关键人物反应、动作结果、道具或FX后果没有漏拍


□ Optional内容没有挤压Required Coverage


□ UNIT顺序、Entry / Exit Anchor与State Ledger连续


□ 单个UNIT重试没有破坏已接受的前序素材


---

# Failure Return


Coverage设计遗漏或UNIT边界错误：

返回Sequence Planning Workflow。


COV已经正确但SHOT未承担：

返回Shot Design Workflow。


设计正确但生成结果漏拍：

返回Video Generation Workflow或Editing Workflow。


---

# 08 Motion Review


检查视频运动。


包括：


□ 动作自然


□ 人物运动合理


□ 物理关系正确


□ 无明显变形



---

# Failure Return


动作错误：


返回：

Shot Design Workflow



---

# Spatial Continuity QA

逐Scene和逐Clip把Confirmed Spatial Blocking Result（Structured Blocking Map、Text Spatial Rules与适用Top-down Map）依次对照Detailed Shot Design、Confirmed Clip Production Plan、STATE-08 Prompt和生成结果。

检查：

□ 场景复杂度判定正确：简单场景可Text-Only；双人明显走位、3人以上、打斗 / 追逐 / 多人进出、复杂道具空间、连续多Clip或严格180度轴线已优先双锁，或有明确Structured Text Fallback原因与风险

□ 场景边界、门窗 / 桌椅 / 柱 / 障碍和关键道具保持原位置，没有空间结构漂移或人物穿越固定物

□ A / B / C在每个适用机位下的左右、前后、高低、面对方向、视线目标和距离符合Text Spatial Rules；没有无动作换边、层级交换、随机转身或瞬移

□ 每名角色从起点经已锁定路径到终点；谁移动 / 谁不动正确，移动过程没有断裂、跳步、错误转向或在Clip边界被重置

□ C1 / C2 / C3位置、朝向和视锥与设计一致；摄影机保持在授权轴线侧，没有无授权跨越180度轴线；有意越轴具有中性机位 / 连续可见路径、固定地标和稳定新轴线侧

□ 关键视线、攻击、武器、追逐、交接、水流 / 能量等Connector保持来源 → 路径 → 目标方向，没有反向或错主体

□ 道具身份、位置、朝向、持有者、交接过程和结束状态连续，没有无动作换手或位置跳变

□ 每个Continuous Handoff满足`Previous Clip End State → Next Clip First Frame Reference`：Direct逐项继承；Reference-Only只改变已授权机位 / 景别 / 构图；Motivated Discontinuity明确Not Inherited、断点与重建依据

□ Top-down Blocking Map仅作为Planning Reference，没有被登记为Canonical Asset、Storyboard或写入STATE-08【参考资产】

任何反轴、左右漂移、人物换边、移动路径断裂、瞬移、道具位置 / 持有状态不连续、摄影机跨轴或尾帧—首帧不一致，均必须定位到具体Scene、SHOT、CLIP、Boundary和字段，不得只写“空间不连贯”。

## Spatial Continuity Return Route

- Spatial Blocking Decision、地图 / 文字规则、SHOT站位 / 路径 / 轴线或边界设计缺失 / 错误：返回STATE-06，只修Affected Scene / SHOT及相邻边界。
- STATE-06正确，但Clip起始 / 结尾、尾帧用途或`Previous Clip End State → Next Clip First Frame Reference`组织错误：返回STATE-07，只修Affected Clip与Cross-Clip Ledger。
- STATE-06 / 07正确，仅STATE-08转译、生成执行或参考帧使用偏差：返回STATE-08，只修Affected Clip Prompt或重试该Clip。
- Environment / Prop / Character资产的固定空间事实本身错误：返回对应STATE-03资产拥有者；Scene剧情动作或结构事实不足：返回STATE-05。
- 复杂场景缺少Confirmed Spatial Blocking Result属于Hard Gate失败；不得用审美分数覆盖，也不得只在Prompt里补一句“保持一致”。

Spatial Continuity QA结果映射到`templates/16_review_report.md`已有的`Shot-Level QA → Space / Action`、`Adjacent-Shot Continuity QA`与`Problems And Corrective Actions`，不新增Review Template字段。

---

# Director QA


逐Scene / Shot Group对照Director Decision Notes，并逐Clip检查其在Clip Movement Plan、STATE-08 Prompt或生成结果中的实现。Director QA审核“为什么这样拍及观众如何经历”，不替代Camera Language QA的技术核对，也不重新进行Knowledge选择。


检查：


□ 每个镜头是否有明确叙事目的；能否说明观众在当前段落应知道什么、感受什么、等待什么，而不是只提供漂亮画面


□ 人物调度是否通过距离、视线、站位、身体朝向、先后动作、靠近/后退或停顿表达人物关系；是否存在人物只是并排站立说台词的平铺直叙


□ 镜头运动是否有明确理由、触发和停止点；Static / Locked-Off是否保护表演、信息或等待；是否存在无叙事收益的环绕、推拉、升降、甩镜、长镜头或其他纯炫技


□ 构图与Lens / Distance是否分配观察权、亲密度、隔离感、环境压力或负空间，并在关系变化后形成可读终点


□ 色彩/灯光是否承担功能：变化具有真实光源、空间移动或剧情事件依据，并改变信息/关系可读性；没有功能性变化时是否保持光态、色态、肤色和资产固有色稳定


□ 表演应外放或克制的尺度是否清楚；谁先反应、谁延迟、谁泄漏、谁压住，以及结束状态是否与关系和情绪连续


□ 声音哪里加强、哪里留白是否有设计；环境底声、同步Foley/动作声、对白/呼吸、剧情内声源和声音尾部是否承担空间、等待、转折或余韵，而不是平均铺满


□ Editing / Rhythm是否有建立、累积、高潮、停顿、释放或余韵；视觉高潮与最克制镜头是否有层级，摄影强调是否平均铺满整段


□ 是否存在两种相反失败：一是知识、运镜、构图、色光或声音堆砌造成纯炫技；二是所有镜头只按剧情顺序平铺、没有关系调度、观众等待、高潮或留白


□ Director Decision Notes是否保持内部：正式Seedance Prompt没有出现Notes标题、十三维度、内部问答、候选/拒绝理由、Knowledge文件名或“因为导演决策所以……”等元说明


## Director QA Return Route

- Narrative Objective、Audience Experience、Character Relationship、Blocking或总体视听方向错误/缺失：返回STATE-06，只修Affected SHOT / Shot Group及相邻边界。
- 导演方向正确，但Clip主导镜头语言、节奏、调度、视觉高潮/留白或复杂度组织错误：返回STATE-07，只修Affected Clip。
- STATE-07保持正确，但Knowledge策略选择、执行转译或内部Notes泄漏：返回STATE-08，只修Affected Clip Prompt。
- 设计与Prompt均正确、仅生成或后期呈现偏差：进入Video Generation重试、Editing或对应局部修复；不得无必要重做上游。


---

# 09 Camera Review


检查摄影执行。


包括：


□ 景别正确


□ 运镜正确


□ 构图符合设计


□ 镜头节奏合理


□ 焦段倾向、摄影机距离与景别共同形成的空间尺度符合设计


□ 透视没有被错误归因于焦段，景深/虚化具有可成立的对焦与空间依据


□ 超广角脸形和边缘保持稳定，长焦无异常抖动、焦点游移或背景尺度抽动


□ 连续镜头的脸部几何、眼线、轴线、背景锚点和焦点状态兼容


## Camera Language QA

逐Clip对照Confirmed Detailed Shot Design中的Camera Language Decision、Confirmed Clip Production Plan中的Clip Movement Plan和STATE-08既有字段语义检查：

□ 每个SHOT的主运镜/Static与镜头目的、情绪功能、人物运动、空间任务和节奏阶段匹配

□ 每个主运镜已在最终执行信息中具体化为摄影机起点、侧位、路径、方向、速度/幅度、触发、人物配合、终点与稳定限制，不是只写术语

□ 没有连续慢推、连续轻微横移或“稳定中景+轻微运动”的无理由模板重复；同类主运镜连续3次以上均有逐镜叙事理由

□ 每个Clip具有明确主导镜头语言；超过4个Shot时通常至少存在2种不同运镜逻辑，例外具有连续动作、长镜观察或刻意重复的叙事理由

□ 多样性来自建立、跟随、揭示、靠近、克制、释放等叙事功能变化；没有为了“每镜不同”随机堆叠运镜

□ 视觉高潮镜头与最克制镜头均按Clip Movement Plan成立，摄影强调没有平均铺满整段

□ 运镜没有抢走表演、破坏关系轴、遮挡关键动作或把普通摄影机运动误当转场

□ Push In、Pull Out、Tracking、Side Tracking、Pan、Tilt、Crane、Handheld、Shoulder Follow、Dolly Tracking与Static优先得到使用；复杂Orbit / 360、穿墙、无人机或多段一镜到底均具有明确必要性、模型容量与稳定降级

□ Seedance复杂度可执行：单镜主路径清楚，无不兼容方向反转，人物/FX/口型与摄影机负荷不过载，结尾能够稳定



## Knowledge Application QA

审核STATE-08 Prompt或其生成结果时，对每个Clip做轻量检查，不重新进行完整创作选择：

□ 本次Prompt是否存在能够明显提升当前Clip、且不破坏一致性与Seedance稳定性的可用Knowledge，却完全没有调用或转译；若采用克制策略，是否明确说明它保护了什么

□ 运镜是否过少、过于单一，或无理由重复“缓慢推进 / 轻微横移 / 稳定中景”；若选择Static / Locked-Off，是否确实为表演、信息或稳定性服务

□ 色调是否只停留在“低饱和、冷暖对比、电影感”等笼统描述，而没有颜色来源、主辅强调层级、饱和度/明暗/偏色、肤色保护与稳定结束色态

□ 构图是否缺少由真实空间成立的前景 / 中景 / 后景层次、人物左右关系、负空间或视觉焦点变化，并且没有稳定终点

□ 人物表演是否仍然过于笼统，只写情绪名称而没有刺激、注意变化、视线 / 呼吸 / 手部或身体反应、行动选择与稳定结束状态

□ 声音设计是否只有环境音堆砌，缺少明确声源、同步动作声 / Foley / 呼吸 / 对白、空间距离、节拍重点或声音尾部

□ 是否知识堆砌：同一效果被Camera、Composition、Color / Tone、Lighting、Performance、Sound、Editing Rhythm或Director Style重复描述、加入互相竞争的技巧，或破坏剧情、资产、关系轴、动作 / 道具状态与跨镜连续性

□ 是否超出Seedance稳定执行范围：动作 / 口型 / FX / 摄影机负荷过高、路径过多、指令相反、缺少稳定终点或没有安全降级

□ 最终Prompt是否只保留具体可执行语义，没有只写知识名称、导演名字、模式ID或暴露内部Opportunity Check / Reflection Record

判定：明显可用知识完全遗漏、知识堆砌或执行转译失败，返回STATE-08只修Affected Clip；Camera Language Decision错误返回STATE-06，Clip Movement Plan或编排冲突返回STATE-07，剧情/资产/Visual Direction事实冲突返回对应拥有者。没有合格的增强技巧时，采用一条能具体保护表演可读性、连续性或Seedance稳定性的克制策略是合法结果，不得把“少动”本身判错。



---

# Failure Return


摄影错误：

返回：

Shot Design Workflow

细分返回路由：Camera Language Decision或逐镜主运镜选择错误返回STATE-06；Clip主导逻辑、重复规避或复杂度编排错误返回STATE-07；决策正确但STATE-08转译退化、路径不具体或违背计划时返回STATE-08。只修复Affected IDs及相邻边界，不无必要重做导演风格、资产或完整Pipeline。



---

# 10 Style Review


检查整体视觉。


包括：


□ 色调一致


□ 主色、辅助色、强调色拥有已确认来源与稳定空间位置，没有凭空新增彩色光源


□ 饱和度、明度/黑位/高光、综合色温与绿色—品红偏色符合Project Bible


□ 肤色、中性色、服装、道具和环境固有色保持可信且可识别


□ 高饱和无通道溢出，低饱和未丢失身份色，暗调不欠曝，霓虹光源与反射方向一致


□ 连续镜头无综合色彩闪变、肤色漂移、白平衡抽动、饱和度泵动或资产换色


□ 光影一致


□ 时代符合


□ 世界观符合


Color设计或综合色彩连续性错误：

项目级体系返回Visual Development；逐镜综合色彩变化返回Shot Design / Video Generation；光源或曝光错误返回Lighting；局部后期偏色可进入Editing Workflow。



---

# Quality Result


审核结果分为：


## PASS


符合要求。


进入：

后期流程。



---

## REVISE


需要修改。


返回对应Workflow。



---

## REBUILD


严重错误。


重新执行资产或镜头设计。



---

# Review Report


最终Review Report必须使用：

templates/16_review_report.md

Workflow负责判断Result、问题归属、最小修复与返回路由；Template独占字段名称、顺序和最终排版。

Review Report保存到：

`<active-project-root>/reviews/REVW-XXX.md`



---

# Status Update


审核后把`rules/completion_gate.md`作出的Review Decision按`references/project_state_contract.md`写回Selected State Source；本Workflow不复制Root / Portable同步顺序。

PASS：

- Current State：STATE-09
- State Status：COMPLETE
- Review Result：PASS
- Last Successful Checkpoint：已通过Review的Revision
- Next Workflow：Project Complete / Post

REVISE：

- Current State：STATE-09
- State Status：IN_PROGRESS
- Review Result：REVISE
- Affected IDs：具体镜头、资产、边界或UNIT
- Return Route：最小必要修复Workflow
- Recheck Scope：受影响内容及相邻边界
- Next Workflow：Return Route指定Workflow

REBUILD：

- Current State：STATE-09
- State Status：IN_PROGRESS
- Review Result：REBUILD
- Affected IDs：具体上游事实或设计范围
- Return Route：对应事实拥有者或Shot Design
- Recheck Scope：所有受影响下游产物

REVISE或REBUILD不得写STATE-09 Complete。修复后必须重新进入本Workflow。每种Review结果写入后都同步或输出完整Portable State，并执行references/project_state_contract.md的`Portable Required Field Writeback`；同步失败不得改变Return Route。



---

# Final Principle


AI生成不是终点。


审核才是生产闭环。
