# Asset Discovery Workflow

# 资产发现流程


## Workflow Purpose


本Workflow负责：

根据剧本分析结果，

确定AI影视项目需要制作的视觉资产。


目标：

建立完整资产需求清单。

为CHAR、ENV、PROP执行Asset Tiering Decision，确定Core Asset或Support Asset及其制作方式。

为后续资产制作提供依据。



本阶段：

不制作资产。


---

# Workflow Position


当前阶段：


STATE-02 Asset Discovery



前置阶段：


STATE-01 Script Analysis



下一阶段：


STATE-03 Asset Development



---

# Input


输入：


02_script_analysis_workflow输出结果。


读取：

references/asset_lock_contract.md


project_bible.md


project_status.md

它表示按优先级选定的State Source；普通Chat本机Root不可读时使用Portable State。状态写入服从references/project_state_contract.md，记录State Status、Checkpoint、Active Artifact与Revision ID，并按环境同步或输出更新后的Portable State。



包括：


Character List。


Environment List。


Prop Candidate List。


FX Candidate List。


Visual Requirement。



---

# Asset Discovery Process


## 01 Character Asset Discovery


根据人物分析结果：

确认需要制作的角色资产。



输出：


Character Asset List。



格式：


CHAR-001


名称：


身份：


剧情作用：


出现阶段：


视觉需求：


参考需求：

Asset Tier：Core / Support

Tier Decision Basis：

Board ID：Core写`Not Applicable`；Support写稳定Board ID

Item ID：Core写`Not Applicable`；Support写板内稳定编号



---

## 02 Environment Asset Discovery


根据环境分析结果：

确认需要制作的环境资产。



输出：


Environment Asset List。



格式：


ENV-001


名称：


地点类型：


剧情作用：


空间需求：


视觉需求：

Asset Tier：Core / Support

Tier Decision Basis：

Board ID：

Item ID：



---

## 03 Prop Asset Discovery


根据剧情物件分析：

确认关键道具资产。



输出：


Prop Asset List。



格式：


PROP-001


名称：


剧情作用：


重要程度：


视觉需求：

Asset Tier：Core / Support

Tier Decision Basis：

Board ID：

Item ID：



---

## 04 FX Asset Discovery


识别需要复用、绑定、跨镜头继承或保留物理后果的效果需求。


输出：


FX Asset List。


格式：


FX-001


名称：


类别：


剧情作用：


触发条件：


涉及资产：


连续性需求：


制作方式：正式FX Asset / Inline Effect / 后期合成待定


以下情况优先建立正式FX Asset：

- 多镜头复用
- 影响角色、环境或道具状态
- 需要固定外观、方向、强度或生命周期
- 具有关键叙事作用


---

# Asset Tiering Decision

Asset Tier与后文Primary / Secondary / Background制作优先级是两个独立维度。Asset Tier只决定STATE-03采用“独立资产包”还是“同类Support Reference Board”；Priority继续决定生产先后，不得互相替代。

本Two-Tier Asset System适用于CHAR、ENV与PROP。正式FX Asset继续使用现有Formal FX / Inline Effect / 后期合成判定，本次不强制套用Core / Support。

## Core Asset

CHAR、ENV或PROP满足下列任一条件时优先判为`Asset Tier: Core`；Core条件与Support表面特征冲突时，Core优先：

- 主角或固定角色
- 跨场景或跨Clip反复出现
- 承担强剧情识别、角色识别或品牌识别
- 需要高一致性和跨阶段重复调用
- 关键场景或主要表演空间
- 剧情关键道具

Core Asset在STATE-03独立制作：核心角色建立独立三视图、面部特写与必要状态变体；核心环境建立独立主参考图、多视角与关键区域设定图；核心道具建立独立主参考图与必要状态/细节图。

## Support Asset

不满足Core条件，且主要承担补充、背景、氛围或低频功能时判为`Asset Tier: Support`，典型包括：

- 一次性配角、群演
- 群体背景角色
- 同类家具与环境小物
- 氛围装饰
- 低频道具

