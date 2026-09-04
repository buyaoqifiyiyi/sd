# Skill Experience Ledger

## Storage Boundary

本文件只保存已获用户明确确认的跨项目技能经验。它不是Project State、Project Bible、Asset Registry或任何项目交付物。

## Current Status

- Ledger Status: EMPTY
- Next Experience ID: EXP-0001
- Last Updated: Not Initialized

## Confirmed Experiences

None

## Record Rules

- 只有`references/skill_experience_contract.md`定义的候选在用户明确确认后才能写入。
- 每条记录必须包含Experience ID、Statement、Applicability、Evidence、Confidence、Validated Count、Created / Last Validated与Status。
- 经验只作为相关产出和项目迭代的只读建议；冲突时暂停应用并标记REVIEW或RETIRED。
- 每次写入都必须递增Skill Version / Build ID并执行完整Skill Update Self-Check。
