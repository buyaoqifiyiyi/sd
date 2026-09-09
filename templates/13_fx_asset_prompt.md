# FX Asset Template

## Ownership

本Template只定义FX Asset记录结构。

它不是STATE-08 Clip-based Video Prompt / Video Generation Template，不得替代templates/10_video_prompt.md。

当前agent能直接生成图片且用户请求制作FX资产时，按`modules/assets.md`的Direct Image Default直接输出生成的Candidate Image Review，不展示Prompt；用户明确要求查看/只要Prompt、当前agent不能生成图片或用户选择外部服务时，才输出FX Image Prompt。图片确认仍不可跳过。

---

# FX Asset

FX ID:

Name:

Category:

Story Purpose:

Status:

Version:

Visual Production Status:

Prompt Revision:

Target Image Tool / Model:

Asset Image Route:

FX Image Prompt:

Prompt Confirmation:

Candidate References:

Image Confirmation:

Reference Assets:

---

## Trigger And Source

Trigger:

Emitter / Source:

Initial State:

---

## Effect Process

Propagation:

Direction And Speed:

Scale And Coverage:

Intensity Shape:

Material Behavior:

End State:

Residue:

---

## Asset Interaction

Character Impact:

Environment Impact:

Prop Impact:

Lighting / Shadow / Reflection:

Sound Event:

Visibility / Occlusion:

---

## Continuity Contract

Inherited State:

Allowed Change Conditions:

Irreversible Consequences:

Safe End Boundary:

Known Termination / Cleanup:

---

## Execution Notes

Complexity Risks:

Single-generation Plan:

Post-production Requirement:

Negative Constraints:

---

## Visual Production Checkpoint

用户要求查看/只要Prompt、当前agent不能直接生成图片或用户选择外部图像服务时，固定顺序为`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`。否则按`modules/assets.md`的Direct Image Default直接生成Candidate Image。FX Image Prompt必须完整包含Effect身份、Trigger/Source、Lifecycle、材质行为、交互、光影、构图/视角、一致性、必要负面限制与生成参数。生成图在用户确认前仅为Candidate References；未经图片确认不得登记Canonical References、Active Version或confirmed asset。
