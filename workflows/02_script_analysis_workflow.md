# Script Analysis Workflow

# 剧本分析流程


## Workflow Purpose


本Workflow负责：

对输入剧本进行系统分析。


目标：

理解故事内容。

提取人物关系。

识别剧情结构。

发现后续制作所需的视觉信息。


本阶段属于前期分析阶段。

不进行正式资产制作。



---

# Workflow Position


当前阶段：


STATE-01 Script Analysis



前置阶段：


STATE-00 Project Setup



下一阶段：


STATE-02 Asset Discovery



---

# Input


输入：


- 已是制作剧本
- 粗略剧本或初稿
- 小说、故事梗概、品牌文案、历史事件、影视桥段、长篇素材或概念
- 用户明确的改写许可、禁止改写要求或局部优化范围



读取：


project_bible.md


project_status.md



---

# Script Adaptation And Optimization Gate

本Gate是STATE-01内部子流程，不创建新STATE。除No Revision / Final Script例外外，所有新输入的固定入口为：

`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`

首次调用只完成诊断、报告与询问。任何Adaptation Draft、改写后的剧本正文、替换台词、Screenwriting Optimization、Directorial Interpretation或Production Script Proposal都必须位于用户明确授权之后。

## 00 Input Classification

Input Class只使用：

- **A — Production Script**：已经具备可供制作分析的场景、行动、对白和叙事结构。
- **B — Rough Script / First Draft**：以剧本为目标，但结构、因果、节奏、台词或可视化可能仍需优化。
- **C — Source Material**：小说、故事梗概、品牌文案、历史事件、影视桥段、长篇素材或概念，尚不是可直接制作的剧本。

同时记录：

- User Revision Intent：`Decision Pending / Optimization Approved / Optimization Rejected / No Revision / Local Optimization`
- Optimization Opportunity Grade：`A 无明显优化必要 / B 有轻度优化空间 / C 有明显结构问题 / Not Applicable`
- Optimization Scope：`Full / 用户指定范围 / None / Pending`
- Protected Creative Locks：核心创意、世界观、角色身份与关系、关键设定、名场面、品牌要求及用户明确不可改内容
- Adaptation Need：`Required / Not Required / Pending / Not Applicable`
- Adaptation Target：目标形式、时长、平台/画幅、受众、单集或系列；未知项写Pending
- Adaptation Intensity：`LEVEL 1 Light Adaptation / LEVEL 2 Structural Adaptation / LEVEL 3 Free Adaptation / Not Applicable / Pending`
- Adapter Load：`short_form_drama_adapter / Not Applicable / Pending`
- Current Script Status：`Source Material / Adaptation Draft / Optimized Proposal / Production-Locked`

Input Class与Optimization Opportunity Grade是两个独立维度。分类必须以用户明确语言和当前可读项目事实为依据；报告档位必须以制作适配程度和问题影响为依据。冲突指令按用户最新、最具体且修改范围最小的明确要求执行。不得把用户原文仅因完整、可分析或被诊断为A档就静默标记为Production-Locked。

## 01 Route LOCK — No Revision / Final Script

触发：用户明确说“不要改剧本”“严格按这个版本制作”“已定稿”或同义表达。

本分支优先于默认入口和A/B/C内容改写路由：

1. Optimization Opportunity Report记录为Not Applicable；将`knowledge/script_adaptation.md`、`knowledge/adaptation/short_form_drama_adapter.md`、`knowledge/screenwriting_optimization.md`和`knowledge/directorial_interpretation.md`记录为Not Applicable，理由为用户禁止内容改写。
2. 不执行Script Adaptation、Screenwriting Optimization或Directorial Interpretation，不生成改写版Production Script Proposal。
3. 仍完整执行下方Story、Character、Environment、Visual Element与Visual Requirement Analysis。
4. 用户的明确No Revision / Final Script指令构成锁定授权；分析完成后将用户版本登记为`Script Status: Production-Locked`。
5. 原有Completion Gate通过后进入STATE-02。

分析中可以指出执行风险或事实歧义，但不得以“优化”为名改写内容。真正无法支持后续制作的矛盾写入Pending Decision；不得静默修复。

## 02 Default Entry — Diagnosis Before Authorization

