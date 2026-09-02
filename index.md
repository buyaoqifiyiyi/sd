# SD Film

# AI影视虚拟制片生产系统


## Introduction


SD Film是一套用于AI影视制作的完整生产流程系统。


它不是简单的Prompt生成工具。


而是模拟真实影视制作流程：

项目建立。

剧本分析。

资产管理。

视觉开发。

场景设计。

镜头设计。

文字分镜执行规划。

AI视频生成。

电影海报与Key Art设计（按需）。



---

# Core Workflow


SD Film遵循：


创意 / Brief / 已有剧本

↓

项目初始化

↓

剧本分析

↓

资产发现

↓

资产制作

↓

视觉开发

↓

场景设计

↓

详细镜头设计

↓

Clip Production

↓

视频生成

↓

审核优化



禁止跳过前置阶段直接进入后续制作。



---

# Main Capabilities


## 01 Project Setup


建立影视项目基础。


包括：


- Project Bible
- Asset Registry
- Project Status



---

## 02 Script Analysis


在同一STATE中从创意生成可导演剧本，或分类、诊断、改编并分析已有故事内容。


包括：


- Creation Brief直接进入Director-first Screenplay Development，不要求用户先在Skill外写完整剧本
- Dramatic Intent、Audience Experience、人物目标/关系、信息策略、视觉动作、表演机会、空间潜力、节奏与AIGC Directability
- 每场内部Scene Director Intent与Directable Screenplay QA；最终剧本不变成分析表或提前写好的分镜
- 剧情结构
- 人物关系
- 环境信息
- 视觉元素
- Existing Script / Material先输出Optimization Opportunity Report；已有明确“直接优化”授权时不重复询问
- 用户明确授权后执行C类Source Material的Script Adaptation，或A/B类Screenwriting Optimization
- Production Script Proposal输出后的第二次确认与Production-Locked门禁



---

## 03 Asset Management


管理影视制作资产。


包括：


- Character Asset
- Environment Asset
- Prop Asset
- FX Asset（按项目需要）



保证：

角色一致性。

环境一致性。

FX生命周期与后果连续性。

项目复用。



---

## 04 Visual Development


建立项目视觉方向。


包括：


- 美术风格
- 色彩体系
- 光影方向
- 摄影基调
- 表演尺度
- 声音原则

当用户明确请求时，可在STATE-04追加电影海报与Key Art辅助流程，包括影片宣传判断、视觉母题、构图、字体层级、分层制作和交付质检。

后期Music / Score不属于STATE-04默认声音原则。只有用户显式请求配乐规划或SeedMusic提示词时，才进入独立MUSIC / SEED-MUSIC模块；该模块专业规划音乐与留白，默认纯音乐，并与视频Prompt永久隔离。



---

## 05 Scene And Shot Design


将剧情转换为影视语言。


包括：


- 场景设计
- 长序列与Coverage规划
- 镜头设计
- 摄影规划



---

## 06 Detailed Shot Design


生成导演层的`Professional Detailed Shot Script`：以精确TC IN / TC OUT和时长为时间轴，为每个Shot完整记录景别、焦段、场景/美术、分层构图、人物动作链、机位与摄影参数、摄影机—人物联合调度、叙事性色光、特效/转场、台词、声音、AI执行备注与Canonical资产引用。


用于：

作为STATE-07 Clip Production的直接输入；内部Director Decision Layer读取这份专业分镜形成决策，但不新增STATE或用户可见字段。



---

## 07 Clip Production

把详细Shot按场景、时间、动作、摄影机、空间、道具、模型复杂度与4—15秒窗口组织为CLIP-001……。Shot是导演设计单位，Clip是AI视频生成单位。

Storyboard只在用户明确要求时作为Optional/Auxiliary Workflow调用，不绑定STATE，也不进入STATE-08参考资产。

---

## 08 Clip-based Video Prompt / Video Generation

按Confirmed Clip Production Plan一对一生成连续Seedance Prompt；一个Clip即使包含多个Shot，也只输出一条Prompt。


根据：

Shot Design。

已确认资产。


生成AI视频制作Prompt。

所有Seedance视频Prompt永久禁止背景音乐、配乐、BGM、主题音乐与氛围音乐。配乐只在用户显式调用独立MUSIC / SEED-MUSIC模块后另行交付。

---

## Auxiliary Music / SeedMusic Score

仅在用户明确请求配乐规划、Music Spotting、Cue Sheet、主题动机或SeedMusic提示词后触发。系统审阅完整范围，专业决定哪里使用音乐、哪里保留同期声与留白；默认输出纯音乐。Clip存在时可在Cue标题和`Related Clip(s)`中表明服务的Clip，但SeedMusic执行正文只使用`style + structure`。



---

# Directory Structure


```text
SD Film

├── SKILL.md
├── config.md
├── index.md
├── project_registry.json
├── project_bible.md       # 兼容入口，不保存真实项目状态
├── asset_registry.md      # 兼容入口，不保存真实项目状态
├── project_status.md      # 兼容入口，不保存真实项目状态
├── portable_project_status.md # 普通Chat最小状态镜像；Work/Codex中不覆盖真实Project Root
│
├── rules/
│   ├── runtime_reload.md
│   ├── state_source.md
│   ├── chat_compatibility.md
│   ├── progression_rules.md
│   ├── activation_rules.md
│   ├── completion_gate.md
│   ├── compatibility_mapping.md
│   ├── resource_loading.md
│   └── 01—05 production rules
│
├── workflows/
│
├── knowledge/
│   ├── fx/
│   ├── performance/
│   ├── poster_design/
│   ├── quality/
│   ├── sequence/
│   ├── music_score/
│   └── sound_language/
│
├── templates/
├── references/
└── scripts/
```

Work/Codex中的真实项目数据位于独立Project Root，例如：

```text
<project-root>/
├── project_manifest.json
├── project_bible.md
├── asset_registry.md
├── project_status.md
├── execution_ledger.md
└── artifact_registry.md
```
