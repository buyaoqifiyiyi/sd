# Visual Styles Index

# SD Film 视觉风格知识库索引

## Purpose

本目录负责把导演、影片或视觉美学参考转换为可执行的影视生产语言，服务于：

- STATE-04 Visual Development：建立项目级 Visual Direction。
- STATE-06 Detailed Shot Design：把已确认 Visual Direction 落到具体镜头。
- STATE-08 Clip-based Video Prompt / Video Generation：把Clip级镜头风格信息转成 Seedance 可执行内容。

本目录属于 Knowledge Layer。

它不替代 Workflow，不改变 Pipeline，不覆盖已确认资产，也不定义 STATE-08 最终输出 Schema。

---

## Core Retrieval Principle

导演文件元数据与统一Schema服从：

`knowledge/visual_styles/director_metadata_contract.md`

STATE-04确认混合风格后，必须在Project Bible持久化Primary Style Logic、Secondary Borrowed Traits、Rejected Conflicts与最终主摄影/光线/剪辑体系。

导演名和影片名首先是：

```text
Knowledge Retrieval Labels
```

但单独出现时不是完整的：

```text
Final Production Language
```

任何“某导演风格”请求都必须转译为具体的：

- 叙事语气与情绪过程
- 构图与人物调度
- 摄影机稳定性、位置、方向和运动
- 焦段倾向与观看距离
- 光源、方向、光比和环境反射
- 主色关系、饱和度与对比度
- 美术、材质与空间边界
- 表演动作、停顿和情绪尺度
- 剪辑节奏、动作连接和时间处理
- 环境声、动作声、声音桥与音乐边界
- 天气、空气介质和物理连续性

禁止只把导演名、影片名或“电影感、高级感、大片感”写入最终提示词。

---

## Current Director Library

当前维护以下十个已存在文件：

| ID | Director | File | Primary Retrieval Axis |
|---|---|---|---|
| 01 | Wong Kar Wai / 王家卫 | `directors/01_wong_kar_wai.md` | 都市私人情绪、受阻空间、主观时间、人工光 |
| 02 | Iwai Shunji / 岩井俊二 | `directors/02_iwai_shunji.md` | 日常成长、自然光、季节、开放空间、私人记忆 |
| 03 | Denis Villeneuve / 丹尼斯·维伦纽瓦 | `directors/03_denis_villeneuve.md` | 未知、尺度、极简秩序、环境重量、克制感知 |
| 04 | Christopher Nolan / 克里斯托弗·诺兰 | `directors/04_christopher_nolan.md` | 因果、任务、时间压力、空间地理、物理后果 |
| 05 | Akira Kurosawa / 黑泽明 | `directors/05_akira_kurosawa.md` | 群像、阵型、自然力量、动作方向、道德选择 |
| 06 | Steven Spielberg / 史蒂文·斯皮尔伯格 | `directors/06_steven_spielberg.md` | 人物视线、奇观揭示、人文情感、连续调度、群体反应 |
| 07 | David Fincher / 大卫·芬奇 | `directors/07_david_fincher.md` | 心理控制、程序调查、制度空间、微小异常、精确摄影 |
| 08 | Stanley Kubrick / 斯坦利·库布里克 | `directors/08_stanley_kubrick.md` | 几何秩序、制度寓言、仪式重复、疏离、形式偏差 |
| 09 | Zhang Yimou / 张艺谋 | `directors/09_zhang_yimou.md` | 综合色彩、仪式阵列、材质身体、权力秩序、个体反抗 |
| 10 | Bong Joon-ho / 奉俊昊 | `directors/10_bong_joon_ho.md` | 阶层空间、家庭群像、类型转调、社会机制、环境因果 |

本次目录没有 `directors/index.md`；本文件是唯一导演风格导航入口。

未实际存在的导演文件不得写入索引或假装可调用。

---

## Fast Retrieval Map

根据用户目标选择最相关的一份文件，而不是默认加载全部导演：

