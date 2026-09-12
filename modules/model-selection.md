# Model Selection Module

位置：`workflows/02_script_analysis_workflow.md`的`Production Setup Gate`在Script `Production-Locked`后确认项目级视频模型偏好，STATE-06 Detailed Shot Design确认后、STATE-07 Clip Planning前复核该偏好是否适用于当前Clip；它不创建新STATE。

1. 在`Production Setup Gate`的`Production Setup Proposal`中，与项目图像模型默认项一起展示视频模型偏好：Seedance 2.0 / Seedance 2.5 / MiniMax H3、对应Adapter、已知时长和参考能力边界。用户已在项目请求中指定时只展示该候选；否则不默认选择。确认后写`Project Video Model Preference`，不是Clip执行Profile。
2. STATE-06后读取Confirmed Detailed Shot Design、已确认Script / Director Intent / Blocking / Assets、每Clip实际时长、所需首尾帧/视频编辑/多模态参考和`Project Video Model Preference`。
3. 如果偏好覆盖当前Clip的时长、Execution Mode、真实参考输入（包括Required `REF-SKETCH`）和入口能力，直接提升为`SELECTED_MODEL`，不重复询问。读取唯一对应Adapter，只写能力Profile（时长、Timeline、参考能力、声音/口型能力、连续生成能力与安全降级条件），不创建Clip、也不输出`KEEP / ADAPT_SPLIT / RETURN`。
4. 偏好不兼容时只返回最小明确选择：例如H3 Start-End / Video Edit不能提交Required `REF-SKETCH`，必须改为H3 All-Reference、改选兼容模型或返回STATE-06/07降低该Blocking需求；不得把草图写成已提交。不得因为某模型参考容量更大而改写导演设计。
5. 把`SELECTED_MODEL`、Adapter Profile、实际Execution Mode、Reference Capacity Audit与受影响批次写入既有状态合同；STATE-07是Natural Unit与Execution Clip的唯一决策owner。内部模型字段不进入最终Prompt。

用户变更项目视频偏好或当前Clip例外模型时，只重新处理受影响的STATE-07 Execution Clip Plan / STATE-08 Prompt；Production-Locked Script、Confirmed Assets、Director Intent与Shot Design不因此失效。
