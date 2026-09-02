# SD Film v1.2 Index

# AI影视虚拟制片系统索引

> Compatibility Overview：Knowledge的唯一总路由入口是 `knowledge/00_knowledge_index.md`。本文件只保留系统概览，不拥有阶段映射。


## System Overview


SD Film 是一个面向AI影视制作的完整生产工作流系统。


用于：

- AI短剧制作
- AI电影预演
- Seedance视频生成
- 角色资产管理
- 场景视觉开发
- 镜头设计
- Clip Production
- 系列项目管理


核心原则：

资产优先。

流程优先。

镜头优先。


---

# System Architecture


SD Film采用分层结构：


```text
SKILL.md

↓

rules/

↓

workflows/

↓

knowledge/

↓

templates/
```


---

# Poster Design Knowledge

Purpose:

把已确认影片事实、资产与Visual Direction转换为电影海报、Key Art或One-sheet的宣传视觉系统。

Relevant knowledge:

knowledge/poster_design/

Formal workflow:

workflows/17_poster_design_workflow.md

Output owner:

templates/15_poster_design_package.md

Poster Design是STATE-04条件性辅助模块。未请求海报时不触发；不创建主STATE，不改变上游资产，也不修改STATE-08 Seedance Schema。

---

# Clip Production Knowledge

Purpose:

在STATE-06 Detailed Shot Design完成后，把相邻兼容Shot编排为4—15秒Clip，并为每个Clip建立起始状态、连续动作、摄影机/空间关系、道具连续性、结尾状态和跨Clip连接合同。

Relevant knowledge:

knowledge/clip_planning/

knowledge/clip_preflight_check.md（STATE-07每Clip只做Visual Blocking Risk Pre-Assessment；STATE-08每个单Clip Prompt前执行Final Gate）

Formal workflow:

workflows/10_clip_production_workflow.md

Output owner:

templates/20_clip_plan.md

Clip Production是STATE-07主阶段；STATE-08以Confirmed Clip Production Plan为最小生成单位，每个Clip只生成一条连续Prompt。每Clip必须检查但不强制生成Visual Blocking Sketch；Required时先草图、验证、注册并在下一Checkpoint才Prompt。
