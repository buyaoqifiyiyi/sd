# SD Film 使用说明书

> **本文件是面向人的使用说明书，属于非运行时文件。** 它未被任何Workflow列为Required Resource，不参与运行时读取，也不得作为运行时规则、恢复、路由或Schema的规范来源；运行时权威是`SKILL.md`、`rules/`、`workflows/`、`knowledge/`、`references/`与`templates/`。

这是一份面向用户的“怎么用”手册。想知道某件事该怎么下指令、SD Film 会做什么、会在哪一步停下来等确认，直接查本文件即可。

内部 Pipeline、字段权威和开发规则仍以 `SKILL.md`、`rules/`、`workflows/`、`references/` 与 `templates/` 为准；当前安装版本只看 `SKILL.md` 中的 `Skill Version` 和 `Build ID`。

## 默认导演系统

SD Film现在默认由`Director Module / Director Intelligence Layer`贯穿剧本→视觉→场景→镜头→Clip→Prompt→Editing→Review。它从“这段戏为什么存在、观众先知道/感受什么、人物关系怎样变化”开始，再让镜头语言承担构图、景别、机位、焦段/距离、前中后景、遮挡/揭示、运镜触发与Hold / Cut节奏。最终Seedance Prompt仍使用原有模板，不会多出一整套导演分析字段。

正常调用方式不变：继续使用`调用sd`开始或路由，使用`下一步 / 下一个 / 继续 / 往后做 / 接着做`从当前Checkpoint推进。当前已经展示且可核对的确认点上，这些以及其他同义推进表达也直接视为确认，不再额外要求你说“确认”；普通推进不会无意义全量reload。

## 自动推进模式

当你想少确认、多产出时，明确说：`调用sd，开启自动推进，按快速制作模式继续。` 也可以明确说`尽量少确认`、`只在关键节点停`或`自动完成可逆步骤`。之后SD Film会把STATE-04到STATE-08中已锁定、可追溯且QA通过的工作连贯推进：自动确认符合条件的资产提示词、批量生成GPT Image 候选、自动接受Detailed Shot与Clip Plan、验证调度草图后同轮编译Prompt，并按顺序交付所有已确认Clip的完整Prompt（单轮容量不足时只在完整Clip之间分批，继续即可续交）。已确认的外部图像模型批次会自动得到可提交的生成包，但不会代替你向外部服务提交。

它仍会在制作版剧本锁定、首次或变更图像/视频模型、缺失必要输入、真实人物/品牌/法务内容、外部服务提交、资产候选图片转为正式Canonical资产，以及实际视频Review等需要选择或额外授权的情况停下。随时说`关闭自动推进`即可恢复标准模式。

每次资产图或调度草图生成后，系统会先做候选清理：客观错误、重复或超出数量的未确认图直接从项目候选和后续引用中移除，并明确告诉你保留的Candidate ID与弃用原因；它们不会再混入资产登记、草图参考或视频模型预算。只有多张图都合格、但确实需要审美取舍时，才会展示这些合格项让你选。若系统拥有本次未确认临时文件的精确路径，会直接删除；聊天历史、外部平台和用户上传原件只能移出项目引用，不能假称已物理删除。

## 统一交付包

快速模式会默认把连续可推进的结果合成一次交付。标准模式下也可明确说`统一输出`、`合并输出`、`一次性制作包`或`按包交付`。

- `Preproduction Package`：视觉方向摘要（仅要求查看时）+ 场景拆解 + 完整专业分镜。
- `Execution Package`：完整 Clip Plan + 按顺序的完整目标模型视频 Prompt；前提是模型已锁定、FAST可自动接受Clip Plan且逐Clip检查通过。
- `Asset Candidate Package`：同批次资产Prompt、生成结果筛选与合格候选；它必定停在候选图确认，不会越过资产锁定。

这只合并展示，不跳过内部检查、状态写回或原有输出模板。模型选择、候选图确认、外部提交和实际视频Review会在最近边界截断交付包；内容过长时只在完整Artifact或完整Clip之间分批，继续即可续交。

在Codex中需要确定性启动时使用`$sd-film`。在当前用户客户端的普通Chat中，`@`选择器只显示Plugin，本机独立SD Film没有以`@`选择显示名的入口；`agents/openai.yaml`也不会把它注册成Plugin。普通Chat只有在宿主实际暴露本机Skills时，才可能通过`调用sd`等自然语言隐式选择。Skill更新后若Codex旧会话没有刷新，先重启桌面应用或新建Codex任务再试。当前运行时安装位置为`.codex/skills/sd-film`；不要为了普通Chat、网页端或移动端边界复制为第二份本机Skill。

如需查看内部方向，可以说：`显示当前Scene的导演意图`、`为什么这样拍`或`显示这个Clip的镜头语言策略`。Skill只会给简洁摘要，不会把完整内部Packet塞进最终Prompt。

## 先记住这条万能公式

```text
调用sd + 我要做什么 + 当前输入 + 必须保持什么 + 重点优化什么 + 做到哪一步停
```

### 已有资产快速通道

如果项目目录已有角色、环境、道具或FX图片，可以直接说“使用现有资产”或“跳过制作阶段”。SD Film会只核验当前对象，将文件登记为Candidate Reference，并请求你确认；确认后才升级为Canonical Reference与Active Version。该路径不会重复生成图片，但不会省略资产确认和一致性锁定。

如果你只是说明“这些资产我已经有了”、并不打算提交文件，系统照常给出完整资产清单，只在条目上标注`已有（用户声明）`，不会要求你上传、发送或补齐素材，也不会因此停下来追问；缺什么由你主动说即可。

### 资产创作的图像模型

剧本定稿（`Production-Locked`）之后、资产开始之前，系统会把图像模型默认项、图像交付形态、视频模型偏好与项目视频风格基线放在同一个`Production Setup`选择里；不会默认使用GPT Image或默认某个视频模型。当前图像可选`GPT Image`或`Midjourney`，视频可选`Seedance 2.0`、`Seedance 2.5`或`MiniMax H3`。你在请求中直接写“资产用Midjourney，视频用Seedance 2.5”时，系统只展示这一组候选；在这个检查点说“下一步”、`继续`等即可确认。未选择模型时，“下一步”不会替你猜选模型。剧本没定稿前不会先问你模型和风格。

选择`Midjourney`时，系统会改用Midjourney专属最终提示词模板，输出可直接粘贴的英文提示词；不调用GPT Image，也不把提示词当作已生成图片。你在Midjourney生成后把结果回传，系统才继续候选图确认与资产锁定。选择`GPT Image`时，也会使用它自己的专属模板；当前环境实际可生成才生成Candidate，否则只交付Prompt。这个图像选择会作为后续资产批次的默认项，不再每批重复问；你明确要求例外模型、模型不可用或主动改模型时才重新确认。

明确指定其他外部图像模型时，系统不会静默改用GPT Image；只有已验证Adapter和专属最终提示词模板同时存在时才会加入图像模型选择，没有时提供不假设平台能力的自然语言资产提示词。每个新模型都将独立建模板，不会混用GPT Image、Midjourney或视频模型规则。若要编辑已有图，请同时提供该图并明确“只改什么、其余保持什么”；结果回传后仍需经过候选图确认。

例如：

```text
调用sd，根据这个已定稿剧本进入完整视频制作流程。不要修改剧情和人物关系，重点保证角色、空间与道具连续性。项目启动和状态记录在内部完成；默认只给我剧本、设定资源、分镜表、Clip表和最终提示词。
```

## 快速索引

