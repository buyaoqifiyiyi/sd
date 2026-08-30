# Clip Preflight Check / Clip生成前检查

## Module Contract

- Module Name：`Clip Preflight Check / Clip生成前检查`。
- Module Type：STATE-07与STATE-08共享的强制Quality / Continuity Knowledge Gate；不创建新主STATE，不拥有最终Prompt Schema。
- Trigger：每个候选Clip在STATE-07形成执行合同时执行前置版；每个Confirmed Clip在STATE-08正式Prompt编译与Template Mapping之前执行最终版。
- Not Triggered As：不得把它当成新的制作阶段、资产生成Workflow、转场特效生成器或STATE-08新增栏目。
- Required Inputs：上一Clip End State与尾帧用途、当前Clip Start Requirement、逐分镜世界状态、Confirmed Assets及其Active Version、角色数量事实、Spatial Blocking / Relational Screen Geometry、关键道具状态链、适用Transition事实与Confirmed Clip Production Plan。
- Input Owners：剧情与时空事实由Script / Scene拥有；资产身份与版本由Asset Registry拥有；镜头与Blocking由STATE-06拥有；Clip边界与组织由STATE-07拥有。
- Output Owner：STATE-07检查记录由`templates/20_clip_plan.md`拥有；STATE-08只把通过后的语义映射到`templates/10_video_prompt.md`现有字段，本模块不新增、删除或改名最终字段。
- Allowed Writes：STATE-07 Clip Plan中的Preflight记录、既有连续性/预算/风险栏目，以及STATE-08内部Projection / QA记录；不得把内部检查表原样输出为Seedance字段。
- Consumers：`workflows/10_clip_production_workflow.md`、`workflows/11_video_generation_workflow.md`与STATE-09 Review。
- Conflict Route：剧情/世界层事实冲突返回其事实拥有者；资产状态冲突返回STATE-03；Shot / Blocking /转场设计冲突返回STATE-06；Clip边界、参考预算或Clip执行合同冲突留在STATE-07；仅Prompt转译措辞错误留在STATE-08。

## Three Global High-Priority Rules

以下三条先于Reference Budget、Prompt润色与模型适配执行：

1. **视觉连续 ≠ 剧情连续，连续性意图 ≠ 资产已经存在。** 先分类，再检查上一Clip是否有实际可用的最终尾帧图、定格图或经确认截图。`视觉连续`且实际尾帧可用时强制正式引用；没有实际尾帧图时不得虚构资产，只以文字承接End State。`剧情连续`或`主动切场 / 切世界`不得机械引用。
2. **参考资产必须先通过当前世界状态检查。** 资产只有在当前分镜所在时空层实际存在、实际出场或正在执行合法状态转换时，才有资格进入候选清单。
3. **跨世界镜头必须先设计转场，再生成提示词。** 先锁定转场五要素，再写正式视频执行语句；不得用含糊的“金光一闪 / 突然切换”替代过程，除非用户明确要求这种省略。

## Execution Order

每个Clip固定按以下顺序执行，不得把Reference Budget提前到世界状态和连续性分类之前：

`Continuity Classification → World-State Check → Character Count Lock → Spatial Composition Lock → Prop State Check → Transition Check（适用时）→ Reference Asset Check / Budget → PASS或Return Route`

- STATE-07执行前置版：检查设计是否可生成，并把结果写入Clip Plan。任何失败先修Clip设计，禁止确认Clip Plan。
- STATE-08执行最终版：按实际资产、实际首尾帧和最终逐镜文案复核。任何失败不得Template Mapping、不得输出Prompt；先回到对应拥有者做最小必要修正。

## A. Temporal / Spatial Continuity Classification

逐Clip成对比较`Previous Clip End State → Current Clip Start Requirement`，只允许选一个主分类：

### 1. 视觉连续 / Visual Continuity

同一连续时间、空间与动作链，当前Clip首帧需要继承上一Clip可见人物、环境、道具、动作阶段或镜头几何。

- 必须检查上一Clip尾帧资产可用性。实际存在、可访问且已确认可用时，必须按`REF-TAIL-XX｜CLIP-XX尾帧参考`正式引用；不存在时不得虚构，只能以文字完整承接上一Clip End State并继续使用Canonical角色、环境与道具资产。
- 构图可直接起步时使用`Direct Start-Frame Handoff`。
- 已确认的新机位、景别、视角或构图仍依赖上一尾帧锁定人物/空间状态时使用`Reference-Only Handoff`。
- 当前首帧不得重播已完成动作、无过程换位、换向、换手或换世界。

