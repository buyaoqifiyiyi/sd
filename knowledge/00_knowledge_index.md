# Knowledge Index

# SD Film知识库索引


## Purpose


本文件用于说明knowledge目录中各知识文件的适用阶段。

本文件是SD Film Knowledge的唯一总路由入口。`knowledge/index.md`与旧版顶层知识文件只作为兼容指针，不得建立第二套路由。

每次加载遵循：Required始终读取；Conditional只在触发条件成立时读取；Not Applicable必须记录理由；禁止为了“全面”无差别加载全部知识。


knowledge用于辅助Workflow执行。


不能替代Workflow。


不能改变Pipeline顺序。



---

# Knowledge Loading Principle


知识加载顺序：


当前Workflow确定

↓

匹配Knowledge

↓

辅助当前阶段任务



禁止：

根据知识库内容直接跳过Workflow阶段。



---

# Knowledge Stage Mapping


## STATE-01 Script Analysis


Required routing：

- 除No Revision / Final Script例外外，先由`workflows/02_script_analysis_workflow.md`固定执行`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`，报告后停止，不加载改写Knowledge。

Conditional — Class C报告Adaptation Need且用户明确同意优化/改编时：

- knowledge/script_adaptation.md

只有Adaptation Target Detection确认目标为短剧、竖屏剧情或1—3分钟剧情视频时，额外加载：

- knowledge/adaptation/short_form_drama_adapter.md

Conditional — Class A/B在报告后获得明确优化授权，或Class C已获授权并形成Adaptation Draft时：

- knowledge/screenwriting_optimization.md
- knowledge/directorial_interpretation.md

用户明确“不要改剧本 / 严格按这个版本制作 / 已定稿”时，跳过Opportunity Report，上述四份Knowledge全部记为Not Applicable；仍执行原有Script Analysis。用户在报告后拒绝优化/改编时同样不加载改写Knowledge，并锁定原稿。


用途：


辅助：

- 故事结构分析
- 人物分析
- 叙事分析
- 首次只形成Optimization Opportunity Report并等待用户决策
- 明确授权后将C类Source Material改编为Adaptation Draft
- 明确授权后形成Production Script Proposal并再次等待用户确认



禁止：

生成镜头。

生成视频Prompt。

在Opportunity Report后自动改写；把Adaptation Draft当作Production Script Proposal；未经用户确认把Optimized Proposal标记为Production-Locked或进入STATE-02。



---

## STATE-02 Asset Discovery


适用知识：


资产拆解相关知识。


用途：


辅助：

- 角色需求识别
- 环境需求识别
- 道具需求识别
- FX需求识别与Inline Effect判定



禁止：

直接制作最终资产。



---

## STATE-03 Asset Development


适用知识：


资产制作规范。

有对白角色追加：

- knowledge/sound_language/voice_generation.md（仅用户显式请求音色提示词、音色制作、角色声音、Seed Audio、配音音色或声音资产时，由AUDIO / SEED-AUDIO Voice Asset模块读取；普通视频/角色/Clip/STATE-08流程不得自动读取）


FX设计与连续性知识：

knowledge/fx/


用途：


辅助：

- 角色设计
- 环境设计
- 道具设计
- 正式FX Asset设计
- 把已确认角色事实转换为可执行的声学Voice Profile与纯人声音色样本Prompt；不把竹雀示例当作全局默认



---

## STATE-04 Visual Development


适用知识：


视觉风格相关知识。

Required / Conditional routing：

- knowledge/visual_styles/index.md（存在导演、影片、类型或综合色觉参考时）
- knowledge/camera_language/index.md（建立项目级摄影方向时）
- knowledge/lighting/index.md（建立光线体系时）
- knowledge/color/index.md（建立综合色彩体系时）


表演与声音方向知识：

- knowledge/performance/
- knowledge/sound_language/
- knowledge/fx/（项目存在效果美学时）


用途：


辅助：

- 美术方向
- 色彩体系
- 光影方向
- 项目级表演尺度
- 项目级声音原则
- 项目级FX表现原则
- 电影海报的视觉母题、构图、字体与分层制作（仅在Poster Design触发时）


海报请求追加：

knowledge/poster_design/



---

## STATE-05 Scene Breakdown


适用知识：


场景设计相关知识。


复杂项目追加：

knowledge/sequence/


用途：


辅助：

