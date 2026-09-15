# SD Film Project Bible Template

# AI影视项目视觉圣经模板


## Project Information


项目名称：

项目类型：

媒介形式（`live_action` / `3d_animation` / `2d_anime`；未确认写 `Pending`）：

目标模型：

制作目标：



---

# 1. Story Foundation

## Story Overview


故事简介：




## Core Theme


核心主题：




## Narrative Style


叙事风格：




## Emotional Direction


情绪基调：




---

# 2. World Building


## World Setting


世界背景：




## Time Period


时代背景：


说明：时代背景是**项目事实**，由用户或已确认项目材料拥有，本节只负责记录。它的**可见约束与时代错置判据**（器物与技术可用性、服装形制、文字与标识、照明与交通通讯条件）由`knowledge/period_and_place/index.md`唯一拥有，本节不重复定义；未登记时下游记`Period And Place: PENDING`，不加载该知识域，也不得从媒介、类型、平台或导演风格推定时代。


## Location System


主要地点：


说明：主要地点同样是项目事实，本节只负责记录。它的**地域可见表达与反刻板纪律**（空间组织、称谓与语言、身体语言与社交距离、日常器物与习俗的可见面）由`knowledge/period_and_place/index.md`唯一拥有；与已登记时代冲突时以时代的技术边界优先。


## Social Environment


社会环境：




---

# 3. Visual Identity


## Overall Visual Style


视觉风格：

Primary Style Logic：

Secondary Borrowed Traits（最多两项）：

Rejected Conflicts：

视觉母题与变化轨迹（至少三次可出现 / 变化 / 反转，不是装饰性重复）：

最终主摄影稳定性体系：

最终主光线体系：

最终主剪辑节奏：

导演/影片名称仅作为内部检索标签，不替代以上执行规则。

本区与Color System、Lighting Style、Composition Rules共同承载Aesthetic Decision Lock：四项决定必须各写明选择、被放弃的选项、依据与可见后果；缺少被放弃的选项视为尚未做出决定。


例如：

现实主义。

东方美学。

赛博朋克。

古典电影感。



---

## Color System


颜色真实来源（资产 / 环境 / 光源 / FX / 材质）：

主色、辅助色、强调色及占比/空间位置：

综合色相关系与饱和度层级（必须写明构成画面张力的两个色相关系，而不是只给色调名）：

整体明度、黑位、高光与局部对比：

白平衡 / 综合色温与绿色—品红偏色倾向：

肤色、中性色与关键资产固有色保护：

材质反射 / 吸收与介质综合色彩响应：

允许的综合色彩变化、稳定结束色态与跨镜连续性：

适用的Color模式语义（内部，不把CLR编号写入最终Prompt）：



---

## Lighting Style

主导光源与环境光逻辑：

光源空间锚点与方向：

光质、强度、光比与衰减（必须写明主光比的程度，以及它在何种情绪节点变化）：

综合色温与冷暖关系：

人物面部、皮肤、服装与道具受光：

环境材质、地面与反射：

天气 / 雾烟尘水等介质关系：

允许的动态光态与变化范围：

跨镜光影连续性与禁止突变：

适用的Lighting模式语义（内部，不把模式ID写入最终Prompt）：



---

# 4. Cinematography Rules


## Camera Style


摄影风格：



例如：

固定观察。

手持纪实。

电影运动镜头。



---

## Lens Preference


画幅基准或全画幅等效倾向：

主要焦段范围与摄影机距离倾向：

人物脸部几何、边缘安全与背景尺度规则：

景深与对焦原则：

广角运动、长焦跟焦与连续覆盖的稳定规则：

焦段不自动等于景别、情绪、透视、虚化或画面质感；具体逐镜选择由STATE-06完成。



---

## Composition Rules


构图原则（必须写成全片可执行的构图主张，并写明放弃了哪一类常规构图）：




---

# 5. Character Direction


## Character Design Rules


人物整体设计方向：




---

## Costume Rules


服装体系：




---

## Character Consistency Rules


必须保持：


脸型。


年龄。


身体比例。


标志性特征。


核心服装。



---

# 6. Environment Direction


## Environment Style


环境视觉方向：




---

## Architecture / Space


建筑或空间规则：




---

## Material Language


材质体系：



木。

石。

金属。

玻璃。

布料。




---

# 7. Prop Direction


## Important Props


关键道具：




## Prop Design Rules


道具设计原则：




---

# 8. Performance, FX And Sound Direction


## Performance Direction

默认表演强度与现实主义尺度：

角色中性面部、视线、呼吸、姿态与动作基线：

刺激 → 注意 → 评估 → 可见反应 → 行动选择 → 恢复原则：

压抑 / 伪装 / 混合情绪与泄漏尺度：

泪水、脸红、颤抖等条件性身体结果与连续性：

对白说话、倾听、口型和呼吸原则：

双人 / 多人反应顺序与视觉重点：

必须避免的固定表情公式和舞台化倾向：




## FX Direction


效果的现实主义程度、视觉强度、物理交互与连续性原则：




## Sound Direction


对白、环境声、动作声、剧情内声源、同期声音留白与声音连接原则（不在此处规划后期配乐；Music / Score只有用户显式调用独立模块后另行交付）：




---

# 9. AI Generation Rules


## Reference Priority


优先级：


角色参考图

＞

环境参考图

＞

文字描述



---

## Prompt Rules


遵循：


主体。

动作。

环境。

摄影。

光影。



避免：

过长描述。

无关背景。

大量负面词。



---

# 10. Continuity Rules


## Character Continuity


人物连续性要求：




## Environment Continuity


环境连续性要求：




## Prop Continuity


道具连续性要求：




## FX Continuity


效果触发、强度、方向、覆盖范围、残留后果与声音尾部连续性要求：




---

# 11. Production Notes


## Model Specific Notes


模型适配说明：




## Special Requirements


特殊制作要求：




## Delivery Spec｜交付规格

交付画幅（横屏 / 竖屏及比例；未确认写 `Pending`）：

交付规格（分辨率、时长或集长、必要平台限制；未知写 `Unknown`）：

目标平台 / 渠道：

来源（用户当前明确请求 / 已确认目标形式与项目材料）：

确认状态：`UNSELECTED / SELECTED`

说明：本节是`项目已确认交付规格`的**唯一记录位置与定义owner**——其他文件里"用户当前明确例外或项目已确认交付规格优先"一律指本节，不再各自解释这个词。写入规则：用户在当前请求中明确给出画幅、比例或平台时直接写入并标`SELECTED`；只有能从已确认项目材料直接确认时才登记。**未确认时保持`UNSELECTED`**，此时资产图按`rules/02_asset_rules.md`的`Asset Canvas Ratio Default｜资产图画幅默认`取类别默认，成片画幅按STATE-08既有字段规则处理；**不得**从任何参考图的宽高比、平台标签、目标形式或素材比例反推交付规格。本节只记录事实：不授权外部提交，不改变资产双确认、Reference Budget或任何Hard Stop；与用户当前明确指令冲突时以用户当前指令为准，并在同一次写入中更新本节。

---

# Project Summary


项目视觉核心：




项目不可改变元素：




项目可变化元素：




---

# Final Principle


Project Bible 是整个AI影视项目的视觉最高规则。

所有：

资产。

场景。

镜头。

视频Prompt。


必须遵循本文件。
