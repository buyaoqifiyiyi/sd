# Asset Rules

# AI影视资产管理规则


## Rule Purpose


用于保证影视资产稳定性。


所有视觉生产必须建立资产基础。



---

# 01 Asset First Rule


AI影视制作必须遵循：

Asset First。



流程：


Character Asset

+

Environment Asset

+

Prop Asset

+

FX Asset（仅在剧情需要正式效果资产时）


↓

Scene

↓

Shot

↓

Video



---

# 02 Required Asset Categories


影视项目必须识别：


## Character Asset


人物资产。



包括：

外貌。

年龄。

服装。

身份。



---

## Environment Asset


环境资产。



包括：

地点。

建筑。

空间结构。

时代。



---

## Prop Asset


道具资产。



包括：

关键物件。

剧情物品。

视觉标志。



---

## FX Asset


需要复用、绑定、跨镜头继承或产生持续后果的效果资产。


包括：


天气与大气效果。

火、烟、水、碎屑与破坏。

变形、能量与自发光效果。


单次、低复杂度且无需连续追踪的效果可以标记为Inline Effect，不强制建立正式FX Asset。



---

# 03 Asset ID Rule


正式资产必须拥有唯一ID。


格式：


Character:

CHAR-001


Environment:

ENV-001


Prop:

PROP-001


FX:

FX-001


Scene:

SCENE-001


Shot:

SHOT-001



---

# 04 Asset Registry Rule


所有资产必须登记：


asset_registry.md



包含：


资产ID。

名称。

类型。

状态。

版本。

Active Version。

Canonical References。

Immutable Traits。

Mutable State Dimensions。

Dependencies与Downstream Usage。

Visual Production Status。

Asset Tier。

Board ID与Item ID。

Prompt Status、Image Status与Confirmed Status。

Prompt Revision与Prompt Confirmation。

Candidate References与Image Confirmation。

正式资产锁定与变更必须服从：

references/asset_lock_contract.md



---

# 05 Asset Priority Rule


资产使用优先级统一服从references/asset_lock_contract.md。

Canonical Reference必须先登记到Asset Registry并绑定Active Version；Registry之外的参考不得独立覆盖已锁资产。



---

# 06 No Redesign Rule


已有资产：

禁止重新设计。


包括：


角色脸型。

服装。

环境结构。

关键道具。



除非用户明确要求修改。

用户明确修改时也必须先创建Candidate Version、完成影响检查并切换Active Version，不得在下游Prompt中直接改写资产。


## Character Appearance / Form Hard Lock

角色已有用户明确指定的外观基准，或已有Active CHAR Version与Canonical References时，必须执行`references/asset_lock_contract.md`中的Canonical Character Appearance And Form Lock。

该角色资产包是后续全部外貌与形态内容的唯一基准。必须锁定脸型、五官、年龄感、发型、头饰、体型、身高与身体比例、服装形制、主配色与辅助配色、物种形态、羽毛/毛发等物种特征，以及非人角色身体结构。不得用动作图、比例图、场景示意、Storyboard、海报、封面、风格参考、Shot Design、Prompt或生成结果反向重设计角色。

若任务只改变动作、姿势、表情、机位、景别、构图或镜头运动，只有这些维度可以变化。任何超出Active Version的外观变化必须返回Character Asset Workflow建立Candidate Version并经用户批准；不得在下游直接修改。非人角色被锁定为本体形态时不得擅自拟人化，例如孔雀本体不得改成人形或半人形。



---

# 07 Asset Gate Rule


未完成资产阶段：

禁止进入：


Scene Breakdown。


Shot Design。


Video Generation。



---

# 08 Asset Binding Rule


Scene必须绑定：


Character。

Environment。

Prop。



Shot必须绑定：


Scene。


并绑定该镜头实际出现的：

Character。

Environment。

Prop。

FX。


未出现或已明确不适用的资产类别不得为了填表虚构绑定。


Video必须绑定：


Shot。


---

# 09 Two-Tier Asset System Rule

STATE-02必须为每个CHAR、ENV、PROP执行Asset Tiering Decision；Asset Tier与Primary / Secondary / Background优先级相互独立。

满足任一条件即优先`Core`：主角或固定角色、跨场景或跨Clip反复出现、承担强剧情/角色/品牌识别、需要高一致性、关键场景、剧情关键道具。Core角色独立制作三视图/面部特写/必要状态变体；Core环境独立制作主参考图/多视角/关键区域图；Core道具独立制作主参考图/必要状态或细节图。

