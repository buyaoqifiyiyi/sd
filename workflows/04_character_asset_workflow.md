# Character Asset Workflow

# 角色资产制作流程


## Workflow Purpose


本Workflow负责：

根据资产需求清单，

制作正式角色资产。

角色资产包括视觉角色资产。


目标：

建立稳定、可复用的角色视觉资产。

角色声音身份不由本Workflow自动制作。只有用户显式请求音色提示词、音色制作、角色声音、Seed Audio、配音音色或声音资产时，才另行调用`20_seed_audio_voice_asset_workflow.md`；角色有对白本身不构成触发。



本阶段：

只处理角色资产。


---

# Workflow Position


当前阶段：


STATE-03 Asset Development



子阶段：


Character Asset Development



前置阶段：


03_asset_discovery_workflow



下一阶段：


05_environment_asset_workflow


06_prop_asset_workflow



---

# Input


输入：


03_asset_discovery_workflow输出结果。


读取：

references/project_state_contract.md

references/asset_lock_contract.md


asset_registry.md


project_bible.md



包括：


角色ID。

Asset Tier。

Tier Decision Basis。

Board ID与Item ID（Support必填；Core为`Not Applicable`）。


角色定位。


剧情作用。


视觉需求。


已确认角色身份与视觉设计依据。



---

# Character Asset Development Process


## Visual Production Sequence

角色视觉资产固定执行：

```text
Asset Design
→ Image Prompt Generation
→ 用户确认提示词
→ Image Generation
→ 用户确认图片
→ Asset Registry
```

每个Checkpoint都写入同一CHAR Version的`Visual Production Status`。Prompt确认与图片确认是两个独立Hard Gate；未经当前Prompt Revision确认不得生成图片，未经图片确认不得登记Canonical References、Active Version或confirmed asset。

## Two-Tier Execution Gate

进入制作前必须读取STATE-02的Asset Tiering Decision，不得在STATE-03凭方便重分层：

- `Asset Tier: Core`：对该CHAR独立执行角色定义 → 三视图提示词 → 面部特写提示词 → 必要状态变体提示词 → 用户确认提示词 → 生成图片 → 用户确认图片 → 登记。
- `Asset Tier: Support`：按STATE-02分配的同类型Board ID与Item ID进入Support Character Reference Board；不得为每个Support角色制作完整三视图、独立面部特写或完整独立资产包。Board建议包含4—9个对象，统一项目风格，同时用轮廓、服饰、颜色、比例和功能差异清楚区分每个Item。

Core与Support都必须执行同一双确认闭环。Support Board图片确认前，Board及其Item均不得标记confirmed；部分Item未获明确批准时，不得用对整板的含糊确认替代。

## Director-led Character Presence Pass｜Internal

读取STATE-02的Asset Dramatic Function、Narrative Priority与Casting Logic，只把会影响视觉资产执行的结果投影到现有角色定义、外观、服装与风格区域：Character Presence / Screen Presence、身份辨识优先级、主要表演载体与Performance Feasibility，以及剧情需要时的Costume / Silhouette Dramaturgy。服装、轮廓、姿态与动作习惯必须服务人物身份、关系或状态变化；不得为了“更有设计感”改写Canonical身份，也不新增固定Template字段。


## 01 Character Identity Confirmation


确认角色基础信息。


包括：


角色名称。


角色身份。


年龄。


性别。


时代背景。


人物定位。


性格与剧情中的情绪基调。



输出：

角色基础档案。



---

# 02 Appearance Design


设计角色视觉特征。


包括：


面部特征。


体型。


发型。


肤色。


气质。

Screen Presence与主要表演可读性；例如面部、身体轮廓、手部或姿态中哪一类必须在既定媒介和景别中保持可读。



要求：

保持角色唯一性。



---

# 03 Costume Design


设计角色服装。


包括：


服装类型。


材质。


颜色。


时代依据。


身份体现。

剧情适用时的服装/轮廓功能与状态变化；不适用时不机械增加换装或象征设计。



---

# 04 Character Style Definition


建立角色视觉规范。


包括：


整体气质。


表情特点。


动作习惯。


视觉关键词。



---

# 05 Voice Asset Isolation Gate

