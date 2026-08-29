# Script Adaptation

## Purpose

本Knowledge只在STATE-01已经把非制作剧本诊断为需要Adaptation、输出Optimization Opportunity Report并取得用户明确优化/改编授权后，把Source Material改编为可继续编剧优化的`Adaptation Draft`。报告与授权之前不得加载本Knowledge执行实际改编。它不创建独立STATE，不拥有用户可见Schema，不替代`workflows/02_script_analysis_workflow.md`，也不创建SCENE、SHOT、CLIP、资产或Seedance Prompt。

核心原则：改编优先忠于核心叙事价值，而不是忠于原文字面结构。

## Module Contract

- **Module Name**：Script Adaptation Module
- **Module Type**：STATE-01条件性改编Knowledge
- **Trigger**：Input Classification为C类，Optimization Opportunity Report已说明Adaptation Need，且用户明确表示“优化 / 继续优化 / 进入优化”或无歧义同义授权
- **Not Triggered As**：A类已是制作剧本、B类粗略剧本/初稿、No Revision / Final Script分支、独立STATE、Scene Breakdown、Shot Design或Prompt编译器
- **Position**：`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate → Adaptation Target Detection → Script Adaptation → Adaptation Draft → Screenwriting Optimization`
- **Required Inputs / Owners**：用户Source Material、Project Bible已确认事实、目标形式/时长/平台/受众、品牌与IP约束、Protected Creative Locks；事实由用户与已确认项目资料拥有
- **Output Owner**：本Knowledge只提供改编判断与`Adaptation Draft`内容；最终可见字段、顺序与排版由`templates/02_script_analysis_prompt.md`拥有
- **Read / Write Boundary**：只读用户素材和已确认项目事实；只把改编结论交给STATE-01 Workflow写入当前项目Artifact与Script Status，不修改资产、Visual Direction、SHOT、CLIP、Portable Schema或后续Prompt
- **Downstream Consumers**：`knowledge/screenwriting_optimization.md`、`knowledge/directorial_interpretation.md`及用户确认后的Production-Locked Script
- **Protected Upstream Facts**：核心事件、核心人物关系、主题、关键情绪、名场面、关键道具、世界观、品牌诉求、用户明确锁定的台词/事件及授权边界
- **Conflict Route**：改编需要突破Protected Creative Locks、目标形式不明且会实质改变结构、或来源事实互相冲突时，保持STATE-01 IN_PROGRESS并记录Pending Decision；不得擅自补造
- **Deterministic Invariants**：报告与明确授权之前不改编；六层改编过程全部完成；每项删并改排可追溯；Adaptation Intensity合法且有依据；No Revision与Optimization Rejected不加载本模块；短剧Adapter只按Target Detection条件加载；Adaptation Draft不得进入STATE-02

## Adaptation Intensity

在改写前锁定一个强度等级，并记录`Selected Level + Selection Evidence + Protected Locks`：

- **LEVEL 1 — Light Adaptation**：保留原结构，主要进行压缩、视觉化、台词优化与最小必要连接。
- **LEVEL 2 — Structural Adaptation**：允许合并人物、重排事件、提前冲突、强化高潮，但必须保留核心叙事价值与保护项。
- **LEVEL 3 — Free Adaptation**：保留核心人物、主题与名场面，可重构适合目标短视频形式的新故事结构。

默认根据用户要求、素材离制作剧本的距离、目标时长与结构容量选择最低足够等级。不得为了“更戏剧化”自动升级。用户明确“基本不要改剧情”或同义表达时只能选择LEVEL 1；若LEVEL 1无法满足目标，必须说明冲突并请求用户决定，不得静默升级。

## Required Adaptation Process

### 1. Source Essence Extraction

从Source Material建立`Source Essence Ledger`，至少记录：

- 核心事件
- 核心人物关系
- 主题
- 关键情绪
- 名场面
- 关键道具
- 世界观
- 品牌诉求（适用时）
- 用户明确不可改内容与权利/事实边界

