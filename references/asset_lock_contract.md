# SD Film Asset Lock Contract

## Purpose

本文件定义 `asset_registry.md` 中正式资产的Active Version、一致性锁、Canonical Reference和变更路由。

它不创建资产，不替代STATE-03 Asset Workflows，也不把参考图置于Registry之外形成第二真源。

---

## Authority

资产身份与当前生效版本只由Active Project Root中的 `asset_registry.md` 持有。

参考图只有在Registry中被登记为Canonical Reference并绑定到Active Version后，才具有下游权威性。

---

## Unified Priority

下游读取资产时统一使用：

```text
用户明确批准的新资产Revision
→ Asset Registry中的Active Version与Canonical References
→ Project Bible中的项目级不可变规则
→ 已确认阶段交付物
→ 用户当前补充的临时说明
→ 未确认文字推断
→ AI自由生成
```

用户当前补充若改变已锁资产，不直接覆盖下游；先返回对应STATE-03 Asset Workflow创建新Revision并获得批准。

---

## Required Record

每个正式CHAR、ENV、PROP、FX记录必须包含：

```text
Asset ID
Name
Type
Asset Tier
Board ID
Item ID
Status
Active Version
Canonical References
Immutable Traits
Mutable State Dimensions
Dependencies
Continuity State
Source / Provenance
Approved By / Approval Basis
Approved At
Supersedes
Downstream Usage
Visual Production Status
Prompt Status
Image Status
Confirmed Status
Prompt Revision
Image Prompts
Prompt Confirmation
Candidate References
Image Confirmation
```

`Visual Production Status`与资产版本生命周期的`Status`是两个独立字段。前者只使用：

```text
Prompt Draft
Prompt Confirmed
Image Generated
Asset Confirmed
```

固定迁移顺序为`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`。Prompt Draft必须等待用户确认当前Prompt Revision；Prompt Confirmed才允许调用图片生成；Image Generated只允许登记Candidate References；Asset Confirmed必须有用户对图片的确认依据，才可写入Canonical References并切换Active Version。

### Two-Tier Record Semantics

CHAR、ENV、PROP的`Asset Tier`只使用`Core`或`Support`。Core采用独立资产包；Support采用同类型Support Reference Board。正式FX Asset本次不强制套用Two-Tier，相关字段可写`Not Applicable`。

- Core：`Board ID: Not Applicable`、`Item ID: Not Applicable`。
- Support：必须记录全局稳定Board ID、板内稳定Item ID、Board Name、Included Asset IDs、Item ID Mapping，以及Canonical Board Reference中的区域/标签对应关系。
- Board ID示例：`BOARD-CHAR-001`、`BOARD-ENV-001`、`BOARD-PROP-001`。Item ID示例：`A-01`、`A-02`、`A-03`；后续按`<Board Name> / <Board ID> / <Item ID>`引用。确认后的Item ID不得重排、复用或静默转给其他资产。
- 同一Board只容纳同一资产类型及相近生产用途，不得跨CHAR / ENV / PROP混板。建议每板4—9个对象；不足4个不得虚构填充，超过9个拆板。

`Prompt Status`、`Image Status`与`Confirmed Status`是便于Registry核对的明确投影，不得形成第二套生命周期：

```text
Prompt Draft     → Prompt Status: Draft     / Image Status: Not Generated / Confirmed Status: No
Prompt Confirmed → Prompt Status: Confirmed / Image Status: Not Generated / Confirmed Status: No
Image Generated  → Prompt Status: Confirmed / Image Status: Candidate     / Confirmed Status: No
Asset Confirmed  → Prompt Status: Confirmed / Image Status: Confirmed     / Confirmed Status: Yes
```

Core Asset、Support Board和Support Item均只有在用户明确确认对应图片后才能写`Confirmed Status: Yes`。Support的整板确认必须能核对Board ID与Item ID；部分Item未获明确批准时，该Item继续为`No`，不得由含糊的整板状态自动升级。

CHAR记录还允许在同一Active Version内保存由用户显式调用`AUDIO / SEED-AUDIO Voice Asset`模块创建的文字型角色音色子资产：

```text
Voice Asset Status
Voice Profile
Voice Profile Basis
Voice Sample Prompt
Voice Audio Reference Status
Voice Audio Reference
```

`Voice Asset Status`只使用`Confirmed`或`Pending`；字段不存在表示用户尚未显式创建声音资产，不等于错误，也不得触发补齐。Voice Profile与Voice Sample Prompt只有在用户明确请求音色制作时才可写入，不创建独立视觉Asset ID。普通Character Asset、角色有对白、视频制作、Clip或STATE-08均不得自动创建、更新或标记`Not Required`。

