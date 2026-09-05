# FX Asset Workflow

## Purpose

将STATE-02已经识别的效果需求转换为可复用、可绑定、可追踪连续性的FX Asset。

本Workflow属于STATE-03 Asset Development的辅助Workflow。

它不新增主STATE，不生成具体SHOT，不生成Storyboard，也不定义最终Seedance Prompt Schema。

---

## Entry Gate

执行前必须确认：

- State Source已按`rules/state_source.md`选定；本Workflow不复制其优先级或Chat fallback细节
- Script Analysis与Asset Discovery已经识别该效果需求
- 涉及的Character、Environment、Prop已有ID或明确处于待开发状态
- 效果具有剧情、空间或视觉功能

如果效果只是单镜头可临时描述且无需复用、连续性或资产绑定，可在Asset Discovery中标记为Inline Effect，不强制创建正式FX Asset。

---

## Required Knowledge

- references/asset_lock_contract.md
- references/artifact_revision_contract.md

必须读取：

- knowledge/fx/index.md
- knowledge/fx/physical_effects.md
- knowledge/fx/fx_continuity.md
- rules/02_asset_rules.md
- rules/04_consistency_rules.md

涉及声音时按需读取knowledge/sound_language/。

---

## Step 1: Confirm Effect Function

确认：

- 故事目的
- 视觉重点
- 触发事件
- 涉及资产
- 首次出现与后续复用
- 是否需要跨镜头保留后果

无法说明作用的纯装饰效果不得自动升级为正式FX Asset。

---

## Step 2: Create FX Identity

分配唯一ID：

FX-001

确定：名称、类别、状态、版本、参考来源。

---

## Step 3: Build Effect Lifecycle

建立：

Trigger → Source → Initial State → Propagation → Interaction → End State → Residue

必须说明运动方向、速度倾向、尺度、覆盖范围和强度变化。

---

## Step 4: Bind Interactions

绑定并记录：

- Character impact
- Environment impact
- Prop impact
- Lighting / reflection impact
- Sound event
- Camera visibility / occlusion risk

不得无原因重设计已确认资产。

---

## Step 5: Establish Continuity Contract

记录：

- 哪些状态必须跨镜头继承
- 哪些后果不可自动恢复
- 允许改变强度或方向的条件
- 镜头边界的安全结束状态
- 已知的结束、熄灭、清理或消散原因

---

## Step 6: Complexity And Execution Check

检查：

- 是否存在过多独立发射源
- 是否与复杂人物动作或复杂运镜竞争
- 变化阶段是否可读
- 模型无法稳定执行时是否应简化或拆镜
- 是否需要后期合成而非单次生成

---

## Step 7: Register Asset

正式FX视觉资产同样受`rules/02_asset_rules.md`的Visual Asset Production Gate约束：先按`modules/assets.md`的Asset Image Route用templates/13_fx_asset_prompt.md输出完整FX Image Prompt并写`Prompt Draft`，等待用户确认；只有`Prompt Confirmed`后才按该路由获得图片（Midjourney只交付外部生成Prompt，不调用内置生成）；实际获得图片后才写`Image Generated`并登记Candidate References，再次等待用户确认；只有图片确认后才写`Asset Confirmed`并登记Canonical References与Active Version。

当前环境不能生成图片时，保留完整Prompt与确认Checkpoint并保持STATE-03 `IN_PROGRESS`，等待外部生成结果回传或工具恢复。

完成双确认后使用templates/13_fx_asset_prompt.md整理正式资产记录。

将FX ID、名称、类型、状态、版本写入：

`<active-project-root>/asset_registry.md`

将跨阶段必须继承的效果事实写入：

`<active-project-root>/project_bible.md`

---

## Completion Gate

完成后更新可用asset_registry.md的Active Version与Canonical References，并在Selected State Source按references/project_state_contract.md登记FX Artifact、Checkpoint与Revision ID；随后同步或输出完整Portable State，并执行其`Portable Required Field Writeback`。

随后执行STATE-03共享Completion Gate：全部Required资产Active或Not Applicable时写STATE-03 COMPLETE并进入07_visual_development_workflow.md；否则保持STATE-03 IN_PROGRESS。

完成必须满足：

- FX ID唯一
- 故事目的和触发条件明确
- 生命周期完整
- 交互资产已绑定
- 结束状态与残留后果明确
- 连续性规则明确
- 执行复杂度已检查
- Asset Registry已更新
- Visual Production Status为`Asset Confirmed`，且Prompt Confirmation与Image Confirmation均已记录

完成后仍处于STATE-03，直到全部必需资产类别完成或明确不适用。
