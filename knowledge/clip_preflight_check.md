# Clip Preflight Check / Clip生成前检查

## Module Contract

- Module Name：`Clip Preflight Check / Clip生成前检查`。
- Module Type：STATE-07与STATE-08共享的强制Quality / Continuity Knowledge Gate；同时唯一拥有Visual Blocking Anchor Assessment、Sketch Validation与Persistence判断；不创建新主STATE，不拥有最终Prompt Schema。
- Trigger：每个候选Clip在STATE-07形成执行合同时执行前置版；每个Confirmed Clip在STATE-08正式Prompt编译与Template Mapping之前执行最终版；用户以“下一个 / 下一步 / 继续”逐Clip请求时自动执行，无需另行提醒。
- Not Triggered As：不得把它当成新的制作阶段、资产生成Workflow、转场特效生成器或STATE-08新增栏目。
- Required Inputs：上一Clip End State与尾帧用途、当前Clip Start Requirement、逐分镜世界状态、Confirmed Assets及其Active Version、角色数量事实、Spatial Blocking / Relational Screen Geometry、Pose Hierarchy、Relationship Topology、STATE-06 Performance Goal / Performance Arc Map、上一有效Performance State、关键道具状态链、适用Transition事实、Action PREVIS、Confirmed Clip Production Plan，以及生成草图时必须读取的`references/ref_sketch_master.md`注册状态与Sketch Presentation Authority合同；实际生图输入包由`templates/23_visual_blocking_sketch_prompt.md`唯一拥有。
- Input Owners：剧情与时空事实由Script / Scene拥有；资产身份与版本由Asset Registry拥有；镜头与Blocking由STATE-06拥有；Clip边界与组织由STATE-07拥有。
- Output Owner：STATE-07检查记录由`templates/20_clip_plan.md`拥有；STATE-08只把通过后的语义映射到`templates/10_video_prompt.md`现有字段，本模块不新增、删除或改名最终字段。
- Allowed Writes：STATE-07 Clip Plan中的Preflight记录、`Spatial State / Continuity Risks / Reference Budget`既有栏目，以及STATE-08当前Clip Checkpoint / Projection / QA记录；可在这些既有位置保存Visual Anchor State与Blocking Signature，不新增主STATE、平行Registry或Seedance字段。Work/Codex把Confirmed Visual Blocking Sketch作为当前Clip受控参考写入Active Project Root既有`clips/`交付目录并登记文件 / 受控ID与Revision；普通Chat保留可回查的当前对话媒体引用和Checkpoint摘要。它计入图片预算，但不得登记为Canonical Character / Environment / Prop / FX Asset。
- Consumers：`workflows/10_clip_production_workflow.md`、`workflows/11_video_generation_workflow.md`与STATE-09 Review。
- Conflict Route：剧情/世界层事实冲突返回其事实拥有者；资产状态冲突返回STATE-03；Shot / Blocking /转场设计冲突返回STATE-06；Clip边界、参考预算或Clip执行合同冲突留在STATE-07；仅Prompt转译措辞错误留在STATE-08。

## Five Global High-Priority Rules

以下五条先于Reference Budget、Prompt润色与模型适配执行：

1. **视觉连续 ≠ 剧情连续，尾帧需求 ≠ 尾帧当前可用性。** 先做连续性主分类，再在既有判定中把尾帧使用方式明确为A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】。A/B均标记`Tail Frame Required = YES`，C标记`NO`；图片暂缺不能改变A/B/C。A/B缺图时仍须在【参考资产】直接列出统一`REF-TAIL`名称、用途与“待用户提供/待上传、未确认”，占Projected位但不计为已提交图片；不得伪造路径或声称已上传/已确认。Prompt可完整编译和交付，实际提交生成前补图。
2. **参考资产必须先通过当前世界状态检查。** 资产只有在当前分镜所在时空层实际存在、实际出场或正在执行合法状态转换时，才有资格进入候选清单。
3. **跨世界镜头必须先设计转场，再生成提示词。** 先锁定转场五要素，再写正式视频执行语句；不得用含糊的“金光一闪 / 突然切换”替代过程，除非用户明确要求这种省略。
4. **视觉参考条目必须具有实际视觉输入资格。** 每个视觉候选都必须能回答“这是不是一张实际会被投喂/引用的视觉资产？”只有答案为“是”的真实视觉文件/受控ID，或已经确定需要用户实际补入、且明确标记`待用户补充/待上传、未确认`的具体视觉参考图，才可进入【参考资产】。站位、换边、距离、共坐关系、数量、空间、行为、禁止项与镜头规则等纯文字约束一律移入其既有语义字段，不得用“参考说明”伪装成资产。
5. **每个Clip必须检查草图，但不强制每个Clip生成草图。** STATE-07只做Visual Blocking Risk Pre-Assessment；每次真正输出单Clip最终Prompt前执行Before-Single-Clip-Prompt Gate。Final=`NONE`直接编译Prompt；Final=`REQUIRED`时本轮先生成并验证适用草图，注册为Confirmed Visual Anchor并加入当前Clip【参考资产】，本轮不得同时输出最终Prompt。普通Prompt重写只复用已确认草图；Blocking Signature发生实质变化时才重新评估。

## Execution Order

