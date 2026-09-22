# Regression Scenarios｜Parameters And Delivery Fidelity

本文件是回归集的**参数与交付保真族**：模型与平台的操作参数（时长粒度、计费与选型）、打包器选版、Prompt 校验器的证据判定。这些场景的共同点是它们**只在跨项目复用**——每次平台改价、改时长窗口或改交付约定时，都要能从这里找到"当时怎么判的、依据是什么"。

按编号寻址，不整集通读；编号唯一性由`scripts/validate_sd_film.py`的`check_regression_ids`确定性执行。

---

## R88 Clip Duration Granularity Regression

### R88-A A Fractional Clip Duration Is Not A Submittable Value

输入：一个Seedance 2.5项目的Clip表写着 CLIP-001 `6.5秒`、CLIP-002 `7.5秒`、CLIP-006 `9.5秒`、CLIP-007 `10.5秒`、CLIP-008 `5.5秒`、CLIP-010 `8.5秒`，合计75.0秒；Adapter只声明`duration: 4—30秒`。

PASS：判定这些Clip时长不可提交。平台`duration`参数是 [4, 30] 内的整数秒或 `-1`；小数秒只属于video editing任务继承源片时长的情形。按项目已记录的授权区间与工作目标取整（本例取floor得72.0s，等于项目自己的72.0s工作目标），逐Clip重算时长与Prompt时间线，写回Clip Plan、全片索引与两个Ledger，按`references/artifact_revision_contract.md`建立新Revision（旧Revision记Superseded、下游记Invalidates），并在Adapter的`O｜Operational Parameter`补上整数秒约束与取证日期。**该约束只作用Clip目标时长**：Seedance 2.5时间线的中间阶段边界是提示词文本，可以是小数（见R88-C），只有末阶段末端边界仍需整数并与确认时长相等。

FAIL：把 `6.5秒` 当作可提交参数直接生成；只改Prompt数字而不改时间线；把0.5秒余量留在末尾静帧句里继续声明该时长；不经用户确认就改变总时长或剧情容量；或只在报告里口头提醒而不修计划层与交付物。

### R88-B Integer Rounding Must Not Leave A Timeline Gap

输入：CLIP-006 原时长 `9.5秒`，时间线为 `[0—2] [2—5] [5—7] [7—9]`；取整到10秒时把余量插入中间，得到 `[0—2] [2—4] [5—7] [7—10]`。

PASS：阶段必须严格递进、无重叠、无断档。余量放在末段（吸收为结尾保持），或按邻近节点整体重算，使首尾相接；改完用`scripts/validate_prompt_package.py`复验，`INVALID: 时间线阶段必须严格递进且无重叠/断档`必须消失。

FAIL：只让首段与末段对上就交付；把中间断档当作"模型会自动补"；或为了让数字对上而删除、合并阶段或改变剧情动作。

### R88-C Fractional Intermediate Stage Boundaries Are Legal

输入：一个10秒Seedance 2.5 Clip的时间线写作 `[0—3.2秒] [3.2—7秒] [7—10秒]`，中间边界落在3.2秒。

PASS：判定合法并交付。平台`duration`参数只约束Clip目标时长，而目标时长只由时间线**末阶段的末端边界**承担；中间边界是提示词文本，没有对应的可提交参数，因此`3.2秒`与`3秒`同样可用，只要求严格递进、无重叠无断档。末阶段末端`10秒`仍必须是整数且等于Confirmed Clip Production Plan的确认时长。仍按`rules/03_prompt_rules.md`的数值执行价值规则检查精度：`3.2秒`这类标住真实节拍的边界保留，`3.27秒`这类无可见收益的精度压缩。

FAIL：把中间小数边界判为不可提交参数并强制取整；或用"时间线只能写整数秒"为由改写已确认的动作节拍；或让末阶段末端跟随中间精度变成小数，使目标时长脱离平台参数窗口。

---

## R89 Packager Version Resolution Regression

### R89-A Active Version Decides Between Two Copies Of One Locked Name

输入：Registry 写着 `Active Version: v002`，而 `CHAR-001｜Identity.png` 在 `canonical/CHAR-001/v001/identity/` 与 `canonical/CHAR-001/v002/identity/` 各有一份。

PASS：打包器在候选文件上先按 Registry 的 Active Version 过滤，选中 v002 那份并复制进包；被忽略的其他版本以非阻断提示写明"按Active Version v002选择…另有N个同名文件属于其他版本，已忽略"。