| 任务 | 你可以直接这样说 | 默认进入 / 调用模块 |
|---|---|---|
| 完整视频 | `调用sd，根据这个剧本进入完整视频制作流程。` | STATE-00 → STATE-09 主流程 |
| 从创意写剧本 | `调用sd，我只有一个故事概念，直接从剧本开始。` | STATE-01 Screenplay Generation branch |
| 品牌需求写短片 | `调用sd，根据这个品牌需求写一支宣传短片，先完成剧本提案。` | STATE-01 Screenplay Generation branch |
| 剧本优化 | `调用sd，分析这个剧本并给出优化机会报告，先不要改写。` | STATE-01 Script Analysis |
| 定稿剧本直接制作 | `调用sd，这个剧本已经定稿，不要修改剧情，直接进入制作。` | STATE-01 No Revision / Final Script 路由 |
| 资产缺失检查 | `调用sd，只检查当前项目缺少哪些角色、环境、道具和正式FX资产，不生成图片。` | STATE-02 Asset Discovery / 状态核验 |
| 角色资产 | `调用sd，只制作CHAR-001角色视觉资产，先输出生图提示词，等我确认。` | STATE-03 Character Asset |
| Midjourney角色资产 | `调用sd，只制作CHAR-001角色视觉资产，用Midjourney，先输出提示词。` | STATE-03 Character Asset / Midjourney Prompt Only |
| 其他外部图像模型资产 | `调用sd，只制作CHAR-001角色视觉资产，用<模型名>，先输出提示词。` | STATE-03 Character Asset / Explicit External Prompt Only |
| 环境资产 | `调用sd，只制作ENV-001环境资产，先输出生图提示词，等我确认。` | STATE-03 Environment Asset |
| 固定场景空间重建 | `调用sd，为ENV-001判断是否需要环境多视角空间重建；如需完整重建，按ENV-01至ENV-04先输出提示词，等我确认。` | STATE-03 Environment Asset |
| 道具资产 | `调用sd，只制作PROP-001道具资产，先输出生图提示词，等我确认。` | STATE-03 Prop Asset |
| 正式FX资产 | `调用sd，只制作FX-001正式效果资产，锁定触发源、物理驱动、状态变体和跨镜头残留；先输出生图提示词，等我确认。` | STATE-03 FX Asset |
| 角色音色 | `调用sd，为CHAR-001设计角色音色，并输出独立Seed Audio兼容提示词。` | AUDIO / SEED-AUDIO 可选模块 |
| 配乐 | `调用sd，为整条片子规划配乐与留白，并输出需要的SeedMusic纯音乐提示词。` | MUSIC / SEED-MUSIC 可选模块 |
| 专业分镜 | `调用sd，根据已确认场景和资产制作Professional Detailed Shot Script。` | STATE-06 Detailed Shot Design |
| Storyboard | `调用sd，根据已确认Detailed Shot Design制作Storyboard。` | Optional Storyboard |
| Shot组合为Clip | `调用sd，把已确认的Detailed Shot Design组织为Clip；沿用项目级视频模型偏好，并按当前Clip能力复核。` | STATE-07 Clip Production |
| MiniMax H3 Clip | `调用sd，使用MiniMax H3组织已确认Shot为Clip并输出CLIP-003视频提示词。` | STATE-07 → STATE-08；H3为4—15秒，支持首/尾帧、全能多模态参考、已有视频编辑、分镜/切镜、明确对白与口型；按官方三段式提示词编译 |
| Dreamina长视频 | `调用sd，使用Dreamina网页端为已确认项目准备180秒长视频提交包。` | Seedance 2.5 / Dreamina Web；仅网页端能力，不改写方舟API的4—30秒路线 |
| Dreamina标注编辑 | `调用sd，使用Dreamina网页端编辑这段视频；在我标注的区域与时间点把X改成Y，其余保持。` | Seedance 2.5 / Dreamina Web；须提供原视频、标注与时间点 |
| 单个Clip Prompt | `调用sd，只输出CLIP-003的目标模型视频提示词。` | STATE-08 单Clip交付 |
| 全部Clip Prompt | `调用sd，按顺序输出全部Confirmed Clip的完整目标模型视频提示词；过长就按完整Clip自动分批。` | STATE-08 批量交付 |
| 下一个Clip | `调用sd，下一个Clip。` | STATE-08 下一个未交付Clip |
| Clip返修 | `调用sd，只修CLIP-003的站位错误，其他内容和字段保持不变。` | STATE-08最小修订或对应上游Return Route |
| 连续性检查 | `调用sd，只检查CLIP-002到CLIP-003的角色、站位、道具、轴线和首尾帧连续性，不重新生成。` | STATE-07 / STATE-09连续性核验 |
| Review | `调用sd，审核这个实际生成结果，给出PASS / REVISE / REBUILD、KEEP / RE-EDIT / REGENERATE / REDIRECT和最小返修方案。` | STATE-09 Technical + Director's Cut Review |
| 技能经验 | `调用sd，Review后提出可跨项目复用的经验候选，等我确认后再写入Skill。` | Skill Experience候选确认机制 |
| 电影海报 / Key Art | `调用sd，根据当前项目设计一张9:16数字竖版电影Key Art，沿用现有角色和环境资产。` | Poster Design辅助Workflow |
| 继续旧项目 | `重新调用sd，恢复当前项目，从最后一个安全Checkpoint继续。` | Runtime Reload + Legacy Project Recovery + Project Resume |
| 检查Skill | `调用sd，只检查当前实际安装版的Pipeline、STATE和音色规则，不执行制作。` | Runtime Reload + 只读规则检查 |
| 修改Skill | `进入Work，读取当前实际安装的sd Skill，只修改我指定的规则，并同步版本、回归检查和USER_GUIDE.md。` | Work / Codex本地修改任务 |

## SD Film 什么时候会停下来

常见停止点如下：

1. 新项目首次进入时，项目初始化和`Creation Brief / Existing Script / Material`入口登记在内部完成，不会展示项目登记页、搜索类似项目或越级输出分镜、Clip或视频 Prompt。
2. 只有创意并明确要写剧本时，STATE-01直接生成`Production Script Proposal`，不要求你先去普通Chat写完整剧本，也不先对不存在的剧本做优化机会报告。
3. 上传已有剧本/来源材料时，默认先给 `Optimization Opportunity Report`，等你决定锁定、轻度优化或结构优化；如果当前指令已明确“直接优化 / 直接改写”，不会重复询问是否优化。
4. 任一创作或优化分支生成 `Production Script Proposal` 后都会停下来，等你确认制作版剧本。
5. 每类视觉资产先给生图 Prompt，等你确认；生成候选图后再停一次，等你确认图片。
6. STATE-06 若复杂空间需要俯视 Blocking Map，可能先给地图 Prompt，等你确认后再生成图；不需要图或工具不可用时可使用完整文字 Blocking。
7. 你可以上传色卡并明确“将此色卡作为项目色彩基线”。它会作为`Project Color Reference`进入视觉开发，而不是角色、环境、道具或效果资产；只有真实图片已可访问、你已确认采用、且某个Clip确有光色漂移风险时，才会作为该Clip的受控模型图片输入。
8. 图像模型默认项、图像交付形态、视频模型偏好与项目风格基线在剧本`Production-Locked`后只确认一次；STATE-03直接继承图像默认项与风格基线，STATE-06/07按当前Clip时长、首尾帧、编辑模式和参考输入能力复核视频偏好。能兼容时不重复问；不兼容时才给最小替代选择，不会用模型能力偷偷改导演设计。选择会自动路由到对应内部提示词编译模板，写入内部执行Profile与Clip Plan，不进入最终视频Prompt。MiniMax H3的全能参考最多9图、3视频、3音频且总计12个文件；每个实际投喂素材必须在提示词中写明`@图片N / @视频N / @音频N`与用途。Clip Plan确认前切换模型只重跑受影响的STATE-07/08，不重做剧本、资产、场景或Detailed Shot Design。
9. Seedance 2.0为4—15秒。Seedance 2.5为4—30秒：实际生成秒数由你在该窗口内选择；4—15秒沿用稳定`Standard Clip`，16—30秒由目标时长自动进入内部严格预检，不要求你额外选择`Long-form Clip`。未知网关状态不会自动限制为15秒；若实际提交被平台拒绝，系统才返回Clip规划做最小调整。2.5现在使用独立的多模态时间线Prompt模板，默认按30图、10视频、10音频、合计50项（视频/音频各自总时长≤30秒）的能力上限规划；它会按当前Clip实际需要少用，但不再人为回退成9图上限。每项参考仍必须有唯一用途。纯音频驱动动作、口型或节奏也必须由你明确指定。2.5最终Prompt拥有独立`主风格：`字段；MiniMax H3保持官方三段式，但其`核心创意：`第一行固定为`主风格：`，两者都会把项目风格含义与最小充分的可见载体写在剧情前。
10. 只有你明确说“使用Dreamina网页端”时，系统才会按该入口准备30—180秒一键长视频、标注编辑、绿幕、双视频转场或多格分镜的提交方案；这些不会被误报为方舟/API默认能力。
11. 标准模式下，Clip Plan、分镜或其他需要确认的生产成果仍会在可核对的当前版本展示后才标为Confirmed；快速模式会在现有QA和状态写回通过后自动接受Detailed Shot与Clip Plan。
12. 长视频 A / B 接续模式缺少上一 Clip 尾帧时，Prompt 可以先交付，但真正提交生成前会要求你补入尾帧。
13. 单个Clip在最终Prompt前若被判定需要Visual Blocking Sketch，标准模式会先给你经验证的调度草图、注册名与用途说明，暂停Prompt；快速模式则在验证、登记并确认真实输入已绑定后同轮输出Prompt。草图不是“文字里提一下”：Seedance 2.0必须绑定实际文件/受控ID，Seedance 2.5必须是实际`@图片N`，MiniMax H3必须在All-Reference模式作为实际`@图片N`。图片不可访问、签名不匹配、预算无位或H3处于首尾帧/视频编辑模式时，系统会明确说生成包未就绪并返回最小修复路径，绝不声称草图已被使用。简单Clip不会为了统一流程强制出草图。
14. Review同时区分Technical Review与Director's Cut Review，并在兼容的`PASS / REVISE / REBUILD`外给出`KEEP / RE-EDIT / REGENERATE / REDIRECT`处置。技术正确但信息或情绪提前暴露仍会返修；修复后必须重新Review。
15. Review或失败复盘后，系统可以自动提出跨项目技能经验候选；候选不会自动写入Skill。只有你明确确认后才入库，并在适用条件满足时影响后续产出或形成项目迭代建议。经验不能直接覆盖已确认剧情、资产、镜头、Clip或Prompt，项目修改仍经过对应流程与确认。

