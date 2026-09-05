# SD Film Environment Asset Workflow

# AI影视环境资产制作流程


## 1. Workflow定位


用于：

制作ENV环境资产。


负责：

建立：

空间。

材质。

光影。

氛围。



---

# 2. Core Principle


环境不是背景图。


环境是：

角色行动的视觉空间。

环境资产固定执行：

```text
Asset Design
→ Image Prompt Generation
→ 用户确认提示词
→ Image Generation
→ 用户确认图片
→ Asset Registry
```

Prompt确认与图片确认是两个独立Hard Gate；未经当前Prompt Revision确认不得生成图片，未经图片确认不得登记Canonical References、Active Version或confirmed asset。

执行前必须读取STATE-02的Asset Tiering Decision：

- `Asset Tier: Core`：核心环境独立制作主参考图、多视角与关键区域设定图，形成可重复拍摄的空间锁。
- `Asset Tier: Support`：同类环境小物、氛围装饰或低频环境元素按Board ID整合为Support Environment Reference Board；不得逐项制作完整Wide / Medium / Detail资产包。每板建议4—9个对象，风格统一但在轮廓、材质、颜色、比例和功能上清晰区分。

Core与Support均执行相同的提示词确认与图片确认闭环。Support Board图片确认前，Board及其Item均不得标记confirmed。

## Director-led Environment Function Pass｜Internal

读取STATE-02的Asset Dramatic Function、Writer Intent中的环境剧情身份 / Scene Exit State / Setup-Payoff义务与当前Director Intent，把Environment Narrative Force、Dramatic Geography、可调度前中后景、遮挡/Reveal来源、关系距离、关键入口/出口、负空间和状态变化需要投影到现有Wide / Medium / Detail、Environment Consistency与Prompt。Writer事实不直接规定视觉细节；环境不仅承载角色行动，也应在需要时施加压力、隔离、连接或隐藏信息。不得新增不存在的结构、光源或道具，也不新增Template字段。



---

# 3. Input

执行前先由`references/project_workspace.md`解析项目候选，并按`rules/state_source.md`选定唯一State Source；本Workflow不复制其优先级或Chat fallback细节。然后读取当前运行环境可提供的适用资源：

- project_status.md
- project_bible.md
- asset_registry.md
- references/project_state_contract.md
- references/asset_lock_contract.md（存在后必须读取）
- templates/05_environment_asset_prompt.md


输入：


ENV-ID。

Asset Tier、Tier Decision Basis、Board ID与Item ID。


包括：


地点。

时代。

空间功能。

视觉特点。



---

# 4. Required Asset Set


Core环境必须包含：



## A. Wide Shot


大全景。


目的：


建立空间关系。



表现：

建筑。

地形。

整体布局。



---

## B. Medium Shot


中景。


目的：


展示人物活动区域。



表现：

入口。

工作区域。

主要互动空间。



---

## C. Detail Shot


细节。


目的：


建立材质真实感。



表现：

纹理。

装饰。

局部元素。



---

# 5. Environment Consistency


锁定：


空间结构。


建筑关系。


主要元素位置。


材质逻辑。



---

# 6. Image Prompt Generation

先完成环境定义，再按`modules/assets.md`的Asset Image Route和Asset Tier使用`templates/05_environment_asset_prompt.md`输出完整可直接生图的Prompt Package：

- 主参考图Prompt（Main Reference Image Prompt）：通常为Wide Shot，完整建立环境身份、空间骨架、主要动线、建筑/地形关系、材质、实用光源与综合色彩。
- 必要多视角Prompt（Required Multi-View Prompts）：根据人物活动区和镜头需求输出Medium Shot、反向视角、入口视角或高位布局视角；不需要时写`Not Required`及依据。
- 关键区域/细节Prompt：对剧情交互区、关键材质、标志性结构或尺度锚点输出独立可执行Prompt。

以上独立Prompt Package只适用于Core环境。

Support环境参考板Prompt按一个Board输出一条完整可执行Prompt，列明Board Name、Board ID、4—9个Item ID、Included ENV IDs及逐项轮廓/材质/颜色/比例/功能差异；统一风格、清晰标签、完整可见且不得互相遮挡。Support分支不得逐项制作完整多视角或关键区域套图；若某Item实际承担关键场景空间或需要高一致性，返回STATE-02复核并升级Core。

