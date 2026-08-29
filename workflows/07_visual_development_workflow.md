# STATE-04 Visual Development

# 视觉开发阶段


## Purpose


Visual Development负责将剧本信息、已确认资产与用户视觉需求转换为统一的项目视觉方向。


主要任务：


- 确立整体视觉风格
- 建立空间氛围
- 确定光影方向
- 确定色彩体系
- 建立摄影语言
- 确定基础电影摄影参数
- 服务后续Scene Breakdown与Shot Design


本阶段负责：

建立项目统一Visual Direction。


本阶段不负责：

重新设计角色资产。

重新设计环境资产。

重新设计道具资产。

正式拆解场景。

正式设计镜头。

Clip Production Plan。

视频Prompt。


当用户明确请求电影海报、Key Art、One-sheet、先导/正式/角色海报或标题字时：

完成Visual Direction后，按条件调用`workflows/17_poster_design_workflow.md`。

海报输出由`templates/15_poster_design_package.md`拥有，并写入Active Project Root的`poster_design/`目录。

未请求海报时不得自动追加该流程。


---

# Workflow Position


当前阶段：

STATE-04 Visual Development


前置阶段：

STATE-03 Asset Development


下一阶段：

STATE-05 Scene Breakdown


对应下一Workflow：

08_scene_breakdown_workflow.md


---

# Entry Gate


执行前必须确认：


Script Analysis已经完成。


Asset Discovery已经完成。


核心Character Asset已经完成。


核心Environment Asset已经完成。


关键Prop Asset已经完成或已明确无需制作。


读取：

project_status.md

它表示按优先级选定的State Source；普通Chat本机Root不可读时使用Portable State。状态保存服从references/project_state_contract.md，记录State Status、Visual Direction Artifact、Checkpoint与Revision ID，并按环境同步或输出更新后的Portable State。

project_bible.md

asset_registry.md


如果核心资产尚未完成：

不得进入正式Visual Development。


返回：

STATE-03 Asset Development。


---

# Input


输入包括：


- Script Analysis结果
- Character Asset信息
- Environment Asset信息
- Prop Asset信息
- User Visual Requirements
- Visual Style References
- Project Bible
- Asset Registry


已有资产与已确认项目设定：

优先级高于临时视觉描述。


Visual Development：

只能建立统一视觉方向。


不得改变：

角色身份。

角色核心外观。

环境基础结构。

关键道具设定。

剧情事实。


---

# Processing Pipeline


Visual Analysis

↓

Style Reference Detection

↓

Visual Style Retrieval

↓

Style Translation

↓

Visual Direction Development

↓

Cinematic Parameter Definition

↓

Visual Consistency Check

↓

Output Visual Guide

↓

Update Project Status


---

# Step 1: Visual Analysis


分析剧本与项目资产中的视觉信息。


包括：


## Story Atmosphere


分析：

- 故事基调
- 情绪方向
- 时间环境
- 叙事节奏
- 世界观气质


---

## Environment Analysis


分析：

- 空间类型
- 场景规模
- 环境材质
- 时代背景
- 天气
- 时间
- 环境综合色彩
- 主要光源条件


环境分析必须：

基于已经确认的Environment Asset。


不得：

为了匹配某种风格重新改变场景身份。


---

## Character Visual Relationship


分析：

- 人物与空间关系
- 人物状态
- 人物视觉重点
- 人物与环境的综合色彩关系
- 人物服装与背景的视觉层级


不得：

重新设计Character Asset。


---

## Prop Visual Relationship


如果存在关键道具：

分析：

- 道具在环境中的视觉位置
- 材质关系
- 色彩关系
- 视觉强调程度


不得：

在Visual Development阶段重新设计Prop Asset。


---

# Step 2: Style Reference Detection


检测用户是否提供明确视觉参考。


检测内容：


- 导演名称
- 电影名称
- 摄影风格
- 类型电影风格
- 艺术风格描述
- 色彩参考
- 光影参考


例如：


用户输入：

“王家卫式城市雨夜”


“岩井俊二式青春氛围”


“诺兰式现实主义科幻”


“黑泽明式东方历史空间感”


进入：

Visual Style Retrieval。


如果不存在明确视觉参考：

继续普通Visual Development。


不得：

为了增加电影感自动指定某个导演风格。


