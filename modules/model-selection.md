# Model Selection Module

位置：`workflows/02_script_analysis_workflow.md`的`Production Setup Gate`在Script `Production-Locked`后确认项目级视频模型偏好，STATE-06 Detailed Shot Design确认后、STATE-07 Clip Planning前复核该偏好是否适用于当前Clip；它不创建新STATE。

1. 在`Production Setup Gate`的`Production Setup Proposal`中，与项目图像模型默认项一起展示视频模型偏好：Seedance 2.0 / Seedance 2.5 / MiniMax H3、对应Adapter、已知时长和参考能力边界。用户已在项目请求中指定时只展示该候选；否则不默认选择。确认后写`Project Video Model Preference`，不是Clip执行Profile。
2. **区分偏好与硬锁，并记录判定依据**：`Project Video Model Preference`默认为**偏好**——用户说“用Seedance 2.5”“用2.5”即属偏好，它决定候选范围，不构成全程锁定。只有用户明确表示不考虑其他模型（例如“只能用2.5”“不接受其他模型”“不必再评估其他模型”）时才写`Project Video Model Lock: HARD`；未出现该明确表达时保持`Project Video Model Lock: PREFERENCE`。判定依据写入Project State，使后续能被复核而不是靠记忆。偏好模式下，系统可以提出更便宜的可行方案供用户决定；硬锁模式下遵从用户选择，不反复推荐替代方案。
3. **STATE-06后：交付模型规划包络并锁定 Adapter。** 本步**只读已存在的事实**，不得读取尚未创建的 Clip 数据：

   - Confirmed Detailed Shot Design（30个正式Shot的时长、动作链、空间与情绪因果）
   - `Project Video Model Preference`与`Project Video Model Lock`
   - 由分镜直接汇总的**全片大致时长**（Shot时长之和），不是Clip时长
   - 资产类型与规模（Canonical资产数量与参考位需求）
   - 是否存在蒙太奇、长动作链、跨世界交叉剪辑、声音或编辑任务
   - 用户的成本与质量偏好

   **输出：`Model Planning Envelope`（模型规划包络）**，逐项写入 State Contract 并随 Adapter Revision 一同锁定：`Selected Model`、`Adapter Revision`、时长窗口、长时生成能力、参考图/视频/音频容量、Timeline能力、连续生成能力、首尾帧能力、可用Execution Mode、严格预检触发条件、安全降级条件、**规划倾向**（优先保护什么）。包络是STATE-07规划的自然输入，不是对已有Clip的审核结论。

   本项目（Selected Model = Seedance 2.5，Adapter `adapters/seedance-2.5.md`）的包络示例：时长窗口 4—30 秒；16—30 秒允许但须长时严格预检；Timeline 适用于多Beat、蒙太奇与复杂连续动作；图片容量最多30张；规划倾向为优先保护完整动作链、情绪因果与回忆蒙太奇。

   **包络锁定后，STATE-07必须在该包络内规划。** 包络缺失或与Adapter不匹配时不得创建Execution Clip。

4. **本步不得做的事**：不创建Clip、不输出`KEEP / ADAPT_SPLIT / RETURN`、不读取"每Clip时长/参考数量"、不做逐Clip能力等级或成本判定。逐Clip的适用性验证属于STATE-07第三遍（见`workflows/10_clip_production_workflow.md`），不在这里执行。因果顺序是**模型→规划**，不是**规划→审核模型**：Clip不是模型选择的前置输入，而是模型锁定后的产物。
5. 偏好不兼容时只返回最小明确选择：例如H3 Start-End / Video Edit不能提交Required `REF-SKETCH`，必须改为H3 All-Reference、改选兼容模型或返回STATE-06/07降低该Blocking需求；不得把草图写成已提交。不得因为某模型参考容量更大而改写导演设计。
6. 把`SELECTED_MODEL`、`Adapter Revision`、`Model Planning Envelope`与受影响批次写入既有状态合同；STATE-07是Natural Unit与Execution Clip的唯一决策owner。内部模型字段不进入最终Prompt。`Model Planning Envelope`是内部规划输入，不进入Clip Plan用户可见字段，也不进入最终Prompt。
7. **模型变更路由**：模型发生改变时，`Model Planning Envelope`与Adapter Revision 随之更新，受影响的 STATE-07 Execution Clip Plan 与 STATE-08 Prompt **自动失效并重新规划**；Production-Locked Script、Confirmed Assets、Scene Breakdown 与 Detailed Shot Design 保持有效。重新规划必须在**新包络内**重做 Natural Unit 与 Execution Clip，不得沿用旧模型的切分习惯。

## Clip Adequacy Verification｜Clip适用性验证（STATE-07第三遍，不是模型选择）

本节由 STATE-07 在 **Execution Clip 草案形成之后**执行，输入是已形成的 Clip 与其真实数据。**它不属于 Model Selection**：在 Clip 存在之前不得运行，也不得用它去反推或推翻已锁定的`Model Planning Envelope`。

逐Clip记录：Clip ID、时长、实际图片/视频/音频参考数量、所需Execution Mode、必须能力、最低充分模型、用户偏好模型、预计生成费用、最终选择理由。并判定该Clip对已锁模型的**能力使用等级**：

