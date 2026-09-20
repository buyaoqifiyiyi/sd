# Project Start Template

# AI影视项目启动模板


## Project Status


项目状态：

STATE-00 Project Setup



---

# Project Information


项目名称：




项目类型：


□ 短剧

□ 电影

□ 系列剧

□ 动画



---

# Input Material


输入类型：


□ Idea / Brief / Concept

□ 品牌需求

□ 完整剧本

□ 粗略剧本 / 初稿

□ 剧情大纲

□ 小说章节

□ 人物设定

□ 世界观设定



输入内容摘要：


Script Entry Route：

□ Creation Brief → STATE-01 Screenplay Generation branch

□ Existing Script / Material → STATE-01 Script Diagnosis branch




---

# Client Brief｜客户与商业 brief（条件节）

`# Input Material`已勾选`品牌需求`且内容已给出时填写本节；普通叙事项目整节省略，写`Not Applicable`。本节记录**客户侧事实**，用户未提供时保持空白并进入`Pending`，**不得由制作推断、补写或"按常识填"**。

**填本节前先判定`交付语境`，它是本节其余各项的适用前提**：

- **交付语境**：`self_initiated`（自制，用户即出品方）/ `client_commissioned`（委托，存在外部委托方）/ `Pending`
- **判定依据**：是否存在外部委托方要求本片、是否由其提供诉求与商业事实、是否由其终审

| 交付语境 | 品牌诉求 | 本节填写规则 |
|---|---|---|
| `self_initiated` | 无 | **整节写`Not Applicable`、一个字段都不填**（含业务目标与主传达目标）；按通用编剧判据推进，不触发商业事实门 |
| `self_initiated` | 有（自有品牌 / 自有产品） | 本节**只填**业务目标、主传达目标、商业形态、产品与品牌调性、受众与决策链、交付物与规格、**自有品牌事实**（功效 / 价格 / 资质 / 免责表述，由用户以品牌方身份提供）与预算内修改轮次；`客户与委托关系`写`自有品牌`，`审批链`写`用户（品牌方）` |
| `client_commissioned` | 有 | 本节各项全部适用，包括外部审批链 |

**商业事实的来源纪律按交付语境解释**：`client_commissioned`时"必须由客户提供或确认"指外部委托方；`self_initiated`时指**用户以品牌方身份**提供或确认。两种语境下制作都不得推断、不得用近似物替代、不得把未确认的事实写成模型生成承诺。

- 客户与委托关系：
- 业务目标与主传达目标（多个卖点时必须排出**一个**第一注意目标，其余明确降级或不做）：
- 商业形态：`宣传` / `科普` / `产品` / `案例` / `招商` / `雇主品牌`
- 产品与品牌调性：
- 受众与决策链角色：
- 交付物与规格：条数 / 版本 / 画幅 / 时长 / 是否含字幕与落版。**客户通常不规定参数**：客户未指定时由制作按目标形式与已提供平台**提议**并标注`制作建议｜待确认`，写入后在STATE-01 `Production Setup Gate`随媒介与目标形式一并确认；**不得留空，也不得静默采用**。制作提议的是交付参数（条数与时长区间、画幅、字幕与落版有无）；平台的推荐机制、时长上限、审核与尺寸数值属外部事实，仍必须由用户提供或引用可核对来源——制作不得声称建议值"符合"任何未确认的平台机制
- 审批链：客户方终审人（角色或姓名）；`self_initiated`时写`用户（品牌方）`
- 客户提供的受监管表述原文：资质、功效、价格、免责声明、授权人物或声音
- 预算内修改轮次与范围：

本节的商业事实按`workflows/03_asset_discovery_workflow.md`的`## Commercial Fact Triage｜Conditional Internal`归类；客户方终审人只决定客户侧由谁确认，不改变资产双确认、Production Script Proposal确认与任何Hard Stop。**`self_initiated`时`审批链`是`用户（品牌方）`，不产生第二个确认主体。**

**规格的提议权与事实权分属两个owner，不得混用**：交付参数（条数与时长区间、画幅、字幕与落版）由**制作提议、用户确认**；平台事实（推荐机制、时长上限、审核条文、尺寸数值）与商业事实（价格、SKU、Logo文字、功效与资质、受监管承诺、授权人物或声音）由**用户或客户提供**。制作不得用"行业惯例""平台通常""看起来专业"填补后两类。




