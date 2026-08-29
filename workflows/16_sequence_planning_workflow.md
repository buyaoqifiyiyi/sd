# Sequence Planning Workflow

## Purpose

将已确认Scene Breakdown组织为长序列覆盖计划、生成单元和跨单元状态合同。

本Workflow是STATE-05的条件性辅助Workflow。

它不新增主STATE，不替代Scene Breakdown，不创建正式SHOT，不生成Storyboard，也不定义STATE-08最终Prompt Schema。

不得创建SHOT ID；正式SHOT及其编号只由STATE-06 Detailed Shot Design拥有。

UNIT是Sequence Coverage、状态继承与Retry Boundary规划容器，不是Clip。UNIT与Clip不存在默认一对一关系；不得创建CLIP ID，不得把Source Script Label或UNIT直接改名、顺序映射或一对一映射为CLIP。Clip只能在STATE-06形成Confirmed Detailed Shot Design后由STATE-07创建。

---

## Module Contract

执行前必须读取：

- references/module_contracts.md
- references/artifact_revision_contract.md
- knowledge/sequence/index.md
- knowledge/sequence/coverage_design.md
- knowledge/sequence/sequence_continuity.md
- knowledge/sequence/generation_unit_design.md
- rules/04_consistency_rules.md
- templates/14_sequence_plan.md

---

## Position

位置：STATE-05 Scene Breakdown完成之后，STATE-06 Detailed Shot Design开始之前。

当前项目仍记录为STATE-05，直到条件性Sequence Planning完成或明确Not Applicable。

---

## Trigger Gate

满足任一条件时执行：

- 一个连续剧情段包含多个Scene
- 故事情节或动作密度需要多个生成单元
- 存在蒙太奇、追逐、战斗、群戏、长对白或复杂FX链
- 需要检查建立、行动、反应、细节、结果与转场覆盖
- 需要从已接受素材继续下一段
- 用户要求整场戏、完整段落、系列片段或长序列规划

以下情况可以标记Not Applicable：

- 单一简单Scene
- 单一镜头目的明确
- 无跨生成单元状态
- Scene Breakdown可以直接、安全地进入Shot Design

Not Applicable必须记录理由，不得静默跳过。

---

## Required Inputs

- `rules/state_source.md`选定的唯一State Source
- Selected State Source允许读取时的project_manifest.json与项目身份信息
- project_bible.md
- asset_registry.md
- 已确认Scene Breakdown
- 已确认Visual Direction
- 已确认资产和连续性事实

---

## Step 1: Establish Sequence Identity

分配唯一SEQ ID，记录项目、Scene范围、故事起点、故事终点与Sequence目的。

---

## Step 2: Build Beat Map

将Sequence拆成有因果的BEAT：

Initial State → Stimulus → Development → Decision / Turn → Result → Exit。

只使用已确认剧情，不新增事件。

---

## Step 3: Build Coverage Matrix

为观众必须理解的每项信息建立COV ID。

标记Required、Supporting或Optional，并说明完成证据。

此时只定义覆盖功能，不决定正式景别、机位或SHOT ID。

---

## Step 4: Design Generation Units

把BEAT与COV组织为UNIT。

每个UNIT必须拥有稳定Entry Anchor、可执行变化、稳定Exit Anchor和Retry Boundary。

UNIT只用于生成组织，不替代SHOT。

UNIT不对应一次最终视频模型调用，也不预先决定Clip数量或Shot-to-Clip分配。

---

## Step 5: Build State Ledger

逐UNIT记录人物、表演、环境、道具、FX、声音、摄影语境和故事认知状态。

每个状态变化必须来自已确认BEAT或叙事断点。

---

## Step 6: Coverage And Redundancy Check

检查：

- 所有Required BEAT是否有Required COV
- Required COV是否具有可见完成证据
- 是否存在重复表达同一信息的无效COV
- 是否遗漏人物反应、动作结果或关键道具/FX后果
- Optional Coverage是否挤压核心叙事

---

## Step 7: Handoff To Shot Design

使用templates/14_sequence_plan.md输出计划。

保存到：

`<active-project-root>/sequences/SEQ-XXX.md`

STATE-06负责创建SHOT ID，并把每个SHOT映射回COV ID。

---

## Completion Gate

- SEQ、BEAT、COV、UNIT ID唯一且连续
- Scene范围明确
- Beat Map保持剧情因果
- 每个Required BEAT至少有Coverage Requirement
- 每个UNIT具有Entry、Change、Exit和Handoff
- State Ledger没有无授权变化
- 没有创建SHOT ID
- 没有创建CLIP ID，也没有建立UNIT-to-Clip默认映射
- 没有定义STATE-08最终字段
- project_status.md记录Sequence Planning Complete或Not Applicable
- Selected State Source更新服从references/project_state_contract.md，并登记Sequence Artifact、Checkpoint与Revision ID，然后同步或输出完整Portable State，执行其`Portable Required Field Writeback`

完成后允许进入STATE-06 Detailed Shot Design。

---

## Error Routing

- Scene范围或剧情事实不清：返回STATE-05 Scene Breakdown
- 资产缺失：返回对应STATE-03 Asset Workflow
- Visual Direction冲突：返回STATE-04
- Coverage完整但无法设计可执行镜头：进入STATE-06处理
- 下游发现Required COV遗漏：返回本Workflow最小补充