Route LOCK未触发时，对Class A、B、C统一执行本入口。登记`Script Status: Source Material`、`State Status: IN_PROGRESS`并锁定Protected Creative Locks。

### Required Diagnosis Dimensions

Optimization Opportunity Report至少逐项检查并给出结论：

1. 开场钩子
2. 核心冲突进入时机
3. 信息重复
4. 台词效率
5. 动作可视化
6. 人物记忆点
7. 节奏
8. 高潮力度
9. 情绪价值
10. 结尾Hook
11. 时长适配
12. 场景/人物复杂度

Class C还必须先判断`Adaptation Need`，指出素材离标准制作剧本的距离、需要改编的原因和方向；此时不得执行Adaptation Target Detection的改写决策、不得选择实际改编内容，也不得生成Adaptation Draft。Input Class为C通常至少为B档；只有确认输入本身已经可直接作为制作剧本时，才应重新归为Class A而不是把Class C评为A档。

### Optimization Opportunity Report Contract

每个存在问题的维度只写：

`问题 → 影响 → 可优化方向`

已成立项可以简述其为何适合制作。不得输出任何改写后的剧本正文、替换台词、重写场景、具体新增情节、Adaptation Draft、Screenwriting Optimization结果、Directorial Interpretation结果或Production Script Proposal。报告的方向只能说明处理策略，例如删减重复、提前冲突、强化动作表达；不得实际代写。

### Three-Level Decision

- **A 无明显优化必要**：不存在会显著影响理解、情绪或制作执行的问题，仅有可忽略的润色空间。告诉用户当前剧本已基本适合制作，并询问是否直接锁定进入下一阶段。
- **B 有轻度优化空间**：问题可通过局部删减、合并、提前、台词压缩、动作化或节奏微调解决，不需重构核心因果。列出具体轻度优化点，并询问是否执行轻度优化。
- **C 有明显结构问题**：核心目标、冲突、因果、高潮、情绪兑现、形式转换或时长容量存在跨段落问题，需要结构重排或Class C Adaptation。列出结构问题、影响与建议方向，并询问是否进入结构优化。

报告输出后必须停止：

- A档：`Pending Decision: 是否直接锁定当前剧本并进入STATE-02`
- B档：`Pending Decision: 是否执行轻度优化`
- C档：`Pending Decision: 是否进入结构优化`

此时统一保持`Script Status: Source Material`、STATE-01 `IN_PROGRESS`、`Next Workflow: 02_script_analysis_workflow.md`。

## 03 User Decision Gate

### A档直接锁定授权

只有用户明确同意“直接锁定”“按当前版本进入下一阶段”或无歧义同义表达，才完成原有Script Analysis、将原版本写为`Production-Locked`并进入STATE-02。用户未明确答复时继续等待。

### B/C档优化授权

只有用户明确表示“优化”“继续优化”“进入优化”“执行轻度优化”“进入结构优化”或无歧义同义表达，才写`User Revision Intent: Optimization Approved`并进入内容改写。单独的“继续”“下一步”“好的”或沉默不得推定为优化授权，仍停在Decision Gate。

### 拒绝优化或改编

用户明确表示“不优化”“不要优化”“保留原稿”“不改编”或无歧义同义表达时：

1. 写`User Revision Intent: Optimization Rejected`。
2. 不执行Script Adaptation、Screenwriting Optimization或Directorial Interpretation，不生成Production Script Proposal。
3. 完成原有Script Analysis；对Class C也保留用户原始输入，不把它自动改编成标准剧本。
4. 将用户原始版本原样登记为`Script Status: Production-Locked`，把报告风险保留为制作注意项。
5. Completion Gate通过后进入STATE-02。

## 04 Class C Approved Route — Adaptation Before Optimization

触发：Input Class为C、报告已输出、用户已明确同意优化/改编，且Route LOCK未触发。

执行顺序固定为：

`Source Material → Adaptation Target Detection → Script Adaptation → Adaptation Draft → Screenwriting Optimization → Directorial Interpretation → Production Script Proposal → User Confirmation → Production-Locked Script`

必须读取：

- `knowledge/script_adaptation.md`
- `knowledge/screenwriting_optimization.md`
- `knowledge/directorial_interpretation.md`

