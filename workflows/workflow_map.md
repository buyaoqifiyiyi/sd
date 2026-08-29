# Workflow Map

# SD Film 工作流索引


## Purpose

本文件用于快速查看SD Film影视生产流程。

用于：

- Workflow路由
- STATE识别
- 前后阶段关系确认
- 辅助Workflow调用

具体执行规则：

以对应Workflow文件和rules为准。


---

# Core Production Pipeline

SD Film主生产流程固定为：

STATE-00 Project Setup

↓

STATE-01 Script Analysis

↓

STATE-02 Asset Discovery

↓

STATE-03 Asset Development

↓

STATE-04 Visual Development

↓

STATE-05 Scene Breakdown

↓

STATE-06 Detailed Shot Design

↓

STATE-07 Clip Production

↓

STATE-08 Clip-based Video Prompt / Video Generation

↓

STATE-09 Review


Editing不作为独立STATE插入主Pipeline。


---

# STATE-00

## Project Setup

对应Workflow：

01_project_setup_workflow.md


输入：

用户项目素材。


可以包括：

- 剧本
- 小说
- 故事大纲
- 剧情文本
- 世界观
- 项目设定


输出：

项目初始化信息。


主要更新：

- project_manifest.json
- project_bible.md
- asset_registry.md
- project_status.md


完成后进入：

STATE-01 Script Analysis。


---

# STATE-01

## Script Analysis

对应Workflow：

02_script_analysis_workflow.md


输入：

项目初始化信息。

用户原始故事素材。


输出：

剧本分析结果。

除用户明确“不要改剧本 / 严格按这个版本制作 / 已定稿”外，入口固定执行`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`。报告只指出问题、影响和方向，并以A无明显优化必要、B有轻度优化空间、C有明显结构问题三档询问用户；不得自动改写。用户明确同意优化后，Class C才经Script Adaptation形成Adaptation Draft再进入优化；A/B直接进入优化且不强制改编。Production Script Proposal输出后再次等待确认。全部子流程仍属于STATE-01，不新增STATE。

只有Class C已获改编/优化授权，且目标为短剧、竖屏剧情或1—3分钟剧情视频时加载Short-form Drama Adapter；其他类型不强制套用短剧规则。用户拒绝优化时原稿锁定；用户明确锁定剧本时跳过机会报告、改编和改写，只完成Script Analysis。


包括：

- 剧情结构
- 人物
- 环境
- 道具
- 重要视觉信息


完成后进入：

STATE-02 Asset Discovery。

进入条件：

`Script Status: Production-Locked`。`Source Material`、`Adaptation Draft`或`Optimized Proposal`均不得推进；用户明确要求不改或已定稿时，原版本完成分析后可以直接锁定。


---

# STATE-02

## Asset Discovery

对应Workflow：

03_asset_discovery_workflow.md


输入：

剧本分析结果。


输出：

资产需求清单。


识别：

- Character Asset
- Environment Asset
- Prop Asset
- 必要FX Asset


完成后进入：

STATE-03 Asset Development。


---

# STATE-03

## Asset Development

STATE-03由多个资产Workflow共同组成。


根据Asset Discovery结果：

按实际需要调用。

每个视觉资产统一执行且不得合并确认Gate：

`Asset Design → Image Prompt Generation → 用户确认提示词 → Image Generation → 用户确认图片 → Asset Registry`

只有图片确认后才能成为Active / Canonical / confirmed asset；工具不可用时停在完整Prompt与确认Checkpoint，STATE-03保持IN_PROGRESS。


---

## Character Asset

对应Workflow：

04_character_asset_workflow.md


输入：

角色资产需求。


输出：

已确认Character Visual Asset；至少包含角色定义、已确认三视图Prompt、已确认面部特写Prompt、必要状态变体Prompt与经确认的Canonical角色图片。角色声音资产不属于本Workflow的默认输出；只有用户显式请求时才由独立`AUDIO / SEED-AUDIO Voice Asset`模块处理。


---

## Environment Asset

