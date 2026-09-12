# SD Film Prop Asset Workflow

# AI影视道具资产制作流程


# Workflow Position

当前阶段：
STATE-03 Asset Development

子阶段：
Prop Asset Development

前置阶段、下一阶段与对应下一 Workflow 的唯一 owner：
`workflows/workflow_map.md`

---

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

### FAST Automation Exception

启用`Automation Policy: FAST`时，读取`rules/automation_mode.md`与`rules/02_asset_rules.md`。图像模型先按`modules/image-model-selection.md`继承Production Setup已确认的项目默认项；只有批次例外或默认项不可用才确认新选择。符合资格的当前Prompt Revision才可自动确认，并按已选图像模型在同一轮内提交当前道具资产批次。所有Candidate仍汇总为一次用户图片审阅，未经明确图片批准不得登记Canonical / Active。此例外覆盖本Workflow中“等待Prompt确认”与逐Prompt停止的表述，不覆盖项目模型偏好/批次例外选择、图片确认、品牌/法务事实、外部服务或任何Hard Stop。

### Image Model Selection Gate

在任何道具Prompt之前，必须按`modules/image-model-selection.md`完成当前道具资产批次的图像模型路由。已确认项目默认项时直接继承；默认项缺失、不可用或用户明确要求例外模型时才展示`Image Model Selection Proposal`并停止；不得默认GPT Image或直接生成。选择确认后，按该模型的独立Prompt Template输出Prompt；图片确认仍是不可跳过的Hard Gate。

执行前必须读取STATE-02的Asset Tiering Decision：

- `Asset Tier: Core`：剧情关键道具独立制作一张固定`1×4横版道具设定图`作为主参考：正面、侧面、背面、关键细节从左至右同图呈现；必要状态变体、第四格仍无法验证的额外细节图与使用关系图按需补充。
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

对应`Prop Completeness Ledger`条目及其`Prop Production Route`。只有已路由为`PROP Core`或`PROP Support Board`的条目可进入本Workflow；发现漏列、路由冲突或缺失Scene / Beat证据时返回STATE-02补全，不在本Workflow临时猜测或跳过资产范围。


包括：

名称。

用途。

剧情价值。



---

# 4. Required Asset Set

以下独立资产套图仅适用于Core道具：



## A. Main 1×4 Prop Sheet


固定一行四格横版：正面、侧面、背面、关键细节。


确认：

整体形态、比例与结构在正面 / 侧面 / 背面三格一致；第四格验证关键机关、纹理、接口、铭文、磨损或尺度锚点。



---

## B. Additional Detail View


仅当1×4主参考图的关键细节格无法清楚验证剧情关键结构时补充。


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

道具资产按`rules/02_asset_rules.md`的`Asset Batch Delivery`分批交付：同一Asset Tier、同一生产形态与同一已选模型归为一批，整批出Prompt、整批出图、整批确认，不逐道具停顿。先完成道具定义，再完成`modules/image-model-selection.md`的选择确认；按`modules/assets.md`的Asset Image Route、已选模型Template、Asset Tier和`templates/06_prop_asset_prompt.md`输出完整可直接生图的Prompt Package：

- 主参考图Prompt（Main Reference Image Prompt）：生成一张`1×4横版道具设定图`，从左至右固定为正面、侧面、背面、关键细节；四格必须是同一道具、同一版本、同一材质与状态，清楚锁定整体形态、比例、结构与关键识别细节。
- 必要状态Prompt（Required State Variant Prompts）：只为剧本确认的开合、点亮、破损、沾污、装填、耗尽等状态输出；不需要时写`Not Required`及依据。
- 必要细节Prompt：仅在主参考图第四格仍无法清楚验证时，对剧情关键机关、纹理、铭文、接口、磨损或尺度锚点输出独立可执行Prompt。
- 使用关系Prompt：只有在比例或握持/佩戴/操作方式无法仅靠Scale Reference锁定时生成；不得借机重新设计角色。

以上独立Prompt Package只适用于Core道具。

Support道具参考板Prompt按一个Board输出一条完整可执行Prompt，列明Board Name、Board ID、4—9个Item ID、Included PROP IDs及逐项轮廓/材质/颜色/比例/功能差异；统一风格、清晰标签、完整可见且不得互相遮挡。Support分支不得逐项制作完整主参考、状态、细节或使用关系套图；若某Item实际为剧情关键道具、承担品牌识别或需要高一致性，返回STATE-02复核并升级Core。

每条Prompt必须完整包含道具主体、尺度参照、结构、材质、表面状态、视点/构图、光影、背景控制、项目视觉风格、一致性限制、必要负面限制与当前图像工具所需参数。不得只写外观说明，也不得使用脱离上下文后不可执行的“同上/参考前述”。