### Adaptation Target Detection

从用户要求与已确认项目事实判断目标形式。只有目标明确为短剧、竖屏剧情或1—3分钟剧情视频时，才读取并执行`knowledge/adaptation/short_form_drama_adapter.md`。其他类型将该Adapter记录为Not Applicable及理由，不得强制套用前3秒、前30秒或五段短剧模型。目标缺失且会实质改变改编结构时，写`Adapter Load: Pending`与Pending Decision，不得猜测平台规则。

### Adaptation Intensity Selection

- LEVEL 1 Light Adaptation：保留原结构，主要压缩、视觉化与台词优化。
- LEVEL 2 Structural Adaptation：允许合并人物、重排事件、提前冲突与强化高潮。
- LEVEL 3 Free Adaptation：保留核心人物、主题与名场面，可重构短视频故事。

选择用户要求和素材状态所需的最低足够等级，并保存选择依据。用户明确“基本不要改剧情”时只能LEVEL 1；若无法满足目标，保持Pending并请求决定，不得自动升级。

### Class C Execution

1. 按`knowledge/script_adaptation.md`完成Source Essence Extraction、Adaptation Objective、Preserve / Compress / Rewrite / Remove Decision、Screen Translation、Duration & Dramatic Restructuring和Adaptation Fidelity Check。
2. 形成完整Adaptation Draft并写`Script Status: Adaptation Draft`；该状态仍是STATE-01 IN_PROGRESS，不得进入STATE-02。
3. 对Adaptation Draft执行Screenwriting Optimization。
4. 执行Directorial Interpretation，把优化结果转换为可视、可听、可表演的制作版叙事；不得创建SHOT、CLIP、焦段、机位、运镜或Director Decision Notes。
5. 使用`templates/02_script_analysis_prompt.md`输出完整Production Script Proposal及其Script Analysis。
6. 写`Script Status: Optimized Proposal`、`State Status: IN_PROGRESS`、`Pending Decision: 等待用户确认Production Script Proposal`，并停止；不得进入STATE-02。

## 05 Class A/B Approved Route — Optimization Without Forced Adaptation

触发：Class A或B的报告已输出，且用户已明确同意优化。不得读取`knowledge/script_adaptation.md`或短剧Adapter，不形成Adaptation Draft。即使目标时长为1—3分钟，也不得仅因此把A/B类强制改走Script Adaptation。

固定执行：

`Screenwriting Optimization → Directorial Interpretation → Production Script Proposal → User Confirmation`

必须读取`knowledge/screenwriting_optimization.md`与`knowledge/directorial_interpretation.md`：

1. 只在已授权范围内执行Screenwriting Optimization。
2. 执行Directorial Interpretation，不提前进入后续技术层。
3. 使用Template输出Production Script Proposal与Script Analysis。
4. 写`Script Status: Optimized Proposal`、`State Status: IN_PROGRESS`、`Pending Decision: 等待用户确认Production Script Proposal`，并停止。

### Local Optimization Scope Lock

用户只要求局部优化时：

- 只允许修改明确指定的场、段落、人物线、台词、节奏问题或其他范围。
- 范围外内容保持原文事实与语义，不顺手润色、重排或补设定。
- 为解决局部因果而确需影响相邻内容时，先把影响列为Pending Decision，不得自动扩大范围。
- Proposal必须标明修改范围、未修改范围与必要的相邻影响。

## 06 Production Script Proposal Confirmation Gate

- Production Script Proposal输出后必须再次停止，保持`Script Status: Optimized Proposal`、STATE-01 `IN_PROGRESS`与`Next Workflow: 02_script_analysis_workflow.md`。
- 用户明确确认当前Proposal：把唯一确认版本写为`Script Status: Production-Locked`，清除Pending Decision，再执行STATE-01 Completion Gate并进入STATE-02。
- 用户要求修改Proposal：保持`Optimized Proposal + IN_PROGRESS`，只修订用户指出范围，输出新Proposal Revision并再次等待确认。
- 用户只说“继续”“下一步”“好的”但没有明确确认提案：不得推定同意；仍停在Proposal Confirmation Gate。


---

# Script Analysis Process


## 01 Story Structure Analysis


分析：


