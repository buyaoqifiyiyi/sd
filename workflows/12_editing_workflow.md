# SD Film Editing Workflow

# AI视频修改优化流程


## 1. Workflow定位


用于：

已有视频结果的调整和优化。



---

# 2. Trigger Condition

执行前按`rules/state_source.md`取得Selected State Source，再读取`references/project_state_contract.md`、`references/artifact_revision_contract.md`、当前有效Director Intent / Director Decision Notes、Confirmed Clip Plan、实际素材与适用的`knowledge/quality/`，确认当前Accepted Unaffected Artifacts。本Workflow不维护Chat fallback规则。


当用户要求：


- 修改视频
- 延长镜头
- 改变动作
- 改变风格
- 修复一致性



触发。



---

# 3. Editing Principle


修改优先级：


保持原镜头。

小范围调整。


避免：

重新生成完全不同内容。

Editing不是重新导演。它优先保护Editorial POV、信息时序、人物关系、关键反应与情绪余韵；只在现有素材能够支持时改变镜头顺序、切点、Hold长度、声音连接和局部视觉处理。素材不足以恢复导演意图时，必须返回STATE-08重生成或相应设计owner。

Editing同样不是重新编剧。它必须保护Writer Rhythm：Writer Beat order、Setup / Payoff timing、Reveal timing、Trigger / Reaction logic、Scene Value Change、Relationship Delta与Scene Exit State。不能为节奏便利提前Payoff、删掉使行为成立的Trigger / Reaction或交换因果顺序。

## Editorial Decision Pass

每个受影响Scene / Clip先判断并记录到现有修改目标与编辑Prompt语义：

- **Editorial POV**：观众此刻跟谁知道、看谁的反应、何时切换认同
- **Cut / Hold Motivation**：切在动作前、动作点、反应点还是余韵后；继续Hold保护什么
- **Information Timing**：Reveal / Withhold / Delay / Confirm / Recontextualize是否按导演意图发生
- **Reaction Priority**：重大事件后谁的反应比事件本身更重要；反应可在同镜Hold或通过切换呈现
- **Emotional Rhythm**：BUILD / HOLD / PEAK / RELEASE如何落实为镜头时长、停顿、动作密度和呼吸空间
- **Ellipsis / Match / Contrast**：省略什么、用何种动作/构图/声音匹配或对比，以及省略后观众仍能理解什么
- **J-cut / L-cut / Sound Bridge**：剧情内声音如何先行、延续或结束，不能自动引入配乐
- **Transition Logic**：每个边界只有一种主要视觉转场，并服从Outgoing / Cut / Incoming锚点
- **Shot-duration Pressure / Release**：哪些镜头缩短增加压力，哪些镜头延长让反应、确认或余韵成立
- **Writer Rhythm Protection**：Beat order、Setup / Payoff、Reveal timing、reaction logic、Scene Value Change与Relationship Delta在调整后是否仍成立；失败若来自故事设计返回STATE-01/05，若来自镜头/Clip呈现返回STATE-06/07，若只因现有剪辑顺序或切点则在Editing最小修正



---

# 4. Edit Types


## Motion Adjustment


调整：

动作速度。

动作方向。



---

## Camera Adjustment


调整：

运镜。

景别。



---

## Visual Adjustment


调整：

光影。

色彩。



---

## Continuity Adjustment


修复：

人物。

环境。

道具。


---

## Transition And Audio Post

读取：

knowledge/transitions/

用户已显式调用MUSIC / SEED-MUSIC模块并提供Confirmed Music Package时，按该Artifact只读应用；否则不得自动加载音乐Knowledge或规划配乐

执行：

- 根据STATE-08已经生成的Outgoing Anchor、Cut Point与Incoming Anchor完成Direct Cut、Match Cut、J-cut、L-cut、Dissolve、Fade、Smash Cut或已确认的遮挡/光效转场
- 每个边界只保留一种主要视觉转场；无充分依据时使用Direct Cut
- 只有已确认素材足够时才使用遮挡、FX或奇幻转场，不用后期效果掩盖连续性错误
- 只有已存在且Confirmed的独立Music Package才可在此阶段按Cue Sheet添加；若用户此时新请求配乐，先经`workflows/music_router.md`进入独立模块。Editing不得自行设计或自动补齐音乐，且任何音乐都不回写STATE-08字段
- 对白、环境声、Foley和剧情内声源与画面同步；J-cut/L-cut优先使用剧情内声音

如果生成素材缺少可剪辑把手：

返回STATE-08进行最小重生成，不在后期伪造人物、道具或场景状态。



---

# 5. Output

最终输出必须使用：

templates/12_edit_prompt.md

Workflow负责最小修改判断与返回路由；Template独占修改目标、修改Prompt、影响范围和结果记录的最终结构。

Editing结果必须在Selected State Source登记新Revision和受影响ID，完成后重新进入13_review_workflow.md，不得直接把项目标记为完成；随后同步或输出更新后的完整Portable State，执行references/project_state_contract.md的`Portable Required Field Writeback`。



---

# Final Principle


AI后期不是重做。

而是在保持一致性的基础上优化。