本Workflow不得读取`knowledge/sound_language/voice_generation.md`，不得输出Voice Profile、Seed Audio Voice Sample Prompt或Audio Reference，也不得把角色有对白视为音色制作授权。

只有用户当前请求显式要求音色提示词、音色制作、角色声音、Seed Audio、配音音色、声音资产或同义角色声音身份制作时，才退出本Workflow并读取唯一`workflows/audio_router.md`；只有其返回AUDIO Route才调用`workflows/20_seed_audio_voice_asset_workflow.md`并严格使用`templates/21_seed_audio_voice_asset.md`。该显式辅助模块的完成与否不进入Character Visual Asset Completion Gate。


---

# 06 Image Prompt Generation


先完成角色定义，再根据Asset Tier使用`templates/04_character_asset_prompt.md`输出完整可直接生图的Prompt Package。


包括：


Core角色三视图Prompt：同一画布中的正面、严格侧面、背面全身，锁定脸型、身体比例、发型、服装结构、材质与色彩。


Core角色面部特写Prompt：正面或轻微三分之二视角，锁定五官、脸型、肤质、年龄感、发际线与发型细节。


Core角色必要状态变体Prompt：只在Script Analysis或Asset Discovery确认湿润、污损、受伤、伪装、换装等剧情状态时生成；必须锁定角色身份和未变化的Immutable Traits。

Support角色参考板Prompt：按一个Board输出一条完整可执行Prompt，列明Board Name、Board ID、4—9个Item ID及逐项身份/轮廓/服饰/颜色/比例/功能差异，要求统一视觉风格、完整可见、标签清楚、对象之间不混脸不串服装。Support分支不输出逐角色三视图、逐角色面部特写或逐角色状态变体；确有高一致性或独立状态锁需求的对象必须返回STATE-02复核是否应升级Core，而不是在Support分支暗中扩展。


每条Prompt必须完整包含：主体身份、可见外观、姿态/视角、构图、服装与材质、光影、项目视觉风格、背景控制、一致性限制、必要负面限制、画幅/分辨率或当前图像工具所需参数。不得使用“同上”“参考前述”“保持一致”等脱离上下文后不可执行的占位表达。


输出时写：

- `Visual Production Status: Prompt Draft`
- `Prompt Revision`
- `Asset Tier`、`Board ID`、`Item ID`
- Core：三视图Prompt、面部特写Prompt、必要状态变体Prompt或`Not Required`依据
- Support：Support Character Reference Board Prompt、Item ID Mapping与对象差异检查
- `Prompt Status: Draft`
- `Image Status: Not Generated`
- `Confirmed Status: No`
- `Awaiting User Confirmation: Image Prompts`

到此必须停止并等待用户确认，不得同轮直接调用图片生成。


---

# 07 Prompt Confirmation Gate

只有用户无歧义批准当前Prompt Revision后，才记录：

- `Visual Production Status: Prompt Confirmed`
- `Prompt Status: Confirmed`
- `Image Status: Not Generated`
- `Confirmed Status: No`
- Prompt Confirmation原文或批准依据
- Confirmed By
- Confirmed At

如果用户要求修改Prompt，更新Prompt Revision并返回`Prompt Draft`；旧确认不得自动继承。


---

# 08 Image Generation

Prompt Confirmed后才能调用当前环境可用的图片生成工具。Core按已确认Prompt逐项生成三视图、面部特写与必要状态变体；Support按已确认Board Prompt生成整张Support Character Reference Board。

生成后记录：

- `Visual Production Status: Image Generated`
- `Prompt Status: Confirmed`
- `Image Status: Candidate`
- `Confirmed Status: No`
- Candidate References路径或受控外部ID
- 使用的Prompt Revision
- 生成工具/模型与关键参数
- Source / Provenance与权利/授权说明
- `Awaiting User Confirmation: Generated Images`

这些图片仍是Candidate References，不得写入Canonical References或Active Version。

如果当前环境无法直接生成图片，明确写`Image Generation Availability: Unavailable`，保留STATE-03 `IN_PROGRESS`；用户可以在外部用已确认Prompt生成并回传图片。回传图片完成来源记录后进入同一`Image Generated`状态。


---

# 09 Image Confirmation Gate

用户必须明确批准具体Candidate Reference。Support分支还必须能核对Board ID、Item ID与图中对应对象；批准前不得将角色视觉资产、Board或Item视为confirmed asset。

