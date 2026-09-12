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