每条Prompt必须完整包含环境主体、空间关系、视点/构图、尺度锚点、材质、光源方向与光质、综合色彩、天气/时间状态、项目视觉风格、一致性限制、必要负面限制与当前图像工具所需参数。不得只描述“漂亮背景”，也不得使用脱离上下文后不可执行的“同上/参考前述”。

白天、夜晚、雨天等变化状态只有在Asset Discovery或剧本确认需要时才建立；它们必须继承Immutable Spatial Traits。

首次输出写`Visual Production Status: Prompt Draft`、`Prompt Status: Draft`、`Image Status: Not Generated`、`Confirmed Status: No`、`Prompt Revision`与`Awaiting User Confirmation: Image Prompts`，然后停止等待用户确认。


---

# 7. Prompt Confirmation Gate

只有用户无歧义批准当前Prompt Revision后，才写`Visual Production Status: Prompt Confirmed`、`Prompt Status: Confirmed`、`Image Status: Not Generated`、`Confirmed Status: No`及Prompt Confirmation、Confirmed By、Confirmed At。任何实质修改均创建新Prompt Revision并返回`Prompt Draft`。


---

# 8. Image Generation And Confirmation

Prompt Confirmed后按`modules/assets.md`的已记录路由执行：Built-in Image才可调用当前环境可用的内置图片生成；Midjourney只交付外部生成Prompt，不调用内置生成。Core生成独立环境图片；Support生成整张Support Environment Reference Board。实际获得图片后才写`Visual Production Status: Image Generated`、`Prompt Status: Confirmed`、`Image Status: Candidate`、`Confirmed Status: No`，登记Candidate References、使用的Prompt Revision、工具/模型、关键参数、来源与授权，并停止等待用户确认图片。

如果当前环境不能直接生成图片，明确写`Image Generation Availability: Unavailable`并保持STATE-03 `IN_PROGRESS`；用户可用已确认Prompt外部生成并回传，完成来源记录后进入`Image Generated`。

只有用户明确批准具体Candidate Reference后，才进入Asset Registry。Support还必须核对Board ID、Item ID与图中对象对应关系；未明确批准的Item不得confirmed。图片被拒绝时，仅重生返回`Prompt Confirmed`；修改Prompt返回`Prompt Draft`并重新确认。



---

# 9. Output And Registry

最终输出必须使用：

templates/05_environment_asset_prompt.md

Workflow负责空间、材质、状态变化与一致性判断；Template独占最终字段和排版。

图片确认后更新asset_registry.md中的Asset Tier、Board ID、Item ID、`Visual Production Status: Asset Confirmed`、`Prompt Status: Confirmed`、`Image Status: Confirmed`、`Confirmed Status: Yes`、Prompt Revision、Prompt Confirmation、Candidate References、Image Confirmation、Active Version、Canonical References、Immutable Spatial Traits与`Status: Active`。图片确认前不得执行这些Active/Canonical/confirmed写入。



---

# Quality Check


检查：


□ 空间关系明确


□ Core环境的主参考图、多视角与关键区域设定图完整；或Support环境的同类参考板、Board ID与Item Mapping完整

□ 主参考图Prompt与必要多视角/关键区域Prompt完整且可直接生图

□ 当前Prompt Revision已经用户确认

□ 图片已生成或回传且具体Candidate Reference已经用户确认


□ 可进入镜头设计

□ Active Version与Canonical References已登记

□ project_status.md已按references/project_state_contract.md记录Checkpoint

---

# State Update

本Workflow是STATE-03子流程，不创建新STATE。

完成后记录：

- Last Completed Step：Environment Asset Development
- Last Successful Checkpoint：已确认ENV Revision
- Active Artifacts：ENV资产路径和Revision ID
- Next Workflow：下一个尚未完成的STATE-03资产Workflow；全部资产完成后进入STATE-04

全部Required资产均为Active或Not Applicable时，写STATE-03 COMPLETE并把Next Workflow设为07_visual_development_workflow.md；否则保持STATE-03 IN_PROGRESS。每次写入后按references/project_state_contract.md同步或输出完整Portable State，并执行其`Portable Required Field Writeback`。

Environment Asset只有达到`Visual Production Status: Asset Confirmed`、`Confirmed Status: Yes`且`Status: Active`才计入共享Completion Gate。Support Item还必须绑定已确认的Board ID、Item ID与Canonical Board Reference。`Prompt Draft`、`Prompt Confirmed`或`Image Generated`均不算完成。



---

# Final Principle


环境资产目标：

建立可拍摄的虚拟摄影棚。