---

## 1）完整制作一个视频

**最简指令**

```text
调用sd，根据这个剧本进入完整视频制作流程。
```

**进阶指令**

```text
调用sd，根据这个剧本制作一条9:16真人剧情短片。保持核心剧情、人物关系和结局不变，重点保证角色外貌、空间轴线、道具和跨Clip连续性。按STATE-00到STATE-09推进，每遇到剧本决策、资产Prompt、候选图片、Clip Plan或返修决定时停下来等我确认；STATE-08默认逐个Clip输出。
```

**Skill 行为 / 停止点**

- 固定主流程是 `STATE-00 Project Setup → STATE-01 Script Analysis → STATE-02 Asset Discovery → STATE-03 Asset Development → STATE-04 Visual Development → STATE-05 Scene Breakdown → STATE-06 Detailed Shot Design → STATE-07 Clip Production → STATE-08 Video Prompt / Generation → STATE-09 Review`。
- 视觉开发（STATE-04）会在内部锁定四项排他性美学决定：反差与光比结构、色彩对抗关系、构图主张、视觉母题与变化轨迹。每项都要写明选择、被放弃的选项和依据，不接受“电影感 / 高级感”这类标签；主光比程度、色彩对抗与构图主张会写入 Project Bible，并作为 STATE-05 到 STATE-08 的执行基准，不会在 Prompt 阶段临时另起一套审美。
- 这四项决定锁定之前，可以选择先**试片**：用已确认的角色 / 环境资产出 1—3 张关键画面，让你先看一眼再定。因为不看画面就把光比、色彩和构图定死，那不是决定，是赌注。试片帧是**草稿**——不登记为资产、不写入项目状态、不进后续任何阶段、也不会成为视频参考图；用完即可丢弃，它的作用是让你在锁定前修正决定。你说不想出图或环境不支持时会跳过并记录原因，其余流程照常。想用就说`先出2张试片看看`，系统最多出3张，且每张只回答一个美学问题。
- 项目启动时会确认一次**媒介形式**：`live_action`（真人 / 实拍）、`3d_animation`（三维 / 三渲二 / CG）、`2d_anime`（二维 / 漫剧 / 手绘 / 动态漫画）。它不改变题材，但会改变镜头、表演与美学三套语言——尤其是 2D 漫剧不能沿用实拍焦段、光比与器材参数。你只说“动画”而没指明二维或三维时，系统会问你一次，不会默认按真人剧往下做；已在指令里说明媒介时不会重复问。
- “我要最终视频”只表示目标，不表示可以跳过前置阶段。
- 新项目首次响应静默完成项目确认、初始化和输入分析准备，并直接交付当前合法的剧本阶段成果。
- Storyboard、角色音色和配乐都不是主流程必经步骤，只有显式请求才进入对应辅助模块。
- STATE-08 默认一次输出一个尚未交付的 Clip；想一次拿全部，必须明确说“全部 / 批量 / 连续输出多个”。

## 2）只有故事概念，先开发剧本

**最简指令**

```text
调用sd，我只有一个故事概念，先开发剧本。
```

也可以直接说：

```text
调用sd，帮我写一个雨夜双女主重逢短片。
```

```text
调用sd，根据这个品牌需求写一支宣传短片，先从剧本开始。
```

**进阶指令**

```text
调用sd，把这个故事概念开发成一条3分钟竖屏剧情片的可制作剧本。必须保留核心人物、世界观和结局；先建立人物目的、因果、冲突、关系弧、潜台词、Writer Beat、信息策略和Setup / Payoff，再由导演模块建立观众体验与可见表演方向。完成完整剧本提案后停下来等我确认。不要提前写分镜、焦段或运镜。
```

**Skill 行为 / 停止点**

- 只有Idea / Brief且明确要求写剧本时，会被识别为 `Creation Brief`，STATE-01直接进入Screenplay Generation，不要求你先提供完整剧本。
- SD Film现在默认同时包含Screenwriter Module与Director Module。Screenwriter负责故事、人物、因果、潜台词、Writer Beat、Setup / Payoff和信息架构；Director负责观众体验、表演调度、空间、镜头语言、构图、运镜与呈现节奏。
- 两者通过内部Writer → Director Handoff衔接；用户不需要填写完整WRITER INTENT PACKET，最终交付仍是可独立阅读的剧本。
- `Writer Beat ≠ Shot`。Writer只确定人物/剧情状态发生了什么变化；一个Beat用一个或多个Shot、或多个Beat用一个长镜头，由Director决定。
- 这不等于提前写分镜；35mm、推镜、特写、摇镜、机位、SHOT / CLIP仍留给后续Director / STATE-06/07。
- 剧本内部会经过Directable Screenplay QA，但最终交给你的仍是可独立阅读的剧本，不是十项分析报告。
- Proposal 输出后会停在确认点；你说任一推进表达即可成为 `Production-Locked Directable Screenplay`并进入后续资产阶段。
- 你说“修改这一场”时会保持在Script Development，只改该场与必要相邻因果，不会跳到Shot Design。
- 只有当缺失信息会实质改变故事架构或造成品牌/事实风险时，Skill才会询问最小必要问题；其他可安全信息会用清楚、可修订的假设继续。

如果你提供的是小说章节、已有故事梗概、品牌文案或其他要保留/转换的叙事正文，它属于`Existing Script / Material`，仍会先诊断并保护来源事实，不会冒充从零创作。

## 3）分析 / 优化 / 改写剧本

**最简指令**

```text
调用sd，分析并优化这个剧本。
```

如果你不想在诊断后重复确认是否优化，可以明确说：

```text
调用sd，直接优化这个剧本；保持世界观、人物身份和结局，完成Production Script Proposal后停下来等我确认。
```

**更稳妥的两步指令**

```text
第一步：调用sd，分析这个剧本并给出优化机会报告，先不要改写。
第二步：调用sd，按刚才的B档建议执行轻度优化，只改台词效率、动作可视化和节奏，不改世界观、人物身份和结局。
```

**进阶指令**

```text
调用sd，只优化第二场和第三场：压缩重复信息，让冲突更早进入，把不可拍的心理描写转成可见动作。其他场次保持原文，不要顺手润色。完成Production Script Proposal后停下来等我确认。
```

**Skill 行为 / 停止点**

- 只要求分析、没有明确允许改写时，会先评为 A（无明显优化必要）、B（轻度优化空间）或 C（明显结构问题），然后停在 User Decision Gate。
- 已有剧本会先检查因果、人物动机、场景价值变化、Writer Beat推进、冲突/风险、潜台词、Setup / Payoff、人物/关系弧、结局回收与信息架构；不会默认改写。
- 可直接说“显示编剧意图”“为什么人物这么做”或“检查潜台词”。这些只展开必要的Writer分析，不改变当前剧本确认边界。
- 如果当前指令已经明确“分析并优化 / 直接优化 / 直接改写 / 只优化某一场”，这已构成改写授权；Skill仍先保留诊断依据，但不会重复问你是否要优化。最终Proposal仍须在当前确认点获得确认；任一推进表达即可完成该确认。
- 单独的推进表达不等于授权开始新的改写范围；但在已展示的Proposal确认点，它确认当前Proposal。
- 局部优化只改指定范围；若必须影响相邻内容，会先列为待决定项。
- 改写后仍需确认当前 Proposal，才能锁定并进入资产阶段；任一推进表达即可确认。

## 4）剧本已定稿，禁止修改，直接制作

**最简指令**

```text
调用sd，这个剧本已经定稿，不要修改剧情，直接进入制作。
```

**进阶指令**

```text
调用sd，这个版本是最终定稿。禁止修改剧情、台词、人物关系、世界观和结局；只做制作分析并把原稿锁定为Production-Locked Script，然后进入资产发现。发现事实矛盾时只列出问题，不要静默修复。
```

**Skill 行为 / 停止点**

