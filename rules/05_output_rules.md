# Output Rules

# AI影视生产输出规则


## Purpose


本规则用于规范SD Film各阶段输出格式。


确保：

输出内容符合当前Workflow阶段。

输出结果可被下一阶段继续使用。


---

# Rule 00

# Default Delivery Surface

完整STATE-00至STATE-09流程、确认Gate、状态写回、资产锁、连续性、Writer / Director判断和Review均为必经内部生产工作；它们不自动成为用户可见交付。默认用户可见交付只允许为：剧本、各类设定资源、分镜表、Clip表、最终视频提示词。

项目启动页、项目状态/Portable State、Registry、Visual Guide、Scene Breakdown、色彩体系、镜头语言、情绪/表演设定、导演分析、经验应用、QA清单和Review报告默认静默。用户明确请求查看、导出、保存、恢复、审核或返修其中某项时，才按对应Template或Contract输出。

内部结论只能在最终交付确实需要的位置折叠呈现：资源包内的资源事实，分镜表内的可见画面与动作，Clip表内的Clip执行边界，最终提示词内的模型执行语义。不得为展示专业度另开色彩、镜头、情绪、摄影、导演或状态报告。本规则优先于本文件其余“允许输出”条款中关于默认展示范围的描述，不改变Template所有权或字段正确性。


---

# Rule 01

# Stage Based Output


所有输出必须匹配当前Workflow阶段。


禁止：

未完成当前阶段任务时，

输出后续阶段成果。



---

# Rule 02

# Project Setup Output


STATE-00 Project Setup阶段：

默认静默完成项目初始化、制作目标确认与状态更新，并在同一响应进入STATE-01。仅当缺失信息会实质影响剧本架构或用户明确请求项目资料时，才显示最短必要信息。


禁止输出：


- 剧本分析
- 分镜表
- Detailed Shot Design
- Clip Production Plan
- 视频Prompt



---

# Rule 03

# Script Analysis Output


STATE-01 Script Analysis阶段：

允许输出：

- 可独立阅读的剧本或剧本提案；
- 只有确认Gate确实需要时附一行最小决定问题。

Input Classification、Optimization Opportunity、适配判断、Writer / Director分析、人物/场景/视觉元素诊断和状态字段均为内部工作，不独立输出。Existing Script在未获改写授权时，最多用简短问题请求用户选择保留或授权优化，不展开诊断报告；不得越过授权生成改写正文。


禁止输出：


- 角色资产
- 环境资产
- 道具资产
- Detailed Shot Design
- Clip Production Plan
- Video Prompt

STATE-01首次报告后必须保持Source Material并停在User Decision Gate；用户拒绝优化时原稿直接锁定。不得在没有明确优化授权时输出Adaptation Draft或Production Script Proposal，不得把Adaptation Draft或Optimized Proposal写成Production-Locked；短剧Adapter不适用时不得输出其规则作为通用硬门。



---

# Rule 04

# Asset Output


STATE-02 / STATE-03阶段：

允许输出：


- 资产需求清单
- 角色资产信息
- 环境资产信息
- 道具资产信息
- 完整可直接生图的角色、环境、道具与正式FX Image Prompt
- Prompt确认Checkpoint与图片确认Checkpoint
- 未确认图片的Candidate Reference记录
- Asset Registry更新（内部）

STATE-03首次交付Image Prompt时必须停在`Prompt Draft`等待确认；不得在同轮直接出图。图片生成后必须停在`Image Generated`等待确认；不得自动输出`Asset Confirmed`或Active/Canonical登记。


禁止输出：


- 分镜
- 镜头设计
- 视频Prompt



---

# Rule 05

# Scene And Shot Output


Scene Breakdown阶段：

输出：

- 场景信息
- 空间关系
- 场景需求



Shot Design阶段：

输出：

- `分镜表`，严格使用`templates/08_shot_design_prompt.md`的默认用户可见Schema；每镜只呈现画面、表演/动作、必要镜头表达、连续性和资产引用。
- 完整时间码、镜头参数、摄影调度、光色推导、声音设计、风险/降级和导演判断仍逐Shot内部维护、核验并传递给STATE-07；不得独立输出，也不得因压缩展示而遗漏生产数据。

内部Camera Language Decision、Execution Risk、Director Decision Notes与Knowledge Reflection不得成为正式用户可见字段或附录。`台词/旁白/口播`是泛化字段，不得退回固定“女声口播”。`同期声音设计`只记录环境声、同步前景声、Foley、剧情内声源与声音尾部，永久禁止任何后期配乐说明。

### Per-Shot Structural Parity Hard Gate

