# Dialogue And Lip-sync Sound Design

## Dialogue Specification

需要对白时确认：

- Speaker / Character Asset ID
- Exact Line（已确认台词）
- Language / Accent（仅在剧情需要时）
- Voice Identity / Tone
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
- 同一角色跨镜保持音色、口音、能量和空间位置连续
- 同一角色跨集优先复用Active CHAR Version中已确认且有授权记录的15—30秒干净单人声Audio Reference；没有已确认Audio Reference时才以Confirmed Voice Profile为第一顺位声音身份依据
- 当前Clip使用用户明确提供的Voice Reference或适用Confirmed Voice Audio Reference时，声音身份只由Reference锁定；STATE-08保留固定字段`音色特征：`并写明Reference锁定且不得文字重定义，不得在台词、音效或其他字段写Voice characteristics、音高、声线、音域、共鸣、语速或音色质感。台词只保留准确文本及“轻声说、无奈地说、短暂停顿后说”等必要轻量表演指令
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