没有来源证据的内容不得写成原作事实。历史事件、品牌事实或既有影视桥段存在不确定性时保持待确认，不用常识补造关键剧情。

### 2. Adaptation Objective

明确本次改编的目标形式、目标时长/集长、平台/画幅、受众、单集或系列、主情绪与商业目标。目标必须来自用户或已确认项目资料；缺失且会改变结构时记录Pending Decision。

随后执行`Adaptation Target Detection`：只有目标为短剧、竖屏剧情或1—3分钟剧情视频时，才读取并执行`knowledge/adaptation/short_form_drama_adapter.md`。电影短片、品牌广告、儿童动画、纪录表达、长片段落等其他目标不得强制套用短剧规则。

### 3. Preserve / Compress / Rewrite / Remove Decision

对每个来源叙事单元记录一个主要决策及理由：

- `Preserve`：原功能和位置基本保留
- `Compress`：压缩重复信息、过程或次要Beat
- `Merge`：合并同功能人物、场景、事件或信息
- `Reorder`：为目标时长、因果或悬念重排
- `Screen Rewrite`：把文学/概念表达转为可见、可听、可演、可拍的行动
- `Remove`：删除不服务目标且不属于Protected Creative Locks的内容

每项决策必须能追溯到Source Essence、Adaptation Objective与Intensity；不得把简单缩写冒充改编。

### 4. Screen Translation

将心理、背景、评价和抽象概念转换为屏幕层可验证表达：人物选择、动作后果、眼神与注意、停顿、身体距离、道具处理、环境变化、剧情内声音或必要短台词。

只描述“发生什么、谁如何反应、观众获得什么信息”，不得提前决定机位、焦段、运镜、正式Blocking Map、SHOT或CLIP。

### 5. Duration & Dramatic Restructuring

按目标形式重组信息与戏剧推进，确保：

- 目标时长内角色、地点、信息、台词、动作阶段与转折容量可执行
- 核心欲望、阻力、升级、兑现与结束功能清楚
- 叙事顺序服务目标受众与平台，但不越过Protected Creative Locks
- 短剧目标的具体节奏只由`short_form_drama_adapter.md`提供；其他类型按自身目标组织

### 6. Adaptation Fidelity Check

逐项回查Source Essence Ledger：

- 核心事件与人物关系是否仍成立
- 主题、关键情绪和名场面是否保留或有明确等价转换
- 关键道具、世界观、品牌诉求与用户锁定项是否被误删或改义
- 每项Merge / Reorder / Screen Rewrite / Remove是否在所选Intensity内
- 新增桥接是否为最小必要且未伪装成来源事实

任一保护项失败，先修正Adaptation Draft；无法在当前Intensity内解决时返回用户决定。

## Handoff

完成后输出给STATE-01 Workflow：

- Source Essence Ledger
- Adaptation Objective与Target Detection
- Adaptation Intensity
- Preserve / Compress / Merge / Reorder / Screen Rewrite / Remove Ledger
- 完整`Adaptation Draft`
- Adaptation Fidelity Check
- Protected Creative Locks与Pending Decisions

Workflow只能在用户明确授权后把`Script Status`从`Source Material`更新为`Adaptation Draft`，随后进入Screenwriting Optimization与Directorial Interpretation。`Adaptation Draft`不是用户已确认制作事实，不得进入STATE-02；Production Script Proposal输出后仍须再次等待用户确认。

## Completion Check

- Input Classification确为C类，Optimization Opportunity Report已输出，用户已明确授权改编/优化，且不存在No Revision / Final Script或Optimization Rejected指令。
- 六层Required Adaptation Process均有结论。
- Adaptation Intensity合法、有证据且未越级。
- Target Detection只在适用目标加载短剧Adapter。
- 改编结果可独立进入编剧优化，但未创建后续STATE实体或技术方案。
- Fidelity Check通过；未通过项已修正或转为Pending Decision。