对应Workflow：

05_environment_asset_workflow.md


输入：

环境资产需求。


输出：

已确认Environment Asset；至少包含环境定义、已确认主参考图Prompt、必要多视角/关键区域Prompt与经确认的Canonical环境图片。


---

## Prop Asset

对应Workflow：

06_prop_asset_workflow.md


输入：

道具资产需求。


输出：

已确认Prop Asset；至少包含道具定义、已确认主参考图Prompt、必要状态/细节Prompt与经确认的Canonical道具图片。


---

## FX Asset

对应辅助Workflow：

15_fx_asset_workflow.md

输入：

需要复用、绑定或跨镜头追踪的效果资产需求。

输出：

已确认FX Asset及连续性合同。

无正式FX需求时：

在Asset Discovery中明确不适用，或保留为Inline Effect。

---

STATE-03完成条件：

当前项目需要的Character、Environment、Prop与FX核心视觉资产均达到`Visual Production Status: Asset Confirmed`并处于Active，或对应类别明确确认无需建立。


完成后进入：

STATE-04 Visual Development。


---

# STATE-04

## Visual Development

对应Workflow：

07_visual_development_workflow.md


输入：

- Script Analysis
- 已确认Character Asset
- 已确认Environment Asset
- 已确认Prop Asset
- 已确认FX Asset（如适用）
- 用户视觉要求
- Visual Style Reference


输出：

统一Visual Direction。


包括：

- Visual Concept
- Cinematography
- Camera Language Direction
- Lighting
- Color
- Environment Treatment
- Texture
- Emotion
- Performance Direction
- Sound Direction
- 必要Cinematic Parameters


完成后进入：

STATE-05 Scene Breakdown。


---

# STATE-05

## Scene Breakdown

对应Workflow：

08_scene_breakdown_workflow.md


输入：

- 剧情信息
- Visual Direction
- 已确认资产


输出：

Scene Breakdown。

用户原剧本中的“镜头1 / Scene 1 / 段落A / Clip A”只作为Source Script Label追溯；STATE-05不得创建SHOT或CLIP ID。


负责：

把剧情组织成可进行镜头设计的场景结构。


条件性辅助Workflow：

16_sequence_planning_workflow.md


触发于：

- 多Scene连续段
- 密集Coverage需求
- 多Generation Unit
- 蒙太奇、追逐、战斗、群戏、复杂对白或复杂FX链


输出：

Sequence Plan，包含SEQ、BEAT、COV、UNIT与State Ledger。


条件性辅助Workflow：

17_poster_design_workflow.md


触发于：

- 用户明确请求电影海报、Key Art、One-sheet、先导/正式/角色海报、Poster Prompt或标题字
- 已确认影片事实、核心资产与Visual Direction足以支持海报设计


输出：

Poster Design Package，写入Active Project Root的`poster_design/`目录。

所属位置：STATE-04 Visual Development辅助，不创建主STATE，不修改STATE-08 Schema。


简单项目：

记录Sequence Planning Not Applicable及理由。


完成后进入：

STATE-06 Detailed Shot Design。


---

# STATE-06

## Detailed Shot Design

对应Workflow：

09_shot_design_workflow.md


输入：

- Scene Breakdown
- Sequence Plan或Not Applicable记录
- Visual Direction
- Character Asset
- Environment Asset
- Prop Asset
- FX Asset或Inline Effect（如适用）
- Camera Language Knowledge
- Performance Knowledge（如适用）
- Sound Language Knowledge（如适用）
- FX Knowledge（如适用）
- Sequence Knowledge与Coverage Requirements（如适用）


输出：

Professional Detailed Shot Script（专业详细分镜脚本）。

正式SHOT由STATE-06重新创建；不得沿用Source Script Label作为正式镜号，也不得在本阶段预划Clip。


每个正式Shot按`templates/08_shot_design_prompt.md`固定输出：镜号、TC IN、TC OUT、时长(s)、景别、焦段、场景/美术、画面内容/构图、人物动作、摄影机/镜头、摄影参数、镜头调度、光线/色彩、画面特效/转场、台词/旁白/口播、音效/BGM、AI制作备注、素材/资产。

