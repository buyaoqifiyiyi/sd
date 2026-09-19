# STATE-08 Prompt Quality Scorecard

## Purpose

为最终Seedance Prompt提供内部100分评分和硬门槛。评分不进入最终Prompt Schema，只进入Review或QA附件。

---

## Hard Gates

任一失败则总结果FAIL，不论分数：

- 当前项目合法进入STATE-08。
- 剧情、关系和镜头目的未被改写。
- 所有资产引用Active Version。
- 每个Clip的【参考资产】显式列出实际使用的Canonical资产/合法帧、用途与锁定约束，且已确认资产优先于临时文字描述。
- 每镜10个固定字段完整且顺序正确。
- 除`时长：`中来自Confirmed Clip Production Plan、由用户选择的单一模型适用平台生成时长外（2.0为4—15秒；2.5为4—30秒，16—30秒须严格预检PASS），无时间码、总片时长、逐镜时长、按秒区间、帧率或帧数进入Prompt。
- 每镜明确首帧来源/要求、稳定清楚可继承的尾帧接口和前后Clip连续性关系；叙事性场景切换明确实体首帧继承、状态基准参考或不继承及重建原因。
- 未触发用户显式批量覆盖时，本轮只有当前一个Clip Prompt Package；“下一个 / 下一步 / 继续”没有展开多个Clip。
- 无任何背景音乐生成指令，且每个Clip反向提示词首个非空内容行无例外逐字为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”。
- Required Coverage未丢失。
- 当前Clip继承并执行了STATE-04 Aesthetic Decision Lock中与本案相关的决定；只写风格标签、器材参数或“电影感”，而未落到已锁定的光比结构、色彩对抗关系、构图主张或视觉母题时，该项不通过。已落到Lock、但未写出可见取舍证据（视觉重心、明暗层级、色彩主从、被放弃的那一边）时，本项同样不通过。

---

## Weighted Score

| Dimension | Weight |
|---|---:|
| Story / Shot Purpose Fidelity | 15 |
| Asset Identity And Version Lock | 15 |
| Spatial / Action / Boundary Continuity | 20 |
| Performance / Dialogue / Lip-sync Executability | 10 |
| Camera / Lens / Composition Motivation（构图是否有主张） | 10 |
| Lighting / Color / FX / Sound（是否有可见的取舍，而不只是执行了 Lock） | 10 |
| Seedance Stability And Risk Downgrade | 15 |
| Template / Semantic Projection Discipline | 5 |

每项按实际证据评分，不得因文字华丽加分。

Camera / Lens / Composition Motivation与Lighting / Color / FX / Sound两项必须落入STATE-04 Aesthetic Decision Lock已锁定的选择，不得在STATE-08另起一套临时审美。

### Aesthetic Criteria｜两项审美维度的评分依据

这两项评的不是"有没有照抄 Aesthetic Decision Lock"，而是**取舍在Prompt里是否可见**。

判据、合格与不合格的分界、以及判定纪律，唯一由`knowledge/quality/aesthetic_judgement.md`拥有；本文件只引用，不复制其正文。评分时逐条给出可观察证据，不得只复述Lock的措辞。

**本评分仍不能替代人工审美判断。** 该文件覆盖的只是审美中可被文字检验的那一半；剩下那一半——"这一眼好不好看"——由STATE-04的`Look Frame`与STATE-09的用户Review承担，不由本评分承担。

---

## Discipline Self-Check｜六条执行自检

本节的六条是**执行自检**，用于在评分前逐条核对当前Clip的Prompt是否达到可交付密度。它**不替代、不新增也不复制**任何规则：每条都指向既有唯一owner。它**不是Hard Gate**，未通过的条目按剩余风险写入Review，不单独判FAIL，也不得被写成最终Prompt字段。

| # | 自检项 | 判据owner |
|---|---|---|
| 1 | **节拍密度**：连续长镜头的每个阶段是否按微节拍逐点推进，而不是一段概括 | `templates/12_seedance_25_video_prompt.md` 的 `### 时间线：` |
| 2 | **身体兑现**：抽象情绪/氛围词是否已全部由可见或可听执行项承担 | `knowledge/prompt_compilation/state08_projection.md` 的 `## Abstract-To-Executable And Physical Anchoring` |
| 3 | **意图可读**：本镜要求观众读到的情绪或关系是否由具体物理载体承担，而不是只给一个标签 | 同上，与 `### Prompt Evidence Specificity` |
| 4 | **失败配对**：进入`全局限制与反向提示词：`的每条风险是否都有对应正向载体写在正文 | 同文件的 `### Positive Specification And Negative Prompt Placement` |
| 5 | **量化可核对**：光比、色温、占比、距离、构图比例是否为"改一个数就改变可见结果"的值，且未混入无视觉收益的工程小数 | 同文件的 `数字与物理描述按执行价值分层` |
| 6 | **元素有源**：画面内每个可见元素是否可追溯到已确认资产、参考输入或上游事实，无默认场景包补入 | 同文件的 `执行Semantic Template Decomposition` 段与 `### Executable Style Carrier Rule` |