| User Intent / Scene Need | Primary File | Why |
|---|---|---|
| 城市夜行、重逢、错过、暧昧、狭窄关系空间 | 王家卫 | 用遮挡、人工光、停顿和错身表现不可抵达 |
| 青春成长、日常记忆、季节、自然光、温柔离别 | 岩井俊二 | 用自然环境、生活动作和陪伴式摄影等待情绪出现 |
| 巨大空间、未知文明、环境压迫、仪式、极简科幻 | 维伦纽瓦 | 用比例、负空间、稳定慢观察和低频声场建立世界重量 |
| 任务危机、倒计时、现实主义奇观、多线因果、物理行动 | 诺兰 | 用清晰地理、目标、规则、结果和节奏收紧建立紧迫感 |
| 群像对峙、阵型变化、风雨、战争、道德选择、动作爆发 | 黑泽明 | 用前中后景、群体方向、天气作用和动作后果建立张力 |
| 日常世界遭遇奇观、儿童视角、家庭冒险、发现与保护 | 斯皮尔伯格 | 用人物视线、分层反应和清楚揭示让奇观获得情感意义 |
| 调查、程序、心理操控、职场权力、都市制度与细节不安 | 芬奇 | 用稳定控制、实景低调光和微小异常积累心理压力 |
| 制度寓言、仪式、封闭几何、黑色幽默、秩序逐步失控 | 库布里克 | 用对称、轴向运动、重复和形式偏差暴露人性裂缝 |
| 色彩权力、仪式群像、东方空间、身体阵列与个体反抗 | 张艺谋 | 用主色系统、阵列和材质把社会秩序转成可见关系 |
| 家庭群像、阶层、黑色喜剧、秘密空间和类型突然转调 | 奉俊昊 | 用楼层、门槛、路线和环境机制产生社会因果 |

当用户只提供抽象描述而未说导演名时，可按上表进行知识检索。最终输出可保留用户的高层风格标签，但重要标签首次出现时必须同时给出项目特定含义与可执行特征。

---

## Director Distinction Matrix

为避免同质化，检索时先判断以下主轴：

| Director | Human–Space Relationship | Camera Attitude | Time / Editing | Primary Emotional Mechanism |
|---|---|---|---|---|
| 王家卫 | 人物与城市很近，却被边界隔开 | 贴近、陪伴、偷看、轻微主观 | 停顿、重复、局部省略、主观余韵 | 未完成动作与关系错位 |
| 岩井俊二 | 人物被自然和日常温柔承载 | 安静观察、保持距离、自然跟随 | 连贯日常、季节呼吸、记忆留白 | 环境继续运动，人物缓慢成长 |
| 维伦纽瓦 | 人物成为巨大未知世界的尺度参照 | 稳定、缓慢、纪念碑式观察 | 耐心揭示、事件后停留 | 先感知力量，再理解信息 |
| 诺兰 | 人物在真实系统中解决问题并承担后果 | 客观、方向明确、随行动推进 | 并行收紧、因果交汇、时间压力 | 选择通过任务和物理行动显露 |
| 黑泽明 | 人物在群体、地形和天气中表明立场 | 预判调度、清晰记录、等待爆发 | 建立阵型→等待→爆发→结果 | 道德选择改变站位与群体关系 |
| 斯皮尔伯格 | 人物视线连接日常世界与非凡事件 | 流畅、清楚、跟随发现与反应 | 准备→异常→反应→揭示→行动 | 人物先感受，奇观随后获得情感意义 |
| 芬奇 | 人物被熟悉制度空间和信息控制困住 | 精确、稳定、近乎无痕地观察 | 程序推进、细节比对、控制裂缝积累 | 一个微小异常暴露谎言或欲望 |
| 库布里克 | 人物成为几何秩序和制度仪式的部件 | 正面、轴向、冷静、形式化 | 重复规则→精确偏差→荒诞或失控 | 形式秩序反向暴露人性裂缝 |
| 张艺谋 | 个体被综合色彩、阵列和权力空间包围 | 稳定展示阵列，随个体偏离而重构 | 建立仪式→个体偏差→群体施压→新秩序 | 颜色与身体站位承担欲望和反抗 |
| 奉俊昊 | 人物必须实际穿越阶层化建筑与生活系统 | 平稳跟随路线，宽镜观察群体 | 生活喜剧→空间揭示→悬疑或暴力后果 | 一个门槛或失误重新排列群体关系 |

