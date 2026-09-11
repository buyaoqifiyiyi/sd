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

适用Core ENV还记录Spatial Reconstruction、Environment View Set、Major Spatial Anchors、Character Activity Zones、Entrances / Exits与Spatial Lock。

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
- 连续性敏感且已锁定的Core ENV → 按`knowledge/environment_multi_view_reconstruction.md`从ENV-01～04或有明确用途的扩展View选择当前摄影机方向、布局/距离和背景结构最相关的2–4张已确认环境Canonical图；不得机械全选，也不得用文字Spatial Truth或STATE-06 Planning Map冒充图片参考。
- 道具造型、材质、尺寸或可识别状态漂移风险 → 当前Active Prop Canonical References；持有者、左右手、位置、方向、接触和变化过程仍写入`道具状态`及起止状态，不把文字合同伪装成图片。
- Final Visual Blocking Assessment=`REQUIRED`且文字 / Canonical / REF-TAIL仍不足以唯一锁定Position、Facing、Distance、Topology、Axis、Camera、Pose、Gaze或Action Path → 选择经Sketch Validation确认的当前`REF-SKETCH`；它不得承担身份、环境结构、道具造型、材质、色彩、灯光或最终画风。
- A【同镜头连续承接】或B【新镜头参考型】确需上一状态锚定 → 按既有规则选择`REF-TAIL`并声明对应用途；C【新镜头且无需尾帧】不得引用或预留旧`REF-TAIL`。
- 光线、天气、综合色彩或场景当前状态存在漂移风险 → 只有实际存在、可回查且已确认的场景视觉基准图、合法首帧/尾帧或其他合格状态参考才可作为视觉输入；如果只有Project Bible、场景视觉基准或环境状态文字，则投影到`主风格 / 环境一致性 / 首帧参考 / 起始状态 / 尾帧限制`，不得虚构“Scene Anchor”或关键帧资产。
- 当前Clip存在综合色相、明度/饱和度或强调色占比漂移风险，且没有更具体的已确认场景状态参考 → 可选择STATE-04已确认、真实可访问的`Project Color Reference`；它是非资产项目视觉参考，只承担综合色相 / 明度 / 饱和度 / 强调色占比，必须标明唯一Primary Role并计入Reference Budget。它不得控制人物、环境、道具、构图、光源、镜头或最终画风，也不得因预算空位、全片存在色卡或文字色彩需求而默认入选。

每个选中条目必须能回答“它解决当前Clip的哪一项具体风险或生成目标”；仅仅Eligible、上一Clip用过、位于Registry、可能有帮助或预算尚有空位都不是入选理由。合格但与当前风险无关的资产必须不选；遗漏必需项、用途选错、A/B/C路由错误或无风险依据的过量引用都视为Reference Selection失败，并按事实拥有者返回最小修正。


---

# 09 Two-Tier Asset System Rule

STATE-02必须为每个CHAR、ENV、PROP执行Asset Tiering Decision；Asset Tier与Primary / Secondary / Background优先级相互独立。

满足任一条件即优先`Core`：主角或固定角色、跨场景或跨Clip反复出现、承担强剧情/角色/品牌识别、需要高一致性、关键场景、剧情关键道具。Core角色先生成一张外观参考图供用户确认角色外观；该图只用于设计决策，不能成为Canonical资产。用户确认后，才独立制作一张正式角色资产设定图：同一画布内固定包含面部特写与正面、严格侧面、背面全身三视图；必要状态变体另作独立图。Core环境独立制作主参考图/多视角/关键区域图；Core道具独立制作主参考图/必要状态或细节图。

不满足Core条件的一次性配角/群演、群体背景角色、同类家具与环境小物、氛围装饰、低频道具通常为`Support`。Support不得逐个制作完整独立资产包，必须按同一资产类型和相近用途形成Support Reference Board；角色、环境、道具不得跨类型混板。

每板建议4—9个对象，风格统一但必须通过轮廓、服饰/材质、颜色、比例和功能差异清楚区分。每板必须有稳定Board ID，每个对象必须有稳定Item ID；确认后不得重排或复用。后续只按`<Board Name> / <Board ID> / <Item ID>`引用。