---

# Step 3: Visual Style Retrieval


当用户存在明确视觉参考时：

调用：

knowledge/visual_styles/


优先读取：

knowledge/visual_styles/index.md


再读取：

对应视觉风格文件。


例如：

用户明确要求城市潮湿情绪型摄影参考：

读取对应Director Style。


用户明确要求多个视觉参考融合：

仅加载：

实际需要的Style文件。


禁止：

无理由读取全部导演风格文件。


---

# Style Knowledge Extraction


从Visual Style文件中提取：


- Style Position
- Core Visual Identity
- Cinematography
- Lens Choice
- Camera Movement
- Lighting
- Color System
- Composition
- Texture
- Environment Treatment
- Emotion
- Scene Application


这些内容属于：

视觉开发知识。


不是：

最终Video Prompt Schema。


---

# Step 4: Style Translation


视觉风格名称：

不能直接作为最终Visual Direction的核心内容。


必须转换为：

可执行影视制作语言。


---

## Camera Language


包括：

- 镜头焦段倾向
- 景别倾向
- 摄影方式
- 运镜方式
- 镜头速度
- 手持或稳定倾向
- 景深倾向


例如：

不要只写：

“王家卫风格。”


应转换为类似：

中长焦人物摄影。

浅景深。

低速跟随。

轻微手持呼吸感。

人物经常通过玻璃、门框、前景遮挡形成空间距离。


---

## Lighting Language


包括：

- 主光方向
- 光源类型
- 明暗关系
- 光比
- 色温关系
- 环境反射
- 氛围效果


例如：

城市夜景可以转换为：

低照度环境光。

局部暖色人工光。

湿润地面反射。

侧逆光强化雨丝。

人物面部保持自然低亮度曝光。


---

## Color Language


包括：

- 主色调
- 辅助色
- 色彩关系
- 饱和度
- 明度
- 冷暖关系
- 调色方向


色彩必须：

服务剧情。

服务环境。

服务人物。


不得：

为了模仿参考风格破坏资产本身的颜色识别。


---

## Composition Language


包括：

- 构图方式
- 空间关系
- 人物位置
- 视觉重点
- 留白方式
- 前景遮挡
- 人物与环境比例


---

## Texture Language


包括：

- 胶片或数字质感
- 颗粒
- 高光
- 阴影
- 空气感
- 雾
- 雨
- 灰尘
- 材质表现


Texture必须：

与项目环境和摄影逻辑一致。


---

## Emotional Language


包括：

- 情绪氛围
- 节奏
- 人物观看距离
- 表演尺度
- 观看体验


情绪语言：

必须转换为可观察的视觉倾向。


不得只写：

悲伤。

浪漫。

高级。

电影感。


---

# Step 5: Visual Direction Development


根据全部输入建立：

当前项目统一视觉方向。


---

## Overall Visual Concept


建立整体视觉概念。


包含：

- 视觉主题
- 情绪基调
- 风格方向
- 真实 / 动画属性
- 时代视觉感
- 项目整体观看体验


整体视觉概念必须：

简洁。

统一。

可以传递给后续Workflow。


---

## Cinematography Direction


建立摄影方向。


包含：

- 焦段倾向
- 景别倾向
- 摄影机稳定程度
- 镜头运动倾向
- 景深
- 人物摄影距离
- 环境摄影方式

焦段倾向必须按`knowledge/camera_language/lens_language/focal_length_and_perspective.md`建立为：

- 默认画幅基准或“全画幅等效倾向”
- 允许使用的焦段范围与摄影机距离倾向
- 人物脸部几何、边缘安全和背景尺度的稳定规则
- 景深/对焦原则，以及广角运动或长焦跟焦的复杂度上限
- 连续覆盖中允许的焦段变化与必须保持的透视锚点

不得把焦段写成画面质感、情绪或景别的替代词；具体焦段仍由STATE-06按镜头目的决定。


本阶段建立的是：

摄影原则。


不是：

具体SHOT。


禁止：

在STATE-04提前制作完整Shot List。


---

## Camera Language Direction


建立项目Camera Language使用原则。


例如：

人物孤独：

可以倾向远景、留白、遮挡。


人物确认：

可以倾向慢推、中近景、视线匹配。


紧张动作：