若无法说出本次调用使用了表中哪一项差异，说明风格选择可能只是名称装饰，应返回剧情功能重新判断。

---

## File Loading Rule

标准加载顺序：

```text
读取 project_status.md
→ 确认当前合法 STATE
→ 读取本 index.md
→ 根据剧情功能选择一份主导演文件
→ 仅在明确混合需求时加载第二份文件
→ 按当前 Workflow 转译
→ 继承已确认资产与 Visual Direction
```

禁止：

- 无理由一次加载全部导演文件。
- 在 STATE-06 或 STATE-08 临时重新选择一套未确认风格。
- 只因场景中出现雨、夜、沙漠、校园或战争就自动匹配导演。
- 用导演知识覆盖 Character、Environment 或 Prop Asset。

---

## Shared Director File Schema

每份导演文件统一提供以下知识维度：

1. Knowledge Role
2. Core Identity
3. Narrative Tone
4. Emotional Grammar
5. Composition
6. Camera Movement
7. Lens Tendencies
8. Lighting
9. Color Palette
10. Production Design
11. Character Blocking
12. Performance Direction
13. Editing Rhythm
14. Sound Design
15. Weather / Atmosphere
16. Best Use Cases
17. Avoid / Misuse
18. Style Translation Rules
19. Seedance Execution Language
20. Combination Rules
21. Final Principle

这些标题是 Knowledge 组织维度，不是任何阶段的最终输出字段。

---

## STATE-04 Visual Development Call Rules

STATE-04 是导演风格的主要决策阶段。

从导演文件提取并统一为项目级 Visual Direction：

- 核心视觉概念与观看体验
- 摄影距离、稳定性、运动倾向和景深原则
- 构图、空间比例、前景与人物位置原则
- 主光来源、方向、冷暖关系和天气影响
- 主色、辅助色、强调色、饱和度和对比度
- 材质、环境空气和 Production Design 原则
- 人物表演尺度与情绪释放方式
- 剪辑节奏和声音方向
- 必须继承到后续阶段的连续性规则

STATE-04 只建立项目倾向，不逐镜头分配景别、焦段、时间码和具体动作。

如果用户只说“某导演风格”，不得直接确认 Visual Direction；必须结合当前剧情功能、资产、时代、地点和媒介属性做适配。

---

## STATE-06 Detailed Shot Design Call Rules

STATE-06 不重新挑选导演，而是读取已确认 Visual Direction，并按镜头叙事目的调用相关导演知识。

每个 Shot 至少判断：

- 镜头为何存在，推动信息、动作、关系还是情绪？
- 人物与环境的主关系是什么？
- 构图机制是什么，且是否保持空间可读？
- 摄影机起点、主要行为和终点是什么？
- 人物调度如何让情绪或立场可见？
- 光线、色彩、天气和声音如何继承场景？
- 镜头结尾留下什么可供下一镜继承的状态？

导演知识只影响镜头选择逻辑，不能成为“随机增加复杂运镜”的理由。

---

## STATE-08 Clip-based Video Prompt / Video Generation Call Rules

STATE-08 将已确认的 Shot Design 和 Visual Direction 转换为 Seedance 可执行内容。

必须执行：

```text
抽象风格词
→ 可见构图与空间关系
→ 可执行人物动作与情绪过程
→ 单一主要摄影机运动
→ 可追踪光线、天气、道具与声音
→ 起始状态—变化—结尾状态
→ 映射 templates/10_video_prompt.md
```

示例：

```text
“孤独、维伦纽瓦式宏大”
```

应转为类似：

