# Clip Production Knowledge

## Role

本模块服务 STATE-07 Clip Production，负责把 STATE-06 Confirmed Detailed Shot Design中的正式Shot编排为可由视频模型一次生成的Clip。

Clip 是AI视频生成执行单位，不是新的剧情层级。一个Clip可以由一个Shot独立构成，也可以把多个相邻Shot组织为一次连续生成；多Shot合并时剧情、时间、资产状态、动作、摄影机、空间、道具和声音必须兼容，且合计在已锁定模型平台窗口：2.0为4—15秒；2.5为4—30秒，16—30秒自动严格预检。每个正式Shot只属于一个Clip；禁止为了减少Clip数量强行合并。

## Required Resources

使用本模块时必须读取：

1. `knowledge/clip_planning/foundations.md`
2. `knowledge/clip_planning/decision_engine.md`
3. `knowledge/clip_planning/continuity_and_projection.md`
4. `knowledge/reference_budget.md`

正式 Clip 表由：

- `workflows/10_clip_production_workflow.md`
- `templates/20_clip_plan.md`

共同拥有。

## Core Principle

先保留正式SHOT，再设计生成批次：

`Confirmed Detailed Shot Design → STATE-07 Clip Production → CLIP-001… → STATE-08每Clip一条G Prompt Package`

不得为了减少生成次数改写剧情、遗漏正式分镜、跨越未授权的时空断点，或把无法稳定执行的镜头强塞进同一 Clip。
