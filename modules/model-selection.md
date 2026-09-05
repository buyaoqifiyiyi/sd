# Model Selection Module

位置：STATE-06 Detailed Shot Design 确认后、STATE-07 Clip Planning 前。它不创建新 STATE。

1. 读取 Confirmed Detailed Shot Design、已确认 Script / Director Intent / Blocking / Assets 与状态。
2. 仅当当前批次没有 `SELECTED_MODEL` 时询问目标模型；不得在剧本、导演、资产或 Storyboard 时询问。
3. 读取唯一对应 Adapter，只写入其能力 Profile（时长、Timeline、参考能力、连续生成能力与安全降级条件），不创建 Clip、也不输出 `KEEP / ADAPT_SPLIT / RETURN`。
4. 把 `SELECTED_MODEL`、Adapter Profile 与受影响批次写入既有状态合同；STATE-07 是 Natural Unit 与 Execution Clip 的唯一决策 owner。内部模型字段不进入最终 Prompt。

切换模型只重新处理受影响的 STATE-07 Execution Clip Plan / STATE-08 Prompt；Production-Locked Script、Confirmed Assets、Director Intent 与 Shot Design 不因此失效。
