const stageDefinitions = [
  { id: "STATE-00", label: "项目设定", artifact: "项目启动卡", workflow: "01_project_setup_workflow.md", description: "建立项目身份、制作目标与可恢复的状态基线。", summary: "明确作品定位、受众和交付边界，为后续工序建立唯一的项目事实来源。", checklist: ["项目名称已确认", "创作目标已填写", "项目状态已初始化"] },
  { id: "STATE-01", label: "剧本分析", artifact: "制作版剧本提案", workflow: "02_script_analysis_workflow.md", description: "将原始剧本转为可执行的制作版提案，并在确认后锁定故事事实。", summary: "雨夜的雾港，一封迟到十年的信迫使返乡的苏岑重新面对父亲失踪的真相。叙事保持悬疑与克制，核心冲突是她在“离开”与“追问”之间的选择。", checklist: ["故事因果已梳理", "人物动机已明确", "制作版剧本已确认"] },
  { id: "STATE-02", label: "资产发现", artifact: "资产发现清单", workflow: "03_asset_discovery_workflow.md", description: "盘点角色、环境、道具及其连续性风险，确定资产开发范围。", summary: "识别需要建立 Canonical Reference 的角色、雾港码头、旧邮局和关键道具“蓝色信封”。", checklist: ["角色资产已枚举", "环境资产已枚举", "优先级已确认"] },
  { id: "STATE-03", label: "资产开发", artifact: "资产设计包", workflow: "04_character_asset_workflow.md", description: "开发可被后续镜头复用的角色、环境与道具资产。", summary: "为每项关键资产建立可追溯的描述、参考图和确认版本；图像模型选择在本阶段完成。", checklist: ["图像模型已选择", "候选资产已生成", "Canonical 版本已确认"] },
  { id: "STATE-04", label: "视觉开发", artifact: "视觉方向锁定", workflow: "07_visual_development_workflow.md", description: "将锁定的故事与资产转译为整体视觉语法。", summary: "定义冷湿色调、低饱和港口雾气和克制的观察式镜头，使全片保持一致的情绪与质感。", checklist: ["色彩方向已确定", "光线原则已确定", "视觉方向已确认"] },
  { id: "STATE-05", label: "场景拆解", artifact: "场景拆解表", workflow: "08_scene_breakdown_workflow.md", description: "把制作版剧本拆成可调度的场景、动作单位与连续性要求。", summary: "按叙事目标和空间连续性形成场景清单，标记每场需要的已锁定资产与关键动作。", checklist: ["场景边界已确认", "资产依赖已标记", "连续性风险已记录"] },
  { id: "STATE-06", label: "详细镜头设计", artifact: "详细镜头脚本", workflow: "09_shot_design_workflow.md", description: "为每个场景设计表演、空间关系、镜头目的和镜头语言。", summary: "把场景意图落实到可拍摄的镜头设计；完成后才选择视频模型适配器。", checklist: ["镜头目的完整", "空间调度已确认", "模型适配范围已选择"] },
  { id: "STATE-07", label: "Clip 制作", artifact: "Clip 制作计划", workflow: "10_clip_production_workflow.md", description: "保护剧情和空间事实，组织为模型可执行的 Natural Unit 与 Execution Clip。", summary: "根据选定模型的时长和参考能力整合 Clip，但不改写已锁定的剧本、资产或镜头意图。", checklist: ["Natural Unit 已建立", "执行边界已确认", "参考预算已审计"] },
  { id: "STATE-08", label: "提示词与生成", artifact: "视频生成提示词包", workflow: "11_video_generation_workflow.md", description: "按唯一模型 Adapter 编译最终提示词，并提交或导出生成任务。", summary: "仅将已经确认的 Execution Clip 投影成模型提示词；视频提示词不自动加入非剧情内配乐。", checklist: ["Adapter 已匹配", "最终 Prompt 已审阅", "生成任务已提交"] },
  { id: "STATE-09", label: "审核", artifact: "审核报告", workflow: "13_review_workflow.md", description: "对生成结果进行连续性、镜头和执行风险审核，决定通过或最小范围返工。", summary: "只有真实查看过结果且审核通过，项目才会完成；需修订时回到受影响最小工序。", checklist: ["生成结果已查看", "连续性已核对", "审核结论已确认"] }
];

const stored = JSON.parse(localStorage.getItem("sd-film-demo-project") || "null");
const state = stored || { projectName: "雾港来信", brief: "雨夜的雾港，一封迟到十年的信迫使返乡的苏岑重新面对父亲失踪的真相。", stage: 1, revision: 3, activity: ["完成制作版剧本提案", "锁定故事核心冲突", "创建项目《雾港来信》"] };
const $ = (selector) => document.querySelector(selector);
const stageNav = $("#stageNav");
const toast = $("#toast");
let toastTimer;

function persist() { localStorage.setItem("sd-film-demo-project", JSON.stringify(state)); }
function say(message) { clearTimeout(toastTimer); toast.textContent = message; toast.classList.add("show"); toastTimer = setTimeout(() => toast.classList.remove("show"), 2600); }
function stageStatus(index) { return index < state.stage ? "已确认" : index === state.stage ? "待确认" : "未开始"; }

