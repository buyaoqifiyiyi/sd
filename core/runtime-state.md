# Runtime And State Core

此文件是路由索引，不复制状态 Schema 或重载协议。

- State Source、项目身份与 portable fallback：`rules/state_source.md`。
- Runtime Reload、Workflow re-entry、Legacy recovery：`rules/runtime_reload.md`。
- 纯推进、局部修改、重试和 anti-duplication：`rules/progression_rules.md`。
- 完成与确认：`rules/completion_gate.md`。
- Canonical State Schema、持久化和同步：`references/project_state_contract.md`。

每次路由必须取得 `CURRENT_STAGE`、`CONFIRMED_STATE`、`ACTIVE_MODULE`、`CURRENT_CLIP`（适用时）、`SELECTED_MODEL`（STATE-06 完成后的 Model Selection 成功后，供 STATE-07/08 消费）及 `OUTPUT_TYPE`。这些是状态合同中的路由视图，不是第二套 Schema。

重新调用某一 Module 时，只执行目标 Module 和为维持其输入有效所必需的最小依赖更新；已确认的无关阶段保持有效。
