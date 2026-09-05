# Seedance 2.0 Stable Compiler

## Scope

仅当`Target Video Model = Seedance 2.0`且Model Execution Lock已锁定时使用。本编译模板把已确认的Clip语义按既有稳定短Clip策略交给共通Seedance Adapter和`state08_projection.md`；它不是最终用户可见Template，不定义或复制任何STATE-08字段。

## Compilation Contract

- 只接受用户选择的4—15秒Confirmed Clip；沿用既有≤9张有效图片预算、最小充分参考、Canonical Authority、A/B/C `REF-TAIL`和End-State合同。
- 只把当前Clip已确认的剧情、资产、动作、空间、摄影机、声音和连续性语义交给共享Projection；不要求2.5专用的素材映射、任务类型、参考角色或编辑时间段。
- `Video Extension`、`Targeted Edit`、Clay Render/白模、2.5参考角色等2.5专用语义不得被臆造或泄漏到2.0编译路径。

## Handoff

完成稳定性与连续性预检后，只将可执行语义交给`state08_projection.md`，由`templates/10_video_prompt.md`唯一决定最终字段、顺序和排版。