逐条给出可观察证据；只写"已符合"而不指出证据的，视为该条未执行。

---

## 联想事故归因与禁用词登记

本节是**归因索引与登记位，不是第二套规则**。它回答一个既有规则都没有回答的问题：**产物已经跑偏之后，这一次属于哪一类，修正该回哪个 owner。**每一行的判据与算法仍只由`判据owner`唯一拥有，本表不复制、不改写、不新增字段，也不进入最终Prompt正文。

**归因对象只限实际观察到的产物**：已生成的帧、成片、被用户指出的那一处画面。不拿"可能被联想"当事故记录，也不把本节当预防性清单使用。

联想链是**模型特定**的：同一措辞在2.0与2.5上的结果可以不同。因此禁用词按当前Model Adapter分别登记，不跨模型继承结论；单次观察且无法分离归因的，按`knowledge/skill_experience.md`记为待复测，不得据此宣称某一词必然有效或必然失败。

| 症状（产物里实际出现的） | 归因 | 判据owner |
|---|---|---|
| 出现没写过或已拍过的场景、服装、道具、天气 | 高共现大词调用默认视觉包 | `rules/03_prompt_rules.md` `### Prompt Pollution Control` 第5类；拆解算法由`state08_projection.md` 的`执行Semantic Template Decomposition`段拥有 |
| 照片级质感被插画、动漫画风替换；真实演员变为模型默认脸 | 高共现大词调用默认视觉包 | 同上 |
| 单人或唯一角色出现复制、分身、镜像重复、背景第二个同类 | 逐镜角色精确数量未正向唯一 + 无合并风险类别 | `state08_projection.md` `## Clip Preflight Projection Gate`的`逐镜角色精确数量`投影行 |
| 受控小动作被放大成夸张动作或另一种情绪读法 | 正向小载体不足，只把否定词反写成形容词 | `state08_projection.md` `### Positive Specification And Negative Prompt Placement` |
| 运镜、走位偏离本Clip的Camera Trigger / Stop与节奏 | 镜头字段未压过装饰性风格词与质量形容词 | `rules/03_prompt_rules.md` `### Prompt Attention / Control Allocation` |
| 风格标签抢走主体、动作与空间的控制位置 | 标签未给出项目特定含义与可执行载体 | `state08_projection.md` `### Style Label Expansion Rule` 与 `### Executable Style Carrier Rule` |
| 出现未授权的音乐、配乐、BGM | 反向段缺固定首句或被压缩掉 | `rules/03_prompt_rules.md` `# Negative Prompt Boundary Rule` |
| 反向段条目越多、越压不住，并带入其他Clip或已废弃情节 | 负向堆叠自身激活概念并稀释控制权重 | 同上`### Prompt Pollution Control` 第4类；类别合并与压缩由`state08_projection.md` `### Positive Specification And Negative Prompt Placement`内的Negative Placement / Negative Compression Pass拥有 |
| 生成画面大致对，但本镜要观众读到的意思丢了 | 失败节拍没有可枚举的小载体 | `state08_projection.md` `### Prompt Evidence Specificity` |
| 画面里出现本镜没有的第二个角色、道具或光源 | 该元素无上游事实或参考输入来源 | 本文件`Discipline Self-Check`第6条「元素有源」 |

**记录位**：本节不新增文件、不新增Template字段。登记只写入既有`templates/17_execution_ledger.md`的`## Generation Attempts`表（每行已含`Failure Class`、`Risk Level`与`Highest-Impact Variable / Retry Scope`）。**本节的归因类别不写入`Failure Class`列**：`Failure Class`是`templates/16_review_report.md`拥有的封闭分类，不得扩充，也不得用本表的归因标签替代它。用户要求显式保存时，把该次事故的`禁用词`与`必用词`按下面两列附在同一行的`Highest-Impact Variable / Retry Scope`中；未要求保存时，只在本轮对话给出表格，不写回项目状态。

- `禁用词`：**本次实际产生该错误输出**的短语原样照抄（不是"哪类词容易出错"的推测）。同义改写视为不同条目，因为改写后的词在模型侧就是另一个触发。
- `必用词`：本项目里**已被反复误读、必须固定写法**的锚定词——登记的是固定写法本身，以及禁止被改写的同义替换；不是"推荐用词"。

**登记后按`Active Model Adapter`分别保留**：换模型、换Adapter版本或平台能力变化时，旧档位转`REVIEW`，未复测前不得作为当前依据继续引用。

---

## Decision

- 90–100：Ready for Review。
- 80–89：可进入Review，但必须列出剩余风险。
- 70–79：REVISE，不得提交生成。
- 0–69：REBUILD或返回事实拥有者。
- 任一Hard Gate失败：FAIL。

Score不能覆盖Hard Gate，也不能替代人工审美判断。