`Voice Audio Reference Status`只使用`Not Generated`、`Candidate`、`Confirmed`或`Not Required`。它不替代`Voice Asset Status`。角色候选音色确定后，建议从已授权候选中截取15—30秒干净、单说话者、无背景音乐、无环境声、无音效的人声作为后续Audio Reference；登记时必须记录受控路径或外部ID、时长、语言、同一CHAR Version、来源、生成/录制方式、授权依据与批准信息。未确认候选不得标记`Confirmed`，不得自动成为视觉Canonical Reference，也不得触发独立资产ID。

只有用户显式调用AUDIO模块并确认结果后，Active CHAR Version才具有`Confirmed` Voice Profile。角色有对白不要求必须创建Voice Profile；默认假定外部已有可用音色资源，声音资产字段缺失不阻塞STATE-03至STATE-09，也不得使任何下游流程自动进入AUDIO模块或返回Character Asset补齐。基础音色身份的变化遵守本合同的Version与Change Protocol；单场情绪、距离、体力或剧情授权的特殊状态变化属于Dialogue Performance，不自动创建新角色版本。

同一角色跨集制作时，若存在绑定当前Active CHAR Version的`Confirmed` Voice Audio Reference且目标工具支持Audio Reference，可由输入音频自身锁定声音身份；文字Voice Profile仍作为声音资产内部语义基线。二者默认都不投影到STATE-08视频Prompt，也不得用“已有音色”“参考音色锁定”“未建立音色资产”等状态文案占位。只有用户明确要求把声音控制写进当前视频模型Prompt时，才按`Source Carries State, Prompt Carries Delta`最小引用适用Reference或必要Voice Profile特征；不得在台词、音效或其他字段重复Voice characteristics、音高、声线、音域、共鸣、语速或音色质感。基础音色身份发生实质变化时，也只有用户显式要求更新声音资产才进入AUDIO模块创建Candidate并重新确认。

允许的Status：`Planning`、`Generating`、`Candidate`、`Approved`、`Active`、`Superseded`、`Archived`。

只有一个Version可以是Active。Approved候选不自动等于Active。

---

## Version Format

资产实体ID保持稳定，例如 `CHAR-001`。

版本独立记录为 `v001`、`v002`……。引用时使用：

```text
CHAR-001@v001
ENV-002@v003
```

不得把 `CHAR-001-v2` 当作新的角色实体ID。

---

## Canonical Reference Rule

每个Canonical Reference必须记录：路径或受控外部ID、用途、绑定Version、允许的变换、来源和权利/授权说明（适用时）。

用途只使用：Identity / Costume / Scale / Layout / Material / State / FX Phase。

未经登记的附件只能作为Candidate Reference，不得覆盖Active Version。

图像工具新生成或用户外部回传的图片，在用户确认之前也只能作为Candidate Reference。`Image Generated`不等于`Asset Confirmed`；Prompt确认不等于图片确认。只有Image Confirmation记录了明确批准的Candidate Reference与当前Version后，才可把该图片升级为Canonical Reference。

---

## Canonical Character Appearance And Form Lock

当用户提供角色资产并明确指定或确认其为该角色外观基准，或CHAR记录已经具有Active Version与Canonical References时，该Active角色资产包及其Canonical References共同构成该角色后续生产的唯一外观基准。用户明确批准的新角色资产Revision在切换Active Version前按Change Protocol处理；登记期间保持受保护，不得被临时文字、风格图、构图图、新生成结果或AI推断改写。

CHAR的外观与形态Immutable Traits至少覆盖：

- 脸型、五官、年龄感、发型、发色与头饰
- 体型、身高比例、身体比例与可识别轮廓
- 服装形制、结构、关键材质识别、主配色与辅助配色
- 物种形态、羽毛、毛发、皮肤、鳞片或其他物种识别特征
- 非人角色的身体结构、肢体组织、头身关系与非拟人化边界
- 该Active Version登记的其他身份性视觉特征

上述锁定贯穿角色设定图、动作状态图、比例图、场景示意图、Storyboard/分镜参考图、海报、Key Art、封面、Detailed Shot Design、Clip Production、图片/视频Prompt、Seedance Prompt、最终视频生成与Review。任何阶段只能引用当前Active CHAR Version及其适用Canonical References，不得用下游产物反向重定义CHAR身份。

