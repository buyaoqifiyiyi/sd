# SD Film Editing Workflow

# AI视频修改优化流程


## 1. Workflow定位


用于：

已有视频结果的调整和优化。



---

# 2. Trigger Condition

执行前按`rules/state_source.md`取得Selected State Source，再读取`references/project_state_contract.md`、`references/artifact_revision_contract.md`与适用的`knowledge/quality/`，确认当前Accepted Unaffected Artifacts。本Workflow不维护Chat fallback规则。


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

knowledge/sound_language/music_and_silence.md（仅在用户或项目明确需要音乐时）

执行：

- 根据STATE-08已经生成的Outgoing Anchor、Cut Point与Incoming Anchor完成Direct Cut、Match Cut、J-cut、L-cut、Dissolve、Fade、Smash Cut或已确认的遮挡/光效转场
- 每个边界只保留一种主要视觉转场；无充分依据时使用Direct Cut
- 只有已确认素材足够时才使用遮挡、FX或奇幻转场，不用后期效果掩盖连续性错误
- 背景音乐、配乐、歌曲、节拍和音乐进入退出只在此阶段添加，不回写STATE-08“音效”字段
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