Core与Support执行同一双确认闭环。`Automation Policy: FAST`仅可按`rules/automation_mode.md`自动确认符合资格的Prompt并汇总生成Candidate；未确认图片不得把Core、Board或Item标记confirmed。若Support对象在制作中被发现实际需要高一致性、独立状态或关键识别，返回STATE-02复核并升级Core，不得在Support分支暗中制作完整独立套图。

正式FX Asset继续服从既有Formal FX / Inline Effect规则，本Two-Tier变更不改其Workflow。

---

# 10 Visual Asset Production Gate

### Asset Checkpoint Confirmation Semantics

STATE-03的资产确认仍是可审计的Gate；确认输入语义由`rules/progression_rules.md`的`Confirmation Input Semantics`唯一拥有。资产确认检查点包括当前Prompt Revision、当前Candidate Image / Candidate Reference（包括用户外部回传的图片与Existing Asset Fast Path），以及Core角色的当前外观参考图。该确认必须写入相应的Prompt Confirmation、Image Confirmation或Appearance Confirmation及时间、Revision、Candidate / Board / Item范围。

对同一轮清楚列出的Candidate批次，按该全局语义确认该批次中的全部列出对象；Support Board仍须能核对Board ID、Item ID与图中区域/标签。资产记录不得放宽全局规则中的未展示、版本或对象不清、互斥选择、外部提交及Hard Stop边界。

### Existing Asset Fast Path

触发前提是已取得真实视觉文件或受控ID。用户仅口头声明“已有资产”不触发本路径，按本节`User-Declared Existing Assets`处理。

当用户提供或项目目录中存在与CHAR / ENV / PROP / FX实体明确匹配的现有视觉文件时，资产流程先执行：

```text
Existing File Check
→ Candidate Reference Registration
→ User Confirmation
→ Canonical Reference / Active Version
```

该路径可以跳过新Prompt与图片生成，但不能跳过来源核验、用户对具体文件的确认（按`rules/progression_rules.md`解释）、版本记录、Canonical Reference或Active Version登记。现有文件未确认前仍是Candidate Reference，不得标记`Confirmed Status: Yes`、`Status: Active`或作为下游锁定依据。

如果现有文件与实体身份不匹配、缺少必要视角/状态或用户要求重设计，返回标准Asset Design → Prompt → Image双确认路径。只核验当前对象，禁止为确认一个资产扫描或重做其他篇章与资产类别。

### User-Declared Existing Assets

用户以陈述方式说明自己持有资产（例如“已有资产”“这些我自己有”“参考图我这边有”“用现有资产”“不用管素材”）时，这是**资产可用性声明**，不是资源提交义务。该声明不改变Asset Discovery范围、Tier判定、Registry初始化或任何下游Gate。

- **清单优先**：仍完整输出当前项目需要的CHAR / ENV / PROP / FX清单与Tier判定；在清单条目标注`已有（用户声明）`一行，其余按正常判定写`待制作`。这是清单内状态注释，不新增Template固定字段，也不改变Registry的Prompt / Image / Confirmed状态语义。
- **禁止索取**：不得要求用户上交、上传、发送、粘贴或补齐文件，不得要求用户提供路径、文件名或自有素材清单，不得因文件未提供或不可读而重复追问，不得把交付停在素材索取上，也不得因此写BLOCKED或声称清单不完整。
- **声明不等于登记**：`已有（用户声明）`只表示用户自述持有，不构成Existing File Check结果，不写Candidate Reference、Canonical Reference、Active Version、`Image Generated`、`Confirmed Status: Yes`或`Status: Active`，也不得作为下游视觉输入。
- **由用户发起登记**：用户实际提供文件、给出可访问受控ID，或明确要求登记/核验该资产时才执行Existing File Check与后续确认；不得为把声明转成登记而主动索要素材。
- **缺失由用户说明**：不逐项盘问缺什么。只有某个缺口会改变当前对象身份或阻断当前制作步骤时，才一次性指出该**具体**缺口并给最小路径；通用补全、进度催促与逐项确认一律不做。
- **不虚构**：不得反向声称用户已持有其未声明的资产，也不得因用户声明而跳过该资产的Tier判定、Prompt / Image双确认或其他Hard Gate。

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

