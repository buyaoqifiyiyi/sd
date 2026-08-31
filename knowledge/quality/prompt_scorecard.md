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
- 每镜11个固定字段完整且顺序正确。
- 无时间码、时长、帧率或帧数进入Prompt。
- 每镜明确首帧来源/要求、稳定清楚可继承的尾帧接口和前后Clip连续性关系；叙事性场景切换明确实体首帧继承、状态基准参考或不继承及重建原因。
- 未触发用户显式批量覆盖时，本轮只有当前一个Clip Prompt Package；“下一个 / 下一步 / 继续”没有展开多个Clip。
- 无任何背景音乐生成指令，且每个Clip反向提示词首个非空内容行无例外逐字为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”。
- Required Coverage未丢失。

---

## Weighted Score

| Dimension | Weight |
|---|---:|
| Story / Shot Purpose Fidelity | 15 |
| Asset Identity And Version Lock | 15 |
| Spatial / Action / Boundary Continuity | 20 |
| Performance / Dialogue / Lip-sync Executability | 10 |
| Camera / Lens / Composition Motivation | 10 |
| Lighting / Color / FX / Sound Coherence | 10 |
| Seedance Stability And Risk Downgrade | 15 |
| Template / Semantic Projection Discipline | 5 |

每项按实际证据评分，不得因文字华丽加分。

---

## Decision

- 90–100：Ready for Review。
- 80–89：可进入Review，但必须列出剩余风险。
- 70–79：REVISE，不得提交生成。
- 0–69：REBUILD或返回事实拥有者。
- 任一Hard Gate失败：FAIL。

Score不能覆盖Hard Gate，也不能替代人工审美判断。
