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


## Reference Asset Eligibility Strengthening

STATE-07 / STATE-08中的视觉参考条目继续服从既有Asset Registry、Active Version、Canonical Reference、World-State与Reference Budget规则；本节只收紧“什么能被当作视觉参考条目”，不创建新的资产类型、Registry或Prompt字段。

视觉条目只有满足以下任一条件才有资格进入Clip计划或最终`参考资产：`：

- 已确认角色图、环境图、道具图、正式FX图、已确认参考板、合法首帧/尾帧、经Before-Single-Clip-Prompt Gate验证并绑定当前Blocking Signature的Confirmed `REF-SKETCH`，或其他当前Clip确实会向目标模型投喂/引用的真实视觉文件或受控ID；`REF-SKETCH`是受限Visual Blocking Reference，不新增Canonical资产类型；
- 已经确定必须由用户实际补入的视觉参考图，但当前文件尚未提供。此类条目必须明确写出具体图像对象、实际投喂用途和`待用户补充/待上传、未确认`状态，不得伪造路径、受控ID、上传或确认状态；A/B `REF-TAIL`继续按既有专用规则命名、计入Projected位并区分用途。

纯文字约束没有视觉输入资格，不得通过添加“参考”“说明”“用途”或编号伪装成资产。禁止项包括但不限于：站位说明、不可换边、人物距离、同坐一张板凳、道具数量限制、空间关系说明、动作/行为约束、禁止项、镜头/机位规则、首尾帧文字合同或Spatial Blocking Text Rules。它们必须按语义进入现有`空间关系`、`起始状态`、`道具状态`、`首帧参考`、`尾帧限制`、`反向提示词`或Spatial Blocking Rules；不得为了强调而重复塞入`参考资产：`。

如果约束对象本身已有真实视觉资产，应引用正式资产ID和图像，例如`PROP-BENCH-01｜双人钢琴凳`；`板凳参考说明｜用途：锁定两人共坐同一张板凳`不是资产。若缺的是必须新建并成为Canonical的正式CHAR / ENV / PROP / FX视觉资产，仍返回对应STATE-03 Workflow完成双确认，不得用“待补充”占位绕过Asset System。

既有Voice/Audio Reference是独立的非视觉输入支路，继续服从声音资产与Template规则；不得把普通文字音色说明伪装为Voice/Audio Reference。本次补强不改变该支路。

### Reference Selection / Routing Within Eligible Assets

在筛选前读取`references/asset_lock_contract.md`的`Reference Authority Map`：每张入选图在当前Clip必须有一个Primary Responsibility。该映射只决定当前输入解决哪类风险，不改变Canonical Purpose、资产版本或最终Prompt Schema。

视觉输入资格只是准入门槛，不表示所有合格资产都必须进入当前Clip。STATE-07 / STATE-08必须在World-State、当前Clip目标、`Continuity Risks`与下一Clip起始要求明确后，按实际风险选择最小充分参考集合；参考资产按需路由，不是越多越好，也不得把整个Asset Registry机械复制到`参考资产：`。

- 身份、脸型、服装、物种或基础外观漂移风险 → 当前Active Character Version的适用Canonical References。
- 场景结构、门窗/家具/地标、方位或空间尺度漂移风险 → 当前Active Environment Canonical References；站位、路径、轴线与摄影机侧继续由Confirmed Spatial Blocking与文字空间规则承担，Top-down Blocking Map本身没有视频视觉输入资格。
- 道具造型、材质、尺寸或可识别状态漂移风险 → 当前Active Prop Canonical References；持有者、左右手、位置、方向、接触和变化过程仍写入`道具状态`及起止状态，不把文字合同伪装成图片。
- Final Visual Blocking Assessment=`REQUIRED`且文字 / Canonical / REF-TAIL仍不足以唯一锁定Position、Facing、Distance、Topology、Axis、Camera、Pose、Gaze或Action Path → 选择经Sketch Validation确认的当前`REF-SKETCH`；它不得承担身份、环境结构、道具造型、材质、色彩、灯光或最终画风。
- A【同镜头连续承接】或B【新镜头参考型】确需上一状态锚定 → 按既有规则选择`REF-TAIL`并声明对应用途；C【新镜头且无需尾帧】不得引用或预留旧`REF-TAIL`。
- 光线、天气、综合色彩或场景当前状态存在漂移风险 → 只有实际存在、可回查且已确认的场景视觉基准图、合法首帧/尾帧或其他合格状态参考才可作为视觉输入；如果只有Project Bible、场景视觉基准或环境状态文字，则投影到`主风格 / 环境一致性 / 首帧参考 / 起始状态 / 尾帧限制`，不得虚构“Scene Anchor”或关键帧资产。

每个选中条目必须能回答“它解决当前Clip的哪一项具体风险或生成目标”；仅仅Eligible、上一Clip用过、位于Registry、可能有帮助或预算尚有空位都不是入选理由。合格但与当前风险无关的资产必须不选；遗漏必需项、用途选错、A/B/C路由错误或无风险依据的过量引用都视为Reference Selection失败，并按事实拥有者返回最小修正。


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

### Existing Asset Fast Path

当用户提供或项目目录中存在与CHAR / ENV / PROP / FX实体明确匹配的现有视觉文件时，资产流程先执行：

```text
Existing File Check
→ Candidate Reference Registration
→ User Confirmation
→ Canonical Reference / Active Version
```

该路径可以跳过新Prompt与图片生成，但不能跳过来源核验、用户对具体文件的明确确认、版本记录、Canonical Reference或Active Version登记。现有文件未确认前仍是Candidate Reference，不得标记`Confirmed Status: Yes`、`Status: Active`或作为下游锁定依据。

如果现有文件与实体身份不匹配、缺少必要视角/状态或用户要求重设计，返回标准Asset Design → Prompt → Image双确认路径。只核验当前对象，禁止为确认一个资产扫描或重做其他篇章与资产类别。

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