首次输出写`Visual Production Status: Prompt Draft`、`Prompt Status: Draft`、`Image Status: Not Generated`、`Confirmed Status: No`、`Prompt Revision`与`Awaiting User Confirmation: Image Prompts`；`PROMPT_ONLY`、或`AUTO`且当前环境无出图能力时，在此停止等待批次确认，同批资产在同一轮交付、不逐项停止；`DIRECT_IMAGE`且当前执行环境确实具备出图能力、QA通过时，按`rules/02_asset_rules.md`的Prompt Gate在同一轮自行确认本批Prompt Revision并继续生成，Prompt仍完整留档。


---

# 7. Prompt Confirmation Gate

只有用户无歧义批准当前Prompt Revision后，才写`Visual Production Status: Prompt Confirmed`、`Prompt Status: Confirmed`、`Image Status: Not Generated`、`Confirmed Status: No`及Prompt Confirmation、Confirmed By、Confirmed At。任何实质修改均创建新Prompt Revision并返回`Prompt Draft`。


---

# 8. Image Generation And Confirmation

Prompt Confirmed后按`modules/assets.md`的已记录路由执行：仅已选择GPT Image且当前环境实际可用时可调用GPT Image 生成；Midjourney只交付外部生成Prompt，不调用GPT Image 生成。Core首先生成一张`1×4横版道具设定图`；Support按已确认Board Prompt生成整张Support Prop Reference Board。实际获得图片后才写`Visual Production Status: Image Generated`、`Prompt Status: Confirmed`、`Image Status: Candidate`、`Confirmed Status: No`，登记Candidate References、使用的Prompt Revision、工具/模型、关键参数、来源与授权，并停止等待用户确认图片。

如果当前环境不能直接生成图片，明确写`Image Generation Availability: Unavailable`并保持STATE-03 `IN_PROGRESS`；用户可用已确认Prompt外部生成并回传，完成来源记录后进入`Image Generated`。

只有用户按批次明确批准该批具体Candidate Reference后，才进入Asset Registry；按其挑拣时，被指出的项只退该项，同批其余项保持确认。Support还必须核对Board ID、Item ID与图中对象对应关系；未明确批准的Item不得confirmed。图片被拒绝时，仅重生返回`Prompt Confirmed`；修改Prompt返回`Prompt Draft`并重新确认。


---

# 9. Output And Registry

最终输出必须使用：

templates/06_prop_asset_prompt.md

Workflow负责道具身份、功能、状态和一致性判断；Template独占最终字段与排版。

图片确认后更新asset_registry.md中的Asset Tier、Board ID、Item ID、`Visual Production Status: Asset Confirmed`、`Prompt Status: Confirmed`、`Image Status: Confirmed`、`Confirmed Status: Yes`、Prompt Revision、Prompt Confirmation、Candidate References、Image Confirmation、Active Version、Canonical References、Immutable Traits与`Status: Active`。图片确认前不得执行这些Active/Canonical/confirmed写入。



---

# Completion Gate


检查：


□ 外观明确


□ 功能明确

□ Core道具主参考图为正面 / 侧面 / 背面 / 关键细节的1×4横版且四格一致，必要状态或额外细节Prompt完整；或Support道具的同类参考板、Board ID与Item Mapping完整

□ 当前Prompt Revision已经用户确认

□ 图片已生成或回传且具体Candidate Reference已经用户确认


□ 可用于镜头

□ Active Version与Canonical References已登记

□ project_status.md已按references/project_state_contract.md记录Checkpoint

---

# Status Update

本Workflow是STATE-03子流程，不创建新STATE。

完成后记录：

- Last Completed Step：Prop Asset Development
- Last Successful Checkpoint：已确认PROP Revision
- Active Artifacts：PROP资产路径和Revision ID
- Next Workflow：按`workflows/workflow_map.md`的STATE-03路由取值，必须写实际Workflow文件名

全部Required资产均为Active或Not Applicable时，且`Prop Completeness Ledger`中每个`PROP Core` / `PROP Support Board`路由项都已达到对应确认态，才写STATE-03 COMPLETE并按`workflows/workflow_map.md`写回Next Workflow；否则保持STATE-03 IN_PROGRESS。每次写入后按references/project_state_contract.md同步或输出完整Portable State，并执行其`Portable Required Field Writeback`。

Prop Asset只有达到`Visual Production Status: Asset Confirmed`、`Confirmed Status: Yes`且`Status: Active`才计入共享Completion Gate。Support Item还必须绑定已确认的Board ID、Item ID与Canonical Board Reference。`Prompt Draft`、`Prompt Confirmed`或`Image Generated`均不算完成。



---

# Final Principle


道具资产目标：

建立可重复调用的剧情视觉元素。