```text
固定大全景建立前景平台、中景单人和远景巨型结构；
人物占画面高度很小，先停步抬头，再收紧手中设备；
远处结构阴影缓慢移动至人物脚边，摄影机保持稳定，
低频环境震动先于结构变化出现。
```

导演名可在内部检索记录与最终Prompt中保留；最终【主风格】负责在重要标签首次出现时完成项目特定解释，各分镜字段只写当前镜头需要的具体变化，不重复整段解释。

对每个当前Clip，先从导演知识中提取候选，再按`knowledge/prompt_compilation/state08_projection.md`唯一的Style Label Expansion Rule形成`Style Label → Project-specific Style Meaning → Executable Style Carriers → Prompt Compression`，只选择3—5个（或更少）最有价值且彼此兼容的Lighting / Color / Optics / Camera / Texture / Composition / Performance / Rhythm / Atmosphere carriers。不得机械复制导演文件全部维度；名称可以保留，完全冗余时允许省略，但不以“carriers已足够”为默认删除理由。

STATE-08 最终 Schema 唯一来源：

```text
templates/10_video_prompt.md
```

本目录不得定义另一套分镜字段、编号、时间码或最终排版。

---

## Style Translation Gate

任何导演参考进入后续阶段前，必须通过以下检查：

### 1. Story Function

明确本次风格选择服务什么剧情功能。不能只回答“更电影化”。

### 2. Asset Compatibility

确认不改变：

- 角色五官、年龄、发型、服装和身体比例
- 环境地点、时代、建筑结构和道路关系
- 关键道具身份、材质和使用状态

### 3. Observable Language

抽象词必须变成可观察结果：

| Abstract Word | Required Translation |
|---|---|
| 孤独 | 人物比例、留白、距离、视线、动作停顿 |
| 暧昧 | 视线错开、靠近后停止、前景边界、未完成台词 |
| 宏大 | 尺度参照、空间层级、人物比例、声音距离 |
| 紧张 | 时间限制、动作速度、呼吸、目标与障碍 |
| 悲壮 | 阵型变化、行动选择、天气压力、动作后果 |
| 怀旧 | 光线、材质、季节、重复动作、声音锚点 |

### 4. Camera Motivation

每个摄影行为必须说明为什么移动、向哪里移动、何时停止。

### 5. Seedance Simplicity

单镜头优先：

- 一个连续时间段
- 一个清楚空间
- 一个主要视觉事件
- 一个主要人物动作链
- 一个主要情绪变化
- 一个主要摄影机运动

---

## Mixed Style Rule

只有用户明确要求混合，或单一参考无法覆盖已确认 Visual Direction 时，才读取第二份导演文件。

组合流程：

```text
确定主导演知识轴
→ 说明主轴负责哪些维度
→ 从第二参考只提取一至两项辅助特征
→ 检查摄影、光线、节奏和表演冲突
→ 生成一个统一 Visual Direction
```

推荐分工示例：

- 主空间逻辑 + 辅助表演尺度
- 主摄影稳定性 + 辅助色彩关系
- 主动作调度 + 辅助环境气氛
- 主因果节奏 + 辅助情绪余韵

禁止输出：

```text
王家卫 + 岩井俊二 + 维伦纽瓦风格
```

必须输出为一个完整、无冲突的摄影、构图、光线、色彩、表演、声音与剪辑系统。

---

## Conflict Resolution Rules

冲突时按以下优先级处理：

```text
明确用户要求
→ 当前剧情功能
→ 已确认项目世界观
→ 已确认 Character / Environment / Prop Asset
→ 已确认 Visual Direction
→ 主导演知识轴
→ 辅助风格特征
```

常见冲突：

| Conflict | Resolution |
|---|---|
| 近距离轻微手持 vs 远距离纪念碑式稳定 | 按段落或镜头功能分工，不在同镜头叠加 |
| 清透自然光 vs 强人工冷暖色 | 选择一个主光线体系，另一方只影响表演或构图 |
| 耐心停留 vs 高频交叉剪辑 | 选择主时间压力；揭示段慢，任务推进段快 |
| 主观碎片 vs 动作地理清晰 | 动作与多人段优先空间清晰，余韵段允许主观处理 |
| 极浅景深 vs 群像阵型可读 | 群像与连续动作优先足够景深 |
| 强天气表现 vs 资产连续性 | 天气只能在上游确认后使用，并继承物理状态 |

