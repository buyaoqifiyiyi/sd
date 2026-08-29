# Director Decision Layer

## Purpose

本层在STATE-06 Detailed Shot Design结束前、STATE-07组织Clip之前，为每个Scene / Shot Group建立导演级内部决策。它先回答“为什么这样拍、观众如何经历这一段、人物关系如何被看见”，再允许Camera、Composition、Lens、Color、Lighting、Performance、Sound、Editing与Seedance相关Knowledge选择实现方法。

本层不创建新STATE，不改写主Pipeline，不拥有任何用户可见Template字段，也不直接生成Seedance Prompt。默认产物为内部`Director Decision Notes`；正式Prompt只保留Notes所导出的可执行视听语义，不输出Notes标题、维度表、候选方案、拒绝理由或内部推理过程。

## Module Contract

- **Module Name**：Director Decision Layer
- **Module Type**：STATE-06末端生成、STATE-07/08消费、STATE-09审核的内部导演决策Knowledge
- **Trigger**：所有完成内容分镜、准备确认Detailed Shot Design的Scene；每个Scene至少覆盖一个Shot Group
- **Not Triggered As**：独立Workflow、新主STATE、导演风格库、Camera Movement选择器、Knowledge Reflection替代品、用户可见固定章节或STATE-08最终Schema
- **Position**：`STATE-06 Detailed Shot Design → Director Decision Notes → STATE-07 Clip Production`；进入STATE-08后固定为`Clip Production Result → Director Decision Notes → Knowledge Application Reflection → Seedance Prompt`
- **Required Inputs / Owners**：Scene / Beat事实、人物关系、Confirmed Assets、Visual Direction，以及`templates/08_shot_design_prompt.md`形成的Professional Detailed Shot Script由各上游拥有者提供；本层必须读取其时间码、画面内容/构图、人物动作链、摄影机/镜头、摄影参数、镜头调度、光线/色彩、声音、AI制作备注与素材/资产。本层只读，不新增剧情事实
- **Output Owner**：STATE-06 Workflow拥有一次性内部`Director Decision Notes`；Work/Codex需要跨轮持久化时写入Active Project Root的`shots/director_decision_notes.md`或既有Execution Ledger，普通Chat保留在当前Workflow内部上下文；不得写入Skill根目录或Portable State正文
- **Read / Write Boundary**：允许读取当前项目已确认产物；只允许写内部决策记录与既有执行账本，不修改Template Schema、Canonical Assets或已确认剧情
- **Downstream Consumers**：STATE-07 Clip Production、STATE-08 Knowledge Application Reflection / Prompt Compilation、STATE-09 Director QA
- **Protected Upstream Facts**：剧情、角色/环境/道具/FX身份、Visual Direction、SHOT编号与顺序、关系轴、边界合同、时长和用户明确要求
- **Conflict Route**：事实或关系冲突返回其上游拥有者；逐镜目的、Blocking或技术设计不能服务Notes时留在STATE-06最小修订；Clip组织冲突返回STATE-07；仅Knowledge实现与Prompt转译问题留在STATE-08
- **Deterministic Invariants**：每个Scene / Shot Group有且只有一份当前有效Notes；十三个决策维度均有结论或明确Not Applicable理由；观众“知道 / 感受 / 等待”已回答；Notes先于Knowledge Reflection；无新STATE、无新最终字段、无内部决策泄漏

## Responsibility Boundary

Director Decision负责：

- 为什么这样拍，以及这一段的唯一主叙事目的
- 观众此刻应该知道什么、感受什么、等待什么
- 人物关系如何通过距离、视线、站位、动作与空间变化表达
- 总体摄影、构图、焦段距离、色光、表演、声音与节奏方向
- 哪一刻应被强调，哪一刻应留白，以及哪些连续性与Seedance风险必须提前限制

Director Decision不得绕过Professional Detailed Shot Script直接从剧本或知识库重新设计镜头。若专业分镜的十八项正式字段缺失、互相冲突，或不足以支持导演判断，返回STATE-06补齐受影响SHOT及相邻边界；不得在Notes中静默补造正式分镜事实。

Director Decision不负责：

- 从知识库选择具体技巧、模式ID、导演标签或1—3项实现策略
- 重做Camera Language原子定义、Clip Movement Plan或Seedance Adapter
- 创建SHOT / CLIP、改变正式顺序、合并镜头或新增剧情动作
- 定义STATE-08字段、排版、编号或向用户展示内部推理