- 进入 `No Revision / Final Script` 路由，跳过优化机会报告和内容改写。
- 仍会进行故事、人物、环境、视觉元素和制作风险分析。
- 原稿按你的明确授权直接锁定；真正无法支持制作的矛盾会列为 Pending Decision，不会擅自改稿。

## 5）角色资产制作

**最简指令**

```text
调用sd，只制作CHAR-001角色视觉资产。
```

**进阶指令**

```text
调用sd，只制作CHAR-001角色视觉资产。沿用当前剧本和Visual Direction，锁定脸型、年龄感、身体比例、发型、服装形制和配色。先输出当前Revision的完整生图Prompt，停下来等我确认；不要自动生成图片，也不要设计音色。
```

**Skill 行为 / 停止点**

- 必须先有 STATE-02 的角色资产需求和 `Core / Support` 分层。
- Core 角色的外观参考图按批次整批生成、整批给你确认，不逐角色出图；确认后才制作一张正式角色资产设定图（同一画布内固定五个区域：上排三个等宽等高的全身区——正面、严格侧面、背面；下排两个更大的头肩特写区——中性表情与微笑表情）。**正面区不画头部与头发，肩线以上为空白背景**，这是为了让面部与发落各有唯一权威来源，不是出图遗漏。确有剧情需要的状态变体才另作图。外观参考图不进入Canonical资产；Support 角色进入同类型 Reference Board，不逐个做完整套图。
- 资产制作先选择图像模型，再给你该模型的可执行Prompt并等待确认；选择GPT Image且当前环境实际可用时，确认后才生成候选图。无论使用哪种模型，正式候选图仍须由你确认后才能成为资产。
- 固定双确认：`Prompt Draft → 你确认Prompt → 生成候选图 → 你确认图片 → 登记Active / Canonical资产`。
- 按批次交付：同类同 Tier、同一生产形态的资产一次出齐Prompt，并在同一轮内提交整批全部图片（一次多张或并行），不逐张出图、不逐个等确认；环境与道具同理。整批看完你只挑不满意的说即可——被挑出的重做，其余直接登记；没提出问题而直接推进视为整批通过。批次只改变交付节奏，双确认与资产锁定本身不放宽。
- 交付形态（这一轮给你图还是给你Prompt）：默认 `AUTO`——当前环境能直接出图就直接给图，不能就只给Prompt。你也可以一次定死：说「以后直接出图」锁定 `DIRECT_IMAGE`（直接整批出图，不再为Prompt单独停一轮，图仍整批给你挑）；说「只要Prompt / 我在别处出图」锁定 `PROMPT_ONLY`。三种形态都不放宽图片确认与资产锁定。
- 角色有对白不会自动触发音色模块。

## 6）环境资产制作

**最简指令**

```text
调用sd，只制作ENV-001环境资产。
```

**进阶指令**

```text
调用sd，为ENV-001制作可重复拍摄的环境资产，锁定空间结构、入口、主要活动区、关键家具、材质和主光方向。先给主参考图与必要多视角Prompt，等我确认后再生成图片。
```

**Skill 行为 / 停止点**

- Core 环境建立主参考图、必要多视角和关键区域 / 细节；Support 环境按同类 Board 组织。
- 环境不是“漂亮背景”，必须能支持人物行动与空间连续性。
- 同样执行 Prompt 确认和图片确认两道 Gate；候选图未经确认不能成为 Canonical 环境资产。

## 7）道具资产制作

**最简指令**

```text
调用sd，只制作PROP-001道具资产。
```

**进阶指令**

```text
调用sd，为PROP-001制作道具资产。锁定整体形态、尺寸比例、结构、材质和关键识别细节；只为剧本已确认的开合、破损和使用状态制作变体。先输出生图Prompt，等我确认。
```

**Skill 行为 / 停止点**

- 在STATE-02只识别重要道具：承担剧情/信息/品牌识别、关键动作或交接、明确状态变化、跨镜连续性，或由你指定需要锁定的物品。普通陈设、背景装饰和无须锁定的通用消耗品不进入道具资产制作；每个重要候选才明确进入Core、Support Board，或记录不作为正式资产的理由。
- Core 道具的主参考固定为一张1×4横版设定图：正面、侧面、背面、关键细节。只有第四格不足以验证关键结构时才另出细节图；状态图和使用关系图仍只在剧情确有需要时制作。Support 道具进入同类 Board。
- 不能用下游 Prompt 临时重设计正式道具。
- 仍有两个可审计确认点：先 Prompt，后图片；在每个当前确认点，任一推进表达即确认。

### 正式FX资产制作

**最简指令**

```text
调用sd，只制作FX-001正式效果资产。
```

**进阶指令**

```text
调用sd，为FX-001制作正式效果资产。锁定触发源、可见物理驱动、主视觉参考、允许的强弱状态变体，以及跨Shot的残留后果；先输出生图Prompt，等我确认。
```

**Skill 行为 / 停止点**

- 仅当效果需要复用、绑定其他资产、跨镜头继承或留下持续后果时，才建立正式FX资产；一次性、低复杂度的效果会保持为Inline Effect。
- 正式FX会记录触发、来源、传播、交互、结束状态与残留。受风、重力、流体、燃料、能量源或碰撞影响时，系统还会记录实际可见的驱动因素。
- 跨Shot或Clip持续的FX会在每个边界维护状态账本，并锁定主视觉参考、不可变视觉锚点和允许的状态变体；不跨镜头的Inline Effect不会附加这套记录。
- 与其他视觉资产相同：先确认模型选择和Prompt，再确认候选图片，才会成为Canonical FX资产。

## 8）资产缺失检查

**最简指令**

```text
调用sd，只检查当前项目缺少哪些资产，不生成图片。
```

**进阶指令**

```text
调用sd，核对Production-Locked Script、Asset Registry和当前State，只检查CHAR、ENV、PROP和正式FX：列出缺失、未确认、版本冲突、Support Board缺项和会阻塞后续阶段的资产；不要制作资产，不要生成Prompt或图片。
```

**Skill 行为 / 停止点**

- 会区分“未发现”“已登记但未确认”“Prompt已确认但图片未确认”“Active / Canonical版本冲突”等状态。
- 角色音色不属于视觉资产缺失 Gate：默认不检查、不补建、不写 Not Applicable，也不阻塞 STATE-03 或 STATE-08。
- 配乐同样不是资产缺失项，除非你显式请求独立 Music 模块。

## 9）角色音色模块（显式调用才启动）

**最简指令**

```text
调用sd，为CHAR-001设计角色音色，并输出独立Seed Audio兼容提示词。
```

**进阶指令**

```text
调用sd，为CHAR-001建立长期稳定的Voice Profile，并为这句台词输出独立Seed Audio兼容提示词。把稳定声音身份与本句Dialogue Performance分开；只输出Prompt，不生成音频。未知口音不要猜。
```

**如果你确实要把声音控制写进当前视频模型 Prompt**

```text
调用sd，只在CLIP-003这次Seedance视频Prompt中使用已确认的VOICE-REF-01做声音控制，按最小Delta写入；不要复制完整Voice Profile，也不要把授权延续到后续Clip。
```

**Skill 行为 / 停止点**

- 默认不启动：普通视频、角色分析、角色视觉资产、Detailed Shot、Storyboard、Clip、Seedance、对白、口型、音效、“继续”或“下一个”都不会自动制作音色。
- 未显式调用时，默认外部已有可用角色音色资源；不检查缺失、不提示补建、不形成 Asset Gate。
- 常规 STATE-08 视频 Prompt 默认完全不出现 `音色特征：`、Voice Profile、Voice / Audio Reference 或“已有 / 缺少音色”等文字。
- 显式调用后输出独立 AUDIO / SEED-AUDIO Package。当前结构是“基于 Seed Audio 官方支持维度整理的 SD Film 兼容模板”，不是官方唯一字段格式。
- Voice Identity 与当前一句的情绪、停顿、力度、韵律分开；Ambience、Key Sound Effects、Scene Progression 只在场景级声音任务需要时出现。
- 只要求 Prompt 时，交付 Prompt 后即停止；只有你同时明确要求实际音频且工具与授权条件满足时，才生成候选音频。

## 10）配乐 / BGM / 声音设计

### A. 对白、环境声、动作声、Foley 等同期声音

**最简指令**

```text
调用sd，只优化CLIP-003的同期声音设计：对白、环境声、动作声、Foley和声音尾部，不要设计配乐。
```

“声音设计”如果语义更像对白、同期声或音效，不会自动触发角色音色，也不会自动触发 Music 模块。

### B. 后期配乐 / BGM / SeedMusic

**最简指令**

```text
调用sd，为整条片子规划配乐与留白。
```

**进阶指令**