- `REQUIRED`：该Clip确实使用了所选模型的独占能力——例如Seedance 2.5的时间戳多Beat/蒙太奇控制、16—30秒长时连续、Video Extension、Targeted Edit，或Seedance 2.0 / H3各自独有的入口能力。写明是哪一项能力，使判定可复核。
- `ADEQUATE`：所选模型能做，但更便宜的候选模型同样能做；此时按`## Cost Alternative Note`给出替代方案提示。
- `OVERQUALIFIED`：能力明显过配——所选模型相对该Clip的实际需求没有承担任何独占工作；此时**必须**给出替代方案提示，并按`## Cost Alternative Note`标注成本字段状态。

**本等级是内部审计记录与提示**：`OVERQUALIFIED`不阻断交付、不自动更换已锁定模型、不改变已确认的Clip边界与`Selected Model`，也不构成`KEEP / ADAPT_SPLIT / RETURN`。它只要求把"更便宜的可行方案"告诉用户，由用户决定是否改偏好。能力判定看的是**必须能力与参考容量**，不是只看时长或图片数量：时长落在窗口内不等于便宜模型可执行，参考数量超其上限时更便宜的模型反而不成立。

**出现`OVERQUALIFIED`时的正确处理顺序**：先检查规划层——该Clip是否本可与相邻单元合并成更长的连续单元（见 STATE-07 的长时能力利用审计），再谈换模型。因为"用2.5却切成短段"是**规划问题**，换模型只是把规划问题掩盖掉。

## Cost Alternative Note

替代方案提示只有在**真实费率存在**时才有数字。费率属于`O｜Operational Parameter`，必须先取证并带`valid_as_of`日期，未取证前不得推算、不得用“更便宜 / 差不多”这类定性说法冒充价格。已取证档位的唯一登记处是`references/platform_pricing.md`；本模块不复制费率表。

- **已取证档位**：可按`references/platform_pricing.md`给出单次价格与差价（Seedance 2.5 / 2.0 系列已有官方单价）。比较时必须在**同一分辨率与画幅**下进行，并写明币种、分辨率与是否含视频输入；交付画幅仍为`Pending`时按档位并列，不得替用户选定画幅。低分辨率档位不支持的模型（如 2.0 Fast / Mini 无 1080p）不得在 1080p 比较里当作更便宜候选。
- **未取证档位**：写`待用户提供`，不得填入任何数值或区间。当前 MiniMax H3 属此列——官方只声明 H3 需按量购买 API，未公开单价。提示只写"该Clip能力使用等级为`OVERQUALIFIED`／`ADEQUATE`，存在更便宜的可行候选，需费率才能给出差价"。
- **预期成本**：按 `预期成本 = 单次生成价格 × 预计尝试次数` 比较，且尝试次数必须来自本项目已记录的生成运行证据（`references/artifact_revision_contract.md`的Generation Run Record）或用户明确给出的经验值，不得凭模型名称猜测重试率。
- **提示不是门**：无论等级为何，都不得以成本为由拒绝、延迟或静默更换用户已选的模型；改模型属于用户决定，走`Project Video Model Preference`变更与受影响STATE-07/08重跑。

## Total Production Cost｜总生产成本

模型比较不得只比单条价格。总生产成本按四项分解，**但只有前两项在费率已取证时才可以出数字**：

```text
总生产成本 = 生成费用 + 跨Clip尾帧成本 + 连续性修复成本 + 重生成本
```

- **生成费用**：可算。`单价（按分辨率与是否含视频输入）× 各Clip确认时长之和`，费率取`references/platform_pricing.md`已登记档位。**含视频输入与不含视频输入的单价不同**（Seedance 2.5 1080p：11.7 vs 7.0 USD/M tokens），比较时必须写明按哪一种计。
- **跨Clip尾帧成本**：可算，且要看**输入形态**。`REF-TAIL`作为**图片**参考不改变 Seedance 的按秒计价（它只占一个图片输入位、计入图片上限）；只有当尾帧以**视频**形态输入时才触发含视频输入的计价档。逐项写明本片实际形态，不得默认按视频计价，也不得默认不计。
- **连续性修复成本**：**只有本项目已记录的生成运行证据**（`references/artifact_revision_contract.md`的Generation Run Record）或用户明确给出的经验值才能折算；没有证据时写`待运行证据`，**不得凭模型名称猜测重试率**。
- **重生成本**：同上——`单次生成价格 × 实际重试次数`，重试次数来自Generation Run Record。无证据时写`待运行证据`。

**比较纪律**：四项里只要有一项是`待运行证据`，就不得给出"某模型总生产成本更低"的结论，只能并列已算出的项并标明缺项。这与`## Cost Alternative Note`的"费率不是门"同一口径：总成本也不得成为拒绝、延迟或静默更换用户已选模型的理由。

## Mixed-Model Boundary

同一交付轮使用不同模型是**批次的既有不变量**，不因成本提示开放：同一批不得混模型，逐Clip换模型必须由用户明确要求并作为独立批次处理，并按`workflows/10_clip_production_workflow.md`的跨Clip连续性合同复核A/B/C尾帧承接。本模块不承诺跨模型画风一致性的自动检查，也不得声称混合批次已通过该检查。

用户变更项目视频偏好或当前Clip例外模型时，只重新处理受影响的STATE-07 Execution Clip Plan / STATE-08 Prompt；Production-Locked Script、Confirmed Assets、Director Intent与Shot Design不因此失效。