可以倾向跟拍、轻微手持。


这里只规定：

语言倾向。


具体使用：

由STATE-06 Detailed Shot Design决定。


---

## Lighting Direction


建立统一光影方向。


包含：

- 主光逻辑
- 环境光逻辑
- 人物受光逻辑
- 已确认实用光源及空间锚点
- 光线方向、软硬、强度与衰减
- 冷暖关系
- 光比
- 介质、材质与反射关系
- 天气对光线的影响
- 项目级稳定规则与允许变化范围


光影必须：

能够在主要Environment Asset中真实成立。


需要专业拆解或匹配附件光影参考时，读取：

knowledge/lighting/index.md


不得把浅景深、运镜、构图、调色、雾雨火等FX或抽象情绪词写成Lighting原子；具体镜头使用与变化仍由STATE-06决定。


---

## Color Direction


建立综合色彩方向。


包含：

- 主色
- 辅助色
- 强调色
- 饱和度
- 对比度
- 冷暖关系
- 调色倾向

需要建立专业色调或匹配附件参考时，读取`knowledge/color/index.md`，并补齐：

- 综合色彩来源：资产固有色、时间天气、环境/实用光源、FX与材质
- 主色、辅助色、强调色的画面占比、空间位置与叙事优先级
- 综合色相关系、人物/背景/强调色的饱和度层级
- 整体明度、黑位、高光、局部对比与关键表演/动作可读区
- 白平衡/综合色温与绿色—品红偏色倾向
- 肤色、眼白、白衣、灰墙、金属及关键资产颜色保护
- 综合色彩允许变化、稳定结束色态与跨镜连续性


如用户没有提供明确Hex色值：

不得无必要自行创造固定Hex Palette。


可以使用：

自然语言色彩锚点。

不得把冷暖、高低饱和、暗黑、霓虹、糖果或清透自然色当作固定情绪/题材公式；不得用Color新增光源或重写资产固有色。


---

## Environment Direction


建立环境视觉统一规则。


包含：

- 空间视觉重点
- 材质表现
- 空气状态
- 天气表现
- 环境层次
- 光线与材质关系


Environment Direction不得：

改变已经确认的Environment Asset身份。


---

## Texture Direction


建立画面质感。


可以包括：

- Film Grain
- Digital Clean Image
- Soft Highlight
- Controlled Bloom
- Natural Skin Texture
- Atmospheric Haze
- Rain Texture
- Surface Reflection


Texture：

必须服务项目。


不得简单堆叠：

cinematic masterpiece。

8K。

award winning。

ultra detailed。


---

## Emotional Direction


建立人物与镜头共同遵守的情绪原则。


包含：

- 人物状态
- 表演尺度
- 镜头观察距离
- 节奏
- 情绪释放方式
- 观看感受


例如：

“克制重逢”可以转换为：

表演以眼神、停顿和呼吸为主。

摄影机避免过快靠近。

情绪高潮之前保持人物身体距离。

高潮动作完成后保留短暂镜头停留。


---

## Performance Direction


按需读取：

knowledge/performance/


建立项目级表演语法：

- 默认表演强度
- 角色中性基线与个体化面部/身体习惯
- 情绪如何通过注意目标、眉眼/嘴角、呼吸、姿态、手部与动作停顿呈现
- 压抑、伪装、混合情绪和短暂泄漏的统一尺度
- 泪水、脸红、颤抖等条件性身体结果与连续性原则
- 对白场景的说话、倾听与反应尺度
- 双人及多人场景的视觉重点与反应顺序
- 必须避免的舞台化或夸张表演倾向

需要专业表情拆解时读取`knowledge/performance/facial_action_language.md`与`emotion_dynamics.md`；附件/情绪名称只通过`expression_patterns.md`归并，不能作为固定脸型公式。


这里只建立统一原则。


具体表演节拍由STATE-06确定，执行细节由STATE-08完成。


---

## Sound Direction


按需读取：

knowledge/sound_language/


建立项目级声音原则：

- 声音的现实主义或风格化程度
- 对白与环境声的优先关系
- 主要空间底噪与材质声倾向
- 配乐使用条件
- 静默的叙事功能
- 跨镜声音连接倾向


没有明确配乐需求时：

不得为了“电影感”自动增加音乐。


---