- 在新建或重编Image Prompt前，必须由`modules/image-model-selection.md`完成当前资产批次的图像模型路由：优先继承STATE-00已确认的`Project Image Model Default`，只有默认项或当前批次为`UNSELECTED`、当前批次例外或默认项不可用时才提出新选择；`UNSELECTED`时不得编译模型专属Prompt或生成Candidate Image。图像模型选择不是Prompt / Image确认，不放宽任何后续Gate。
- Image Prompt必须是完整、可直接生图的执行文本，不得只输出外观说明、关键词清单或“用于后续生成”的参考要求。
- Prompt至少明确主体身份、可见结构、构图/视角、材质/服装、光影、项目视觉风格、一致性限制、必要负面限制与适用生成参数。
- `Visual Production Status: Prompt Draft`时必须停止在当前Prompt Confirmation Checkpoint；用户的确认输入按`rules/progression_rules.md`解释。只有`Automation Policy: FAST`、输入完整、当前资产不触及`rules/automation_mode.md`的Hard Stop且当前Workflow QA通过时，才可记录自动Prompt确认并继续内置图片生成。
- 同步状态必须为`Prompt Status: Draft`、`Image Status: Not Generated`、`Confirmed Status: No`。
- 当前Prompt Revision获得全局确认语义定义的确认后，才可写`Prompt Confirmed`并按已记录的工具路由继续；`Automation Policy: FAST`的合格资产可由`rules/automation_mode.md`记录自动确认后继续。对外部图像服务，该确认只记录Prompt Confirmed，不构成外部提交授权。
- Prompt发生任何实质修改后返回`Prompt Draft`，旧确认不得自动继承。

## Image Gate

- 已确认选择`Built-in Image`且当前agent具备直接图片生成能力时，在当前Prompt Revision按既有规则确认后生成Candidate Image；选择`Midjourney`或其他外部模型时只交付Prompt，外部图片回传后才进入Image Generated。不得因环境可生成而跳过图像模型选择或Prompt确认。
- 图片生成后先执行本节的`Candidate Output Triage`；只有保留项才写`Image Generated`并把文件或受控外部ID登记为Candidate References。
- Image Generated时同步状态必须为`Prompt Status: Confirmed`、`Image Status: Candidate`、`Confirmed Status: No`。
- 未经全局确认语义定义的用户确认图片，不得写Canonical References、Active Version、`Status: Active`或`Asset Confirmed`。
- 图片被拒绝时，保留其生成记录但不得升级为Canonical Reference；若只需重生则回到已确认Prompt，若需改Prompt则回到`Prompt Draft`重新确认。
- 只有图片获得全局确认语义定义的用户确认后，才能写`Visual Production Status: Asset Confirmed`，完成Canonical References、Active Version、Approval Basis与Approved At登记。
- Asset Confirmed时同步状态才允许为`Prompt Status: Confirmed`、`Image Status: Confirmed`、`Confirmed Status: Yes`；Support还必须记录Board ID、Item ID与图中区域/标签对应关系。

### Candidate Output Triage And Cleanup

每次资产生图或外部图片回传后，必须在展示、Candidate登记或图片确认前，逐项与当前Prompt Revision、资产ID、预期图数、资产类型与必要视角/版式做实际视觉核验。此筛选不是用户对图片的Canonical批准；它只处理客观不合格或多余输出，不放宽后续Image Confirmation Gate。`KEEP / DISCARD / NEEDS_USER_SELECTION`只是当轮分流结论，不新增项目状态、资产版本状态或最终Prompt字段。