```text
调用sd，审阅全部Confirmed Clip，为整条片子做Music Spotting、Music Bible和Cue Sheet，并为实际需要音乐的Cue输出SeedMusic纯音乐提示词。由你专业判断哪里进音乐、哪里只保留同期声；不要全片持续铺乐。
```

**Skill 行为 / 停止点**

- Music 模块只在你明确要求配乐规划、Cue Sheet、主题动机、SeedMusic Prompt等交付物时启动。
- 默认是纯音乐；歌词、演唱、合唱、哼唱、吟唱或 Vocalise 必须另行明确要求。
- 即使你同时要求视频 Prompt 和配乐，也会拆成两个独立 Package。
- STATE-08 视频 Prompt 永久禁止非剧情内配乐；配乐只能进入独立 MUSIC / SEED-MUSIC Package，不能混写进视频 Prompt。
- Music 模块会同时设计音乐与留白，不会把“全片配乐”理解成每个 Clip 都持续有音乐。

## 11）Detailed Shot Design / 专业分镜设计

**最简指令**

```text
调用sd，根据已确认场景和资产制作Professional Detailed Shot Script。
```

**进阶指令**

```text
调用sd，为SCENE-003制作Professional Detailed Shot Script。先完成Spatial Blocking Decision，锁定角色起终点、移动路径、180度轴线、机位侧和关键道具位置；再逐镜完整设计时间码、构图、表演、镜头调度、光色、同期声音、首尾边界和下一镜Handoff。不要输出Seedance Prompt。
```

**Skill 行为 / 停止点**

- 必须已有 Scene Breakdown、必要资产和 Visual Direction；不足时会返回事实拥有者，不靠分镜文字补造。
- 复杂多人、打斗、追逐、进出场或严格轴线场景会优先使用“俯视 Blocking Map + 文字规则”双锁；如需生成地图图像，会先给地图 Prompt 等确认。
- 正式输出是完整 Professional Detailed Shot Script，不是“景别 + 运镜 + 画面”简表。
- 单镜和批量字段完全相同；过长时默认按每批约 4—5 个完整 Shot 分批，不会压缩字段或写“同上”。
- STATE-06 不输出 Seedance Prompt，也不提前创建 Clip ID。

**分镜的三种形态（别混）**

- **默认分镜表**：最常用的交付。镜号、画面与动作、画面表达、连续性、资源五列，可直接用于拍摄和验收。
- **完整版专业分镜**：说`给我完整版专业分镜`，才展开十八个字段的完整记录（时间码、景别/焦段、构图、表演、摄影参数、镜头调度、光色、转场、台词、同期声音、AI制作备注、资产）。用于跨人交接或自己逐镜抠细节。
- **Storyboard 视觉分镜板**：另一条可选辅助链路（见下一节），只有显式请求才启动。它不改变上面两种文字分镜，也不作为视频参考资产。

## 12）Storyboard 分镜板

**最简指令**

```text
调用sd，根据已确认Detailed Shot Design制作Storyboard。
```

**进阶指令**

```text
调用sd，把SHOT-001到SHOT-006制作成16:9 Storyboard，每镜一个画格，保留Shot ID、构图、人物空间关系、关键动作状态和边界注记。不要改变镜头设计，也不要把Storyboard作为视频参考资产。
```

**Skill 行为 / 停止点**

- Storyboard 只有你显式请求时才启动，是可选辅助产物，不是 STATE。
- 前置条件是已确认 Detailed Shot Design 和必要资产。
- 它不替代 STATE-07 Clip Production，不参与 Clip 划分，也不是进入 STATE-08 的必要条件。
- Storyboard 图片、多格拼图、线稿或截图不能成为 STATE-08 Canonical Reference。

## 13）把 Shot 组合为 Clip

**最简指令**

```text
调用sd，把已确认的Detailed Shot Design组织为Clip。
```

**进阶指令**

```text
调用sd，把当前Confirmed Detailed Shot Design按正式Shot顺序组织为Clip。锁定Seedance 2.0时由我选择4—15秒；锁定Seedance 2.5时由我选择4—30秒，16—30秒自动完成严格预检，失败才拆为4—15秒Clip。不要改Shot ID、顺序、剧情或镜头目的；逐Clip完成Preflight、Scope Firewall、End-State Record、Reference Routing、尾帧A/B/C判定和最小充分参考。输出Clip Plan后停下来给我确认。
```

**Skill 行为 / 停止点**

- 只能基于实际可读且 Confirmed 的 Professional Detailed Shot Script；原剧本中的“镜头1 / Clip A”等标题不能直接变成正式 Clip。
- 一个 Clip 可以包含一个或多个相邻、兼容的 Shot；Seedance 2.0为4—15秒，Seedance 2.5为4—30秒，16—30秒必须通过内部严格预检；实际秒数由你在模型窗口内选择。
- 每个正式 Shot 按原顺序且只进入一个 Clip；不能为减少数量强行合并。
- 每个 Clip 原则上只承担一个主要可见 Beat。此前事件不重播，后续事件不提前表演。
- Clip Plan 不输出最终 Seedance Prompt；确认后才进入 STATE-08。

## 14）生成单个或全部 Seedance Clip Prompt

### 单个 Clip

```text
调用sd，只输出CLIP-003的Seedance视频提示词。
```

### 全部 Clip

```text
调用sd，按顺序输出全部Confirmed Clip的完整Seedance视频提示词；过长时只在完整Clip之间自动分批，不要压缩字段。
```

### 指定范围

```text
调用sd，只输出CLIP-003到CLIP-005的完整Seedance视频提示词，其他Clip不要输出。
```

**Skill 行为 / 停止点**

- 必须已有 Confirmed Clip Production Plan；不能直接根据原始剧本生成最终 Prompt。
- 一个 Confirmed Clip 对应一条完整 Prompt；即使包含多个 Shot，也不拆成多条 Shot Prompt。
- 默认一次只交付一个待处理 Clip。批量授权只改变数量，不改变每个 Clip 的完整结构。
- 每个Clip都会在最终Prompt前自动检查是否需要人物 / 空间调度草图。判定不需要时直接输出Prompt；判定需要时先生成并验证草图，把它作为只控制站位、朝向、距离、关系轴、姿态或动作路径的参考资产，下一次继续才输出Prompt。草图不替代角色、环境或道具正式资产。
- 当前Skill已注册真实`REF-SKETCH-MASTER`图片。生成需要的草图时会把该PNG作为实际视觉参考输入，并走独立Technical Visual Blocking Sketch模板，不会调用Storyboard模板；只有文件或工具输入失败时才会明确报告文字合同回退。草图人物默认统一使用无性别技术调度人偶，仅靠角色标签、技术颜色和位置区分；明显脸、发型、服装、性别化体态或角色外貌重绘会被拒绝注册。候选图缺少主Blocking、角色标签、箭头、适用俯视 / 路径图、镜头信息、动作权限或用途说明，或仍是单幅电影感铅笔插画时，也会以`Artistic Storyboard Drift`失败并拒绝注册。
- `REF-SKETCH-MASTER`只用于生成当前Clip的`REF-SKETCH-XX`，默认不会出现在最终视频Prompt的`参考资产：`里，也不占视频模型的9张图片预算；真正投喂视频模型的是经验证的当前Clip草图。
- 已确认的项目色卡可按当前Clip的真实光色漂移风险选择性投喂，并计入模型图片预算；它在模型参考列表中会明确标为`Project Color Reference（非资产）`，且只控制综合色相、明度、饱和度与强调色占比。色卡不会锁定人物、环境、道具、构图、光源、镜头或最终画风，也不会因为全片存在色卡而自动进入每个Clip。
- 编译前会做 Prompt Control：只填补当前 Clip 尚未被资产、首尾帧或 Blocking 锁定且确实需要控制的内容；内部控制矩阵不会变成最终 Prompt 的额外栏目。
- 会先做字段归属：每条约束只在一个权威字段完整定义。`首帧参考`负责起始状态，`尾帧限制`负责结束状态与carryover，`人物一致性`只负责长期人物身份，`环境一致性`只负责场景结构与环境基线，逐镜只写新增动作/状态变化/局部连续性；其他位置只在真实变化或边界接口需要时写最短Delta，不会为强调而在6—9个字段全文重复。
- 会做 Prompt Pollution 清理：合并重复、消解冲突。导演名、流派名、题材风格名、情绪标签和“电影级 / 高级感 / 治愈感 / 青春感 / 潮湿夏日”等高层词可以保留；重要标签首次出现在最终 Prompt 时，会在同一风格段解释它在本项目中的具体含义，并选择当前 Clip 必要的 3—5 个（或更少）可见 / 可听执行项。具象化后不会默认删除标签，只有完全冗余、无关、冲突或会误触发默认视觉包时才省略。项目风格已由正式资产、视觉开发或 Style Bible 锁定后，后续连续 Clip 只补当前差异，不重复整段解释；动作复杂 Clip 会把风格压到 1—3 项或更少，确保主体、动作、空间、时间顺序、镜头与状态承接优先。“短”或“长”本身都不是质量标准。
- 会分配 Generation Budget：只设一个主要生成负荷，最多一至两个辅助负荷，并主动降低非核心复杂度；不会把身份一致性、复杂动作、高密场景、复杂运镜、群体、口型、FX和光色变化同时拉满。
- 会执行 Reference Routing：只选择能解决当前风险的最小充分参考集合，不会因为资产在 Registry 中、上一 Clip 用过或预算还有空位就全部塞入。
- 会遵守 Clip Scope Firewall：已发生的事件不重播，只执行本 Clip 的主要可见 Beat，未来事件和暂不应出现的结果不提前进入画面；这些内部标签不会出现在最终 Prompt 中。
- `画幅：`除比例与媒介外，还会写明本 Clip 分镜总数（例如“本Clip为3个分镜，禁止生成额外镜头”），并且该总数与逐分镜实际数量严格一致；模型有扩写单镜倾向时，末尾`反向提示词：`会补一句同义兜底。这是既有字段的内容要求，不会新增任何 Prompt 栏目。
- 每个分镜的`画面描述：`会同时承担背景与环境活动：画面里出现非主要角色时逐人写明镜内任务、注意对象、反应时点与强度差异（谁先察觉、谁晚半拍、谁完全不看），环境按地点与时间维持自己的节奏；没有人物活动时写清环境动态或有意留白与仅有环境声，不会用“安静”“空”概括，也不会出现全员同一时点同向同强度动作或同时冻结。
- 常规视频 Prompt 默认不出现音色字段；雨声、风声、纸张、脚步、道具或乐器声只进入各分镜`音效`。正文以正向、可执行的目标状态为主：能写成“表演克制、镜头简洁自然、左手持续持伞”等正向要求时，不在`主风格`、一致性或各分镜里反复堆“禁止 / 不要 / 避免”。通用高风险禁止项会合并压缩到每个Clip末尾唯一的`反向提示词：`，该段固定以禁背景音乐规则开头，并且后面不再追加任何正文。历史事故物、其他Clip状态、未来剧情和与当前Clip无关的词会删除，同义错误合并为少量当前风险类别。只有必须贴近某个具体动作、空间关系或物理连续性才能说清楚的最小约束，会留在对应分镜字段。