每个Clip固定按以下顺序执行，不得把Reference Budget提前到世界状态和连续性分类之前：

`Continuity Classification（含Tail Frame Required判定）→ World-State Check → Character Count Lock → Spatial Composition Lock → Performance / Emotion Check → Visual Blocking Anchor Assessment → Prop State Check → Transition Check（适用时）→ Reference Asset Eligibility / Check / Budget → PASS或Return Route`

- STATE-07执行前置版：检查设计是否可生成，并对每个Clip记录`Visual Blocking Risk Pre-Assessment = NONE / POSSIBLE / REQUIRED`及理由；只标风险，不生成草图。任何失败先修Clip设计，禁止确认Clip Plan。
- STATE-08执行最终版：按实际资产、实际首尾帧和当前Blocking Signature复核；在撰写任何最终Prompt句子前执行Before-Single-Clip-Prompt Gate。任何失败不得Template Mapping、不得输出Prompt；先回到对应拥有者做最小必要修正。

## Visual Blocking Anchor Assessment / Before-Single-Clip-Prompt Gate

本Gate服务单个Clip的生成执行，不等同于STATE-06 Scene Top-down Blocking Map、Storyboard或正式Keyframe。每个Clip都检查，但只有高漂移风险且视觉锚点能实质降低歧义时才生成草图；不得为了流程统一给所有Clip出图。

### Dual Trigger, Single Execution

1. **Shot → Clip Integration / STATE-07**：轻量预判`NONE / POSSIBLE / REQUIRED`，记录风险来源、建议`S-SKETCH / P-SKETCH / A-SKETCH / Combined`和初始Blocking Signature；不调用图像生成。
2. **Before Every Single-Clip Prompt / STATE-08**：用户请求指定Clip、说“下一个 / 下一步 / 继续”，或普通/批量流程即将编译某Clip最终Prompt时，执行Final Assessment。不得要求用户另说“检查草图”。
3. **Final = NONE**：直接继续Prompt编译；简单单人、固定位置、普通转头且无复杂空间/轴线/动作关系时通常属于NONE。
4. **Final = REQUIRED**：选择最小充分草图类型，先生成或接收草图并执行Sketch Validation。验证通过后注册`REF-SKETCH-XX｜CLIP-XX…草图`为Confirmed Visual Anchor，加入当前Clip【参考资产】，说明用途与Authority，更新Reference Budget；本轮在草图和用途说明处停止，不输出该Clip最终Prompt。用户下一次继续时先确认Anchor仍为Confirmed且Blocking Signature未变化，再输出Prompt。
5. 图像工具不可用、草图未生成或验证失败时，保持当前Clip Prompt Pending并说明缺口；不得以纯文字假装已完成Required Anchor，也不得越过Gate输出最终Prompt。

批量输出仍逐Clip执行。若按顺序遇到`REQUIRED`且尚无Confirmed Anchor的Clip，在该Clip处暂停，不得跳过、重排或为保持批量而绕过草图。

### Risk Assessment Dimensions

至少检查以下维度，并沿用现有执行风险术语；内部可使用`LOW / MEDIUM / HIGH / ACTION HIGH`，但不得机械输出为最终Prompt字段：

1. 两人及以上角色；
2. 固定左右 / 前后关系；
3. 共享同一座椅、桌面、车辆、床、门口或其他空间结构；
4. Facing、Eyeline、Interaction Axis或180°轴线；
5. 身体不动、只允许眼睛 / 头部 / 手部变化等局部姿态约束；
6. 人物换位、走位、进出画；
7. 前 / 中 / 后景复杂关系；
8. 复杂道具交互；
9. 正反打、并排、背对背、包围、追逐等高漂移Relationship Topology；
10. A2 / A3复杂动作或复杂机位。

任一维度命中不自动等于REQUIRED。最终判断必须比较：现有Canonical资产、Scene Spatial Snapshot、文字Blocking、REF-TAIL或Accepted Canon是否已足够唯一；新增一张中性草图是否能显著降低Position / Facing / Topology / Axis / Action Path歧义。

### Sketch Types And REF-SKETCH-MASTER Presentation Routing

- `S-SKETCH / Spatial Sketch`：空间拓扑、左右 / 前后、环境锚点、Interaction Axis、Camera Safe Side与机位。
- `P-SKETCH / Pose Sketch`：Position、Torso Orientation、Shoulder Orientation、Head Orientation、Gaze Direction、Distance与Movement Permission。
- `A-SKETCH / Action Sketch`：动作起点、路径、接触 / 近接触点、受力方向、终点与Next-action Carryover。

允许一张综合草图承担S+P或S+P+A；不得机械拆成多张。选择最小充分草图类型后，必须读取`references/ref_sketch_master.md`：`REF-SKETCH-MASTER`拥有`Sketch Presentation Authority`，只负责技术图表达语言、信息组织与简化程度；Current Clip的Spatial Snapshot、Blocking Signature、Pose / Topology、Camera / Axis与Action Path继续拥有草图内容。内部固定原则为`Master Template carries sketch language; Current Clip data carries blocking content.`

生成分支固定为`TECHNICAL_VISUAL_BLOCKING_SKETCH → templates/23_visual_blocking_sketch_prompt.md`。不得路由到`workflows/10_storyboard_workflow.md`或`templates/09_storyboard_prompt.md`，也不得复用Storyboard的“单镜头视觉预演 / 叙事构图”默认生图指令。