function renderNav() {
  stageNav.innerHTML = stageDefinitions.map((item, index) => `
    <button class="stage-button ${index === state.stage ? "active" : ""} ${index < state.stage ? "complete" : ""}" data-stage="${index}">
      <span class="stage-index">${index < state.stage ? "✓" : String(index).padStart(2, "0")}</span><span class="stage-label">${item.label}</span>
    </button>`).join("");
  stageNav.querySelectorAll("button").forEach((button) => button.addEventListener("click", () => { state.stage = Number(button.dataset.stage); persist(); render(); }));
}

function renderActivity() {
  const entries = state.activity.slice(0, 4);
  $("#activityList").innerHTML = entries.map((entry, index) => `<div class="activity"><span class="activity-mark">${index === 0 ? "✓" : "•"}</span><p>${entry}<br><small>${index === 0 ? "当前版本" : "项目记录"}</small></p><time>${index === 0 ? "刚刚" : `${index + 1} 小时前`}</time></div>`).join("");
}

function render() {
  const item = stageDefinitions[state.stage];
  const isComplete = state.stage === stageDefinitions.length - 1;
  $("#projectNameSide").textContent = state.projectName;
  $("#projectNameTop").textContent = state.projectName;
  $("#stageEyebrow").textContent = `${item.id} · ${item.workflow.replace("_workflow.md", "").replaceAll("_", " ").toUpperCase()}`;
  $("#stageTitle").textContent = item.label;
  $("#stageDescription").textContent = item.description;
  $("#artifactTitle").textContent = item.artifact;
  $("#artifactStatus").textContent = stageStatus(state.stage);
  $("#artifactStatus").classList.toggle("complete", isComplete);
  $("#artifactBody").innerHTML = `<h3>工作摘要</h3><p>${state.stage === 1 ? state.brief : item.summary}</p><div class="fact-grid"><div class="fact"><small>工作流</small><strong>${item.workflow}</strong></div><div class="fact"><small>状态</small><strong>${stageStatus(state.stage)}</strong></div><div class="fact"><small>版本</small><strong>REV-${String(state.revision).padStart(4, "0")}</strong></div></div>`;
  $("#revision").textContent = `REV-${String(state.revision).padStart(4, "0")} · 刚刚更新`;
  $("#currentState").textContent = item.id;
  $("#scriptStatus").textContent = state.stage < 2 ? "Optimized Proposal" : "Production-Locked";
  $("#nextWorkflow").textContent = isComplete ? "Project Complete / Post" : stageDefinitions[state.stage + 1].workflow;
  $("#progressText").textContent = `${state.stage + 1} / ${stageDefinitions.length} 阶段`;
  $("#progressFill").style.width = `${((state.stage + 1) / stageDefinitions.length) * 100}%`;
  $("#progressHint").textContent = isComplete ? "审核通过后，项目将标记为完成。" : `确认后，将进入${stageDefinitions[state.stage + 1].label}。`;
  $("#checkCount").textContent = `${Math.min(2, item.checklist.length)} / ${item.checklist.length}`;
  $("#checklist").innerHTML = item.checklist.map((check, i) => `<li><span class="check-dot ${i < 2 ? "done" : ""}">${i < 2 ? "✓" : ""}</span><span>${check}</span></li>`).join("");
  $("#advanceStage").innerHTML = isComplete ? "标记审核通过 <span>✓</span>" : "确认并下一步 <span>→</span>";
  renderNav(); renderActivity();
}

$("#advanceStage").addEventListener("click", () => {
  const current = stageDefinitions[state.stage];
  if (state.stage < stageDefinitions.length - 1) { state.activity.unshift(`确认${current.label}，进入${stageDefinitions[state.stage + 1].label}`); state.stage += 1; state.revision += 1; say("已保存确认记录，并进入下一工序"); }
  else { state.activity.unshift("审核通过，项目制作流程完成"); state.revision += 1; say("审核已标记为通过"); }
  persist(); render();
});
$("#editStage").addEventListener("click", () => say("编辑器将在后端工件接口接入后打开；当前为前端原型。"));
$("#viewArtifact").addEventListener("click", () => say("工件详情视图将在下一迭代接入。"));
$("#openProjectDialog").addEventListener("click", () => $("#projectDialog").showModal());
const projectDialog = $("#projectDialog");
function closeProjectDialog() { projectDialog.close(); $("#projectForm").reset(); }
document.querySelectorAll("[data-close-project-dialog]").forEach((button) => button.addEventListener("click", closeProjectDialog));
projectDialog.addEventListener("click", (event) => { if (event.target === projectDialog) closeProjectDialog(); });
$("#projectForm").addEventListener("submit", (event) => {
  event.preventDefault();
  const name = $("#newProjectName").value.trim(); const brief = $("#newProjectBrief").value.trim();
  if (!name || !brief) return;
  Object.assign(state, { projectName: name, brief, stage: 0, revision: 1, activity: ["初始化 STATE-00 项目状态", `创建项目《${name}》`] });
  persist(); closeProjectDialog(); render(); say("项目已创建，状态基线已保存");
});
render();