其中镜头调度必须完整表达摄影机运动、人物调度、两者配合/触发与镜头结束状态；画面内容/构图必须建立前中后景与主体位置、遮挡/反射/景深等层次；光线/色彩必须说明叙事功能与起止色光状态。


注意：

STATE-06字段属于镜头设计生产信息。内部Director Decision Notes读取该专业分镜，但不新增STATE、不改变表头，也不随正式输出暴露。

不得直接作为STATE-08最终Seedance Prompt Schema。


完成后进入：

STATE-07 Clip Production。


---

# STATE-07

## Clip Production

对应Workflow：

10_clip_production_workflow.md


输入：

- Confirmed Detailed Shot Design
- 实际可读的Detailed Shot Design Artifact / Portable Checkpoint及匹配Revision
- Sequence Plan（如适用）
- 已确认资产
- Visual Direction


输出：

Confirmed Clip Production Plan；把正式 Shot 按场景、时间、动作、摄影机、空间、道具、模型复杂度与4—15秒生成窗口组织为 CLIP-001、CLIP-002……。


每个 Clip 必须确认：

- 包含哪些 Shot 及其原顺序
- 起始状态与连续动作
- 人物/环境空间关系、轴线、视线与行进方向
- 摄影机/构图/焦段/对焦执行路径
- 道具身份、持有者、位置、方向与状态连续性
- 结尾状态、稳定尾帧与下一Clip Handoff
- 模型执行风险、降级与可复算4—15秒时长


完成后进入：

STATE-08 Clip-based Video Prompt / Video Generation。

Template：`templates/20_clip_plan.md`。

Shot 是导演镜头设计单位；Clip 是 AI 视频生成执行单位。Storyboard 仅为用户明确请求时调用的 Optional/Auxiliary Workflow，不绑定 STATE，也不参与本阶段完成门槛。

Source Script Label、SCENE、BEAT、COV与UNIT均不得直接改名或一对一映射为CLIP；UNIT不是Clip。缺少Confirmed Detailed Shot Design Artifact、匹配Revision、STATE-06 Complete证据或完整正式SHOT清单时，不得创建任何暂定或正式CLIP ID。


---

# STATE-08

## Clip-based Video Prompt / Video Generation

对应Workflow：

11_video_generation_workflow.md


输入：

- Confirmed Detailed Shot Design
- Confirmed Clip Production Plan
- Sequence Plan（如适用）
- Character Asset
- Environment Asset
- Prop Asset
- FX Asset或Inline Effect（如适用）
- Visual Direction
- Camera Language
- Performance Direction
- Sound Direction
- Continuity Information


执行辅助：

knowledge/11_seedance_adapter.md

knowledge/performance/（有人物表演时）

knowledge/sound_language/（存在声音设计时）

knowledge/fx/（存在FX时）

knowledge/sequence/（存在Sequence Plan时）


最终输出格式：

templates/10_video_prompt.md


输出：

Seedance Video Prompt。


STATE-08负责：

将已经确认的影视生产设计转换为AI视频模型可执行的信息。


不得：

重新设计角色。

重新设计环境。

无原因改变剧情。

直接继承STATE-06的字段格式作为最终Prompt Schema。


完成后进入：

STATE-09 Review。


---

# STATE-09

## Review

对应Workflow：

13_review_workflow.md


输入：

- AI生成结果
- Project Bible
- Asset Registry
- Shot Design
- Sequence Plan与Coverage Matrix（如适用）
- Visual Direction
- Continuity Information


输出：

Review Report。


审核：

- Character Consistency
- Environment Consistency
- Prop Consistency
- FX Continuity
- Performance
- Dialogue / Lip-sync
- Sound Continuity
- Coverage Completion
- Generation Unit Handoff
- Motion
- Camera
- Visual Style


审核结果：

PASS

REVISE

REBUILD


---

## PASS