若母版注册记录为`REGISTERED`且真实相对路径可读，必须按`templates/23_visual_blocking_sketch_prompt.md`把解析后的绝对路径传入图像工具的真实视觉参考参数；只在文字中写“参考母版”不算加载。若记录为`UNAVAILABLE`、`NOT REGISTERED`、文件不可读或工具不支持图像参考，只允许明确使用`Text Contract Fallback`并记录失败来源，不得声称已经看见、加载或引用母版图片，也不得伪造路径。母版是否可用不改变Assessment，不得因存在母版而把`NONE`升级为`REQUIRED`。

草图是导演技术调度锚点，不是正式美术资产，也不是电影感铅笔插画。生成核心必须写成`Technical Director Blocking Sheet / Spatial Blocking Diagram`，不得以铅笔感、电影感、青春感、岩井俊二、阴雨氛围、唯美、高燃或其他最终画风词驱动。默认信息组织按母版合同自适应包含：最大区域的Main Blocking Diagram；证明Topology / Shared Facing / Axis / Camera Safe Side的Spatial / Top-down Diagram；最小Camera Information；按风险选择的Blocking / Movement Permission；Usage / Reference Authority。人物绘制层必须服从`references/ref_sketch_master.md`的`Neutral Mannequin Representation Rule`：S / P / A / Combined统一使用无性别技术调度人偶，只靠角色名 / ID、技术颜色与位置标签区分；不得从Character Asset重画脸、发型、服装、年龄感、体型或身份。三人围桌、追逐、武打、车辆内等场景允许重新布局，不要求像素级复刻。

Formal Keyframe只在确需锁定最终视觉身份、光影、材质、构图或画面状态时另行使用；它不是默认草图替代物，也不能因Blocking风险自动创建。

### Sketch Validation Gate And Reference Authority

生成或接收草图后，注册Confirmed前先执行Layout Validation Gate。实际视觉检查必须确认：1）Main Blocking Panel；2）Character / role labels；3）Direction / gaze / movement annotation；4）Spatial / Top-down Diagram（S/P高风险默认必须，A-SKETCH至少有可验证的Spatial / Action Path Diagram）；5）Camera Information；6）Blocking / Movement notes or permission；7）Usage / Authority note。候选若退化成单幅电影场景、单幅铅笔叙事插画或只有完整人物 / 环境而无上述技术分区，即使大致站位正确，也固定判`FAIL = Artistic Storyboard Drift`。

随后继续核对：role mapping；left / right / front / back；Position；Torso / Body Facing；Relationship Topology；Same-seat / prop / environment-anchor relation；Gaze / Head Delta；Interaction / Eyeline Axis；Camera side与意外跨轴；Movement Path（适用时）；是否提前出现未来动作；是否与Active Character / Environment / Prop资产、Scene Spatial Snapshot、Shot-State Memory、Accepted Canon State或canonical blocking发生Authority冲突；并执行`references/ref_sketch_master.md`定义的`Template Content Leakage Check`，确认没有无依据继承母版示例的人物数量、人物外观、钢琴、琴凳、窗户、乐谱、雨景、文字、色彩 / 灯光或其他剧情内容。

再独立执行`Character Appearance Leakage Check`：确认所有人物均为无真实五官、无发型、无具体服装、无明显性别化胸腰臀 / 体态、无年龄 / 美貌 / 气质身份表达的中性技术人偶；角色只由名称 / ID、技术颜色与位置标签识别；没有依据Character Asset重画人物外观。A-SKETCH因物理可达性确需比例时也只能保留最小必要比例，不恢复角色视觉身份。任一人物不通过即固定判`FAIL = Character Appearance Leakage / Identity Contamination`，状态为`FAILED / REVISE`，不得注册Confirmed。

视觉检查结果必须按`templates/23_visual_blocking_sketch_prompt.md`写Candidate Evidence Record，并实际运行`scripts/validate_sd_film.py sketch`。命令PASS只是注册的必要条件，不替代视觉检查；任何版式项、Blocking Match、泄漏检查或图片可读性失败都不得登记Confirmed。

任一项不通过，草图状态为`FAILED / REVISE`，不得进入当前Clip的Confirmed Visual Anchor。`Artistic Storyboard Drift`必须回到同一Technical Visual Blocking Sketch route按专用模板重做，不得转入Storyboard。若草图与已确认Spatial Snapshot或canonical blocking冲突，修正 / 重做草图；不得反向修改正式空间事实来迁就草图。

Confirmed条目至少解释：

```text
REF-SKETCH-04｜CLIP-04空间与姿态调度草图
用途：只控制人物位置、身体朝向、共同座椅 / 空间关系、人物距离、视线、轴线、摄影机位置与适用动作路径。
Authority：草图人物为无性别调度人偶，仅用于空间 / 姿态 / 机位关系，不作为人物外观参考；人物外观服从正式Character Asset。草图也不控制环境 / 道具造型、材质、色彩、灯光与最终画风。
```