不满足Core条件的一次性配角/群演、群体背景角色、同类家具与环境小物、氛围装饰、低频道具通常为`Support`。Support不得逐个制作完整独立资产包，必须按同一资产类型和相近用途形成Support Reference Board；角色、环境、道具不得跨类型混板。

每板建议4—9个对象，风格统一但必须通过轮廓、服饰/材质、颜色、比例和功能差异清楚区分。每板必须有稳定Board ID，每个对象必须有稳定Item ID；确认后不得重排或复用。后续只按`<Board Name> / <Board ID> / <Item ID>`引用。

Core与Support执行同一双确认闭环。未确认Prompt不得生成图；未确认图片不得把Core、Board或Item标记confirmed。若Support对象在制作中被发现实际需要高一致性、独立状态或关键识别，返回STATE-02复核并升级Core，不得在Support分支暗中制作完整独立套图。

正式FX Asset继续服从既有Formal FX / Inline Effect规则，本Two-Tier变更不改其Workflow。

---

# 10 Visual Asset Production Gate

所有STATE-03视觉资产，包括Character、Environment、Prop与正式FX Asset，必须按以下顺序生产：

```text
Asset Design
→ Image Prompt Generation
→ 用户确认提示词
→ Image Generation
→ 用户确认图片
→ Asset Registry
```

## Prompt Gate

- Image Prompt必须是完整、可直接生图的执行文本，不得只输出外观说明、关键词清单或“用于后续生成”的参考要求。
- Prompt至少明确主体身份、可见结构、构图/视角、材质/服装、光影、项目视觉风格、一致性限制、必要负面限制与适用生成参数。
- `Visual Production Status: Prompt Draft`时必须停止并等待用户确认。
- 同步状态必须为`Prompt Status: Draft`、`Image Status: Not Generated`、`Confirmed Status: No`。
- 只有用户对当前Prompt Revision明确说出“确认生成该图”“按此Prompt生成”或其他无歧义、指向该具体Revision的生成授权后，才可写`Prompt Confirmed`并调用图片生成工具。单独的“继续 / 下一步 / 下一个 / next”始终只是纯推进指令，即使只有一个待确认Prompt Package也不得视为Prompt确认或图片生成授权；必须服从`rules/progression_rules.md`。
- Prompt发生任何实质修改后返回`Prompt Draft`，旧确认不得自动继承。

## Image Gate

- 图片生成后只写`Image Generated`，并把文件或受控外部ID登记为Candidate References。
- Image Generated时同步状态必须为`Prompt Status: Confirmed`、`Image Status: Candidate`、`Confirmed Status: No`。
- 未经用户确认图片，不得写Canonical References、Active Version、`Status: Active`或`Asset Confirmed`。
- 图片被拒绝时，保留其生成记录但不得升级为Canonical Reference；若只需重生则回到已确认Prompt，若需改Prompt则回到`Prompt Draft`重新确认。
- 只有用户确认图片后，才能写`Visual Production Status: Asset Confirmed`，完成Canonical References、Active Version、Approval Basis与Approved At登记。
- Asset Confirmed时同步状态才允许为`Prompt Status: Confirmed`、`Image Status: Confirmed`、`Confirmed Status: Yes`；Support还必须记录Board ID、Item ID与图中区域/标签对应关系。

## Tool Availability

当前环境不能直接生成图片时，最低交付仍是完整Image Prompt与明确的Prompt确认Checkpoint。用户确认后保持STATE-03 `IN_PROGRESS`，等待外部生成图片回传或图像工具恢复；不得把纯文字设定登记为已确认视觉资产。


## Downstream Character Lock Inheritance Gate

Asset Registry登记Active CHAR Version后，以下阶段和产物必须显式继承同一版本及其适用Canonical References：STATE-04 Visual Development与Poster/Key Art、STATE-05场景示意、Optional Storyboard、STATE-06 Detailed Shot Design、STATE-07 Clip Production、STATE-08图片/视频Prompt与最终视频生成、STATE-09 Review，以及角色设定图、动作状态图、比例图和封面。

任何阶段发现新参考、风格指令、Prompt文本或生成结果与锁定角色资产冲突，必须以锁定资产为准并拒绝冲突内容；不得折中拼接不同外貌。只有按Change Protocol获批并切换的新Active Version可以改变继承基准。

