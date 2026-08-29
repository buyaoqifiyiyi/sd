# Generation Unit Design

## Purpose

将长Sequence组织为可独立生成、可重试、可续接的UNIT，同时保留跨UNIT状态。

UNIT不是SHOT，也不是最终Prompt章节。

---

## Unit Boundary Criteria

适合划分新UNIT的情况：

- 生成模型无法稳定容纳当前动作密度
- 明确的场景或时间断点
- 已完成一个可验证的叙事结果
- 资产、空间或FX状态发生显著但合法的变化
- 后续内容可以从稳定视觉锚点继续
- 某段失败时需要单独重试而不破坏已接受素材

不应划分新UNIT的情况：

- 只是为了平均长度
- 会切断尚未完成的关键动作
- 会把对白或反应拆成无法理解的两部分
- 无法建立稳定Exit State

---

## Unit Contract

每个UNIT包含：

- Unit ID
- Included Scene / Beat / Coverage IDs
- Narrative Purpose
- Entry Anchor
- Required Change
- Exit Anchor
- Carry-over State
- Retry Boundary
- Upstream Dependencies
- Downstream Dependency

---

## Retry Safety

重试某个UNIT时：

- 不修改已接受的上一UNIT结果
- 使用上一UNIT已确认Exit Anchor
- 只改变导致失败的最小执行层信息
- 不借重试机会重设计资产或改写剧情
- 新结果通过边界检查后才替换该UNIT旧版本

---

## Timing Boundary

Sequence Plan可以内部记录估算时长和容量，用于拆分与预算。

这些信息不得自动进入STATE-08最终Prompt；平台时长参数仍位于Prompt之外。

