# Sequence Plan Template

## Ownership

本Template只定义Sequence Plan的阶段输出结构。

它不创建SHOT，不定义Detailed Shot Design或Clip Production Plan，不替代templates/10_video_prompt.md。

UNIT是Coverage / State / Retry规划容器，不是Clip；不得创建CLIP ID，不得把Source Script Label或UNIT直接映射为Clip。

---

# Sequence Plan

Project ID:

Sequence ID:

Sequence Name:

Status: Planning / Confirmed / Not Applicable

Not Applicable Reason:

Scene Scope:

Story Start:

Story End:

---

## Narrative Contract

Sequence Purpose:

Audience Must Understand:

Authorized Story Facts:

Forbidden Additions:

---

## Scene Scope

Included Scene IDs:

Spatial / Temporal Relationship:

Confirmed Breaks:

---

## Beat Map

| Beat ID | Scene ID | Narrative Function | Entry State | Authorized Change | Result |
|---|---|---|---|---|---|
| BEAT-001 | SCENE-001 |  |  |  |  |

---

## Coverage Matrix

| Coverage ID | Beat ID | Priority | Coverage Function | Visual Evidence | Completion Evidence |
|---|---|---|---|---|---|
| COV-001 | BEAT-001 | Required |  |  |  |

---

## Generation Units

| Unit ID | Included IDs | Narrative Purpose | Entry Anchor | Required Change | Exit Anchor | Retry Boundary |
|---|---|---|---|---|---|---|
| UNIT-001 | BEAT-001, COV-001 |  |  |  |  |  |

---

## State Ledger

| Unit ID | Character / Performance | Environment | Prop | FX | Sound | Camera Context | Story Knowledge | Next-unit Handoff |
|---|---|---|---|---|---|---|---|---|
| UNIT-001 |  |  |  |  |  |  |  |  |

---

## Handoff And Risk

Required Coverage For STATE-06:

Unresolved Items:

Continuity Risks:

Execution Risks:

Downstream Notes:

---

## Completion Check

- [ ] All IDs are unique and consecutive
- [ ] Every required beat has coverage
- [ ] Every unit has a stable entry and exit anchor
- [ ] State changes are authorized
- [ ] No SHOT ID has been created
- [ ] No CLIP ID or UNIT-to-Clip mapping has been created
- [ ] STATE-08 final Schema has not been duplicated