## 15）逐个 Clip 输出（支持“下一个”）

**开始**

```text
调用sd，从下一个尚未交付的Clip开始，每次只输出一个完整Seedance视频提示词。
```

**继续**

```text
调用sd，下一个Clip。
```

或：

```text
调用sd，继续输出下一个尚未交付的Clip，不重复前面的内容。
```

**Skill 行为 / 停止点**

- 会读取当前 Checkpoint，只输出下一个未交付 Clip，不重复已完成内容。
- 推进表达只授权一个合法Checkpoint，不自动授权批量输出、启用音色或启用配乐；当该Checkpoint是已展示、可核对的确认点时，它同时确认当前Artifact。它仍不替代外部提交、缺失尾帧/文件、互斥选择或额外权限。它会自动执行单Clip草图Gate：若当前Clip确实需要Visual Blocking Anchor，系统可先生成并验证这张受限调度草图，因为这是该Prompt的内部必经检查。
- 下一步若需要选择、外部输入或尾帧，会在对应Checkpoint停下说明；若只是确认，直接推进。

## 16）优化 / 返修某个 Clip Prompt

**最简指令**

```text
调用sd，只优化CLIP-003的Seedance视频提示词，其他Clip不变。
```

**单变量返修示例**

```text
调用sd，CLIP-003只有站位错：A应该在画面左侧，B在右侧，摄影机保持原轴线侧。只修Spatial / Blocking和必要的首尾边界，剧情、动作、资产、运镜、光色、声音和其他Clip全部不变。
```

```text
调用sd，CLIP-003只修雨伞从右手瞬移到左手的问题。保持人物、镜头、表演、环境和风格不变。
```

```text
调用sd，CLIP-003只修模板格式，补齐缺失字段，不重新设计镜头。
```

**Skill 行为 / 停止点**

- 先诊断问题属于 Identity、Spatial / Blocking、Prop、Motion / Performance、Camera、Lighting / Color、FX / Sound、Coverage 或 Prompt Scope / Template。
- 第一轮只改影响最大的一个变量及必需相邻边界，保留 Accepted Unaffected Artifacts。
- 如果根因在角色 / 环境 / 道具资产、Shot Design或Clip Plan，会返回对应上游最小修正；不会用 Prompt 掩盖上游错误。
- 同一Clip只是改措辞、压缩、主风格、反向提示词、台词或音效时，会继续复用已确认草图，不重复生成。只有并排变面对面、换位、离座、明显转身 / 靠近、正反打切换、轴线侧 / 环绕、角色数量、复杂道具、动作路径或Clip起止Blocking发生实质重构时，才重新判断并KEEP / REPLACE / RETIRE / CREATE草图。
- 同类失败第二次必须使用稳定降级；第三次停止盲重试并返回事实 / 设计拥有者。

## 17）长视频连续性：REF-TAIL 三种模式

用户不必记英文术语，只要说明你想怎么接：

| 模式 | 什么时候用 | 是否需要上一Clip尾帧 | 可复制指令 |
|---|---|---|---|
| A 同镜头连续承接 | 上一个镜头在下一Clip继续，接近一镜到底 | 需要 | `调用sd，CLIP-004必须从CLIP-003同一镜头无缝续接，使用上一Clip最终尾帧作为直接承接依据，不得重新摆位或重播动作。` |
| B 新镜头但参考尾帧 | 换了新机位 / 景别，但仍要锁定站位、朝向、距离、空间或道具状态 | 需要 | `调用sd，CLIP-004另起新镜头重新构图，但参考CLIP-003尾帧保持人物站位、朝向、距离和道具状态。` |
| C 新镜头无需尾帧 | 明确反打、特写、俯仰拍、重构图、换场或其他不依赖旧画面的新镜头 | 不需要 | `调用sd，CLIP-004是新镜头且无需上一尾帧；用Canonical资产、Spatial Blocking和文字End State重建首帧。` |

**Skill 行为 / 停止点**

- A / B 都会标记 `Tail Frame Required = YES`。即使你尚未上传尾帧，Prompt 仍可先完整交付，但会把 `REF-TAIL` 标为“待用户提供 / 待上传、未确认”；实际提交生成前必须补图。
- A 是同镜头直接接上；B 是新镜头重新构图，只用尾帧保持连续性。两者不能混写。
- C 标记 `Tail Frame Required = NO`，不会要求截图，也不会把上一尾帧列入参考资产。
- 尾帧只锁定瞬时姿态、站位、动作阶段和构图；角色身份、环境结构、道具造型仍以正式 Canonical 资产为准。
- 每个 Clip 都必须定义自己的新稳定尾帧，最后 1 秒不启动新复杂动作，供下一 Clip 再判断 A / B / C。

## 18）连续性 / 穿帮检查

**最简指令**

```text
调用sd，只做连续性和穿帮检查，不重新生成。
```

**进阶指令**

```text
调用sd，只检查CLIP-002到CLIP-004：角色身份、人数、左右站位、180度轴线、视线、动作阶段、道具持有者、环境结构、光色、声音尾部和REF-TAIL用途。逐项指出问题、受影响ID、事实拥有者和最小修复；不要改Prompt或重新生成。
```

**Skill 行为 / 停止点**

- 会把计划的 End-State、实际生成的 Observed State、已接受的 Canon State 分开核对。
- 会检查 A / B / C 是否选对、尾帧用途是否正确、参考资产是否越权，以及是否发生换脸、换边、道具瞬移、动作重播、无授权跨轴等问题。
- Review 报告里的逐镜台账与相邻镜台账是全覆盖记录，不是问题清单：每个受审 SHOT 和每个受审边界都会单独占一行，每一列都会给出结论（通过写`PASS`或`无风险`，不适用写`N/A`并写明理由），不会只列有问题的镜头或用一段总体评价代替逐镜检查。任一镜头或任一维度为空，这次 Review 就算没做完，不会给出 `PASS`。
- 只分析时不会自动生成、重试、修改资产或把结果写成 Accepted Canon；需要修复时会先给 Return Route。

## 19）根据实际生成结果更新 Accepted Canon

**最简指令**

```text
调用sd，我接受CLIP-003的这个Take。根据实际画面更新Accepted Canon，并让后续Clip从这个实际状态继续。
```

**进阶指令**

