# STATE-08 Video Prompt / Generation Workflow

# Workflow Position

当前阶段：
STATE-08 Clip-based Video Prompt / Video Generation

前置阶段、下一阶段与对应下一 Workflow 的唯一 owner：
`workflows/workflow_map.md`

---

## Contract

Input：Confirmed Execution Clip Plan、Selected Model / Adapter Profile、Confirmed Script、Director Intent、Spatial Blocking、Canonical Assets、首尾帧与状态。Output schema：按Selected Model路由，Seedance 2.0为`templates/10_video_prompt.md`，Seedance 2.5为`templates/12_seedance_25_video_prompt.md`，MiniMax H3为`templates/13_minimax_h3_video_prompt.md`。本 Workflow 不选择模型、不创建或拆分 Clip、不调用旧 Compiler。

## Required reads

- `modules/prompt-generation.md`
- 当前 Selected Adapter
- `knowledge/director_decision_layer.md`（当前Clip的1—3个已确认导演优先级）
- `project_bible.md` 的已确认 Aesthetic Decision Lock（反差与光比结构、色彩对抗关系、构图主张、视觉母题与变化轨迹）
- `knowledge/prompt_compilation/state08_projection.md`
- 当前 Model Compilation Template（MiniMax H3 时为 `knowledge/prompt_compilation/minimax_h3_compilation.md`）
- 当前Clip使用Spatial Lock环境时：`knowledge/environment_multi_view_reconstruction.md`
- `knowledge/clip_preflight_check.md`、`knowledge/reference_budget.md`
- `references/asset_package.md`：交付义务只读`## Package Timing And Delivery`与`## Access Precondition`；实际构建包时再按该文件的`# Read Scope`加读构成、入选、命名与位置各节——包的规范正文始终由该文件唯一拥有
- 最终输出Template：Seedance 2.0为`templates/10_video_prompt.md`；Seedance 2.5为`templates/12_seedance_25_video_prompt.md`；MiniMax H3为`templates/13_minimax_h3_video_prompt.md`

## Procedure

1. 核验 Execution Clip Plan、Adapter Profile、状态、资产、Shot/Blocking Revision，以及当前Clip Director Intent / Director Decision Notes一致；缺失或冲突回 STATE-07 或相应事实 owner。
2. 对当前一个Confirmed Execution Clip执行最终Reference、A/B/C尾帧、Visual Blocking Anchor、连续性和Prompt Preflight，并在Template投影前完成`Required Sketch Submission Binding`。Spatial Lock环境只使用STATE-07按风险预选并仍为Active/Confirmed的2–4张环境View；不得把Storyboard、STATE-06 Top-down Planning Map或文字Spatial Truth作为视频参考。Final=`REQUIRED`时，草图必须是实际可访问输入并按Adapter占用真实图片位：2.0使用现有参考资产中的真实文件/受控ID，2.5与H3 All-Reference使用`@图片N`；H3其他模式必须先回STATE-07改Execution Mode或模型。`Automation Policy: FAST`下，验证、登记和输入绑定PASS后可在同一轮继续当前Clip编译；STANDARD仍保留草图Checkpoint，任何失败照常返回最小owner。
3. 通过 Projection 写入Selected Model的唯一最终Template。每个 Clip 独立完整输出；不输出 Adapter 或内部账本。Seedance 2.5使用独立多模态时间线模板，默认按30图 / 10视频 / 10音频 / 合计50项能力上限审计，按需少用但不回退为9图模板；时间线按当前Clip写必要阶段。H3使用独立官方三段式模板；2.0保留自己的固定Template。未来模型没有独立Template时不得编译最终Prompt。
4. 不改写剧情、关系、导演意图、Shot 目的、Blocking 或 Canonical Asset；STATE-08也不重新决策运镜、空间或Blocking：Trigger / Stop、Movement Phase、轴线与Blocking语义只从已确认Shot / Clip结果继承并翻译，不重新调用Camera / Blocking知识做新决策。Voice 仅显式 opt-in；Prompt 永久禁止 BGM/配乐。
5. 交付或生成当前 Clip 的最终 Prompt 时，同轮按`references/asset_package.md`的`## Package Timing And Delivery`与`## Access Precondition`处理生产交付包（入选、命名与位置判据由该文件拥有）：包是**本交付轮的正式收尾交付物**，随该轮自动执行、不需要用户另行下令——门条件与`## Access Precondition`均满足时同轮附上包（或给出包路径与已生成证据）；条件不满足时按其降级阶梯交付清单 / 命名映射并标注`未打包`，或逐项报告缺失类别与所在 Gate。**不得静默略过交付包**，也不得声称已打包而实际未生成。打包不是进入本阶段的前置条件（缺包不阻塞Prompt），但交付轮未附包、也未给出降级形态时不得判完成。

# Completion Gate

只改当前 Clip 的 Prompt 映射问题留在 STATE-08；Clip 边界、预算、尾帧或连续性组织问题回 STATE-07；Shot/Blocking 回 STATE-06；事实或资产回对应 owner。全部检查 PASS 后交付或生成，随后主流程收尾：交付轮必须已按`references/asset_package.md`提交包或其降级 / 缺失报告（**不得静默略过交付包**）；state写回必须显式声明`State Status: COMPLETE`、由`workflows/workflow_map.md`确定的下一Workflow与`Pending Decision`：仍有未交付Clip时下一Workflow保持本阶段、`Pending Decision`写下一个待交付Clip；全部应交付Clip的最终Prompt都交付后主流程收尾，写`Next Workflow: Project Complete / Post`与`Pending Decision: None`。STATE-09是显式调用阶段：交付完成后**不停在等待成片的Review检查点**、不自动进入STATE-09、不主动索要生成结果，也不代判PASS或失败；用户明确要求审核成片或携带具体成片问题时才按其owner进入STATE-09，用户明确接受具体Take时按Review owner的`Accepted Take Canon Writeback`登记。
