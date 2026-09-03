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

## Persistent Screenwriter + Director Modules

所有主STATE按需读取`knowledge/screenplay_development.md`与`knowledge/director_decision_layer.md`。前者是唯一Screenwriter Module / Writer Intelligence Layer owner，维护内部WRITER INTENT PACKET、故事/人物逻辑与Writer → Director Handoff；后者拥有Project / Scene / Shot / Clip四层轻量DIRECTOR INTENT PACKET与跨阶段投影合同。两者均不创建新STATE或用户固定Schema。`knowledge/camera_language/index.md`仍是Director Module下Camera Language Module的唯一owner；具体空间、表演、动作、连续性和Prompt编译继续由既有专业owner执行。

STATE-00只建立Project Director Baseline；STATE-01形成Scene source data；STATE-04建立Visual Dramaturgy；STATE-05形成Beat Map与Scene Camera Strategy；STATE-06具体化Shot与Camera；STATE-07形成Dramatic Execution Unit；STATE-08只翻译；Editing与STATE-09保护和审核意图。

---


## STATE-01 Script Analysis


Required routing：先由`workflows/02_script_analysis_workflow.md`识别`Creation Brief / Existing Script / Material`。

Conditional — Creation Brief且用户明确要求创作剧本：

- knowledge/screenplay_development.md
- knowledge/directorial_interpretation.md

该分支直接执行Screenwriter-led Story Development、Writer → Director Handoff与Directable Screenplay QA，输出Production Script Proposal后等待确认；不对尚不存在的剧本输出Optimization Opportunity Report，也不要求用户先在普通Chat提供完整剧本。

Conditional — Existing Script / Material：

- 除No Revision / Final Script例外外，先执行`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`；没有明确改写授权时报告后停止，不加载改写Knowledge。用户当前已明确“直接优化 / 直接改写 / 按指定范围优化”时，报告后不重复询问同一授权。

Conditional — Class C报告Adaptation Need且用户明确同意优化/改编时：

- knowledge/script_adaptation.md

只有Adaptation Target Detection确认目标为短剧、竖屏剧情或1—3分钟剧情视频时，额外加载：

- knowledge/adaptation/short_form_drama_adapter.md

Conditional — Class A/B在报告后获得明确优化授权，或Class C已获授权并形成Adaptation Draft时：

- knowledge/screenwriting_optimization.md
- knowledge/directorial_interpretation.md

用户明确“不要改剧本 / 严格按这个版本制作 / 已定稿”时，Existing route跳过Opportunity Report，改写Knowledge全部记为Not Applicable；仍执行原有Script Analysis。用户在报告后拒绝优化/改编时同样不加载改写Knowledge，并锁定原稿。Creation route不适用No-Revision逻辑，除非用户实际提供了已有剧本。


用途：


辅助：

- 故事结构分析
- 人物分析
- 叙事分析
- 从Idea / Brief直接形成可导演的原创Production Script Proposal并等待用户确认
- Existing首次无改写授权时只形成Optimization Opportunity Report并等待用户决策
- 明确授权后将C类Source Material改编为Adaptation Draft
- 明确授权后形成Production Script Proposal并再次等待用户确认



禁止：

生成镜头。

生成视频Prompt。

对Existing在Opportunity Report后未经授权自动改写；把Adaptation Draft当作Production Script Proposal；未经用户确认把Optimized Proposal标记为Production-Locked或进入STATE-02；在Creation剧本阶段提前写镜头、焦段、机位、运镜、SHOT或CLIP。



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
- 在用户显式启动AUDIO模块时，把已确认角色事实转换为可执行Voice Profile与按需Seed Audio兼容Prompt，并分离稳定Voice Identity、当前Dialogue Performance、Ambience、Sound Effects与BGM / Score



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
- knowledge/action_previs.md（Action-dominant / Mixed，以及需要展开物理动作的镜头；拥有A1/A2/A3与Kinetic Chain，不拥有动作构图或最终Prompt字段）
- knowledge/camera_language/index.md
- knowledge/transitions/index.md（存在相邻镜头时）