```text
调用sd，审核RUN-CLIP003-02的实际起止状态。我明确接受这个Take：把可观察到的人物站位、朝向、动作阶段、道具持有、摄影机终点和临时光态写入Accepted Canon；不要把其中的脸部或服装漂移升级为角色资产。绑定Run ID、Prompt Revision和Review ID。
```

**Skill 行为 / 停止点**

- 只有你明确接受具体 Take，才会建立 / 更新 Accepted Canon；技术 Review PASS 本身不等于用户接受。
- Accepted Canon 来自实际 `Observed State`，不是把原计划值抄一遍。
- 后续 Clip 在同一维度优先从 Accepted Canon 继续，不能无过程强行纠回原计划。
- 已接受 Take 中的脸、服装、环境结构或道具造型漂移不会覆盖正式 Canonical 资产；只继承合法瞬时状态，并把漂移列为 Continuity Risk。

## 20）STATE-09 Review / 是否重做 / 单变量返修

**最简指令**

```text
调用sd，审核这个实际生成结果，判断PASS、REVISE还是REBUILD。
```

**进阶指令**

```text
调用sd，对CLIP-003的实际视频做STATE-09 Review。对照Project Bible、Canonical Assets、Detailed Shot Design、Clip Plan、Prompt和上一Clip Accepted Canon，输出受影响ID、问题等级、最小必要修复、Return Route、Recheck Scope和Must Not Change。第一轮只修最高影响变量，不要整段推翻。
```

**Skill 行为 / 停止点**

- `PASS`：硬门槛通过，允许完成 Review；如要把 Take 写成 Accepted Canon，仍需你明确接受该 Take。
- `REVISE`：局部可修复，返回最小必要 Workflow；修完必须重新 Review。
- `REBUILD`：上游事实或设计严重错误，返回事实 / 设计拥有者；不会把 STATE-09 标为完成。
- 站位错优先只修 Spatial / Blocking；身份漂移优先修 Identity Reference 路由；动作错优先修 Motion / Performance；镜头错优先修 Camera。
- 只有多变量确实耦合、单变量无法形成合法输入，或你明确要求整体重做时，才允许多变量修订。
- Review 会额外做一组**审美判断**，它问的不是“有没有执行已确认的设定”，而是“**取舍在画面里看不看得出来**”：第一眼落在哪、有没有明暗层级、主色强调色分不分主从、当初放弃的那一边是不是真被放弃了、有没有“每样都有一点”。六条判据只给你看证据。
- **“好不好看”由你说了算。** 系统只输出观察结论，不会替你判定审美；你没给结论时这次 Review 记为 `PENDING_USER`，**不会判 PASS**。当初做过试片的话，Review 会拿那张试片帧对照成片。
- 如果发现是**当初的美学决定本身选错了**（不是没执行），会返回 STATE-04 重做那一项，而不是让你在 Prompt 上反复补救。

## 21）视频封面设计

**当前能力边界**

当前 Skill **没有独立的普通“视频封面”Workflow**。现有正式能力是电影海报 / Key Art，包括数字竖版海报与横版平台 Key Art；普通社媒封面和普通缩略图被 Poster Workflow 明确排除。

如果你要的是影片主视觉式封面，推荐这样说：

```text
调用sd，根据当前项目设计一张9:16数字竖版电影Key Art，作为视频封面主视觉。沿用已确认角色、环境和道具资产，不重新设计；保留标题安全区，不生成最终文字。
```

你也可以说：

```text
调用sd，根据当前项目设计9:16视频封面。
```

但 Skill 应先判断它是否能合法归入“电影 Key Art / 数字竖版海报”；若你要的是普通平台缩略图，则会明确提示当前未支持，而不是伪装成现有模块。

**停止点**

- 核心影片事实、资产或 Visual Direction 不足时，会返回对应阶段补齐。
- 片名、日期、credits、logo 或授权不确定时会标为待确认，不会虚构。
- 默认继承现有角色 / 环境 / 道具资产；除非你明确要求并走资产变更流程，否则不重新设计。

## 22）宣传海报设计

**最简指令**

```text
调用sd，根据当前项目设计电影海报。
```

**进阶指令**

```text
调用sd，根据当前项目设计一张9:16先导电影海报。沿用当前Active Character、Environment和Prop资产，只改变宣传构图、光色和视觉母题；片名为“……”，其他日期、credits和logo未确认的内容不要生成。输出Poster Design Package、Base-image Prompt和排版规格。
```

**Skill 行为 / 停止点**

- 正式支持电影海报、Key Art、One-sheet、先导 / 正式 / 角色 / 概念海报和标题字方向。
- 默认选择一个一级视觉母题和一个主要构图模型，不做无意义头像墙。
- 准确文字采用可控排版层；生成式文字只作草案，最终需逐字核验。
- 参考图只提取抽象设计原则，不能复制可识别构图；未授权素材不进入最终海报。
- 海报是辅助 Workflow，不改变主 Pipeline 当前 STATE。

## 23）社媒封面 / 缩略图

**当前状态：未发现专用支持。**

当前 Poster Workflow 明确不处理普通社交媒体封面、普通缩略图或非电影宣传图。因此不要把下面这类任务当作已有 SD Film 正式模块：

```text
为普通账号做YouTube缩略图、直播封面、信息流社媒卡片。
```

如果目标本质上是影片的横版 / 竖版平台 Key Art，可以明确按电影 Key Art 路由：

```text
调用sd，把当前电影海报主视觉重排为16:9横版平台Key Art。沿用现有资产与视觉母题，不做普通网红缩略图风格。
```

若目标确实是普通社媒封面或缩略图，应使用其他合适的设计工具 / Skill；SD Film 会如实说明当前未支持，不硬写不存在的流程。

## 24）只分析图片 / 视频结果，不重新生成

**最简指令**

```text
调用sd，只分析这个图片/视频结果，不重新生成，也不要修改Prompt。
```

**进阶指令**

```text
调用sd，只读检查这个CLIP-003实际结果。对照当前Canonical Assets、Detailed Shot Design、Clip Plan和上一Clip尾帧，分析身份、空间、动作、道具、摄影、光色、声音与连续性；列出证据、问题和最小Return Route。不要生成、编辑、重试、改状态或写入Accepted Canon。
```

**Skill 行为 / 停止点**

- 需要实际图片 / 视频或可访问的生成结果；未看到结果时不会假装完成 Review。
- 只分析不会自动重做、后期编辑、生成新 Prompt、确认候选图片或更新 Canon。
- 如需把结果接受为 Canon，另发第19节的明确接受指令。

## 25）继续旧项目 / 重新调用最新 Skill

### 继续但不强制重载

```text
继续。
```

会从当前已验证 Checkpoint 继续最近未完成步骤；普通“继续”不是 Skill 重载指令。

### 重新读取当前实际安装版再继续

```text
重新调用sd，恢复当前项目，从最后一个安全Checkpoint继续。
```

或：

```text
重新加载SD，保留当前项目、Production-Locked Script、Confirmed Assets、Accepted Artifacts和用户约束，然后继续下一个合法步骤。
```

**Skill 行为 / 停止点**

- 首次或普通`调用SD / 调用sd / 调用SD流程`会激活SD Film，读取当前可访问规则并按项目事实进入正确STATE / Workflow；不存在可恢复项目时可建立新项目入口。
- 明确`重新调用SD / 重新调用sd / 重新加载SD / 重新加载sd / 按当前Skill继续 / 按当前 skill 继续`会重新读取当前可访问Skill，同时保留已确认的项目事实，从当前STATE / Workflow入口重新处理当前对象；不会只拿上一版Prompt继续润色，也不会无故清空已确认资产、草图或进度。
- `重新调用sd，恢复当前项目`会优先使用当前Chat实际可访问的Skill资源，并依次尝试可用项目状态、Portable Project State和当前可验证的项目上下文；Skill规则来源和项目事实来源可以不同，不会因此恢复失败。
- 普通`继续 / 下一步 / 下一个`只从当前合法Checkpoint继续，不等于强制重新加载；当前Workflow本来要求的检查仍会照常执行。
- 普通Chat会先使用当前运行时可访问的Skill资源；本机Windows路径不可读不代表必须切Work。Work不是恢复旧项目的默认要求，只有必须读取/修改普通Chat无法访问的本地文件且现有Portable State与项目上下文不足时才需要。
- 旧项目已有的定稿剧本、角色/环境/道具资产、Blocking、Spatial Snapshot、Confirmed草图、Accepted Take / accepted prompt和已确认镜头会保留；新版Screenwriter / Director规则只补当前Workflow确实缺少且可可靠推导的Intent，不会把项目退回STATE-01重做。
- 只有本轮真的读到当前Skill入口、版本和必需路由文件，Skill才能说“已重新加载”或“严格按当前Skill执行”；失败时会说明实际使用的是当前可访问资源、Portable State或Project Context等fallback，不会拿旧对话摘要冒充当前安装版。
- 显式恢复会简短显示Skill来源、项目状态来源、映射后的STATE、当前Workflow / Object、保留的Canon、需要补的Writer / Director Intent和Next Workflow，方便核对实际恢复依据。
- 会核验 Project ID、State Source、Revision、Checkpoint和 Artifact；不能唯一识别项目时会停下确认，不会猜“最近项目”。
- 生成失败第一次最小修正，第二次稳定降级，第三次返回事实 / 设计拥有者。