FAIL：报 ambiguity 并放弃该资产（等于让 Registry 的 Active Version 形同虚设）；按路径排序取第一个；或因为存在多版本就要求用户重命名文件。

### R89-B Version Filtering Does Not Excuse Same-Version Duplicates

输入：`Active Version: v002` 下 `state-药岩/` 与 `state-负伤/` 各有一份 `CHAR-001｜State.png`，Registry 只写裸文件名。

PASS：仍判 FAIL，指出 Active Version 下仍有多个同名文件，必须在 Registry 中补足以区分的 View Code / Purpose 或状态键。

FAIL：因为做过版本过滤就把同版本内的同名当作已消歧，任意选一份打进包。

---

## R90 Plane Token False-Positive Regression

### R90-A Shot Language Is Not Mirror Evidence

输入：Seedance 2.5 Prompt 含 `画面与镜头：固定机位，镜头缓慢推进`、`运镜保持平稳，分镜数不变`，环境参考只列母参考 `ENV-001｜…_ENV-01`。

PASS：不产生窗 / 玻璃 / 镜面或反射平面提示。裸 `镜` 不是平面词——`画面与镜头`、`运镜`、`分镜` 是每个阶段都有的镜语字段，一旦被当成平面证据，一部没有镜子的片子每个 Clip 都会弹同一条提示，真实风险被噪声淹没。平面证据只认 `镜子 / 镜面 / 反光镜 / 倒影 / 反射 / 反光 / 玻璃 / 窗` 这类实际表面词。

FAIL：因为 `镜头` 里含 `镜` 而报"出现反射平面"；或反向地把 `人物看向镜面` 也放过。

### R90-B A Plane Needs A Side Lock Or A Reflection Decision

输入：Prompt 出现 `窗` / `玻璃` / `镜面` 且环境参考只列母参考，但文字未写"人物在结构的哪一侧"也未写反射是否表现。

PASS：给出非阻断提示，要求补反向 / 侧向 View 或在字段里写明平面关系与反射策略；写成 `人物在窗内侧走过，不表现反射` 后提示消失。

FAIL：把缺锁当阻断错误拒绝交付，或提示后仍默认主体与反射副本都会正确生成。

---

## R93 Model Cost Alternative Regression

### R93-A Rates Come From The Truth Table Or They Do Not Exist

输入：项目交付画幅仍为`Pending`，用户拟比较 Seedance 2.5 与 Seedance 2.0 的执行成本。

PASS：从`references/platform_pricing.md`取已登记档位（2.5：480p 0.103 / 720p 0.231 / 1080p 0.569 USD/秒；2.0：0.07 / 0.15 / 0.37 / 0.78），**在同一分辨率与画幅下**并列并写明币种、分辨率与是否含视频输入；交付画幅未定时不替用户选定画幅。MiniMax H3 与 MiniMax 点数换算因未公开单价的，写`待用户提供`；已过期的限时折扣（2.5 1080p 28% off，2026-09-17 结束）不得继续按 0.41 USD/秒 计算。

FAIL：用"2.5 更贵 / 差不多"这类定性说法代替数字；拿不同分辨率的单价直接比大小；把第三方博客或推算值写成官方价；沿用已过期的折扣价；或未取得 H3 单价就编一个。

### R93-B A Cost Finding Never Replaces The User's Model

输入：某Clip的能力使用等级判定为`OVERQUALIFIED`，用户偏好 Seedance 2.5 且未硬锁。

PASS：交付 Prompt 照常按 2.5 编译，同时给出成本替代提示与原价对比；改不改模型由用户决定，走`Project Video Model Preference`变更与受影响STATE-07/08重跑。提示不写入Clip Plan或最终Prompt字段。

FAIL：因为价格更高就自动降级模型、拒绝出Prompt、把`OVERQUALIFIED`当成`RETURN`，或把成本字段写进交付物。

### R93-C A Named Model Is A Preference, Not A Lock

输入：用户在项目请求里说"用 Seedance 2.5"，未说只能用2.5。

PASS：写`Project Video Model Preference: Seedance 2.5`与`Project Video Model Lock: PREFERENCE`，STATE-06后按每Clip真实能力需求复核并允许提出更便宜的可行候选；只有用户明确表示不考虑其他模型时才写`HARD`，此后不再反复推荐替代。能力判定看必须能力与参考容量，不只看时长或图片数量。

FAIL：把"用2.5"直接当成全程锁定而不再评估；或反向地把硬锁也当偏好、反复推荐替代方案。