图片被拒绝时：仅重生则回到`Prompt Confirmed`；需要修改Prompt则返回`Prompt Draft`并重新走Prompt Confirmation Gate。


---

# 10 Asset Registry Update


只有图片确认后：


更新：


asset_registry.md



记录：


资产ID。


角色名称。


版本。


状态。

Asset Tier。

Board ID与Item ID。

Visual Production Status：`Asset Confirmed`。

Prompt Status：`Confirmed`。

Image Status：`Confirmed`。

Confirmed Status：`Yes`。

Prompt Revision与Prompt Confirmation。

Candidate References与Image Confirmation。


参考文件。

Active Version。

Canonical References。

Immutable Traits与Mutable State Dimensions。

本Workflow不新增、不修改也不要求Voice Asset字段。若同一CHAR Version已存在由显式AUDIO模块确认的Voice Profile或Voice Audio Reference，保持原记录不变，不得因本次视觉资产更新而删除或重写。

变更与锁定遵守references/asset_lock_contract.md。



---

# Output

最终输出必须使用：

templates/04_character_asset_prompt.md

本Workflow负责角色资产设计与确认；Template独占最终角色资产Prompt结构。


输出：


## Character Asset Sheet


角色资产表。



包含：


角色信息。


外貌设定。


服装设定。


视觉关键词。

角色声音资产不在本Workflow输出中；已有记录只保持不变。



---

## Character Reference Specification


角色参考规范。



用于：

图像生成。

视频生成一致性。



---

# Forbidden Actions


当前阶段禁止：


禁止重新分析剧情。


禁止拆解场景。


禁止设计镜头。


禁止生成Storyboard。


禁止生成视频Prompt。



禁止改变：

角色核心身份。


---

# Completion Condition


完成：


角色视觉设定。

Core角色的完整三视图、面部特写与必要状态变体提示词已经用户确认；Support角色所在Board的完整参考板提示词与Item Mapping已经用户确认。

Core独立图片或Support Reference Board已经生成或回传，并经用户明确确认；Support Item在Board确认前不得单独视为完成。


角色资产记录。


角色一致性规则。

视觉资产必须达到`Visual Production Status: Asset Confirmed`；`Prompt Draft`、`Prompt Confirmed`或`Image Generated`均不满足角色资产Completion Gate。Voice Profile、Seed Audio Voice Sample Prompt或Audio Reference是否存在，不属于STATE-03或Character Visual Asset Completion Gate，不得阻塞主Pipeline。



更新：


project_status.md

这里的状态文件是`rules/state_source.md`选定的Selected State Source；所有字段与写回只按`references/project_state_contract.md`执行。



状态：


STATE-03保持当前主STATE；在Last Completed Step记录Character Asset Development Complete。



---

# Next Workflow

每个STATE-03资产子流程完成后执行共享Completion Gate：所有Required Character / Environment / Prop / FX均为Active，或对应类别明确Not Applicable。

如果共享Gate通过：

- Current State：STATE-03
- State Status：COMPLETE
- Last Successful Checkpoint：全部Required Assets Locked
- Next Workflow：07_visual_development_workflow.md

如果未通过：保持STATE-03 IN_PROGRESS，进入下一个Pending Asset Workflow。

每次上述状态变化后都同步或输出更新后的完整Portable State，并执行references/project_state_contract.md的`Portable Required Field Writeback`；同步失败不阻塞STATE-03路由。


根据项目资产需求：

进入：


05_environment_asset_workflow.md


或


06_prop_asset_workflow.md



---

# Core Rule


Asset Discovery回答：

“需要哪些角色。”


Character Asset回答：

“Core角色具体是什么、用哪些已确认Prompt生成独立三视图/面部特写/必要状态图；Support角色位于哪张同类参考板、对应哪个稳定Item ID，以及哪些图片已被确认。”


角色资产完成后：

后续所有镜头必须引用该角色资产。

如果同一Active CHAR Version已经存在由用户显式请求并确认的Voice Profile或Voice Audio Reference，保持为声音系统Source State；如果不存在，下游不得反向触发AUDIO模块或返回本Workflow补齐。STATE-08默认不读取、不序列化也不声明声音资产状态；只有用户明确要求把声音控制写进当前视频模型Prompt时才按其Template最小投影。