## 26）只检查 Skill 当前 Pipeline / STATE / 某条规则，不执行制作

**最简指令**

```text
调用sd，只检查当前Pipeline和STATE，不执行制作。
```

**进阶指令**

```text
调用sd，读取当前实际安装版SKILL.md、config、workflow map和相关权威文件，只检查“Voice opt-in、STATE-08音色省略、REF-TAIL A/B/C、单Clip交付”四条规则是否一致。报告文件证据、冲突和当前版本；不要修改文件、推进项目、生成Prompt或调用媒体工具。
```

**其他可复制示例**

```text
调用sd，只告诉我当前项目处于哪个STATE、依据是什么、下一个合法Workflow是什么，不继续执行。
```

```text
调用sd，只检查CLIP-003的Reference Budget和Reference Routing规则是否满足，不修改Prompt。
```

**Skill 行为 / 停止点**

- “调用sd”会先重新解析当前Chat可访问的Skill资源并重读入口；只有实际取得 `Skill Version`、`Build ID`和必要读取证据才能报告 `RELOADED`或声称严格遵守当前Skill。
- 只检查不会自动推进主 Pipeline，也不会因发现问题直接修改 Skill 或项目成果。

## 27）进入 Work 修改 Skill 的推荐指令

**最简指令**

```text
进入Work，读取当前实际安装的C:\Users\Lenovo\.agents\skills\sd，只修改我指定的规则。
```

**推荐完整指令**

```text
进入Work，修改用户当前实际使用的C:\Users\Lenovo\.agents\skills\sd。

先完整读取SKILL.md，并读取config、workflow map、相关rules/workflows/templates/references；先搜索是否已有同类规则，优先修改权威原文件，不平行新增重复Schema。

本次目标：<写清要改什么>。
必须保持：<写清不能动什么>。
影响范围：<指定Workflow、STATE、Template或规则>。
完成标准：<列出需要通过的正例、反例和回归场景>。

正式修改后按SKILL.md的版本纪律同步更新Skill Version和Build ID，并自动执行`references/maintenance_self_check.md`中的16项`Skill Update Self-Check`与两个Guard（判据真源为`references/maintenance_self_check_protocol.md`）。如果用户调用方式、模块入口、Prompt输出结构、音色、连续性或Review等用户可见行为变化，同步更新USER_GUIDE.md。最后报告变更分类、修改文件、规则真源、重复/冲突/污染/路由/模板/引用检查、定向回归、USER_GUIDE同步状态和未解决Warning。
```

**Skill 修改任务建议写清**

- 改什么：例如“音色必须 opt-in”“只修 REF-TAIL B 模式”“增加一个真正的社媒封面模块”。
- 不改什么：例如“不改变主 STATE 编号”“不修改视频 Prompt Template”“不重做已有项目资产”。
- 权威位置：规则、Workflow、Template、Reference分别由谁拥有；不知道时要求先扫描路由再决定。
- 验证场景：至少写正向触发、负向不触发、旧项目恢复、单 Clip / 批量、Review返修等。
- 完成后不要只说“已改”，要报告实际文件、版本、回归检查和残留冲突。

**以后固定执行的 Skill 维护链**

```text
读取当前规则
→ 定位相关规则与权威来源
→ 分类现有覆盖
→ 最小修改
→ Skill Update Self-Check
→ 对整个 Skill 的发现项做风险分级
→ 当轮修复所有安全和可控问题
→ 对原始修改与附带修复分别做定向回归
→ 用户可见行为变化时同步 USER_GUIDE
→ 输出变更报告
```

变更分类固定使用`no_change / optimize_existing / merge_existing / add_new / deprecate/remove`。自检是维护层，不是新的影视制作STATE；它不会推进项目或改变已确认成果。纯拼写修正也会至少检查重复、冲突和文件引用。

自检的发现范围覆盖整个Skill，不只检查本次改动。已经发现的安全局部问题和所有者、回归路径明确的跨文件问题，应在当轮修复；只有可能改变用户已确认行为、主Pipeline、STATE、资产锁、最终Schema、外部兼容，或无法可靠验证的大规模迁移，才可标记`WARN`并说明证据、影响、修复方案和需要的决定。“与本次修改无关”本身不再是延期理由。

## 28）万能指令公式

```text
调用sd + 我要做什么 + 当前输入 + 必须保持什么 + 重点优化什么 + 做到哪一步停
```

### 模板

```text
调用sd，我要【目标】。
当前输入是【剧本 / 项目 / 资产 / Shot / Clip / 实际生成结果】。
必须保持【剧情、角色身份、资产版本、空间关系、道具、风格、已接受结果】。
重点优化【节奏 / 表演 / Blocking / Camera / Lighting / Sound / Prompt Control】。
只做到【具体STATE / 具体Artifact / 具体Clip / 诊断报告】后停下来，等待我确认；不要【明确禁止的动作】。
```

### 示例：完整视频

```text
调用sd，我要把这个定稿剧本做成9:16视频。当前输入是最终剧本和现有角色参考图。必须保持剧情、人物关系和现有角色外貌。重点优化空间连续性、动作可执行性和长视频接续。先完成项目初始化、剧本锁定和资产缺失检查，在资产清单后停下来；不要修改剧本或设计音色。
```

### 示例：单个 Clip

```text
调用sd，我要CLIP-003的Seedance视频提示词。当前输入是Confirmed Clip Plan和上一Clip已接受Take。必须保持Accepted Canon中的站位、动作阶段、道具持有和摄影机轴线。重点优化动作稳定性和尾帧可继承性。只输出CLIP-003，其他Clip不动；默认不要写任何音色文字。
```

### 示例：单变量返修

```text
调用sd，我要返修CLIP-003。当前问题只有A/B站位左右颠倒。必须保持剧情、角色资产、动作、运镜、光色、声音和其他Clip。重点只修Spatial / Blocking及必要首尾边界。输出修订后的CLIP-003 Prompt后停，不要整段重写。
```

## 常见误区

- `调用sd，生成Seedance Prompt` 不代表前置阶段可以跳过；Skill 会先检查 State 和 Confirmed Artifacts。
- `继续 / 下一步 / 下一个 / 往后做 / 接着做 / 好的` 不等于同意新的剧本改写范围、作出互斥选择、提交外部服务或授权批量输出；但在当前已展示、可核对的确认点，它们都确认当前Artifact。
- 角色有对白不等于要做音色；没有音色资产也不阻塞主流程。
- “声音设计”不自动等于角色音色或配乐；请明确说“角色音色”或“配乐规划”。
- Storyboard 不是 STATE，也不能作为视频参考资产。
- 一个 Shot 不是一个 Prompt；一个 Confirmed Clip 才对应一条完整 Seedance Prompt。
- 尾帧不是角色资产替代物；尾帧轻微换脸时仍以角色 Canonical Reference 锁身份。
- 局部错误先修单变量；不要用“整体感觉不对”直接推翻全部已接受成果。
- 电影海报 / Key Art 当前受支持；普通社媒封面和普通缩略图当前没有专用模块。

## 维护约定

每次Skill正式修改完成后都必须执行`references/maintenance_self_check.md`中的16项`Skill Update Self-Check`、`Standalone Skill Discovery Guard`和`Unconditional Chat Runtime Startup And Recovery Guard`。即使只修改文案、Knowledge、Template或拼写，也必须运行普通Chat启动与旧项目恢复基线，以及独立Skill发现基线，避免后续优化使Chat无法正常调用、出现两份同名Skill或误要求Work。该Reference是维护QA的唯一权威来源；本说明书只说明用户可见的调用和报告方式，不复制完整检查细则。

以后发生以下用户可见变化时，应同步更新本说明书：

- 用户调用方式或主要模块入口改变；
- 主 Pipeline、STATE路由或关键停止点改变；
- Prompt最终输出结构、默认单 Clip / 批量行为改变；
- 角色音色、配乐、连续性、REF-TAIL、Accepted Canon或Review行为改变；
- 海报、封面或其他对用户宣称的能力边界改变；
- 推荐指令不再能正确触发当前 Workflow。

不要求每次内部 Knowledge、实现细节或不影响用户下指令的文件变化都同步更新。只更新会改变“用户该怎么说、Skill 会做什么、何时会停”的内容。