`knowledge/knowledge_application_reflection.md`只回答“用哪些已读取知识最有效地实现已确认导演意图”。它不得反向重定义本层已经锁定的叙事目的、观众体验、人物关系或总体视听策略。

## Decision Unit

默认按`Scene / Shot Group`决策。Shot Group是同一Scene内承担同一主叙事推进、人物关系变化或情绪阶段的一组连续正式SHOT；它不是新ID实体，不占用SHOT、CLIP、BEAT、COV或UNIT命名空间。

- 同一Scene只有一个清楚的关系/情绪推进时，可以整Scene作为一个Shot Group。
- 主叙事目的、关系状态、时空、观察立场或节奏阶段发生实质变化时，建立新的Shot Group。
- Shot Group边界不得重排SHOT，也不得替代STATE-07的Clip边界；一个Group可映射一个或多个Clip，一个Clip原则上只执行一个清楚的主导演方向。若Clip跨越互相冲突的Group方向，返回STATE-07拆分或STATE-06复核。

## Required Decision Dimensions

每个Scene / Shot Group依次形成以下十三项内部结论。结论必须具体到当前剧情与空间；没有适用变化时写明保持项及原因，不得用“电影感、克制、高级、紧张”等抽象词代替。

### 1. Narrative Objective

- 这一段观众必须知道什么？
- 哪一项信息、选择、关系变化或动作结果是唯一主推进？
- 哪些信息现在不能提前揭示？

### 2. Audience Experience

- 观众应感受什么？情绪是建立、累积、转折、释放还是余韵？
- 观众应等待什么，等待在何种可见或可听信号后结束？
- 观众是先于人物知道、与人物同时知道，还是晚于人物知道？

### 3. Character Relationship

- 当前权力、亲密、疏离、戒备、依赖或误解关系是什么？
- 本段结束时关系是否变化；变化的可见证据是什么？
- 谁拥有观察权、行动权或沉默权？

### 4. Blocking

- 人物初始距离、站位、身体朝向、视线目标和高低/前后关系是什么？
- 谁先动、谁停、谁靠近或后退、谁回避或保持视线；这些变化如何表达关系？
- 动作结束后留下什么可继承的空间状态？

### 5. Camera Strategy

- 镜头总体应该动还是停，为什么？
- 摄影机是在观察、跟随、逼近、揭示、释放还是拒绝介入？
- 运动只在什么人物动作、信息或节奏变化上被触发；哪些炫技或无动机运动必须禁止？

本项只定义导演方向，不替代STATE-06 Camera Language Decision中的具体主运镜、起点、路径、速度、终点和原子知识证据。

### 6. Composition Strategy

- 谁占据画面、谁被留在边缘/前景/背景/负空间；这种分配如何表达关系与信息？
- 视觉焦点何时转移，遮挡、反射、内框或引导线是否有真实空间依据？
- 结束构图应压住、打开、对称、失衡还是保持距离，为什么？

### 7. Lens / Distance

- 摄影机与人物应保持近、中、远何种关系，目的是亲近、隔离、压缩关系、保留环境还是保护表演？
- 需要怎样的脸部几何、背景尺度、前后层次和对焦可读性？
- 焦段倾向只能与摄影机距离和景别共同决定，不把焦段单独当作情绪或透视原因。

### 8. Color & Lighting Strategy

- 已确认光源、时间、天气、材质和资产提供什么颜色与光线依据？
- 色彩/灯光是否需要随剧情发生功能性变化；如果需要，变化由什么真实事件或空间移动触发，承担什么叙事功能？
- 如果不需要变化，哪些综合色温、肤色、中性色、资产固有色与受光方向必须稳定？

### 9. Performance Direction

- 表演应外放还是克制，为什么符合角色与当前关系？
- 情绪通过哪一个主要面部变化和哪一个支持身体/呼吸/手部变化泄漏？
- 谁先反应、谁延迟、谁压住；结束时留下什么可继承的情绪与身体张力？

### 10. Sound Strategy

- 哪个环境声、动作声、对白、呼吸、Foley或剧情内声源承担主声音叙事？
- 哪里加强前景声，哪里削弱声场或保留有理由的近静默？
- 什么声音跨越镜头，什么声音在切点停止，尾部如何服务等待、转折或余韵？

### 11. Editing / Rhythm

- 信息、动作、视线、对白和静默的节拍如何排列？
- 哪一刻应延长观察，哪一刻应切断或加快；视觉高潮与留白分别在哪里？
- 边界使用连续继承、明确断点还是未决安全尾帧；普通运镜不得被当作转场。

