# Dialogue And Lip-sync Sound Design

## Dialogue Specification

需要对白时确认：

- Speaker / Character Asset ID
- Exact Line（已确认台词）
- Language / Accent（仅在剧情需要时）
- Voice Identity（只作Source State；默认不写入视频Prompt）
- Volume And Energy
- Pace And Pauses
- Emotional Subtext
- Spatial Position
- Distance From Camera
- Occlusion / Environment Effect
- Lip-sync Priority

---

## Rules

- 不改写已确认台词，除非用户要求或口型容量必须回到上游调整
- 同一角色跨镜的Voice Identity由外部音频资源或已确认Source State保持；能量、距离与空间位置属于当前Dialogue Performance / Sound State
- 已确认且有授权记录的Audio Reference或Confirmed Voice Profile可供声音制作系统维持跨集身份，但默认不投影到STATE-08视频Prompt，也不设置本地固定秒数要求
- 用户未明确要求当前视频Prompt包含声音控制时，完全省略Voice Reference、Voice Profile与`音色特征：`。用户明确要求时只按最小Delta引用，不得在台词、音效或其他字段重复Voice characteristics、音高、声线、音域、共鸣或音色质感
- 台词可保留准确文本及“轻声说、无奈地说、短暂停顿后说”等必要Dialogue Performance；它们只控制当前一句，不得重定义稳定Voice Identity
- 当前情绪、人物距离、体力、呼吸与空间只形成表演状态变化，不得覆盖基础Voice Identity或把未确认候选音频当作正式Reference
- 台词长度必须容纳自然停顿，不得靠异常语速塞入镜头
- 嘴部被遮挡或角色背对摄影机时，不把精确口型设为主要执行目标
- 旁白、画外音、现场对白必须明确区分
- 重叠对白只在剧情明确且模型/后期流程能够支持时使用

---

## Sync Check

对白开始和结束必须对应可见说话动作。

人物停止说话后，口部回到自然状态；非说话者不得产生误口型。

表演动作规则同时参考：

knowledge/performance/dialogue_performance.md