---

# Project Initialization


Project Root：


建立项目文件：


□ project_manifest.json


□ project_bible.md


□ asset_registry.md


□ project_status.md

□ execution_ledger.md

□ artifact_registry.md



---

# Initial Production Analysis


## Story Overview


故事简介：




## Genre


类型：




## Era


时代背景：




## Main Location


主要空间：




## Visual Direction


初步视觉方向：

---

# Medium Form

媒介形式（`live_action` 真人 / `3d_animation` 三维 / `2d_anime` 二维；用户未提供时写 `Pending`）：

# Target Form

目标形式（用户未提供时写 `Pending`；值域与确认时点由`workflows/02_script_analysis_workflow.md`的`### Target Form Confirmation`拥有，STATE-00只登记用户已明确输入的值，不询问、不推定）：

□ `短剧`　□ `竖屏剧情`　□ `1—3分钟剧情视频`　□ `电影短片`　□ `儿童动画`　□ `纪实非虚构`　□ `长篇影视`　□ `品牌与商业片`

□ `live_action`（真人 / 实拍）

□ `3d_animation`（三维 / 三渲二 / CG）

□ `2d_anime`（二维 / 漫剧 / 手绘 / 动态漫画）

□ `Pending`（用户未提供；在`Production Setup Gate`询问一次）

确认状态：`UNSELECTED / SELECTED`

说明：STATE-00只登记用户已明确输入的值，未提供时保持`Pending`；确认由STATE-01在剧本`Production-Locked`后与下一节的项目级默认项在**同一张**`Production Setup Proposal`中一次性完成。确认前不得进入STATE-02，也不得生产媒介相关资产——角色资产结构与材质、光学语言按媒介分化（见`templates/04_character_asset_prompt.md`的媒介适用条件与`knowledge/medium_profiles.md`的`Cross-Medium Asset Rule`）；值域与三档分化规则由`knowledge/medium_profiles.md`唯一拥有。

---

# Project Model Preferences

项目图像模型默认项：

□ GPT Image

□ Midjourney

图像交付形态：

□ AUTO（按当前执行环境能力自动路由）

□ DIRECT_IMAGE（直接出图，不再为Prompt单独停一轮）

□ PROMPT_ONLY（只交付Prompt）

项目视频模型偏好：

□ Seedance 2.0（4—15秒，最多9张视觉参考）

□ Seedance 2.5（4—30秒，图片≤30 / 视频≤10 / 音频≤10 / 合计≤50，受当前入口限制）

□ MiniMax H3（4—15秒；全能参考最多9图、3视频、3音频、12文件；Required草图仅All-Reference模式可提交）

确认状态：`UNSELECTED / SELECTED`

说明：此处是项目级默认/偏好，由STATE-01在剧本`Production-Locked`后经`Production Setup Gate`一次性确认；STATE-03直接继承图像默认项；STATE-06后仍按每个Clip的时长、首尾帧、编辑模式和真实参考输入能力复核视频偏好。选择不等于资产图片确认，也不提交外部服务。图像交付形态只决定这一轮交付图片还是交付Prompt：`AUTO`按当前执行环境的真实出图能力路由，未设置时即按`AUTO`，不得用历史推断。




---

# Asset Discovery Preparation


首次资产分析目标：



## Character Assets

正式资产：待STATE-01 Script Analysis与STATE-02 Asset Discovery后分配ID。



---

## Environment Assets

正式资产：待STATE-01 Script Analysis与STATE-02 Asset Discovery后分配ID。



---

## Prop Assets

正式资产：待STATE-01 Script Analysis与STATE-02 Asset Discovery后分配ID。

## FX Assets

正式资产：待STATE-01 Script Analysis与STATE-02 Asset Discovery后决定正式FX Asset、Inline Effect或Not Applicable。



---

# Pipeline Lock


当前阶段：


STATE-00


禁止进入：


Detailed Shot Design


Clip Production


Clip-based Video Prompt / Video Generation



---

# Next Workflow


完成项目初始化后进入：


02_script_analysis_workflow.md