### 12. Continuity Risk

- 人物左右、朝向、关系轴、视线、动作阶段、道具、情绪、光态、色态、声音和尾帧中，哪些最容易漂移或翻转？
- 必须锁定哪些首尾状态；哪些变化需要明确断点？
- 为保证关系表达，哪些连续性限制高于视觉技巧？

### 13. Seedance Feasibility

- 当前时长内人物、口型、动作、摄影机、FX、光色变化与声音负荷是否可稳定执行？
- 哪些方向应简化为单一路径、有限动作、少量变化或固定机位？
- 安全降级是什么；若降级仍不能保留导演意图，应返回拆Clip或拆Shot，而不是让Prompt自行调和。

## Mandatory Director Questions

每个Scene / Shot Group在确认前必须能直接回答：

1. 观众在这一段应知道什么、感受什么、等待什么？
2. 人物关系如何通过距离、视线、站位和动作变化被看见？
3. 镜头应该动还是停，为什么；运动由什么触发，在哪里停止？
4. 色彩或灯光是否需要随剧情发生功能性变化；若不变，稳定本身保护什么？
5. 表演应外放还是克制，谁先泄漏、谁压住？
6. 声音在哪里加强、在哪里留白、以什么尾部连接下一节拍？

任一问题只能用风格标签、技巧名称或“为了电影感”回答时，Notes不合格。

## Internal Notes Shape

内部可使用以下紧凑记录；这是决策记录，不是逐步隐式推理，也不是用户可见Template：

```text
Scene / Shot Group:
Source SHOTs:
Narrative Objective:
Audience Experience — Know / Feel / Wait:
Character Relationship:
Blocking:
Camera Strategy — Move / Hold + Reason:
Composition Strategy:
Lens / Distance:
Color & Lighting Strategy — Functional Change / Hold:
Performance Direction — Expressive / Restrained:
Sound Strategy — Emphasis / Restraint / Tail:
Editing / Rhythm — Build / Peak / Negative Space / Boundary:
Continuity Risk:
Seedance Feasibility / Safe Downgrade:
Downstream Non-negotiables:
```

`Downstream Non-negotiables`只保留3—7条必须由STATE-07/08维持的方向，不列Knowledge候选，也不预选1—3项策略。

## Workflow Handoff

### To STATE-07

STATE-07先读取Notes，再组织Clip。Clip内的主导镜头语言、节奏、Blocking延续、视觉高潮与最克制/留白镜头必须能够追溯到Notes；不能为了减少Clip数量把互相冲突的导演方向强行合并。

### To STATE-08

STATE-08读取Confirmed Clip Production Result后，重新读取该Clip对应Notes，先锁定导演方向，再调用Knowledge Application Reflection选择1—3项最合适的实现策略。顺序不可反转：Knowledge只能实现导演意图，不能根据知识库里“有什么技巧”反向改写剧情方向。

### To STATE-09

STATE-09执行Director QA，检查叙事目的、人物关系、Blocking、镜头运动理由、功能性色光、表演尺度、声音/节奏与高潮/留白是否实现，并识别纯炫技或平铺直叙。

## Internal Visibility Rule

默认不向用户输出Director Decision Notes。用户明确要求查看时，只给简洁的导演决策摘要，不展示逐步隐式推理；该摘要仍不得成为后续Seedance Prompt固定章节。

正式Prompt中禁止出现：

- `Director Decision Notes`标题或十三维度表
- “观众应知道 / 感受 / 等待”的内部问答
- 候选方案、被拒绝方案、风险权衡过程或Knowledge文件名
- “因为导演决策所以……”等元说明

正式Prompt只保留能够被模型执行和观察的构图、调度、摄影机、光色、表演、声音、节奏、边界与稳定降级语义。

## Completion Check

- 每个Scene / Shot Group均回答Mandatory Director Questions。
- 十三个维度均有具体结论或Not Applicable理由。
- 镜头动/停、色光变/不变、表演外放/克制和声音加强/留白均有叙事原因。
- 决策没有新增剧情、资产、光源、FX、动作结果或关系事实。
- Notes与Detailed Shot Design、边界合同和Seedance容量兼容；冲突已在STATE-06最小修订。
- STATE-07/08可消费Notes，但Notes没有成为新Template字段。
- Knowledge Reflection只选择实现策略，没有反向主导剧情。
- 最终Prompt无内部决策泄漏。