### 2. 剧情连续 / Narrative Continuity Only

剧情因果继续，但当前Clip不是上一尾帧的画面延续，例如主动回到同一故事线的另一时空、另一个地点或独立建立镜头。

- 上一尾帧不作为当前Clip正式生成参考资产。
- 只核对仍有效的人物身份、服装、道具后果、情绪或主题锚点。
- 当前首帧从已确认Scene初始状态、当前世界资产与当前Shot Start Boundary独立重建。
- 若实际需要上一尾帧锁定画面几何，必须把分类改为`视觉连续`，不得一边声称剧情连续、一边机械引用尾帧。

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

1. 当前Clip每个出场核心角色优先保留各自独立三视图/角色锁定图。
2. 删除未出场角色、未使用环境、未使用道具、未使用动作图与当前World-State不适用的资产。
3. 去重后，仅在`视觉连续`的Direct / Reference-Only分类下核验上一Clip尾帧：实际存在、可访问且已确认时以`REF-TAIL-XX｜CLIP-XX尾帧参考`加入；不存在时只记录文字承接，不得创建名称占位、伪造路径或计入已提交图片位。`剧情连续`或`主动切场 / 切世界`不得预留该尾帧图片位。
4. 按既有Reference Budget阈值计算Projected Final Count，最终必须`≤9`。
5. 只有信息过多、接近或超过参考位上限时，才整合环境多视角、道具组、空间/动作/使用关系等非角色信息；不得默认整合核心角色。
6. 不存在、未确认或不能完整覆盖零散信息的“总图”不得虚构进入清单。

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
- 数量限制不得只藏在反向提示词；`人物一致性`、适用分镜的`画面描述`或`空间关系`中必须有正向唯一性证据。
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

## G. Prop State Check

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

- `PASS`：七项检查全部适用项通过，允许确认STATE-07 Clip Plan或进入STATE-08 Template Mapping。
- `FAIL / Return Route`：列出Affected Clip / Shot、失败项、冲突事实与最小修正路由。先修正Clip设计或返回事实拥有者，再从A开始重跑全部Preflight；不得边失败边生成最终Prompt。

STATE-08不得把内部Preflight标题或检查表变成最终字段。通过后的语义必须映射到`templates/10_video_prompt.md`既有字段。

## Acceptance Scenarios

| 场景 | 必须得到的结果 |
|---|---|
| A. Clip B尾帧在耳界；Clip C主动切回现实 | 分类为`主动切场 / 切世界`；B尾帧不进入C的正式参考资产，C从现实场景资产与现实首个稳定构图重建 |
| B. Clip D完全在耳中玉境 | World-State只允许耳中玉境资产；删除现实标准耳勺，保留已经完成转换的武器化耳勺 |
| C. 剧情规定小鬼唯一1只 | 正向字段明确“始终只有唯一一只小鬼”，前/中/背景无第二只；反向提示词禁止复制、分身、镜像重复、背景第二只和相似替身 |
| D. 吴御史追逐小鬼 | 默认后追前逃；小鬼在前方更深景别逃跑，吴御史在后方追击；禁止双方并排正对镜头与海报式合影 |
| E. 现实→耳中玉境 | 正式Prompt前必须完整定义起点状态、转换媒介、运动方向/过程、终点状态与转场后首个稳定构图；缺一即FAIL |
| F. 视觉连续但无实际尾帧图 | 保持Direct / Reference-Only连续性意图；`参考资产`不列虚构尾帧，`首帧参考`用文字承接上一Clip End State并依靠Canonical基础资产维持一致性 |

## Validator Invariants

- 本文件被STATE-07与STATE-08 Resource Gate显式引用。
- `templates/20_clip_plan.md`具有逐Clip Preflight记录与PASS / Return Route。
- `templates/10_video_prompt.md`不新增Preflight字段，只在既有字段内容合同中承载世界状态、数量、空间、转场与道具语义。
- Reference Budget在Continuity Classification与World-State过滤之后执行。
- 六个Acceptance Scenarios与Three Global High-Priority Rules可被静态检索。