Character Asset继续拥有gender / identity / face / hair / costume / age impression / body identity与其他人物视觉身份；Environment Asset拥有scene identity / spatial structure / material baseline；Prop Asset拥有prop identity / canonical state；`REF-SKETCH-MASTER`只拥有Sketch Presentation Authority；草图人偶只是blocking proxy且不拥有Character Identity Authority；当前Clip的Confirmed `REF-SKETCH-XX`只拥有Clip Blocking Authority，即Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path；REF-TAIL只拥有上一Accepted transient end state与连续性；Formal Keyframe只在明确需要时拥有最终视觉构图 / 光线 / 状态锁。母版与当前草图都不得覆盖前三类Canonical Authority。

### Sketch Persistence / Blocking Canon

同一Clip针对当前稳定Blocking State的Confirmed `REF-SKETCH`默认只生成一次并持续有效。普通Prompt优化、压缩、措辞重写、主风格优化、反向提示词整理、台词 / 音效调整或Template重映射，只要Blocking Signature没有实质变化，必须复用原草图，不得再次生成。

Visual Anchor State / Blocking Signature保存在Clip Plan现有`Spatial State / Continuity Risks / Reference Budget`或当前STATE-08 Checkpoint中，按需包含：Characters、Topology、Position、Shared Facing、Seat / Spatial Relation、Allowed Delta、Camera Logic、Axis、Movement Path、Clip Start / End Blocking、Anchor ID / Revision与`NONE / POSSIBLE / REQUIRED / CONFIRMED / RETIRED`状态。每次Prompt Rewrite前只比较`Current Revision vs Blocking Signature`。

只有Blocking-affecting Revision才触发Visual Blocking Anchor Reassessment，包括但不限于：并排变面对面 / 背对背；左右 / 前后交换；共同坐变一人起身 / 离开；仅侧眼变明显转身 / 靠近；双人同框与正反打互换；轴线侧重大改变或环绕；增删角色；新增复杂道具交互；Movement Path显著变化；Shot合并 / 拆分改变空间状态；Clip起点 / 终点Blocking大幅变化；机位 / 构图重构到足以改变Topology读取。

Reassessment只能得到：`KEEP existing sketch`、`REPLACE with REF-SKETCH-XX-v2`、`RETIRE sketch`或`CREATE new sketch`。轻微机位、措辞或风格变化不构成自动替换依据。REPLACE / CREATE必须重新通过Sketch Validation；RETIRE后从当前Clip实际投喂清单移除并更新预算，但保留Revision追溯，不假装旧图从未存在。

### Prompt Pollution Boundary

Confirmed Visual Anchor进入`参考资产`时只写ID、用途、Authority、必要状态与一句：`草图人物为无性别调度人偶，仅用于空间 / 姿态 / 机位关系，不作为人物外观参考。`不复制草图全部标注，也不把中性人偶规则展开成负面词清单。Prompt正文继续执行`Source Carries State, Prompt Carries Delta`：只保留当前Clip Delta与仍需贴近局部动作 / 空间才能消歧的最小高风险约束；不得在人物一致性、环境一致性、首帧、每个分镜和反向段反复重述同一Blocking。反向提示词继续在末尾唯一收束，除非现有规则允许的最小局部连续性约束确需留在对应字段。

Scene Top-down Blocking Map、Storyboard、多格分镜板与设计表截图继续禁止进入STATE-08；经本Gate生成、验证、确认且绑定单一Clip / Blocking Signature的Visual Blocking Sketch是严格受限的执行参考例外，不是Canonical Asset或Storyboard。

`REF-SKETCH-MASTER`不属于当前Clip视频输入，不写入最终`参考资产：`、不计入视频模型图片预算。它只在当前执行环境明确支持且真实文件已注册时服务草图生成；真正进入视频参考资产的是验证通过并绑定当前Blocking Signature的`REF-SKETCH-XX`。

## A. Temporal / Spatial Continuity Classification

逐Clip成对比较`Previous Clip End State → Current Clip Start Requirement`，只允许选一个主分类：

### 1. 视觉连续 / Visual Continuity

同一连续时间、空间与动作链，当前Clip首帧需要继承上一Clip可见人物、环境、道具、动作阶段或镜头几何。

- A【同镜头连续承接 / Direct Start-Frame Handoff】：上一Clip最后一个镜头在当前Clip继续、目标接近一镜到底时使用。标记`Tail Frame Required = YES`；【参考资产】中的`REF-TAIL`必须写“同镜头连续承接用途”；【首帧参考】使用固定直接承接句，并锁定姿态、位置、朝向、距离、动作阶段、构图、景别、机位、环境、光线、天气、道具、情绪与持续声音。
- B【新镜头参考型 / Reference-Only Handoff】：当前Clip另起新镜头重新构图，但仍需上一尾帧锁定站位、朝向、人物距离、景别衔接、空间关系、道具状态或起始构图时使用。也标记`Tail Frame Required = YES`；【参考资产】中的`REF-TAIL`必须写“空间/站位/景别参考用途”；【首帧参考】说明保持项与新机位/景别/视角/构图，明确“另起新镜头重新构图”，禁止使用Direct固定承接句。
- A/B的实际尾帧存在、可访问且已确认可用时，记录真实引用；尚未提供时仍在【参考资产】列出统一`REF-TAIL`名称、对应的A/B用途和“待用户提供/待上传、未确认”，并提示用户从上一Clip最终成片截取最终有效尾帧后添加。不得把待补充声明写成已提交资产。
- 当前首帧不得重播已完成动作、无过程换位、换向、换手或换世界。