---

## Asset Protection Rule

导演风格可以影响：

- 摄影距离、焦段倾向、稳定性和运动方式
- 构图、人物位置和环境比例
- 光线、色彩、材质和空气状态
- 表演尺度、剪辑节奏和声音方向

导演风格不能无授权改变：

- 角色身份与外貌
- 服装、时代和文化身份
- 地点、建筑结构和世界观
- 关键道具身份
- 剧情事实、人物关系和动作结果

例如：调用黑泽明知识不代表加入武士或古装；调用王家卫知识不代表改成雨夜霓虹；调用岩井俊二知识不代表改成校园；调用维伦纽瓦知识不代表改成科幻；调用诺兰知识不代表加入爆炸或时间倒计时；调用斯皮尔伯格知识不代表加入儿童或外星奇观；调用芬奇知识不代表加入犯罪与暗绿色；调用库布里克知识不代表所有镜头对称；调用张艺谋知识不代表加入大红和古装；调用奉俊昊知识不代表加入豪宅、地下室和暴雨。

---

## Cinematic Parameter Rule

器材、画幅、焦段、滤镜、光圈、帧率和胶片模拟只有在以下情况使用：

- 用户明确指定。
- STATE-04 已经确认。
- 对执行稳定性或视觉逻辑确有帮助。

禁止机械堆叠：

```text
ARRI + RED + IMAX + Anamorphic + Cooke + 8K + award winning
```

优先描述观看效果和执行行为：真实透视、足够景深、稳定慢推、局部高光柔化、环境材质可读。

---

## Unknown Style Handling

当用户提供当前目录没有的导演或影片参考：

- 不假装存在文件。
- 不创建虚构路径。
- 仅根据用户提供或可确认的视觉特征，分析摄影、构图、光线、色彩、表演、声音和节奏。
- 信息不足时只输出能够支持的临时视觉方向，不虚构具体风格事实。
- 新增导演文件属于单独的知识库扩展任务；当前十份文件不因此自动扩容。

---

## Validation Checklist

调用本目录后检查：

- [ ] 已读取本索引与实际需要的导演文件。
- [ ] 已说明风格服务的剧情功能。
- [ ] 已提取该导演与其他导演的明确区分点。
- [ ] 已将抽象词转成可观察、可执行的影视语言。
- [ ] 最终Prompt中的重要风格标签首次出现时已获得项目特定解释，同一Prompt没有重复展开。
- [ ] 后续连续Clip只在正式Style Source已锁定时使用标签/风格锚点 + 当前delta。
- [ ] 未改变已确认角色、环境和道具资产。
- [ ] 未机械堆叠器材和参数。
- [ ] 未用复杂运镜代替叙事。
- [ ] 多风格已合并为一个统一系统。
- [ ] STATE-04 未提前输出 Shot Design。
- [ ] STATE-06 未重新随机选择风格。
- [ ] STATE-08 已保持动作、空间、道具和情绪连续。
- [ ] STATE-08 最终格式完全服从 `templates/10_video_prompt.md`。

---

## Final Principle

Visual Styles Knowledge 的目标不是让输出更像“某个名字”，而是让抽象参考成为可执行的电影决策：

```text
导演标签用于检索，也可保留为创作锚点
→ 风格知识建立项目特定含义
→ 当前Clip选择可执行载体
→ STATE-04 建立统一视觉方向
→ STATE-06 设计具体镜头
→ STATE-08 转换为 Seedance 可执行信息
→ Template 定义最终输出格式
```

风格必须服务剧情、保护资产、保持连续，并能被摄影机、演员、灯光、美术、声音、剪辑和视频模型真正执行。