当前结果符合项目要求。

STATE-09完成。


更新：

project_status.md


状态：

STATE-09 Complete。


---

## REVISE

存在可修复问题。

根据问题类型：

返回对应Workflow。


例如：

人物问题

→ Character Asset Workflow


环境问题

→ Environment Asset Workflow


道具问题

→ Prop Asset Workflow


镜头或动作问题

→ Shot Design Workflow


视频执行层局部调整

→ Editing Workflow


修改完成后：

重新进入STATE-09 Review。


---

## REBUILD

存在严重问题。

返回：

对应资产阶段

或

Shot Design阶段。


重新执行相关生产步骤后：

再次进入后续流程。


最终必须：

重新Review。


---

# Auxiliary Workflow

以下Workflow不占用固定STATE。

它们属于：

按需辅助流程。

---

# AUDIO / SEED-AUDIO Voice Asset Workflow

对应：

20_seed_audio_voice_asset_workflow.md

路由器：`workflows/audio_router.md`

定位：仅在用户显式请求音色提示词、音色制作、角色声音、Seed Audio、配音音色、声音资产、Voice Profile或角色音色样本Prompt时调用的独立辅助模块。

唯一输出Template：

templates/21_seed_audio_voice_asset.md

显式不触发：普通视频制作、角色分析、Character Asset、Detailed Shot Design、Clip Production、STATE-08 Seedance提示词，以及“继续视频制作 / 下一个Clip / 下一步 / 继续 / 下一个”。角色有对白或下游缺少Voice Profile都不能自动触发。

该模块不创建新STATE；完成后返回调用前Checkpoint。没有显式音色请求时直接按原Workflow Map路由，不生成任何音色资产。

---

# Project Resume And Retry Workflow

对应：

18_project_resume_workflow.md

定位：中断恢复、Review退回、生成重试与Checkpoint验证。

它不创建新STATE，不选择最近项目，不重写已接受产物。


---

# Sequence Planning Workflow

对应：

16_sequence_planning_workflow.md


定位：

STATE-05中Scene Breakdown与STATE-06 Detailed Shot Design之间的条件性长序列、Coverage和Generation Unit规划。


它不创建新STATE，也不创建SHOT ID。


触发时必须在STATE-06前完成；不触发时必须记录Not Applicable理由。


---

# Editing Workflow

对应：

12_editing_workflow.md


定位：

已有AI视频结果的局部修改与优化。


触发条件：

用户明确要求：

- 修改视频
- 延长镜头
- 改变动作
- 改变摄影
- 调整视觉
- 修复局部一致性


或：

Review判断当前问题可以通过局部视频调整解决。


Editing负责：

- Motion Adjustment
- Camera Adjustment
- Visual Adjustment
- Continuity Adjustment


Editing原则：

保持原镜头。

优先局部修改。

避免无必要重新生成完全不同内容。


Editing不是：

新的固定STATE。


Editing完成后：

必须重新进入：

STATE-09 Review


确认修改结果。


---

# Series Management Workflow

对应：

14_series_management_workflow.md


定位：

系列项目、连续剧集或多集内容管理。


它不替代：

单集内部Production Pipeline。


系列项目中的每一个制作单元：

仍然按照：

STATE-00

↓

STATE-01

↓

STATE-02

↓

STATE-03

↓

STATE-04

↓

STATE-05

↓

STATE-06

↓

STATE-07

↓

STATE-08

↓

STATE-09


执行。


Series Management主要负责：

跨项目或跨集管理。


---

# Workflow Routing Principle

先读取并执行`workflows/audio_router.md`中的`AUDIO / SEED-AUDIO Explicit Trigger Gate`：

- 当前用户请求明确要求音色提示词、音色制作、角色声音、Seed Audio、配音音色、声音资产、Voice Profile或同义角色声音身份制作时，声音资产部分优先进入`20_seed_audio_voice_asset_workflow.md`，严格使用`templates/21_seed_audio_voice_asset.md`。该辅助模块不要求先推进主Pipeline。
- 未显式命中时，AUDIO模块优先级为零；不得因对白存在、角色分析、Clip/Seedance请求或声音资产缺失而自动调用。
- 同一请求同时显式要求视频与音色资产时分别路由、分别输出，不混合Template。