### 2. 剧情连续 / Narrative Continuity Only

剧情因果继续，但当前Clip不是上一尾帧的画面延续，例如主动回到同一故事线的另一时空、另一个地点或独立建立镜头。

- 若当前镜头不依赖上一尾帧画面状态，归入C【新镜头且无需尾帧 / Not Required】：上一尾帧不作为当前Clip正式生成参考资产。
- 只核对仍有效的人物身份、服装、道具后果、情绪或主题锚点。
- 当前首帧从已确认Scene初始状态、当前世界资产与当前Shot Start Boundary独立重建。
- 若实际需要上一尾帧锁定站位、朝向、距离、景别、空间关系、道具状态或起始构图，必须使用B【新镜头参考型】，不得一边声称无需尾帧、一边机械引用尾帧。
- 当前Clip不要求严格视觉承接时标记`Tail Frame Required = NO`，不得要求用户截图；可仅以文字状态核对或建立新的首帧。

### 3. 主动切场 / 切世界 / Motivated Scene-or-World Change

已确认地点跳跃、时间跳跃、现实↔幻想、现实↔耳中玉境、尺度层变化、闪回、蒙太奇或其他叙事断点。

- 上一尾帧不得作为当前Clip正式生成输入；只作必要的身份与视觉连续性核对。
- 当前首帧必须写明新时空层、重建依据与首个稳定构图。
- 如果世界切换发生在当前Clip内部，必须继续执行Transition Check，并允许转场前后分别使用各自世界状态资产；若切换已在上一Clip结束，则当前Clip只使用切换后的世界资产。

无法唯一分类时结果为`FAIL / Unresolved Handoff`，返回STATE-07与相邻Clip成对修正；不得默认选视觉连续或默认塞入上一尾帧。

## B. World-State Check

每个分镜必须明确一个当前世界状态；同一分镜包含转换时，分别明确Pre-Transition与Post-Transition状态：

- World-State ID / 名称：现实世界、幻想世界、耳中玉境或项目已确认的其他层。
- 场景、时间、尺度层与空间入口/出口。
- 本分镜实际出场角色及数量。
- 本分镜实际存在的环境、道具、FX及其当前形态。
- 相邻分镜如何继承、转换或重建World-State。

资产候选资格为以下条件的交集：

`真实存在且Confirmed / Active ∩ 当前Clip实际使用 ∩ 当前分镜世界状态适用 ∩ 当前阶段实际存在`

硬规则：

- 完全位于耳中玉境的Clip不得引用现实标准耳勺；只允许引用耳中玉境环境与当前阶段已经完成转换的武器化耳勺。
- 正在执行现实→耳中玉境转换的Clip可同时引用现实标准耳勺与武器化耳勺，但必须分别绑定转换前、转换后阶段，并在Prop State与Transition五要素中写清转换过程；不得把两种形态当作同时存在的两个道具。
- 未出场角色、未使用环境/道具、上一世界已结束且未在本Clip出现的资产直接删除，不能因为“上一Clip用过”继续占参考位。
- 世界状态无法判断、资产跨层冲突或状态转换没有过程时，Preflight失败。

## C. Reference Asset Check

World-State通过后才执行候选筛选与`knowledge/reference_budget.md`：

