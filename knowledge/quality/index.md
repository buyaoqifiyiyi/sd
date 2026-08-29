# Quality Knowledge Index

## Purpose

本目录把分散在Rules、Detailed Shot Design、Clip Production、Video Generation和Review中的质量检查组织为可执行QA。

Quality Knowledge不拥有STATE、不修改上游事实、不定义STATE-08最终Schema。

---

## Routing

- `shot_qa.md`：单镜叙事、资产、动作、表演、摄影、声音、FX和执行稳定性。
- `continuity_pair_qa.md`：所有相邻镜头的边界与继承检查。
- `execution_risk.md`：跨动作、摄影、表演、对白、FX、群体与光学的L1–L4风险分级。
- `prompt_scorecard.md`：STATE-08最终Prompt的硬门槛和100分内部评分。

---

## Stage Mapping

- STATE-06：Shot QA设计前检查与Execution Risk。
- STATE-07：可见证据与相邻镜边界预演。
- STATE-08：Prompt编译前后检查与Scorecard。
- STATE-09：使用templates/16_review_report.md形成正式Review证据。

---

## Output Boundary

QA结果写入Review Report、execution_ledger.md或独立QA附件。

不得把QA标题、分数、L等级、Issue ID或检查表栏目写入templates/10_video_prompt.md。
