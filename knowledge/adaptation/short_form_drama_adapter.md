# Short-form Drama Adapter

## Purpose And Trigger

本Knowledge是`knowledge/script_adaptation.md`的条件性短剧适配器。只有STATE-01 `Adaptation Target Detection`确认目标为以下任一类型时才加载：

- 短剧
- 竖屏剧情
- 1—3分钟剧情视频

其他广告、电影短片、儿童动画、纪录表达、长篇影视或未确认目标一律Not Applicable。它只约束C类Source Material的改编；B类粗略剧本只进入Screenwriting Optimization，不因时长相近而自动触发本Adapter。

## Machine-executable Decision Contract

依次建立并检查以下记录：

```text
Target Evidence
→ Core Event Count
→ Hook Evidence
→ Main Conflict Entry Evidence
→ Character Recognition Cards
→ Dialogue Economy Audit
→ Emotional Payoff Map
→ Five-Beat Rhythm Map
→ Ending Hook Evidence
→ PASS / REVISE / PENDING
```

任一硬门缺失时返回`REVISE`；需要用户决定的保护项冲突返回`PENDING`。不得用新反派、新身份、新世界观规则或无来源反转填补失败项。

## Hard Gates

### 1. Opening Hook Gate

开篇前3秒必须出现以下至少一项，并记录具体文本证据：

- 冲突
- 异常
- 欲望
- 危机
- 强信息

“前3秒”是短剧目标的硬检查窗口，但Hook形式不等于必须吵架、打脸或旁白喊话。视觉奇观、反常行为、身份信息差也必须归入上述五类之一并说明其叙事作用。

### 2. Main Conflict Entry Gate

前30秒必须进入主要矛盾，不能仍只介绍人物、世界或日常过程。若目标总时长短于30秒，则应在前段完成主要矛盾进入；不得为了字面时间码拖到片尾。

### 3. Single Core Event Gate

单集只聚焦1个核心事件。支线只保留推动、阻碍、解释或兑现该事件所需的最小内容；无法服务核心事件的内容执行Compress、Merge或Remove。

### 4. Ending Hook Gate

结尾必须存在可识别Hook，并标注类型与下一步驱动力，例如悬念、反转、新危机、未完成欲望、身份揭示或关系升级。Hook不得凭空推翻已经建立的因果或Protected Creative Locks。

## Character Rapid Recognition

主要角色通常不超过5个；超过时先检查是否可在当前Adaptation Intensity内合并功能。每个主要角色必须建立完整识别卡：

```text
角色功能
+ 核心欲望
+ 性格标签
+ 标志动作
+ 语言特征
+ 视觉记忆点
```

六项缺一则角色快速识别不通过。标签用于短时长强识别，不得替代角色在当前核心事件中的具体选择；不得为了标签化擅改用户锁定的身份、关系或物种。

## Dialogue Economy Rule

- 短句优先，单句通常控制在7字左右，但不是绝对硬限制。
- 一句只承担一个主要信息；复杂信息允许自然延长，不得为满足字数把对白切得机械。
- 能用动作表达，不再用台词重复解释。
- 能用表情或注意变化表达，不再追加同义OS。
- 能用环境、道具或结果表达，不让人物口头介绍。
- 删除与核心事件无关的生活性过渡动作和寒暄。
- OS只在无法通过当前可见行动清楚表达且确有叙事价值时使用，不得作为信息堆放区。

审计时逐句标记`KEEP / SHORTEN / VISUALIZE / REMOVE`及理由。

## Emotional Payoff Map

每集只选择：

```text
1个主情绪 + 最多1个辅助情绪
```

类型只从`爽 / 虐 / 甜 / 惊 / 燃 / 笑 / 悬`中选择。每个主要Beat必须标记它如何积累、释放或反转该情绪；无关情绪线应压缩或删除。动作、表情、停顿、呼吸、手部细节与身体距离优先承担情绪张力，不让角色直接解释“我很愤怒/悲伤/震惊”。

## Five-Beat Rhythm Model

使用以下五段模型形成节奏图：

```text
Hook → Setup → Escalation → Payoff → Next Hook
```

- **Hook**：立即建立冲突、异常、欲望、危机或强信息。
- **Setup**：只补足理解核心事件所需的人物、关系、目标和规则。
- **Escalation**：阻力、代价或信息差持续升级。
- **Payoff**：兑现本集主情绪和核心事件的阶段结果。
- **Next Hook**：以悬念、反转或新冲突驱动下一集/下一段。

该模型是短视频节奏参考，不是死时间码。除“前3秒Hook”和“前30秒进入主要矛盾”两项检查外，不得机械分配每段秒数；应根据总时长、对白密度、动作复杂度和平台生成容量调整。

## Platform And Production Constraints

- 场景通常不超过3个/集；超过时检查合并或删减，但用户锁定的必要场景不得擅删。
- 信息密度应与受众和平台调性一致；没有用户或项目证据时不得刻板推定“下沉市场”或某平台受众。
- 商业植入只能使用已确认品牌诉求、道具、台词或剧情功能，自然融入核心事件，不新增未经确认的功效或品牌事实。
- “3集试错”属于系列发行策略，只在用户目标为系列短剧且明确需要平台测试时记录，不强制改写单集。

## Acceptance Checklist

```text
[ ] Target Evidence明确属于短剧 / 竖屏剧情 / 1—3分钟剧情视频
[ ] 前3秒Hook至少命中五类之一并有文本证据
[ ] 前30秒或更短作品前段已进入主要矛盾
[ ] 单集只有1个核心事件
[ ] 主要角色均具备六项快速识别信息
[ ] Dialogue Economy Audit完成，7字仅为偏好值
[ ] 主情绪1个、辅助情绪不超过1个
[ ] Hook / Setup / Escalation / Payoff / Next Hook五段功能完整
[ ] 结尾Hook可识别且不破坏因果与保护项
[ ] 节奏参考未被误写为全部段落的死时间码
```

全部通过才返回`PASS`并交给通用Adaptation Fidelity Check；否则返回`REVISE`或`PENDING`及最小修正范围。