1. 先逐项执行Visual Input Eligibility Test：`这是不是一张实际会被投喂/引用的视觉资产？`。允许通过的视觉类型为：已确认角色图、环境图、道具图、正式FX图、参考板、合法首尾帧、经本Gate确认的单Clip Visual Blocking Sketch，以及其他当前Clip确实需要用户实际投喂的视觉参考图。真实资产必须有可回查文件/受控ID与用途；待补图必须写明具体图像对象、实际投喂用途与`待用户补充/待上传、未确认`，不得伪造路径或确认状态。
2. 纯文字规则一律判定为`NOT ELIGIBLE`并从视觉候选中移除。站位/不可换边/人物距离/同坐一张板凳/道具数量/空间关系进入`空间关系`、Spatial Blocking Rules或适用的`起始状态`；持有、数量、同一张板凳等道具事实进入`道具状态`；首尾边界分别进入`首帧参考`、`尾帧限制`；禁止项进入`反向提示词`；动作与镜头规则进入对应分镜现有字段。迁移只改变归类，不改变约束本身。
3. 如果对象本身存在正式视觉资产，按真实ID引用，例如`PROP-BENCH-01｜双人钢琴凳`；`板凳参考说明｜用途：锁定两人共坐同一张板凳`不得进入清单。若缺的是应成为Canonical的正式CHAR / ENV / PROP / FX资产，返回STATE-03完成双确认，不得用待补占位绕过Asset System。
4. 读取STATE-07的`Clip End-State Record / Next-Clip Carryover`、当前Clip目标、Visual Anchor State与`Continuity Risks`，对已经Eligible的候选执行Reference Selection / Routing。身份/外观风险选择当前Active Character Canonical References；空间结构风险选择Active Environment Canonical References并继续消费Confirmed Spatial Blocking文字语义；道具造型风险选择Active Prop Canonical References；Visual Blocking Final Assessment为REQUIRED时选择对应Confirmed `REF-SKETCH`并只赋予Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path Authority；A/B状态锚定选择对应`REF-TAIL`，C不选择旧尾帧；光线/天气/场景状态漂移只有在存在真实、已确认且合格的场景视觉基准或合法参考帧时才选图，否则写入现有文字字段。不得因“Eligible、Registry里存在、上一Clip用过或预算有空位”机械全选。
5. 每个入选条目记录`解决的具体风险 / 生成目标 → 资产角色 → 用途`；对Eligible但未选条目记录不选理由。当前Clip每个出场核心角色都视为具有持续身份/外观风险，仍按既有硬门槛保留各自独立三视图/角色锁定图；Reference Routing不得削弱该规则。
6. 删除未出场角色、未使用环境、未使用道具、未使用动作图、当前World-State不适用以及不能解决当前风险的资产。参考资产按需路由，不是越多越好。
7. 去重后，读取同一连续性判定中的A/B/C与`Tail Frame Required`。A/B无论尾帧当前是否已上传都预留1个Projected连续性图片位，并在【参考资产】直接列出`REF-TAIL-XX｜CLIP-XX尾帧参考`、A类“同镜头连续承接用途”或B类“空间/站位/景别参考用途”及真实状态；未提供时标明“待用户提供/待上传、未确认”，不计入已提交图片数，不伪造路径。C不得加入或预留旧尾帧图片位，可由Canonical资产、Spatial Blocking和文字状态承接或重建。
8. 按既有Reference Budget阈值计算Projected Final Count，最终必须`≤9`。
9. 只有信息过多、接近或超过参考位上限时，才整合环境多视角、道具组、空间/动作/使用关系等非角色信息；不得默认整合核心角色。
10. 不存在、未确认或不能完整覆盖零散信息的“总图”不得虚构进入清单。入选资产缺少风险依据、必需资产漏选、用途选错或无理由过量引用时，Reference Asset Check为FAIL。

既有Voice/Audio Reference继续按声音资产合同作为独立非视觉输入检查；本视觉资格测试不删除该支路，但普通文字音色说明不得冒充Voice/Audio Reference。

## D. Transition Check

出现以下任一情况时强制触发：现实→幻想、幻想→现实、现实↔耳中玉境、地点跳跃、时间跳跃、尺度变化、角色形态转换、道具形态转换。

正式Prompt编译前必须锁定转场五要素：

1. **起点状态**：转换发生前的世界、人物、环境、摄影机、道具/形态与动作阶段。
2. **转换媒介**：真实遮挡、光幕、雾、水、反射、门体、空间裂隙、已确认FX或项目世界规则；不得无依据新增媒介。
3. **运动方向 / 过程**：谁或什么从哪里向哪里移动，摄影机如何观察，世界/尺度/形态如何连续变化，哪些状态保持不变。
4. **终点状态**：转换完成后的世界、人物、环境、道具/形态与动作结果。
5. **转场后的首个稳定构图**：人物位置、前中后景、朝向、摄影机位置/轴线侧、环境锚点、道具状态和可冻结的稳定画面。

五项缺一即失败。除非用户明确要求，禁止把过程退化成“金光一闪”“突然切换”“画面一白后已在新世界”。五要素是内部执行合同，STATE-08分别投影到现有`首帧参考`、`起始状态`、`画面描述`、`空间关系`、`道具状态`与`镜头结尾状态`，不新增“转场”字段。

## E. Character Count Lock

每个分镜先建立实际可见角色清单与精确数量，再写动作：

- 逐角色写`角色身份 × 精确数量`，并核对背景、倒影、阴影、画中画、分身与相似替身是否会造成额外计数。
- 剧情规定唯一角色时，正向字段必须明确“画面中始终只有唯一一只 / 一名X，前景、中景、背景均无第二个同类主体”。
- 同时在`反向提示词`禁止复制、分身、镜像重复、倒影误生成实体、背景第二只、相似替身或群体增殖。
- 数量限制不得只藏在反向提示词；适用分镜的`画面描述`或`空间关系`中必须有正向唯一性证据。`人物一致性`只承担长期身份，不重复逐镜数量。
- 场面允许群众时也要写可见数量范围与主次，不得让模型自行补全无剧情依据的角色。

## F. Spatial Composition Lock

追逐、战斗、对峙、对话与多人镜头必须明确：

- 谁在画面前 / 后、左 / 右及前 / 中 / 后景。
- 每个主体面向、视线目标、运动方向与关系轴。
- 摄影机位于轴线哪一侧，谁可正脸、三分之二侧面、侧背或背身。
- 是否允许同一景深；若不允许，写明前后景或距离分离。
- 可追踪的追逐 / 攻击 / 视线来源→路径→目标。

追逐默认合同：

- **后追前逃**：逃者位于前方更深景别并朝远离摄影机或沿明确屏幕方向逃跑；追者位于后方较近景别沿同一路线追击。
- 默认禁止双方并排、同一景深横向站立、同时完整正脸面向摄影机、海报式合影、群像站桩或追逃关系反转。
- 只有用户或已确认Shot Design明确要求其他构图时才可例外，并必须重新锁定关系轴与可读追逃方向。

## G. Performance / Emotion Check

