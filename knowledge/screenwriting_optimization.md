# Screenwriting Optimization

## Purpose

本Knowledge是`knowledge/screenplay_development.md`所拥有Screenwriter Module的授权后优化子模块。它只在STATE-01已经输出Optimization Opportunity Report且用户明确同意优化，或Class C获准改编并形成Adaptation Draft之后使用。首次报告阶段只执行统一Writer Diagnosis，不得借本Knowledge自动改写。它负责把已获授权的优化方向转化为更适合影视生产与目标时长的制作版叙事方案；不创建新STATE，不替代Workflow，不拥有用户可见Schema或第二套Writer Packet。

## Module Contract

- **Module Name**：Screenwriting Optimization
- **Module Type**：STATE-01条件性编剧Knowledge
- **Trigger**：Optimization Opportunity Report已经输出，且用户明确表示“优化 / 继续优化 / 进入优化”或无歧义同义授权；或Class C已按该授权完成并通过Fidelity Check的Adaptation Draft
- **Not Triggered As**：用户明确禁止改写时的分析工具、独立Workflow、资产设计、Scene Breakdown、Shot Design、Director Decision Layer或Prompt编译器
- **Position**：统一位于`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`之后；A/B类为`Screenwriting Optimization → Directorial Interpretation`，C类为`Adaptation Draft → Screenwriting Optimization → Directorial Interpretation`，全部位于STATE-01内部
- **Required Inputs / Owners**：用户原始文本或已通过Fidelity Check的Adaptation Draft、Project Bible已确认事实、用户给定时长/平台/品牌约束、Optimization Scope、Adaptation Intensity与Protected Creative Locks；这些事实由用户和上游项目资料拥有
- **Output Owner**：专业优化结论由本Knowledge提供；最终可见字段与Production Script Proposal排版只由`templates/02_script_analysis_prompt.md`拥有
- **Read / Write Boundary**：只读用户素材和已确认项目事实；只把建议交给STATE-01 Workflow写入当前项目Artifact，不修改资产、镜头、Clip、Portable Schema或Skill根目录项目数据
- **Downstream Consumers**：STATE-01 Directorial Interpretation与用户确认后的Production-Locked Script
- **Protected Upstream Facts**：核心创意、世界观、角色身份与关系、关键设定、品牌要求、用户指定台词/情节锁、禁止修改范围
- **Conflict Route**：建议需要突破保护项或局部范围时，列为Pending Decision并等待用户授权；不得擅自扩大修改
- **Deterministic Invariants**：没有明确优化授权时不改写；所有Required Diagnosis Dimensions均检查；每项修改能追溯到Opportunity Report中的已识别问题；局部优化无越界；Proposal保留保护项；未确认提案不升级为Production-Locked

## Core Principle

优化不是“把文字写得更漂亮”，而是让故事目标、冲突、因果、人物选择、信息节拍和可视行动在目标时长内成立。

先保护用户创意，再处理结构。不得为了通用戏剧公式强加新反派、新感情线、新世界观规则、角色改名换身份或品牌冲突。

## Required Diagnosis Dimensions

首次Opportunity Report与获准后的优化必须共享以下十二个检查维度，并记录“成立 / 需优化 / 不适用 / 用户锁定”；获准后的每项修改必须回指相应维度：

1. **开场钩子**：开场是否在目标媒介允许的注意窗口内建立异常、欲望、悬念、关系张力或视觉问题。
2. **核心冲突进入时机**：主要目标与阻力是否及时出现，是否因前置信息过长而推迟故事启动。
3. **信息重复**：同一事实、情绪或关系是否被旁白、对白、动作或多个Beat重复表达。
4. **台词效率**：台词是否推进目标、冲突、关系或揭示；是否重复画面、过度解释或挤占动作空间。
5. **动作可视化**：抽象心理、背景介绍和评价性文字能否转换为可观察的选择、反应、行为后果或剧情内声音。
6. **人物记忆点**：主要人物是否有与其欲望、矛盾和行为一致的可识别选择、语言习惯、动作、关系张力或视觉行为。
7. **节奏**：建立、刺激、升级、转折、高潮、收束是否过早、过晚或重复；停顿是否有信息或情绪功能。
8. **高潮力度**：最高强度的选择、揭示、动作或情绪兑现是否集中，是否真正回应核心冲突并产生结果。
9. **情绪价值**：观众是否能经历明确的期待、压力、释放、共鸣、惊喜、爽感、虐感、温暖或其他目标情绪，而非只理解事件。
10. **结尾Hook**：结尾是否完成本段兑现，并在项目需要时留下下一事件、关系变化、信息缺口或余韵；不需要续接时可记录Not Applicable及理由。
11. **时长适配**：目标时长内信息量、对白量、动作阶段、转折数量和情绪铺垫是否可执行；未给定时长时记录密度风险，不虚构精确秒数。
12. **场景/人物复杂度**：场景数、角色数、世界切换、群体调度和一次性设定是否超出目标时长与AI制作容量；是否存在可删并的同功能人物、地点或Beat。

