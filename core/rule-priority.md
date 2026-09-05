# Rule Priority

冲突时依次服从：

1. 用户当前明确指令与合法确认边界；
2. Project ID 一致、可访问的锁定项目事实与已接受工件；
3. 当前 `ACTIVE_MODULE` 的 owner contract 与 Completion Gate；
4. 当前 Model Adapter（仅模型能力、输入、时长适配、时间线及编译语义）；
5. 全局 Rules / Core；
6. 默认行为、示例和历史输出。

Model Adapter 永不得覆盖剧情、人物身份、Writer Intent、Director Intent、Canonical Asset、已确认的空间关系、镜头目的或 Template Schema。发现冲突即返回相应事实 owner。