逐Clip、逐角色读取STATE-06已有Performance Goal、Performance Arc Map、相邻Shot Handoff与八组`Clip End-State Record / Next-Clip Carryover`中的Performance State，检查：

1. **Inherited Baseline**：当前首个可见状态是否来自上一镜Settled State、Scene初始事实或有依据的Motivated Discontinuity；不得在Clip或Shot边界自动恢复默认脸。
2. **Trigger And Attention**：情绪、关系或认知变化是否有已确认刺激，人物是否通过视线目标、注意转移或动作停止/继续实际接收到它。
3. **Action-phase Evidence**：动作、台词或信息接收是否在`Pre-action / In-action / Post-action`中拥有当前Clip可见的最小充分阶段，尤其保留动作/台词后的确认、延迟反应、控制/泄漏或余韵。不是每个SHOT都要完整三阶段，但Clip不能只剩“固定表情完成动作”。
4. **Executable Carriers**：每个需要变化的角色至少有一项主要视线/局部面部变化和一项适用的呼吸、手部、肩颈、重心、距离或反应停顿；如果采用`Intentional Hold / 主动保持`，必须写注意目标、压制对象、延迟或低幅身体证据。只写“紧张 / 从容 / 平静 / 愤怒 / 悲伤 / 面无表情”固定FAIL。
5. **Cross-shot Arc**：`Previous Settled State = Current Inherited Baseline`；升级、回落、反转、恢复和重新控制都有触发，Post-action Residue、Arc Endpoint与Next-shot / Next-Clip Carryover可复算。
6. **Relative Performance Hierarchy**：两人以上时明确Primary Performer、Secondary Reactor / Listener / Background Holder、反应顺序、相对`Restrained / Open / Heightened`幅度与视觉重点交接。除非剧情授权，不得所有角色同一时点同强度表演，也不得全员同脸冻结。
7. **Capacity And Readability**：关键微表情、眼神、停顿和余韵在时长、景别、遮挡、对白口型、动作/FX与Camera路径下可读；表演密度超限时按PL1 / PL2 / PL3稳定降级，不删刺激、行动选择和Arc Endpoint。

### Dialogue / Action Capacity Ledger

对含对白、关键接触、产品/道具展示、进食或明确反应链的Clip，在进入Prompt编译前按已确认Shot / Clip时长建立内部容量账本：

- 分别核对实际发声、换气、触发后的理解/反应延迟、走位或接触过程、产品/关键道具可读展示、结尾稳定窗口；不得用单一固定语速替代语言、情绪、动作和景别的实际负荷。
- 对白必须绑定合法说话者与口型窗口；说话、吞咽、遮脸、快速转头、大幅运动或复杂接触发生冲突时，先拆开其顺序或降低其中一个负荷。
- 任何关键动作都必须具有起点、接触/变化过程和结束状态；商业产品或关键道具只在存在足够可见时长时承担识别、状态变化或叙事证明。
- 容量不足时，优先删除重复信息、让可见动作承担文字信息、缩短非关键台词、降低Camera / FX负荷；仍不成立则返回STATE-07拆Clip或STATE-06调整Shot。不得压缩反应、物理接触、吞咽、口型或稳定收尾来伪造通过。

账本只影响现有`连续动作 / 人物动作 / 道具状态 / 音效 / 结尾状态`等语义和Return Route；不得向最终Prompt增加时间码、逐秒区间、固定语速或新的字段。

本Check不授权改剧情、补刺激、增加台词或新增镜头。若STATE-06已经具有完整弧而只是在最终文字投影中缺证据，STATE-08只修现有字段映射；若Performance Goal / Arc本身缺失、镜头容量或可读性不成立，返回STATE-06修Affected SHOT与相邻Handoff；若Clip合并让反应次序、弧线或容量不可执行，返回STATE-07调整Clip组织。通过语义只进入现有`人物动作 / 连续动作 / Performance State / Next-Clip Carryover / 人物动作与情绪 / 镜头结尾状态`，不得新增Template字段。

## H. Prop State Check

每个关键道具逐分镜检查：

- Prop ID / 名称与当前世界状态。
- 当前形态、尺寸和材质状态。
- 持有者、左右手、位置、方向与接触关系。
- 是否允许悬浮；未获授权时必须由人物直接持握或依物理支撑。
- 从上一状态到当前状态的可见变化过程。
- 形态转换是否已经完成；完成前后分别使用哪个Canonical State资产。
- 镜头结尾状态及下一镜继承。

现实标准耳勺与武器化耳勺属于同一道具的不同世界/形态状态：现实阶段只用现实形态；耳中玉境且转换完成后只用武器化形态；转换分镜可按阶段引用两者但必须有Transition五要素。不得同场混用、无过程瞬变、复制成两件道具或让道具无授权悬浮。

## Preflight Result And Failure Handling

每个Clip的检查结果只能为：

- `PASS`：八项检查全部适用项通过，允许确认STATE-07 Clip Plan或进入STATE-08 Template Mapping。
- `FAIL / Return Route`：列出Affected Clip / Shot、失败项、冲突事实与最小修正路由。先修正Clip设计或返回事实拥有者，再从A开始重跑全部Preflight；不得边失败边生成最终Prompt。