- `KEEP`：唯一满足当前资产合同、可读取、无重复且承担当前所需视角/版式的图片。报告其Candidate ID / 文件或受控ID、保留理由和“仍待图片确认”。
- `DISCARD`：超出预期数量、重复、错误实体/资产类型、错误版式或视角、身份/结构/文字水印等硬失败、不可读取，或与当前Prompt Revision明显不符的图片。不得展示为可选Candidate、不得进入Candidate References、Registry、下游参考或模型预算；报告被弃用的ID / 文件或受控ID及最短原因。
- `NEEDS_USER_SELECTION`：两张或以上图片都通过客观合同，但仅剩审美或创作取舍而没有可验证的唯一胜者。只展示这些合格项，明确它们的ID与差异，等待用户选择；用户的图片批准仍只作用所选项。

对`DISCARD`的未确认本地临时输出，若当前运行环境实际拥有且已核验精确路径属于本次生成，则直接删除该文件；保留最小生成记录（Prompt Revision、来源、弃用原因、时间）以便审计，但不保留为项目候选或引用。外部服务、用户上传文件或聊天历史中的图片无法由系统直接删除时，必须明确报告“已从项目候选与后续引用中移除，原平台/聊天记录仍由用户控制”，不得假装已物理删除。已确认Canonical / Active图片、用户明确保留的图片、路径/归属不明的文件一律不得自动删除。

若没有`KEEP`项，不显示伪候选或要求用户在错误图中挑选；按既有最小Return Route重生或修订Prompt。该Triage在STANDARD与FAST下都自动执行；FAST不得把它解释为图片批准。

### Reference Provenance And Degradation｜参考来源与代际劣化

输入图不是中性画面，而是带信息的输入：任何一张参考都会同时携带构图、光线、噪点、材质、角色错误与自己并不需要的细节，被反复改写时携带的无关信息还会增加。资产生图与图改图时必须记录原图来源，并明确本次真正要消费的维度；需要控制构图、机位或空间关系时，优先从原图或已确认的受限技术图出发，不要用一张已带强风格的成图顶替。本规则只约束参考的选取与传代，不改变既有禁用规则：线稿、白模、多格拼图与Storyboard仍不得登记为Canonical Reference，也不得作为STATE-08视频输入；唯一例外仍是已注册且只承担Clip Blocking / Visual Blocking Authority的`REF-SKETCH-XX`。

图改图反复迭代会累积塑料感、脏高光、细碎噪点与材质退化，并逐代放大原始误差。发现代际劣化时按以下顺序处理，不得继续在同一张衍生图上叠加修改：

1. 合并本轮全部修改需求，减少迭代次数；
2. 退回原始图或结构图重新生成，而不是在上一次衍生结果上继续加改；
3. 只有在原图确实不可用时，才从最近一次仍然干净的版本分叉，并把已确认正确的局部重新合成回来。

控制强度按用途选择，不做统一默认：自由探索用于气氛、蒙太奇与非关键覆盖；中等控制用于单人表演与普通对白；强控制用于多人关系、关键连续性、机械步骤、道具状态与地理信息。强控制会减少意外创造，只锁定必须一致的内容，给模型保留产生好镜头的空间。

## Tool Availability

当前环境不能直接生成图片时，最低交付仍是完整Image Prompt与当前Prompt Confirmation Checkpoint。用户按全局确认语义确认后保持STATE-03 `IN_PROGRESS`，等待外部生成图片回传或图像工具恢复；不得把纯文字设定登记为已确认视觉资产。


## Downstream Character Lock Inheritance Gate

Asset Registry登记Active CHAR Version后，以下阶段和产物必须显式继承同一版本及其适用Canonical References：STATE-04 Visual Development与Poster/Key Art、STATE-05场景示意、Optional Storyboard、STATE-06 Detailed Shot Design、STATE-07 Clip Production、STATE-08图片/视频Prompt与最终视频生成、STATE-09 Review，以及角色设定图、动作状态图、比例图和封面。

任何阶段发现新参考、风格指令、Prompt文本或生成结果与锁定角色资产冲突，必须以锁定资产为准并拒绝冲突内容；不得折中拼接不同外貌。只有按Change Protocol获批并切换的新Active Version可以改变继承基准。

