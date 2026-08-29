# Sequence Knowledge Index

## Purpose

本目录用于把一个长场景、连续剧情段或多次生成任务组织为可覆盖、可续接、可审核的Sequence Plan。

它服务于STATE-05辅助Workflow，不新增主STATE，不创建正式SHOT，也不定义STATE-08最终Prompt Schema。

---

## Routing

- coverage_design.md：检查叙事信息是否被必要画面覆盖
- sequence_continuity.md：管理Sequence、Scene与Generation Unit边界状态
- generation_unit_design.md：把长序列组织为稳定的生成与重试单元

创建Sequence Plan时同时读取：

- references/module_contracts.md
- workflows/16_sequence_planning_workflow.md
- templates/14_sequence_plan.md

---

## Identity

- SEQ-001：Sequence
- BEAT-001：Narrative Beat
- COV-001：Coverage Requirement
- UNIT-001：Generation Unit

本模块不得分配SHOT ID。