- 单镜输出与批量输出必须逐Shot使用完全相同的Template字段、顺序与完成标准；批量只改变Shot数量，不改变单镜Schema或内容密度。
- 不得因篇幅、总镜数、上下文长度或输出上限删字段、合并既定字段、缩写/改名字段、使用简化表头、把多镜内容合写为摘要，或只给首镜/示例镜完整结构。
- 每个Shot的`画面内容 / 构图`必须分别明确画面描述、构图与人物位置关系；`人物动作`必须分别明确人物情绪、动作重点与完整动作链；`同期声音设计`必须分别明确环境声、同步音效与声音尾部，且不得包含配乐；`AI制作备注`必须分别明确角色一致性、环境一致性、道具一致性与生成风险/控制项。
- 禁止以“同上”“沿用上一镜”“见前文”“其余一致”“略”或空白代替当前Shot内容；不适用项必须写`不适用`及具体理由。
- 全部Shot一次无法完整容纳时必须自动连续分批，默认每批4—5个Shot，可按复杂度调整；批次边界只能位于完整Shot之间。不得拆开单个Shot，不得压缩单镜结构，不得遗漏、重复或重排SHOT。



禁止：

Scene阶段直接输出视频Prompt。



---

# Rule 06

# Clip Production Output


STATE-07阶段：

输出：

- Confirmed Clip Production Plan
- 每个Clip包含的Shot、起始状态、连续动作、摄影机/空间关系、道具连续性与结尾状态
- 4—15秒时长账本、模型复杂度、风险降级、尾帧用途与下一Clip Handoff



禁止：

把Storyboard图片、分镜板、漫画格、接触表、拼图、Scene Top-down Blocking Map或多画面材料用作Clip/STATE-08输入；也禁止Clip Production替代Detailed Shot Design。经Before-Single-Clip-Prompt Gate确认的单Clip `REF-SKETCH`只作为Visual Blocking Reference严格例外，不开放其他线稿或Planning材料。


禁止：

直接输出最终视频Prompt。



---

# Rule 07

# Clip-based Video Prompt / Video Generation Output


STATE-08阶段：

允许输出：


- 视频生成Prompt
- 动作描述
- 摄影执行要求
- 模型适配参数


输入必须来自：


- 已确认资产
- Confirmed Detailed Shot Design（仅生产数据）
- Confirmed Clip Production Plan（Clip级生成合同）
- 经Before-Single-Clip-Prompt Gate验证并绑定当前Blocking Signature的Confirmed `REF-SKETCH`（仅在Final Assessment=`REQUIRED`时作为受限Visual Blocking Reference）
- 禁止Storyboard图片、分镜板、拼图、Scene Top-down Blocking Map或多画面参考；不得把未验证草图混入上述例外



禁止：

根据原始剧本直接生成视频Prompt。

按Shot拆分Prompt；一个Confirmed Clip无论包含一个还是多个Shot，都只输出一条连续Prompt。



---

# Rule 08

# Template Priority


输出时：

优先使用templates目录中的对应模板。


保持：


- 字段一致
- 命名一致
- 格式一致



---

# Rule 09

# No Premature Output


如果当前阶段信息不足：

禁止补全不存在的信息。



例如：


未完成角色资产：

禁止生成最终角色镜头。



未完成镜头设计：

禁止生成视频Prompt。



---

# Rule 10

# Output Quality


输出必须满足：


- 信息完整
- 阶段明确
- 可继续执行
- 符合生产流程


---

# Rule 11

# Per-Shot Boundary Output


从STATE-06开始，任何逐镜输出必须按当前阶段对应Template，逐镜公开以下等价信息：


- 起始状态来源或继承方式
- 最后一帧稳定限制
- 与下一镜头的连接方式，或无法直接继承的原因


不得只在全局说明、最后一镜汇总或单个示例中提供。


STATE-08必须使用templates/10_video_prompt.md规定的逐镜字段，Rules不得创建替代Schema。


---

# Rule 12

# Clip Duration / No Timeline In Final Prompt


STATE-08最终视频Prompt使用`# CLIP-X｜标题 Seedance视频提示词`区块并保留Clip内`分镜X`编号；不得使用方头括号或独立CLIP标题字段。Gxx如用于尾帧资产命名，只能出现在字段内容中。


只允许在【时长】写一次Confirmed Clip的4—15秒平台生成时长。禁止输出时间码、起止时间戳、总片时长、单分镜时长、按秒动作区间、帧率、帧数或帧区间限制。


除Clip平台生成时长外，上游时长只用于内部动作密度和执行性检查。


Frame Rate或Frame Count必须放在Prompt之外。



---

# Final Principle


输出不是最终目的。


每个阶段输出：

都是下一阶段的生产输入。


正确流程：


分析输出

↓

资产输出

↓

场景输出

↓

镜头输出

↓

Clip Production输出

↓

视频输出