未进入独立AUDIO模块的影视生产任务再选择State Source：

`可访问且Project ID一致的Active Project Root/project_status.md > portable_project_status.md > 当前可验证Project Context（先规范化为Portable State） > 无项目证据时初始化STATE-00 Project Setup`。

当用户输入“调用SD”、“重新调用SD”、“重新加载SD”、“按当前Skill继续”或无歧义同义表达时，必须在AUDIO Router与State Source选择前执行`SKILL.md`的Runtime Skill Reload Gate，重读当前安装入口并取得Skill Version / Build ID。未触发Reload时使用当前激活的instructions。本机Skill目录、Project Root或Registry不可读时直接进入下一可用来源，不得停止、报错、写入`BLOCKED`或要求用户重新提供路径。Work/Codex中的Active Project Root仍是本地交付物的持久化目标。


然后：

根据当前STATE调用对应Workflow。


禁止：

仅根据用户关键词直接跳到后期Workflow。


用户请求：

代表最终目标。


不代表：

当前执行阶段。


---

# Main Workflow Table

| STATE | Stage | Workflow |
|---|---|---|
| STATE-00 | Project Setup | 01_project_setup_workflow.md |
| STATE-01 | Script Analysis | 02_script_analysis_workflow.md |
| STATE-02 | Asset Discovery | 03_asset_discovery_workflow.md |
| STATE-03 | Asset Development | 04 / 05 / 06 Asset Workflows |
| STATE-04 | Visual Development | 07_visual_development_workflow.md |
| STATE-05 | Scene Breakdown | 08_scene_breakdown_workflow.md |
| STATE-06 | Detailed Shot Design | 09_shot_design_workflow.md |
| STATE-07 | Clip Production | 10_clip_production_workflow.md |
| STATE-08 | Clip-based Video Prompt / Video Generation | 11_video_generation_workflow.md |
| STATE-09 | Review | 13_review_workflow.md |


辅助Workflow：

12_editing_workflow.md

14_series_management_workflow.md

15_fx_asset_workflow.md

16_sequence_planning_workflow.md

17_poster_design_workflow.md

18_project_resume_workflow.md

20_seed_audio_voice_asset_workflow.md（仅用户显式请求角色音色资产时调用；不绑定STATE）

10_storyboard_workflow.md（仅用户明确请求时调用的 Optional/Auxiliary Storyboard，不绑定 STATE）

10_shot_execution_plan_workflow.md、19_clip_planning_workflow.md（仅旧项目兼容，不参与新项目路由）


它们不创建新的主Pipeline STATE。


---

# Correct Main Flow

正确：

Project Setup

↓

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

Detailed Shot Design

↓

Clip Production

↓

Clip-based Video Prompt / Video Generation

↓

Review


---

# Revision Loop

生成结果存在问题时：

Clip-based Video Prompt / Video Generation

↓

Review

↓

定位问题

↓

对应Workflow修复

↓

必要时Editing

↓

重新生成或修改

↓

Review


Review是：

质量闭环入口。


Editing是：

修复工具。


不得把二者的职责混淆。


---

# Final Principle

Workflow Map只负责：

描述SD Film阶段关系与Workflow路由。


主Pipeline固定结束于：

STATE-09 Review。


12_editing_workflow.md：

是按需修复Workflow。

不是STATE-09。


13_review_workflow.md：

才对应：

STATE-09 Review。


所有Workflow执行前：

优先检查：

references/project_workspace.md。

按优先级选择State Source。运行环境确实提供本地文件访问时先尝试解析Active Project Root并读取身份一致的project_status.md；Root不可用时读取Portable State；两者都不可用时先从当前可验证Project Context重建Portable State；无项目证据时才初始化STATE-00。历史聊天中的Skill描述不得作为State Source。