STATE-08不得把内部Preflight标题或检查表变成最终字段。通过后的语义必须映射到`templates/10_video_prompt.md`既有字段。

## Acceptance Scenarios（十三个Acceptance Scenarios）

| 场景 | 必须得到的结果 |
|---|---|
| A. Clip B尾帧在耳界；Clip C主动切回现实 | 分类为`主动切场 / 切世界`；B尾帧不进入C的正式参考资产，C从现实场景资产与现实首个稳定构图重建 |
| B. Clip D完全在耳中玉境 | World-State只允许耳中玉境资产；删除现实标准耳勺，保留已经完成转换的武器化耳勺 |
| C. 剧情规定小鬼唯一1只 | 正向字段明确“始终只有唯一一只小鬼”，前/中/背景无第二只；反向提示词禁止复制、分身、镜像重复、背景第二只和相似替身 |
| D. 吴御史追逐小鬼 | 默认后追前逃；小鬼在前方更深景别逃跑，吴御史在后方追击；禁止双方并排正对镜头与海报式合影 |
| E. 现实→耳中玉境 | 正式Prompt前必须完整定义起点状态、转换媒介、运动方向/过程、终点状态与转场后首个稳定构图；缺一即FAIL |
| F. A同镜头连续承接但无实际尾帧图 | `Tail Frame Required = YES`；`参考资产`直接列`REF-TAIL`、同镜头连续承接用途与“待用户提供/待上传、未确认”；`首帧参考`使用Direct固定句并完整锁定；Prompt可交付，实际提交生成前补图 |
| G. B新镜头参考型但无实际尾帧图 | `Tail Frame Required = YES`；`参考资产`直接列`REF-TAIL`、空间/站位/景别参考用途与“待用户提供/待上传、未确认”；`首帧参考`说明另起新镜头重新构图且不使用Direct固定句 |
| H. C新镜头且无需尾帧 | `Tail Frame Required = NO`；不列`REF-TAIL`、不要求截图；依靠Canonical基础资产、Confirmed Spatial Blocking、文字空间规则与当前Scene / World-State / Start Boundary建立新首帧 |
| I. `板凳参考说明｜用途：锁定两人共坐同一张板凳……`混入参考资产 | Visual Input Eligibility为`NOT ELIGIBLE`；从【参考资产】删除并迁移到`空间关系`或`道具状态`。原清单1—5号真实视觉资产保持不动；若确有双人钢琴凳参考图，则改用真实`PROP-BENCH-01｜双人钢琴凳`及其文件/受控ID |
| J. 简单单人原地转头，剧情要求警觉确认 | Visual Blocking Final Assessment=`NONE`且不生成草图；Performance / Emotion Check仍要求“眼睛先定向 → 短暂停顿/屏息 → 头部跟随 → 视线稳定并留下警觉余韵”等最小可执行链。若只写“紧张地转头 / 保持平静表情”，固定FAIL并返回STATE-06补足Affected SHOT，不新增镜头 |
| K. CLIP-04：林夏左 / 许栀右，共坐同一长琴凳并共同朝向钢琴 / 窗外；许栀只允许Gaze + LIMITED Head，其他上层姿态与距离锁定 | 首次单Clip Prompt前判为HIGH / REQUIRED，先生成并验证S+P综合草图；两人使用同一套无性别技术人偶，只由蓝 / 红角色标签、姓名与左右位置区分，不用长短发、裙装或身体曲线区分；注册`REF-SKETCH-04`并加入参考资产，本轮不输出Prompt；Side-by-side漂成Face-to-face即使左右未换仍判Blocking Drift；后续普通Prompt重写复用原图；若重构为许栀起身走到林夏面前，触发Reassessment并REPLACE或RETIRE / CREATE |
| L. A3武打 / 复杂动作 | 可判ACTION HIGH / REQUIRED，使用中性技术人偶的A-SKETCH或S+P+A综合草图锁定起点、路径、接触 / 受力、终点与Next-action Carryover；必要身体比例只表达物理约束，不恢复性别、脸、发型、服装或角色体型身份；草图不得覆盖角色 / 环境 / 道具身份 |
| M. 三人围桌且母版示例为两女 + 钢琴 | 继承Technical Director Blocking Sheet的信息层级并重排为三人Topology；三人使用同一套无性别人偶语言，只靠角色标签、技术颜色与位置区分；不得复制两女外观、钢琴、琴凳、窗户、乐谱、雨景或示例文字；Template Content Leakage或Character Appearance Leakage命中即FAILED / REVISE |

## Validator Invariants

- 本文件被STATE-07与STATE-08 Resource Gate显式引用。
- `templates/20_clip_plan.md`具有逐Clip Preflight记录与PASS / Return Route。
- `templates/10_video_prompt.md`不新增Preflight字段，只在既有字段内容合同中承载世界状态、数量、空间、转场与道具语义。
- `Performance / Emotion Check`被STATE-07、STATE-08与既有Template语义显式消费；它不创建新STATE或最终字段，并能拒绝静态情绪标签、无依据情绪重置与全员同强度表演。
- Reference Budget在Continuity Classification与World-State过滤之后执行。
- 十三个Acceptance Scenarios与Five Global High-Priority Rules可被静态检索；Sketch Validation同时包含`Character Appearance Leakage Check`与固定失败码。
