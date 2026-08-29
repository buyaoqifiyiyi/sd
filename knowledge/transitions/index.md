# Transition Knowledge Index

## Knowledge Role

本模块负责相邻镜头的转场判断、剪辑锚点与生成边界设计。它服务 Detailed Shot Design、Clip Production、STATE-08 和 Editing，但不拥有剧情、资产、镜头目的或最终 Seedance Schema。

转场不是独立特效清单。正确顺序是：先判定镜头边界类型，再选择一种主要转场机制，最后把可执行证据投影到现有字段。

## Required Reading Order

1. `foundations.md`：转场、运镜、光效与后期剪辑的边界。
2. `decision_engine.md`：自动判断顺序与降级规则。
3. `transition_patterns.md`：标准化转场模式及适用条件。
4. `transition_continuity.md`：出镜锚点、入镜锚点与跨镜状态。
5. `image_source_coverage.md`：用户附件术语的去重、纠错与覆盖映射。

## Authority Boundary

- `rules/04_consistency_rules.md`拥有 Continuous Handoff、Motivated Discontinuity、Unresolved Handoff 的分类定义。
- 本模块只能在该分类下选择转场技术，不能改变分类事实。
- `templates/10_video_prompt.md`独占 STATE-08 最终字段与顺序。
- STATE-08 不新增“转场”字段；结果只进入“镜头结尾状态”“与下一镜衔接”和下一镜“起始状态”。
- 音乐与配乐属于后期剪辑；STATE-08 只允许同期对白、环境声、动作声、呼吸、Foley 与剧情内声源。

## Stability Principle

没有充分依据时使用 Direct Cut。没有下一镜资料时使用 Unresolved Handoff 和安全稳定结尾。任何高风险光效、场景变形、镜面传送或世界切换都必须由上游剧情、资产或 FX 明确授权。

## Final Principle

好的转场先保证信息、动作、空间和声音可读，再考虑风格。它应让两个镜头在切点上相互支持，而不是要求视频模型凭空把两个无关场景变形为一个镜头。