Support Asset不得逐个制作完整三视图或完整独立资产包。STATE-02必须先按同一资产类型和相近生产用途分组，形成Support Reference Board计划；不得把角色、环境和道具混装进同一Board，也不得为了凑数量虚构剧本中不存在的对象。

每张Board建议包含4—9个对象，风格统一但个体清晰可区分，重点展示轮廓、服饰或材质、颜色、比例与功能差异。少于4个同类对象时可在不新增剧情对象的前提下建立较小Board并记录理由；超过9个时拆分为多板。

每个Board必须具有全局稳定的`Board ID`，例如`BOARD-CHAR-001`、`BOARD-ENV-001`、`BOARD-PROP-001`；板内每个对象具有稳定`Item ID`，例如`A-01`、`A-02`、`A-03`。后续引用格式固定为`<Board Name> / <Board ID> / <Item ID>`。Item ID一经确认不得重排或复用；新增对象使用下一可用编号。

STATE-02对每张计划Board至少记录：Board Name、Board ID、Asset Type、Included Asset IDs、Item ID Mapping、共同风格约束、逐项差异锚点、建议构图、下游引用方式与生产顺序。

---

# Asset Priority Classification


对资产进行分类：



## Primary Asset


主要资产。


例如：

核心角色。

核心场景。

关键道具。

关键FX。



---

## Secondary Asset


辅助资产。


例如：

普通配角。

次要环境。

背景物件。



---

## Background Asset


背景资产。


例如：

群众。

普通装饰。

环境细节。



---

# Asset Registry Update


完成资产发现后：

更新：


asset_registry.md



登记：


资产ID。


资产名称。


资产类型。

Asset Tier。

Board ID。

Item ID。


优先级。


制作状态。

Prompt Status。

Image Status。

Confirmed Status。

其中Core Asset的Board ID与Item ID写`Not Applicable`；Support Asset两字段必填。STATE-02只能初始化状态，不得提前确认：`Prompt Status: Not Started`、`Image Status: Not Generated`、`Confirmed Status: No`。



---

# Output

最终输出必须使用：

templates/03_asset_discovery_prompt.md

本Workflow负责资产判断、优先级与Registry更新；Template独占清单结构。


输出：


## Character Asset List


角色资产清单。



## Environment Asset List


环境资产清单。



## Prop Asset List


道具资产清单。



## FX Asset List


正式FX Asset、Inline Effect与后期合成待定项清单。



## Asset Priority List


资产优先级。


## Asset Tiering Decision List


逐项记录Core / Support、判定依据、制作方式以及与Priority的独立关系。


## Support Reference Board Plan


按同类型列出Board ID、Board Name、Included Asset IDs、Item ID Mapping、4—9对象建议或例外理由、视觉差异锚点与后续引用格式；没有Support Asset时明确写`Not Applicable`。



---

# Forbidden Actions


当前阶段禁止：


禁止生成角色图片。


禁止生成环境图片。


禁止生成道具图片。


禁止在本阶段直接生成最终FX画面或视频。


禁止设计镜头。


禁止生成Storyboard。


禁止生成Video Prompt。



---

# Completion Condition


完成：


角色资产清单。


环境资产清单。


道具资产清单。


FX资产需求清单，或明确当前项目无需正式FX Asset。


asset_registry更新。

全部CHAR、ENV、PROP已经完成Asset Tiering Decision；全部Support Asset已经分配稳定Board ID与Item ID并形成同类参考板计划。



然后更新：


project_status.md

完成决定作出后，只按`references/project_state_contract.md`执行状态字段、Portable Required Field Writeback与同步；本Workflow不复制同步失败语义。



状态：


STATE-02 Complete



---

# Next Workflow


进入：


04_character_asset_workflow.md


05_environment_asset_workflow.md


06_prop_asset_workflow.md


15_fx_asset_workflow.md（存在正式FX Asset需求时）



---

# Core Rule


Script Analysis回答：


“故事中有哪些人物、地点、物件和关键效果。”


Asset Discovery回答：


“哪些内容需要制作成正式视觉资产，以及应独立制作还是按同类型进入Support Reference Board。”


Asset Development回答：


“如何制作这些资产。”


三个阶段必须保持独立。
