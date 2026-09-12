# FX Asset Template

## Ownership

本Template只定义FX Asset记录结构。

它不是STATE-08 Clip-based Video Prompt / Video Generation Template，不得替代templates/10_video_prompt.md。

任何FX Image Prompt前，必须由`modules/image-model-selection.md`为当前资产批次完成`Selected Image Model`路由。已有已确认`Project Image Model Default`时直接继承；默认项缺失、不可用或当前批次例外时才输出Image Model Selection Proposal，不输出FX Prompt或Candidate Image；选择GPT Image也不跳过Prompt确认。图片确认仍不可跳过。

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

Image Model Selection Status: SELECTED

Image Adapter Profile:

Asset Image Route:

Image Prompt Output Template: GPT Image uses `templates/24_gpt_image_asset_prompt.md`; Midjourney uses `templates/14_midjourney_asset_prompt.md`.

This Template retains the FX asset fields and confirmation state; the final model Prompt body must be compiled only by the selected `Image Prompt Output Template`.

FX Image Prompt:

Prompt Confirmation:

Candidate References:

Image Confirmation:

## Reference Assets And Visual Variant Policy

Reference Assets:

Primary Visual Reference:

Allowed State Variants:

Immutable Visual Anchors:

Variant Transition Conditions:

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

### Physical Drivers

Wind / Gravity / Flow:

Emitter / Fuel / Power Condition:

Collision / Adhesion / Accumulation:

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

## FX State Ledger

仅当效果需要跨Shot或Clip继承时，为每个镜头边界记录；单镜头Inline Effect不填此表。

Boundary (Shot / Clip / Frame):

Active State:

Intensity:

Direction:

Coverage Area:

Source Condition:

Residue:

Affected Asset State:

Lighting Impact:

Sound Tail:

---

## Execution Notes

Complexity Risks:

Single-generation Plan:

Post-production Requirement:

Negative Constraints:

---

## Visual Production Checkpoint

图像模型选择后，固定顺序为`Image Model Selected → Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`。只有选择GPT Image且当前环境实际可用时，Prompt Confirmed后生成Candidate Image；外部模型等待回传。FX Image Prompt必须完整包含Effect身份、Trigger/Source、Lifecycle、材质行为、交互、光影、构图/视角、一致性、必要负面限制与生成参数。生成图在用户确认前仅为Candidate References；未经图片确认不得登记Canonical References、Active Version或confirmed asset。
