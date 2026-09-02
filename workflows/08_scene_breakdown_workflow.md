# SD Film Scene Breakdown Workflow

# AI影视场景拆解流程



## Workflow Purpose


将已完成资产体系的剧本内容转换为影视场景结构。


不是镜头设计。


不是视频Prompt。



---

# Workflow Position


当前阶段：

STATE-05


---

# Entry Gate


执行前必须确认：


存在：


project_bible.md


asset_registry.md



并确认：


CHAR资产完成。


ENV资产完成。


PROP资产完成。


项目需要的FX资产已完成或明确不适用。



---

# Forbidden Entry


如果资产未完成：

禁止执行场景拆解。



返回：

Asset Development。



---

# Scene Breakdown Logic

## Upstream Director Intent Projection

先读取Production-Locked Directable Screenplay及STATE-01随确认版本保留的轻量Scene Director Intent source data。按`knowledge/director_decision_layer.md`的连续性合同，将每场的Scene Objective、Audience Start / End State、Character Objective、Relationship Delta、Information Change / Reveal Strategy、Performance Opportunity / Peak、Spatial Evolution、Rhythm Intent与Transition Intent投影到正式SCENE边界、剧情作用、空间关系和节奏阶段。

这些source data只帮助发现Scene边界和保持导演意图，不新增用户可见固定字段，不允许改写Production-Locked剧情，也不创建SHOT / CLIP。若Intent与锁定剧本冲突，返回STATE-01最小修订Intent；若原项目没有独立Intent Artifact，则从锁定剧本已明确的行动、信息与关系变化提取最小可验证投影，不补造新剧情。

## Director Beat Map And Dramatic Geography

每个Scene按已确认剧情拆出最小充分Beat Map：Dramatic Beat、Relationship Beat、Information Beat、Performance Beat，以及Beat之间的因果与节奏。同步建立Dramatic Geography：固定空间、人物起始关系、可行动区域、信息来源、遮挡/揭示位置、距离或权力变化、Spatial Evolution和场景结束的稳定空间结果。

Scene Breakdown决定Reveal / Withhold / Delay / Confirm / Recontextualize在何个Beat发生，以及观众先于、同时或晚于人物知道；不提前决定具体镜头数量。

## Scene Camera Strategy

每个Scene形成一句到数句轻量策略，使用“观察 / 跟随 / 隐藏 / 揭示 / 压住 / 释放”等功能语言，说明Audience Position、注意力如何移动、何处Hold、何处允许靠近或离开、关系空间如何演化。禁止在此写35mm、85mm、特写、低机位、浅景深、Push In或正式SHOT参数；具体选择留给STATE-06固定决策顺序。

## Source Label Normalization

先把用户原文中的“镜头1 / 镜头2 / Scene 1 / 段落A / Clip A”等标题登记为`Source Script Label`，只用于原文追溯。它们不是正式Scene、Shot或Clip，不得决定下游数量与边界。

本阶段只创建`SCENE-xxx`。不得创建或预留`SHOT-xxx`、`CLIP-xxx`、Clip A/B/C、Gxx，也不得把Source Script Label直接改名为SCENE、UNIT或CLIP。


每个场景分析：


## Scene Identity


包含：


场景编号。


地点。


时间。


人物。


剧情目标。



---

## Spatial Relationship


分析：


人物位置。


空间结构。


视觉重点。



---

## Scene Purpose


确定：


剧情作用。

情绪目标。

视觉目标。


---

## Sequence Eligibility


每个Scene Breakdown完成后判断：

- 是否与前后Scene构成连续剧情段
- 是否包含密集叙事信息或复杂行动链
- 是否需要多个Generation Unit
- 是否需要Coverage完整性检查
- 是否存在跨Scene或跨生成单元状态继承


满足任一条件：

标记Sequence Planning Required，并进入workflows/16_sequence_planning_workflow.md。


不满足：

记录Sequence Planning Not Applicable及理由。



---

# Scene Asset Binding


每个Scene必须绑定：


角色资产。


环境资产。


道具资产。



格式：


SCENE-001


CHAR:

CHAR-001


ENV:

ENV-001


PROP:

PROP-001


FX:

FX-001（如适用）



---

# Completion Check


必须完成：


□ 所有场景编号


□ 场景资产绑定


□ 空间关系明确


□ 时间环境明确


□ 每个项目已判定Sequence Planning Required或Not Applicable

□ Source Script Labels已与正式SCENE命名空间分离，没有创建SHOT或CLIP ID

□ 每个Scene已读取并投影适用的Scene Director Intent；与锁定剧本冲突时已返回STATE-01，没有在本阶段静默改写

□ 每个Scene已形成Dramatic / Relationship / Information / Performance Beat Map、Dramatic Geography、Spatial Evolution与Reveal / Withhold timing

□ 每个Scene已形成轻量Scene Camera Strategy，且没有提前创建SHOT或具体摄影参数



---

# State Update


完成后：


project_status.md

它表示按优先级选定的State Source；普通Chat本机Root不可读时使用Portable State。更新服从references/project_state_contract.md，记录Scene Artifact、Sequence Eligibility、Checkpoint与Revision ID，并按环境同步或输出更新后的完整Portable State，执行其`Portable Required Field Writeback`。


更新：


STATE-05 Scene Breakdown Complete


如果Sequence Planning Required：

保持STATE-05，下一Workflow为16_sequence_planning_workflow.md。


如果Not Applicable：

STATE-05 Complete，允许进入STATE-06。



允许进入：


STATE-06 Detailed Shot Design，或先执行条件性Sequence Planning



---

# Forbidden


禁止：


直接输出镜头表。


直接生成视频Prompt。


跳过Shot Design。

按剧本段落或Source Script Label预划Clip、占位Clip或G Prompt Package。



---

# Output Format

最终输出必须使用：

templates/07_scene_design_prompt.md

Workflow负责Scene拆解、导演Beat Map、Dramatic Geography、Scene Camera Strategy、资产绑定与Sequence Eligibility判断；Template独占Scene输出字段、顺序和排版。

下一阶段仍由project_status.md中的Next Workflow决定：触发时进入Sequence Planning，否则进入Shot Design。