# Step 6: Cinematic Parameter Definition


根据项目需求：

决定是否需要明确基础摄影参数。


参数不是必填。


只有当：

用户明确要求。

视觉风格需要。

后续模型执行确有帮助。


时定义。


---

## Camera System


可以确定：

摄影机类型或总体成像倾向。


例如：

数字电影摄影。

35mm胶片模拟。


如果没有必要：

不得为了专业感随机添加设备名称。


---

## Lens Direction


可以定义：

主要焦段倾向。


例如：

35mm：

环境与人物关系。


50mm：

自然人物观察。


85mm：

情绪近景。


这里建立：

项目倾向。


不是：

给每个Shot直接分配焦段。


---

## Aperture And Depth


可以定义：

景深倾向。


例如：

浅景深。

中等景深。

深焦。


光圈数值：

仅在项目明确需要时指定。


---

## Frame Rate


默认按照项目需求。


如果用户明确：

24fps电影帧率。


则记录。


如果未明确：

不得把复杂Frame Rate设置作为必需项。


---

## Filter And Texture


可以定义：

柔光滤镜。

颗粒。

Bloom。

Highlight Roll-off。


不得：

无逻辑叠加多个滤镜和胶片模拟。


---

# Step 7: Visual Consistency Check


Visual Guide输出前：

检查统一性。


---

## Character Compatibility


视觉风格是否：

适配Character Asset。


不得：

导致角色核心识别特征消失。


---

## Environment Compatibility


视觉风格是否：

适配Environment Asset。


不得：

为了视觉风格把环境改成另一个地点或时代。


---

## Prop Compatibility


关键Prop：

是否仍保持正确材质和视觉识别。


---

## Lighting Consistency


光线体系：

是否与时间。

天气。

环境。


一致。


---

## Color Consistency


色彩体系：

是否能够跨主要场景保持统一。


---

## Camera Consistency


摄影语言：

是否形成统一原则。


不得：

一边要求克制固定摄影。

一边又无理由要求高频复杂炫技运镜。


---

## Style Conflict Check


如果用户要求多个视觉参考融合：

检查：

摄影是否冲突。

色彩是否冲突。

光影是否冲突。

情绪是否冲突。


如果冲突：

根据当前剧情目的：

建立一个统一Visual Direction。


不得：

机械保留所有参考风格特征。


---

# Style Combination


允许组合多个视觉来源。


例如：

东方武侠空间

+

都市情绪摄影

+

现代电影光影


组合规则：

必须融合视觉参数。


禁止：

直接输出多个导演名称。


错误：

“王家卫+黑泽明风格”


正确逻辑：

“35mm情绪摄影结合东方历史空间构图，低速镜头运动，自然环境光影，人物与空间形成孤独关系。”


最终使用的Visual Direction：

必须是一个统一体系。


---

# Unknown Style Processing


当用户提供未知视觉参考：


分析：

- 色彩
- 光影
- 构图
- 摄影方式
- 情绪
- 质感


根据用户已经提供的信息：

建立临时视觉方向。


不要：

虚构具体导演来源。


不要：

假装知道不存在的Style Library文件。


如果参考信息不足：

仅使用能够确认的视觉特征。


---

# Required Output Semantics And Template Handoff

正式Visual Direction必须写入Project Bible，并使用：

templates/01_project_bible_template.md

Template独占Project Bible字段、顺序与排版。以下内容只定义Workflow必须准备的语义，不构成另一套最终Schema。


Visual Development输出：

```text
Visual Concept:

Cinematography:

Camera Language:

Lighting:

Color:

Environment:

Texture:

Emotion:

Performance:

Sound:

Cinematic Parameters:

Continuity Notes:
```


以上结构属于：

STATE-04 Visual Guide。


不是：

STATE-05 Scene Breakdown。


不是：

STATE-06 Detailed Shot Design。


不是：

STATE-08 Clip-based Video Prompt / Video Generation Schema。


---

# Output Requirements


## Visual Concept


描述：

项目整体视觉概念。


用于统一：

美术。

摄影。

光影。

色彩。

情绪。


要求：

简洁。

稳定。

可传递到后续Workflow。


---

## Cinematography


记录：

项目统一摄影原则。


包括：

焦段倾向。

景别倾向。

摄影距离。

摄影稳定性。