Conditional：

- knowledge/camera_language/movement_combinations/（多运镜、多景别、多视点或一镜到底）
- knowledge/lighting/
- knowledge/color/


按镜头内容追加：

- knowledge/performance/（Performance-dominant / Mixed；按PL1/PL2/PL3选择最小充分表演载体）
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
- knowledge/clip_preflight_check.md（每个Clip执行Visual Blocking Risk Pre-Assessment，只标记NONE / POSSIBLE / REQUIRED，不提前生成草图）
- knowledge/clip_planning/
- workflows/10_clip_production_workflow.md
- templates/20_clip_plan.md

用于把相邻兼容Shot编排为4—15秒Confirmed Clip Production Plan，并记录包含Shot、起始状态、连续动作、摄影机/空间关系、道具连续性、结尾状态、风险与Handoff。



---

## STATE-08 Clip-based Video Prompt / Video Generation


适用知识：


AI视频模型相关知识。

STATE-08的Required / Conditional Resources权威清单只由`workflows/11_video_generation_workflow.md`拥有。本索引不复制Resource Gate；它只提供以下发现入口，实际读取范围以当前Workflow判定为准：

- Preflight、Before-Single-Clip-Prompt Gate与参考预算：`knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`
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
- 在每个单Clip Prompt前自动完成Final Visual Blocking Anchor Assessment；NONE直接Prompt，REQUIRED先生成 / 验证 / 注册草图并在下一Checkpoint才Prompt；普通Prompt Rewrite复用Confirmed Anchor
- Prompt结构
- 模型适配
- 动作描述
- 可执行表演节拍
- 对白、环境声、动作声、呼吸、Foley、剧情内声源与同期静默；背景音乐、配乐、BGM、主题音乐与氛围音乐永久不进入STATE-08音效或其他视频Prompt字段
- FX生命周期、物理交互与跨镜后果
- Sequence顺序、Coverage与UNIT边界继承
- Clip内逐镜状态链、4—15秒生成边界与跨Clip尾帧连接

---

## STATE-09 Review

Required：

- knowledge/quality/index.md
- knowledge/spatial_blocking_layer.md（执行Spatial Continuity QA）
- knowledge/knowledge_application_reflection.md（只执行Knowledge Application QA，不在Review重做创作选择）
- templates/16_review_report.md

Conditional：

- knowledge/transitions/
- knowledge/sequence/
- knowledge/fx/

用途：逐镜QA、相邻镜连续性、Prompt评分、Coverage、重试隔离和返回路由。

STATE-09不得因缺少配乐计划而自动加载Music模块。只有用户显式提交或请求复核独立Music Package时，才按`workflows/music_router.md`与`workflows/21_seed_music_score_workflow.md`单独路由。

---

## MUSIC / SEED-MUSIC Score（Explicit-Only Auxiliary）

入口：

- `workflows/music_router.md`
- Positive Route后：`workflows/21_seed_music_score_workflow.md`

Required Knowledge：

- `knowledge/music_score/index.md`
- `knowledge/music_score/spotting_and_silence.md`
- `knowledge/music_score/music_bible_and_cues.md`
- `knowledge/music_score/seedmusic_prompting.md`

唯一Template：`templates/22_seed_music_score.md`。

用途：用户发出明确配乐指令后，由系统专业完成全请求范围的Music Spotting、音乐与留白决策、主题动机、Cue Sheet及SeedMusic提示词。默认纯音乐；歌词、演唱、合唱、哼唱、吟唱或Vocalise只在当前显式要求时允许。Clip存在时以`Related Clip(s)`和Cue标题追踪，但Clip标签不进入SeedMusic `style + structure`执行块。

禁止：自动触发；默认全段铺音乐；把配乐写入Seedance视频Prompt；让用户逐Clip代替系统作Spotting；以`knowledge/sound_language/`代替本独立模块。



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
