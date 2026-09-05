# Prompt Compilation Knowledge

## Purpose

本目录负责把已经确认的生产知识语义投影到 STATE-08 唯一最终 Template。它不创作剧情、不修改上游事实、不拥有最终字段，也不建立新的 Prompt Schema。

## Required Resource

执行 STATE-08 时必须先由已锁定的目标模型选择一个内部 Model Compilation Template，再读取：

[STATE-08 Semantic Projection](state08_projection.md)

[Reference Budget / 参考资产预算控制](../reference_budget.md)

Model Compilation Templates（仅内部编译，不拥有最终字段）：

- [Seedance 2.0 Stable Compiler](seedance_20_compilation.md)：仅在 Lock=`Seedance 2.0` 时读取。
- [Seedance 2.5 Native Compiler](seedance_25_compilation.md)：仅在 Lock=`Seedance 2.5` 时读取，并同时读取`../seedance_25_profile.md`。

前者用于确认 Camera、Composition、Performance、Sound、FX、Sequence、资产、Visual Style 与连续性信息是否进入 `templates/10_video_prompt.md` 已有字段；后者用于在投影前确认单Clip最终图片参考真实存在、没有重复占位且不超过9张，并只在接近或超过上限时触发非角色整合。

## Boundary

- Workflow 决定转换步骤。
- 专业 Knowledge 决定内容。
- Seedance Adapter 决定模型路由与模型可执行性；每个已锁定Clip恰好选择一个内部编译模板。
- 本模块决定“适用语义应落到哪些现有字段”。
- Template 仍是字段名称、顺序、编号和排版的唯一拥有者。

## Final Principle

Preserve Applicable Meaning. Preserve One Schema.
