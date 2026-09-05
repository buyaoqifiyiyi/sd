# SD Film Prop Asset Workflow

# AI影视道具资产制作流程


## 1. Workflow定位


用于：

制作PROP资产。


负责：

建立剧情关键物件。



---

# 2. Core Principle


道具不是装饰。


重要道具：

承担剧情信息。

道具资产固定执行：

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

- `Asset Tier: Core`：剧情关键道具独立制作主参考图与必要状态/细节图；需要时再制作使用关系图。
- `Asset Tier: Support`：同类家具、陈设、文书、环境小物或低频道具按Board ID整合为Support Prop Reference Board；不得逐项制作完整Overall / Detail / Usage资产包。每板建议4—9个对象，风格统一但在轮廓、材质、颜色、比例和功能上清晰区分。

Core与Support均执行相同的提示词确认与图片确认闭环。Support Board图片确认前，Board及其Item均不得标记confirmed。

## Director-led Prop Function Pass｜Internal

读取STATE-02的Asset Dramatic Function、Writer Intent中的Prop Story Function / Setup-Payoff relevance / 信息时机与当前Director Intent，确认道具在剧情中的信息、关系、动作、身份或视觉母题功能，并建立最小`Prop State Evolution`：初始状态、允许变化、关键交接/损坏/开启/消耗、最终可继承状态。Writer事实不直接规定造型或材质；结果投影到现有Overall / Detail / Usage、Consistency与Prompt，不新增字段。无状态变化时明确稳定即可，不为“戏剧性”虚构变化，也不得提前暴露尚未Payoff的道具功能。


---

# 3. Input

执行前先由`references/project_workspace.md`解析项目候选，并按`rules/state_source.md`选定唯一State Source；本Workflow不复制其优先级或Chat fallback细节。然后读取当前运行环境可提供的适用资源：

- project_status.md
- project_bible.md
- asset_registry.md
- references/project_state_contract.md
- references/asset_lock_contract.md（存在后必须读取）
- templates/06_prop_asset_prompt.md


输入：

PROP-ID。

Asset Tier、Tier Decision Basis、Board ID与Item ID。


包括：

名称。

用途。

剧情价值。



---

# 4. Required Asset Set

以下独立资产套图仅适用于Core道具：



## A. Overall View


整体展示。


确认：

形态。

比例。

结构。



---

## B. Detail View


细节展示。


确认：

材质。

纹理。

特殊结构。



---

## C. Usage View


使用状态。


确认：

人与道具关系。

动作方式。



---

# 5. Prop Consistency


保持：


形状。


尺寸。


材质。


关键结构。



---

# 6. Image Prompt Generation

先完成道具定义，再按`modules/assets.md`的Asset Image Route和Asset Tier使用`templates/06_prop_asset_prompt.md`输出完整可直接生图的Prompt Package：

- 主参考图Prompt（Main Reference Image Prompt）：清楚锁定整体形态、比例、结构、材质、关键识别细节与标准展示视角。
- 必要状态Prompt（Required State Variant Prompts）：只为剧本确认的开合、点亮、破损、沾污、装填、耗尽等状态输出；不需要时写`Not Required`及依据。
- 必要细节Prompt：对剧情关键机关、纹理、铭文、接口、磨损或尺度锚点输出独立可执行Prompt。
- 使用关系Prompt：只有在比例或握持/佩戴/操作方式无法仅靠Scale Reference锁定时生成；不得借机重新设计角色。

以上独立Prompt Package只适用于Core道具。

Support道具参考板Prompt按一个Board输出一条完整可执行Prompt，列明Board Name、Board ID、4—9个Item ID、Included PROP IDs及逐项轮廓/材质/颜色/比例/功能差异；统一风格、清晰标签、完整可见且不得互相遮挡。Support分支不得逐项制作完整主参考、状态、细节或使用关系套图；若某Item实际为剧情关键道具、承担品牌识别或需要高一致性，返回STATE-02复核并升级Core。

每条Prompt必须完整包含道具主体、尺度参照、结构、材质、表面状态、视点/构图、光影、背景控制、项目视觉风格、一致性限制、必要负面限制与当前图像工具所需参数。不得只写外观说明，也不得使用脱离上下文后不可执行的“同上/参考前述”。