景深倾向。

环境摄影方式。


禁止：

在这里进行逐镜头Shot Design。


---

## Camera Language


记录：

项目Camera Language倾向。


说明：

哪些类型的镜头语言：

适合当前项目。


以及：

哪些镜头运动应该避免。


具体镜头：

由STATE-06决定。


---

## Lighting


记录：

统一光影体系。


包括：

主要光源逻辑。

人物受光。

环境光。

光源空间锚点与方向。

软硬、强度、衰减与主体可读性。

冷暖关系。

光比。

介质、材质与反射关系。

天气与光线关系。

连续镜头允许的光态变化与禁止突变。


---

## Color


记录：

项目色彩方向。


包括：

主色倾向。

辅助色。

强调色。

冷暖关系。

饱和度。

对比度。

调色原则。


如果用户没有指定固定色值：

无需强制创建Hex Palette。


---

## Environment


记录：

环境视觉处理规则。


包括：

空间层次。

材质。

空气状态。

天气表现。

背景处理。

环境与人物关系。


不得：

改变Environment Asset本身。


---

## Texture


记录：

整体成像质感。


例如：

自然皮肤纹理。

轻微胶片颗粒。

柔和高光。

雨雾空气感。

湿润材质反射。


不得：

堆叠无实际意义的质量关键词。


---

## Emotion


记录：

项目人物表演与观看情绪原则。


包括：

表演尺度。

镜头观察距离。

节奏。

情绪释放方式。


必须尽量转化为：

可观察的表演和摄影行为。


---

## Performance


记录项目统一表演尺度、微表情倾向、对白表演原则和多人反应规则。


不得提前写逐镜完整表演动作。


---

## Sound


记录声音现实主义、对白优先级、空间底噪、配乐条件、静默与声音连接原则。


不得提前写逐镜最终声音Prompt。


---

## Cinematic Parameters


只记录：

当前项目已经确认且真正需要的技术参数。


可以包括：

Camera System。

Lens Direction。

Aperture / Depth。

Frame Rate。

Filter。

Film Emulation。


如果没有明确需要：

可以保持为：

```text
按当前Visual Direction执行，无额外固定摄影设备要求。
```


不得：

为了专业感随机堆叠摄影设备名称。


---

## Continuity Notes


记录：

后续Workflow必须继承的视觉规则。


包括：

角色视觉保护。

环境视觉保护。

综合色彩。

光线方向。

摄影倾向。

画面质感。

表演尺度。

声音连续原则。


用于：

STATE-05

STATE-06

STATE-07

STATE-08


保持视觉连续。


---

# Project Bible Update


Visual Development完成后：

把已经确认的Visual Direction写入：

project_bible.md


优先更新其中已有的：

```text
Visual Direction
Color System
Lighting Rules
Camera Language
Performance Direction
Sound Direction
Style Consistency Rules
```


只写入：

已经确认的信息。


不得：

为了填满Project Bible而制造未确认规则。


不得：

覆盖已经确认的Character Bible。

Environment Bible。

Prop Bible。


---

# Visual Direction Lock


STATE-04完成之后：

当前Visual Direction进入：

Confirmed状态。


后续：

STATE-05 Scene Breakdown

STATE-06 Detailed Shot Design

STATE-07 Clip Production

STATE-08 Clip-based Video Prompt / Video Generation


默认：

继承这套视觉方向。


不得：

每到一个阶段重新随机选择：

导演风格。

综合色彩。

光线体系。

摄影基调。


如果用户明确要求修改整体Visual Direction：

应：

返回STATE-04处理。


不得：

在STATE-08临时重新建立另一套视觉体系。


---

# Output Boundary


STATE-04允许输出：

- Visual Concept
- Cinematography
- Camera Language
- Lighting
- Color
- Environment
- Texture
- Emotion
- 必要的Cinematic Parameters
- Continuity Notes


STATE-04禁止输出：

- 新Character Asset
- 新Environment Asset
- 新Prop Asset
- Scene Shot List
- Shot Design
- Clip Production Plan
- Seedance Prompt
- Video Prompt


---

# Completion Check


进入STATE-05前：

必须确认：


□ Overall Visual Concept已经建立


□ Cinematography Direction已经建立


□ Camera Language Direction已经建立


