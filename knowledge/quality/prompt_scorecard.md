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

这两项评的不是"有没有照抄 Aesthetic Decision Lock"，而是**取舍在Prompt里是否可见**。每项必须给出下列可观察证据，不得只复述Lock的措辞：

- **视觉重心唯一**：写清这一镜第一眼落在哪里。没有重心，或多个重心互相竞争，本项不得满分。
- **明暗有层级**：写清黑位、中间调与高光的分布方向，而不是只写"打亮主体"。
- **色彩有主从**：写清主色 / 辅色 / 强调色的面积关系与位置，而不是列出色彩名称。
- **取舍可见**：Aesthetic Decision Lock中"被放弃的那一边"，在Prompt里必须能看出它确实被放弃了；看不出，等于没有做决定。
- **不平均**：是否避免了"每样都有一点"。平均照亮、均匀分布、处处清楚，本项不得满分。
- **景深 / 清晰度有意图**：写清哪里清楚、哪里不，以及它服务哪一项注意力。

**本评分仍不能替代人工审美判断。** 上述六条只覆盖审美中可被文字检验的那一半；剩下那一半——"这一眼好不好看"——由STATE-04的`Look Frame`与STATE-09的人工Review承担，不由本评分承担。

---

## Decision

- 90–100：Ready for Review。
- 80–89：可进入Review，但必须列出剩余风险。
- 70–79：REVISE，不得提交生成。
- 0–69：REBUILD或返回事实拥有者。
- 任一Hard Gate失败：FAIL。

Score不能覆盖Hard Gate，也不能替代人工审美判断。