仅改变动作、姿势、表情、机位、景别、构图或镜头运动时，只允许改变对应表演与摄影维度。不得借这些请求改变脸、年龄、发型、头饰、体型、比例、服装基础、配色、物种或非人身体结构。剧情授权的污损、湿润、受伤、伪装、换装、年龄阶段或变形只在已登记的Mutable State Dimensions与对应Canonical状态资产范围内合法；超出范围必须创建Candidate Version并重新确认。

新参考或生成结果与锁定资产冲突时，锁定资产优先，冲突结果不得进入Canonical Reference、Confirmed Artifact或最终交付。不得混合两套外貌求折中。只有用户明确批准并正式切换的新Active Version可以取代旧基准。非人角色同样适用：锁定为孔雀本体的角色不得被改为人形、半人形或其他拟人化结构，除非该变化已作为新Version或明确Mutable State获得用户批准。

---

## Immutable And Mutable Boundary

Immutable Traits用于锁定身份，例如脸型、身体比例、环境结构、道具结构、FX视觉身份。

Mutable State Dimensions只允许剧情授权的状态变化，例如湿润、污渍、损伤、开合、持有者、天气状态或FX生命周期阶段。

状态变化不创建新资产身份；设计变化必须创建新Version。

---

## Change Protocol

1. 记录变更请求和Affected IDs。
2. 返回对应Asset Workflow创建Candidate Version。
3. 检查依赖、下游镜头和连续性影响。
4. 批准后切换Active Version。
5. 旧Version标记Superseded但不删除。
6. project_status.md创建新Revision并登记需要重检的下游产物。

---

## Validation Invariants

- Asset ID命名空间合法且唯一。
- 每个正式视觉资产必须具有合法的Visual Production Status，并按`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`单向推进；实质修改Prompt后必须重新确认。
- 每个CHAR、ENV、PROP必须具有合法Asset Tier；Core的Board ID / Item ID为Not Applicable，Support两字段必填且映射唯一。
- Prompt Status、Image Status与Confirmed Status必须与Visual Production Status严格一致；任何图片确认前的Core、Support Board或Support Item都必须为`Confirmed Status: No`。
- Support Canonical Reference必须绑定Board ID及明确Item ID区域/标签；不得跨资产类型混板、确认后重排Item ID或只凭Board存在推定全部Item confirmed。
- Prompt Confirmed、Image Generated与Asset Confirmed必须记录当前Prompt Revision及Prompt Confirmation；Prompt Draft不得触发图片生成。
- Image Generated必须有Candidate References，但不得仅因此拥有Canonical References或Active状态。
- Asset Confirmed必须记录Image Confirmation，且批准对象必须来自当前Version的Candidate References；此时才允许Status为Active并登记Canonical References。
- Active/Approved资产必须有Version、Canonical Reference或明确无图参考依据、Immutable Traits和Approval Basis。
- 同一Asset ID不得同时存在两个Active Version。
- Canonical Reference必须绑定存在的Version。
- Supersedes不得指向自身或形成循环。
- 下游引用的版本必须存在且未被无说明地替换。
- Voice Profile只在用户显式调用AUDIO模块后要求完整；角色有对白而没有Voice Profile是合法状态，不阻塞下游，也不得自动返回Character Asset或AUDIO模块。
- Confirmed Voice Audio Reference必须绑定存在的CHAR Version，并具有15—30秒干净单人声、来源、授权与批准记录；Candidate不得作为下游锁定Reference。
- STATE-08默认省略`音色特征：`及所有声音身份状态文字；已有Confirmed Voice Audio Reference或Confirmed Voice Profile也不改变此默认。只有用户明确要求把声音控制写进当前视频模型Prompt时才允许最小投影，并禁止跨字段重复或临时推导。
- 每个Active CHAR Version必须把Canonical Character Appearance And Form Lock所列的适用身份特征登记为Immutable Traits，或通过Canonical References明确锁定；不得把物种形态或非人身体结构遗漏为可自由推断项。
- 动作、姿势、表情、机位、景别、构图或镜头运动变更不得触发未授权的CHAR外观重设计。
- 与Active CHAR Version冲突的新参考或生成结果不得成为Confirmed Artifact、Canonical Reference或最终视频交付；Review必须拒绝外貌、形态、服装基础、配色、物种或非人结构漂移。

---

## Final Principle

Registry不是资产清单，而是资产身份、当前生效版本和下游一致性锁的唯一控制面。