以下Writer Diagnosis作为上述十二维的底层证据持续检查，不另行取代用户要求的十二项报告结构：

- causality与`Trigger → Interpretation → Desire → Decision → Action → Consequence → New State`
- character motivation、Objective / Hidden Objective与Relationship Need
- scene necessity与Information / Relationship / Decision / Power / Emotional / Expectation Value Change
- Writer Beat progression；Writer Beat不得被误当Shot
- conflict / obstacle / stakes与题材适配的escalation
- `Dialogue → Surface Meaning → Subtext → Hidden Objective`
- Setup / Plant / Foreshadow / Callback / Payoff / Reversal / Recontextualization
- Information Architecture、Character / Relationship Arc与ending payoff

没有任何意义变化、必要建立、呼吸或Setup功能的场景标记`Weak / Replaceable Scene`。角色设定不支持直说时，把直白对白标记为Subtext Opportunity，而不是机械删对白。强商业钩子、固定节拍密度和冲突升级只由适用genre adapter提供，不进入通用优化默认值。

## Optimization Method

### 1. Establish Protected Locks

先列出不得修改项。未获授权的信息不因“更戏剧化”而变成可改项。

### 2. Diagnose Before Rewriting

把问题写成可验证的叙事症状，例如“主角直到结尾才获得行动目标”“同一信息由旁白和对白重复两次”，不得只写“节奏不好”“不够抓人”。首次Opportunity Report只能写问题、影响与方向；只有User Decision Gate取得明确授权后，才在本Knowledge中形成实际改写。

### 3. Choose Minimum Structural Intervention

按最小必要修改依次考虑：

`删除重复 → 合并同功能Beat → 提前刺激/目标 → 重排因果 → 补最小必要动作或信息`

只有前一种不能解决问题时才升级。新增情节必须是保住用户核心创意所需的最小桥接，并在Proposal中显式说明。

### 4. Convert Explanation Into Drama

优先把“人物很紧张”“关系不好”“事情很严重”等说明转换为可见选择、迟疑、回避、打断、失败动作、道具处理、身体距离或剧情内声音。该步骤只定义叙事行为，不设计正式镜头。

### 5. Fit The Target Duration

若用户提供时长，按时长压缩；未提供时长，不虚构精确秒数，但要指出影响节奏和制作容量的密度风险。不得为凑短时长删除用户明确锁定的核心事件。

### 6. Preserve Traceability

每项实质修改必须说明：来源问题、修改范围、保留事实、预期叙事收益、可能影响。局部优化时还要列出未修改范围。

## Partial Optimization Rule

局部优化采用Scope Fence：

- **Inside Scope**：允许修改的明确文本或功能。
- **Outside Scope**：保持原事实、顺序和语义。
- **Boundary Impact**：局部修改对前后因果确有影响时，只提出最小连接建议并等待授权。

不得以修复局部节奏为由自动重写整部剧本。

## Handoff To Directorial Interpretation

交接内容只包括：

- 已保护的核心创意与关键设定
- 经过优化的剧情目标、冲突、因果和Beat顺序
- 每个主要人物的目标、动机与变化
- 信息铺垫/揭示顺序
- 需要可视化的抽象信息
- 目标时长与密度风险
- 明确的修改范围和Pending Decisions
- 更新后的Writer Beats、Scene Value Change、Subtext / Hidden Objective、Setup / Payoff obligations与Scene Exit State

不包含SHOT、CLIP、机位、焦段、运镜、正式分镜表或Director Decision Notes。

## Completion Check

- 已存在明确优化授权，且不是由单独“继续 / 下一步 / 好的”推定。
- 十二组Required Diagnosis Dimensions均有结论。
- 建议采用最小必要修改，且能追溯到具体问题。
- 用户核心创意、世界观、角色身份、关键设定和品牌要求未被擅改。
- 局部优化没有越过Scope Fence。
- 交接材料足够进行Directorial Interpretation，但没有提前进入Scene / Shot / Clip设计。