- 故事主题
- 核心冲突
- 剧情结构
- 主要事件节点
- 叙事节奏



输出：


Story Analysis。



---

# 02 Character Analysis


分析：


- 主要人物
- 人物关系
- 人物目标
- 人物变化
- 人物剧情作用



输出：


Character List。



格式：


角色名称：


身份：


关系：


剧情作用：


人物变化：



说明：


本阶段只进行人物识别与分析。


不生成角色资产。


---

# 03 Environment Analysis


分析：


- 故事发生地点
- 时间背景
- 空间关系
- 主要环境类型



输出：


Environment List。



格式：


环境名称：


出现位置：


剧情作用：


空间特点：



说明：


本阶段只识别故事环境。


不制作环境资产。



---

# 04 Important Visual Element Analysis


分析：


- 关键物件
- 剧情推动元素
- 象征性物品
- 重要视觉元素



输出：


Visual Element List。



格式：


名称：


出现位置：


剧情作用：


重要程度：



说明：


本阶段只识别剧情中的重要视觉元素。


后续由 Asset Discovery 判断是否需要制作正式资产。



---

# 05 Visual Requirement Analysis


提取：


- 时代背景
- 地域特点
- 文化元素
- 整体氛围
- 初步视觉方向



用于：


后续资产发现。

视觉开发。



---

# Output

最终输出必须使用：

templates/02_script_analysis_prompt.md

本Workflow负责分析与边界控制；Template独占字段名称、顺序与排版。

默认首次入口只包含Script Control、Optimization Opportunity Report与User Decision Gate，并在询问后停止，不得输出改写正文、Adaptation Draft或Production Script Proposal。Class C在明确授权后的Adaptation分支必须包含Script Control、Source Essence、Adaptation Decision、Adaptation Draft、Adaptation Fidelity Check、Screenwriting Optimization Summary、Directorial Interpretation Summary、Production Script Proposal与Proposal Confirmation Checkpoint；Class A/B明确授权后的Optimization分支不输出改编栏目。Optimization Rejected与Route LOCK不输出改写Proposal，但必须包含Script Control、原有Script Analysis与Lock / Handoff结论。


输出：


## Story Analysis


故事分析结果。



## Character List


人物列表。



## Environment List


环境列表。



## Visual Element List


重要视觉元素列表。



## Visual Requirement


视觉需求信息。



---

# Forbidden Actions


当前阶段禁止：


禁止生成角色资产。


禁止生成环境资产。


禁止生成道具资产。


禁止输出角色设计稿。


禁止输出环境设计稿。


禁止设计镜头。


禁止生成Storyboard。


禁止生成Video Prompt。



---

# Completion Condition


完成：


- 故事结构分析
- 人物关系整理
- 环境信息整理
- 视觉元素识别
- 视觉需求整理
- Script Status已经是Production-Locked


未完成情况：

- `Script Status: Source Material`：STATE-01保持IN_PROGRESS，等待Optimization Opportunity Report对应的锁定、优化、改编或拒绝决定。
- `Script Status: Adaptation Draft`：STATE-01保持IN_PROGRESS，继续编剧优化与导演化处理，不得进入STATE-02。
- `Script Status: Optimized Proposal`：STATE-01保持IN_PROGRESS，等待用户明确确认Production Script Proposal。
- 任一未完成情况都不得把STATE-01写为COMPLETE，不得进入STATE-02。


更新：


project_status.md

状态读取与保存必须使用`references/project_state_contract.md`选出的State Source；普通Chat本机Root不可读时自动使用Portable State。

并服从references/project_state_contract.md，记录State Status、Checkpoint、Active Artifact与Revision ID；随后按环境同步或输出更新后的完整Portable State，并执行其`Portable Required Field Writeback`。



状态：


STATE-01 Complete

仅当：

`Script Status: Production-Locked`。



---

# Next Workflow


进入：


03_asset_discovery_workflow.md

如果Script Status不是Production-Locked，Next Workflow继续写`02_script_analysis_workflow.md`。



---

# Core Rule


Script Analysis解决：


“这个故事讲什么？”


“故事中有哪些人物、地点和重要元素？”


Asset Discovery解决：


“哪些内容需要制作成正式视觉资产？”


两个阶段必须保持边界。