首次输出写`Visual Production Status: Prompt Draft`、`Prompt Status: Draft`、`Image Status: Not Generated`、`Confirmed Status: No`、`Prompt Revision`与`Awaiting User Confirmation: Image Prompts`，然后停止等待用户确认。


---

# 7. Prompt Confirmation Gate

只有用户无歧义批准当前Prompt Revision后，才写`Visual Production Status: Prompt Confirmed`、`Prompt Status: Confirmed`、`Image Status: Not Generated`、`Confirmed Status: No`及Prompt Confirmation、Confirmed By、Confirmed At。任何实质修改均创建新Prompt Revision并返回`Prompt Draft`。


---

# 8. Image Generation And Confirmation

Prompt Confirmed后按`modules/assets.md`的已记录路由执行：Built-in Image才可调用当前环境可用的内置图片生成；Midjourney只交付外部生成Prompt，不调用内置生成。Core生成独立道具图片；Support按已确认Board Prompt生成整张Support Prop Reference Board。实际获得图片后才写`Visual Production Status: Image Generated`、`Prompt Status: Confirmed`、`Image Status: Candidate`、`Confirmed Status: No`，登记Candidate References、使用的Prompt Revision、工具/模型、关键参数、来源与授权，并停止等待用户确认图片。

如果当前环境不能直接生成图片，明确写`Image Generation Availability: Unavailable`并保持STATE-03 `IN_PROGRESS`；用户可用已确认Prompt外部生成并回传，完成来源记录后进入`Image Generated`。

只有用户明确批准具体Candidate Reference后，才进入Asset Registry。Support还必须核对Board ID、Item ID与图中对象对应关系；未明确批准的Item不得confirmed。图片被拒绝时，仅重生返回`Prompt Confirmed`；修改Prompt返回`Prompt Draft`并重新确认。


---

# 9. Output And Registry

最终输出必须使用：

templates/06_prop_asset_prompt.md

Workflow负责道具身份、功能、状态和一致性判断；Template独占最终字段与排版。

图片确认后更新asset_registry.md中的Asset Tier、Board ID、Item ID、`Visual Production Status: Asset Confirmed`、`Prompt Status: Confirmed`、`Image Status: Confirmed`、`Confirmed Status: Yes`、Prompt Revision、Prompt Confirmation、Candidate References、Image Confirmation、Active Version、Canonical References、Immutable Traits与`Status: Active`。图片确认前不得执行这些Active/Canonical/confirmed写入。



---

# Quality Check


检查：


□ 外观明确


□ 功能明确

□ Core道具的主参考图与必要状态/细节Prompt完整；或Support道具的同类参考板、Board ID与Item Mapping完整

□ 当前Prompt Revision已经用户确认

□ 图片已生成或回传且具体Candidate Reference已经用户确认


□ 可用于镜头

□ Active Version与Canonical References已登记

□ project_status.md已按references/project_state_contract.md记录Checkpoint

---

# State Update

本Workflow是STATE-03子流程，不创建新STATE。

完成后记录：

- Last Completed Step：Prop Asset Development
- Last Successful Checkpoint：已确认PROP Revision
- Active Artifacts：PROP资产路径和Revision ID
- Next Workflow：下一个尚未完成的STATE-03资产Workflow；全部资产完成后进入STATE-04

全部Required资产均为Active或Not Applicable时，写STATE-03 COMPLETE并把Next Workflow设为07_visual_development_workflow.md；否则保持STATE-03 IN_PROGRESS。每次写入后按references/project_state_contract.md同步或输出完整Portable State，并执行其`Portable Required Field Writeback`。

Prop Asset只有达到`Visual Production Status: Asset Confirmed`、`Confirmed Status: Yes`且`Status: Active`才计入共享Completion Gate。Support Item还必须绑定已确认的Board ID、Item ID与Canonical Board Reference。`Prompt Draft`、`Prompt Confirmed`或`Image Generated`均不算完成。



---

# Final Principle


道具资产目标：

建立可重复调用的剧情视觉元素。