- 场景结构
- 空间关系
- Narrative Beat与Coverage Requirement
- Generation Unit与跨单元状态合同



---

## STATE-06 Detailed Shot Design


适用知识：


电影摄影相关知识。

Required：

- knowledge/spatial_blocking_layer.md（每个Scene先执行Spatial Blocking Decision；复杂场景准备Top-down Map + Text Spatial Rules）
- knowledge/camera_language/index.md
- knowledge/transitions/index.md（存在相邻镜头时）

Conditional：

- knowledge/camera_language/movement_combinations/（多运镜、多景别、多视点或一镜到底）
- knowledge/lighting/
- knowledge/color/


按镜头内容追加：

- knowledge/performance/
- knowledge/sound_language/
- knowledge/fx/
- knowledge/sequence/（已建立Sequence Plan时）


用途：


辅助：

- 景别
- 运镜
- 构图
- 摄影语言
- 表演目标与反应顺序
- 声音重点与声音连接
- FX行为与边界状态
- SHOT到COV的覆盖映射



---

## STATE-07 Clip Production


适用知识：


Clip划分、模型执行复杂度、4—15秒时长、段内/跨Clip连续性与Prompt投影规范；禁止把Storyboard视觉材料用作生产输入。

读取STATE-06 Confirmed Detailed Shot Design，并按Shot适用性加载camera、lighting、color、performance与transitions连续性知识；不重新设计上游Shot。


已建立Sequence Plan时追加：

knowledge/sequence/


用途：


主资源：

- knowledge/spatial_blocking_layer.md（读取STATE-06 Confirmed Spatial Blocking Result，不重新设计Blocking）
- knowledge/clip_planning/
- workflows/10_clip_production_workflow.md
- templates/20_clip_plan.md

用于把相邻兼容Shot编排为4—15秒Confirmed Clip Production Plan，并记录包含Shot、起始状态、连续动作、摄影机/空间关系、道具连续性、结尾状态、风险与Handoff。



---

## STATE-08 Clip-based Video Prompt / Video Generation


适用知识：


AI视频模型相关知识。

STATE-08的Required / Conditional Resources权威清单只由`workflows/11_video_generation_workflow.md`拥有。本索引不复制Resource Gate；它只提供以下发现入口，实际读取范围以当前Workflow判定为准：

- Preflight与参考预算：`knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`
- Prompt编译与投影：`knowledge/knowledge_application_reflection.md`、`knowledge/prompt_compilation/`
- 模型适配：`knowledge/11_seedance_adapter.md`
- Clip连续性：`knowledge/clip_planning/`
- 镜头与运镜：`knowledge/camera_language/`
- 转场：`knowledge/transitions/`
- 光色：`knowledge/lighting/`、`knowledge/color/`
- 表演、声音、FX与Sequence：`knowledge/performance/`、`knowledge/sound_language/`、`knowledge/fx/`、`knowledge/sequence/`


用途：


辅助：

- 在每个Clip Prompt编译前扫描Knowledge机会、筛选0—3项高价值策略并转译为现有字段中的可执行语义；默认不向用户输出内部Reflection
- Prompt结构
- 模型适配
- 动作描述
- 可执行表演节拍
- 对白、环境声、动作声、呼吸、Foley、剧情内声源与同期静默；音乐与配乐只属于STATE-09 Editing/Post，不进入STATE-08音效
- FX生命周期、物理交互与跨镜后果
- Sequence顺序、Coverage与UNIT边界继承
- Clip内逐镜状态链、4—15秒生成边界与跨Clip尾帧连接

---

## STATE-09 Review And Editing/Post

Required：

- knowledge/quality/index.md
- knowledge/spatial_blocking_layer.md（执行Spatial Continuity QA）
- knowledge/knowledge_application_reflection.md（只执行Knowledge Application QA，不在Review重做创作选择）
- templates/16_review_report.md

Conditional：

- knowledge/sound_language/music_and_silence.md（仅后期音乐规划）
- knowledge/transitions/
- knowledge/sequence/
- knowledge/fx/

用途：逐镜QA、相邻镜连续性、Prompt评分、Coverage、重试隔离和返回路由。



---

# Restriction


knowledge中的任何内容：

不得触发：

- 跳过前置阶段
- 自动生成后续阶段结果
- 替代Workflow判断



---

# Final Rule


Workflow决定：

现在做什么。


Knowledge决定：

怎么做好。



两者不可混淆。