□ Lighting Direction已经建立


□ Color Direction已经建立


□ Environment Direction已经建立


□ Texture Direction已经建立


□ Emotional Direction已经建立


□ Performance Direction已经建立或明确沿用项目默认自然表演原则


□ Sound Direction已经建立或明确当前项目无额外声音风格要求


□ 必要的Cinematic Parameters已经确认或明确无需固定


□ Visual Style与Character Asset兼容


□ Visual Style与Environment Asset兼容


□ Visual Style与Prop Asset兼容


□ 多视觉参考已经融合成统一Visual Direction


□ 没有直接用导演名称代替Visual Direction


□ 没有提前进行Shot Design


□ Visual Direction已经写入project_bible.md


---

# State Update


完成Visual Development后：

更新：

project_status.md

完成决定作出后，只按`references/project_state_contract.md`执行状态字段、Portable Required Field Writeback与同步；本Workflow不复制同步失败语义。


当前状态：

```text
STATE-04
Visual Development Complete
```


当前执行Workflow：

```text
07_visual_development_workflow
```


Completed Tasks增加：

```text
Visual Development
```


Next Action：

```text
08_scene_breakdown_workflow.md
```


下一状态：

```text
STATE-05
Scene Breakdown
```


---

# Forbidden Actions


禁止：

在STATE-04重新设计已经确认的Character Asset。


禁止：

重新设计已经确认的Environment Asset。


禁止：

重新设计已经确认的Prop Asset。


禁止：

为了匹配导演参考改变项目世界观。


禁止：

直接使用导演名称代替具体视觉规则。


禁止：

把多个导演名称简单堆叠。


禁止：

在本阶段逐镜头输出：

景别。

具体焦段。

镜头时间码。

逐镜头摄影机运动。


禁止：

提前生成Clip Production Plan或任何Storyboard视觉材料。


禁止：

提前生成Video Prompt。


禁止：

提前生成Seedance Prompt。


禁止：

Visual Style定义最终Seedance Schema。


---

# Revision Rule


如果用户只修改：

综合色彩。

光影。

摄影气质。

Texture。

表演尺度。


且：

不影响资产身份。


则：

在STATE-04局部更新Visual Direction。


如果用户要求：

改变人物外貌。

改变角色服装设计。

改变环境结构。

改变关键道具外观。


则：

问题属于Asset Development。


返回：

对应资产Workflow。


不得：

用Visual Development绕过Asset Workflow。


---

# Next Workflow


STATE-04完成后：

进入：

08_scene_breakdown_workflow.md


下一阶段：

STATE-05 Scene Breakdown。


Scene Breakdown负责：

把已经完成：

剧情分析。

资产体系。

Visual Direction。


转换为：

可执行的Scene结构。


Scene Breakdown必须：

继承STATE-04已经确认的：

视觉方向。

色彩原则。

光影原则。

摄影倾向。

环境质感。

人物表演尺度。


---

# Workflow Relationship


正确关系：

Script Analysis

↓

Asset Discovery

↓

Asset Development

↓

Visual Development

↓

Scene Breakdown

↓

Shot Design

↓

Clip Production Plan

↓

Video Generation

↓

Review


Visual Development位于：

Asset Development之后。


原因：

视觉方向必须建立在：

真实项目资产。


基础上。


Visual Development位于：

Scene Breakdown与Shot Design之前。


原因：

后续所有场景与镜头：

需要共享一套Visual Direction。


---

# Final Principle


Visual Development解决：

“这个项目整体应该怎样被看见？”


包括：

摄影。

光线。

色彩。

空间。

质感。

表演。

情绪。


它不解决：

“这一场具体拆成几个镜头？”


也不解决：

“每个镜头具体怎么运动？”


更不解决：

“Seedance最终Prompt采用哪些字段？”


正确职责：

STATE-04

建立统一Visual Direction。


STATE-05

建立Scene结构。


STATE-06

建立Confirmed Detailed Shot Design。


STATE-07

完成Clip Production并确认Clip级起始状态、连续动作、空间/道具连续性与结尾状态。


STATE-08

按Confirmed Clip一对一转换为AI视频执行Prompt。


最终Seedance Schema：

由对应Video Prompt Template负责。


Visual Development必须：

成为后续影视生产阶段共享的视觉基础。
