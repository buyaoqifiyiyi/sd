import { createServer } from "node:http";
import { randomUUID } from "node:crypto";
import { mkdir, readFile, readdir, stat, writeFile } from "node:fs/promises";
import { createReadStream } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const projectsRoot = path.join(here, "data", "projects");
const port = Number(process.env.PORT || 4173);
const maxUploadBytes = 50 * 1024 * 1024;
const allowedUploadExtensions = new Set([".txt", ".md", ".pdf", ".doc", ".docx", ".rtf", ".csv", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".webm", ".wav", ".mp3"]);
let openAiApiKey = process.env.OPENAI_API_KEY || "";
let openAiModel = process.env.OPENAI_MODEL || "gpt-5.6-terra";
let compatibleApiKey = "";
let compatibleBaseUrl = "";
let compatibleModel = "";
const modelAdapters = [
  { id: "openai-terra", label: "GPT-5.6 Terra", provider: "openai", model: "gpt-5.6-terra", multimodal: true, outputMode: "agent", description: "OpenAI Responses API；可分析项目文字和参考图片。" },
  { id: "openai-luna", label: "GPT-5.6 Luna", provider: "openai", model: "gpt-5.6-luna", multimodal: true, outputMode: "agent", description: "OpenAI Responses API；较轻量的文字与图片理解。" },
  { id: "compatible-text", label: "OpenAI 兼容文本模型", provider: "compatible", multimodal: false, outputMode: "prompt", description: "兼容 /chat/completions 的外部接口；只接收文本并输出提示词。" },
  { id: "built-in-image-prompt", label: "Built-in Image 提示词包", provider: "prompt", multimodal: false, outputMode: "prompt", stage: "image", description: "STATE-03 资产开发可用；当前网页仅交付内置图像路线的提示词，不会伪称已生成图片。" },
  { id: "midjourney-prompt", label: "Midjourney 提示词包", provider: "prompt", multimodal: false, outputMode: "prompt", stage: "image", description: "STATE-03 资产开发可用；只交付外部 Midjourney 提示词。" },
  { id: "seedance-25-prompt", label: "Seedance 2.5 提示词包", provider: "prompt", multimodal: false, outputMode: "prompt", stage: "video", description: "STATE-07 之后可用；仅输出 Seedance 2.5 提交提示词包。" },
  { id: "minimax-h3-prompt", label: "MiniMax H3 提示词包", provider: "prompt", multimodal: false, outputMode: "prompt", stage: "video", description: "STATE-07 之后可用；仅输出 MiniMax H3 提交提示词包。" }
];
const stages = [
  ["STATE-00", "项目设定", "项目启动卡", "01_project_setup_workflow.md", "建立项目身份、制作目标与可恢复的状态基线。", "确认项目名称、原始创意、目标受众与交付边界。"],
  ["STATE-01", "剧本分析", "制作版剧本提案", "02_script_analysis_workflow.md", "将原始剧本转为可执行的制作版提案，并在确认后锁定故事事实。", "分析故事因果、人物动机与制作范围，产出待确认的制作版剧本。"],
  ["STATE-02", "资产发现", "资产发现清单", "03_asset_discovery_workflow.md", "盘点角色、环境、道具及其连续性风险，确定资产开发范围。", "识别需要建立 Canonical Reference 的角色、环境与关键道具。"],
  ["STATE-03", "资产开发", "资产设计包", "04_character_asset_workflow.md", "开发可被后续镜头复用的角色、环境与道具资产。", "为每项关键资产建立描述、参考图、候选版本与确认记录。"],
  ["STATE-04", "视觉开发", "视觉方向锁定", "07_visual_development_workflow.md", "将锁定的故事与资产转译为整体视觉语法。", "定义色彩、光线、材质、镜头气质与全片视觉一致性。"],
  ["STATE-05", "场景拆解", "场景拆解表", "08_scene_breakdown_workflow.md", "把制作版剧本拆成可调度的场景、动作单位与连续性要求。", "按叙事目标、空间连续性和资产依赖形成场景清单。"],
  ["STATE-06", "详细镜头设计", "详细镜头脚本", "09_shot_design_workflow.md", "为每个场景设计表演、空间关系、镜头目的和镜头语言。", "完成导演设计后才允许选择视频模型的执行适配器。"],
  ["STATE-07", "Clip 制作", "Clip 制作计划", "10_clip_production_workflow.md", "保护剧情和空间事实，组织为模型可执行的 Natural Unit 与 Execution Clip。", "整合时长、边界与参考输入，不改写已锁定的上游创作事实。"],
  ["STATE-08", "提示词与生成", "视频生成提示词包", "11_video_generation_workflow.md", "按唯一模型 Adapter 编译最终提示词，并提交或导出生成任务。", "仅将确认的 Execution Clip 编译为模型提示词；不自动添加非剧情内配乐。"],
  ["STATE-09", "审核", "审核报告", "13_review_workflow.md", "审核生成结果的连续性、镜头语言和执行风险，决定通过或最小范围返工。", "真实查看生成结果后，才能标记通过；否则返回最小受影响工序。"]
].map(([id, label, artifact, workflow, description, summary]) => ({ id, label, artifact, workflow, description, summary }));
const now = () => new Date().toISOString();
const projectDir = (id) => path.join(projectsRoot, id);
const projectFile = (id) => path.join(projectDir(id), "project.json");
function statusFor(project) {
  const stage = stages[project.currentStage];
  const next = stages[project.currentStage + 1];
  const scriptStatus = project.currentStage === 0 ? "Source Material" : project.currentStage === 1 ? "Optimized Proposal" : "Production-Locked";
  const uploadLines = project.uploads?.length ? project.uploads.slice(0, 8).map((file) => `- ${file.kind}: ${file.name} (${file.size} bytes)`).join("\n") : "None";
  return `# SD Film Project Status

Status Schema Version: 2
Project ID: ${project.id}
Project Name: ${project.name}
Current State: ${stage.id}
State Status: ${project.reviewPassed ? "COMPLETE" : "IN_PROGRESS"}
Script Status: ${scriptStatus}
Active Workflow: ${project.reviewPassed ? "Project Complete / Post" : stage.workflow}
Last Completed Step: ${project.lastCompletedStep || "None"}
Last Successful Checkpoint: ${project.lastCheckpoint || "Project initialized"}
Next Workflow: ${project.reviewPassed ? "Project Complete / Post" : next?.workflow || "13_review_workflow.md"}
Return Route: ${project.returnRoute || "None"}
Pending Decision: ${project.reviewPassed ? "None" : project.returnRoute ? `Reconfirm ${stage.label}; then recheck affected downstream work` : `Confirm ${stage.label}`}
Revision ID: REV-${String(project.revision).padStart(4, "0")}
Updated At: ${project.updatedAt}

## State Control
- Selected State Source: ${project.id}/project_status.md
- Source Selection Reason: Local web project workspace
- Automation Policy: STANDARD
${project.returnRoute ? "- Return After Completion: STATE-09 Review" : ""}
${modelStateControl(project)}

## Completed Tasks
${project.completedStages.length ? project.completedStages.map((id) => `- ${id}`).join("\n") : "None"}

## Pending Tasks
${project.reviewPassed ? "None" : stages.slice(project.currentStage).map((item) => `- ${item.id} ${item.label}`).join("\n")}

## Active Artifacts
- ${stage.artifact} · REV-${String(project.revision).padStart(4, "0")}
${uploadLines}

## Confirmed Assets
None

## Visual Direction Lock
None

## Continuity And Open Risks
- ${modelRisk(project)}
${project.returnRoute ? `- Downstream artifacts are preserved but require recheck: ${(project.invalidatedStages || []).join(", ")}.` : ""}

## Review Control
- Review Result: ${project.reviewPassed ? "PASS" : project.returnRoute ? "REVISE" : "NOT_REVIEWED"}
- Affected IDs: ${project.invalidatedStages?.length ? project.invalidatedStages.join(", ") : "None"}
- Return Route: ${project.returnRoute || "None"}
- Recheck Scope: ${project.recheckScope || "None"}
- Review Artifact: None

## Version History
${project.activity.map((entry) => `- ${entry.at}: ${entry.message}`).join("\n")}
`; }
async function save(p) { p.updatedAt = now(); await mkdir(projectDir(p.id), { recursive: true }); await Promise.all([writeFile(projectFile(p.id), JSON.stringify(p, null, 2)), writeFile(path.join(projectDir(p.id), "project_status.md"), statusFor(p))]); return p; }
async function load(id) { try { const project = JSON.parse(await readFile(projectFile(id), "utf8")); project.artifacts ||= {}; project.uploads ||= []; project.modelRoutes ||= {}; project.invalidatedStages ||= []; project.returnRoute ||= null; project.recheckScope ||= null; return project; } catch { return null; } }
async function list() { await mkdir(projectsRoot, { recursive: true }); const dirs = await readdir(projectsRoot, { withFileTypes: true }); return (await Promise.all(dirs.filter((d) => d.isDirectory()).map((d) => load(d.name)))).filter(Boolean).sort((a, b) => b.updatedAt.localeCompare(a.updatedAt)); }
function send(res, code, data) { res.writeHead(code, { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" }); res.end(JSON.stringify(data)); }
async function readBody(req) { const parts = []; let length = 0; for await (const part of req) { length += part.length; if (length > maxUploadBytes * 1.4) throw new Error("请求内容超过 50 MB 限制。"); parts.push(part); } const text = Buffer.concat(parts).toString("utf8"); try { return JSON.parse(text || "{}"); } catch { throw new Error("请求格式无效。"); } }
function safeFileName(name) { return path.basename(String(name || "upload")).replace(/[\\/:*?"<>|]/g, "_").slice(0, 120) || "upload"; }
const exposed = (p) => ({ ...p, stages });
function adapterById(id) { return modelAdapters.find((adapter) => adapter.id === id) || null; }
function allowedAdapterIds(stageIndex) { if (stageIndex === 3) return ["built-in-image-prompt", "midjourney-prompt"]; if (stageIndex === 7 || stageIndex === 8) return ["seedance-25-prompt", "minimax-h3-prompt"]; return ["openai-terra", "openai-luna", "compatible-text"]; }
function isAdapterAllowed(stageIndex, adapter) { return Boolean(adapter) && allowedAdapterIds(stageIndex).includes(adapter.id); }
function projectContext(project) { return [project.brief, ...Object.values(project.artifacts || {}).map((artifact) => artifact?.content || ""), ...(project.uploads || []).map((file) => `${file.kind} ${file.name}`)].join("\n").toLowerCase(); }
function autoAdapterId(project, stageIndex = project.currentStage) {
  const context = projectContext(project);
  if (stageIndex === 3) return /midjourney|\bmj\b|外部出图/.test(context) ? "midjourney-prompt" : "built-in-image-prompt";
  if (stageIndex === 7 || stageIndex === 8) return /首帧|尾帧|首尾帧|已有视频|视频编辑|短片|15秒以内|15 秒以内/.test(context) ? "minimax-h3-prompt" : "seedance-25-prompt";
  if (!openAiApiKey && compatibleApiKey && compatibleBaseUrl && compatibleModel) return "compatible-text";
  return [1, 4, 6, 9].includes(stageIndex) ? "openai-terra" : "openai-luna";
}
function autoAdapterReason(project, stageIndex = project.currentStage) {
  const adapterId = autoAdapterId(project, stageIndex);
  if (adapterId === "midjourney-prompt") return "检测到 Midjourney / 外部出图偏好，输出可复制提示词。";
  if (adapterId === "built-in-image-prompt") return "资产开发阶段，使用内置图像路线的提示词包。";
  if (adapterId === "minimax-h3-prompt") return "检测到首尾帧、短片或已有视频编辑需求，使用 MiniMax H3 提示词包。";
  if (adapterId === "seedance-25-prompt") return "视频阶段默认优先连续叙事与多参考能力，使用 Seedance 2.5 提示词包。";
  if (adapterId === "compatible-text") return "OpenAI 未连接，自动降级为已连接的兼容文本接口并输出提示词。";
  return adapterId === "openai-terra" ? "该阶段需要更强的剧本、导演、镜头或审核推理，使用 GPT-5.6 Terra。" : "该阶段以结构化整理为主，使用 GPT-5.6 Luna。";
}
function adapterForProject(project) { return adapterById(autoAdapterId(project)); }
function imageRoute(adapter) { return adapter?.id === "built-in-image-prompt" ? { model: "Built-in Image", profile: "adapters/built-in-image.md", template: "templates/24_builtin_image_asset_prompt.md", delivery: "Unavailable — Prompt Only" } : adapter?.id === "midjourney-prompt" ? { model: "Midjourney", profile: "adapters/midjourney.md", template: "templates/14_midjourney_asset_prompt.md", delivery: "External Prompt Only" } : { model: "UNSELECTED", profile: "UNSELECTED", template: "UNSELECTED", delivery: "UNSELECTED" }; }
function videoRoute(adapter) { return adapter?.id === "seedance-25-prompt" ? { model: "Seedance 2.5", profile: "adapters/seedance-2.5.md", template: "templates/12_seedance_25_video_prompt.md", audit: "SEEDANCE_25_CAPABILITY" } : adapter?.id === "minimax-h3-prompt" ? { model: "MiniMax H3", profile: "adapters/minimax-h3.md", template: "templates/13_minimax_h3_video_prompt.md", audit: "ADAPTER_EFFECTIVE_LIMIT" } : { model: "UNSELECTED", profile: "UNSELECTED", template: "UNSELECTED", audit: "NOT_APPLICABLE" }; }
function modelStateControl(project) { const lines = [`- Model Routing: Automatic (${autoAdapterReason(project)})`]; if (project.currentStage === 3) { const route = imageRoute(adapterForProject(project)); lines.push(`- Selected Image Model: ${route.model}`, `- Image Adapter Profile: ${route.profile}`, "- Image Model Selection Status: SELECTED", `- Image Prompt Output Template: ${route.template}`, `- Image Delivery Route: ${route.delivery}`, "- Image Model Selection Scope: current asset batch"); } if (project.currentStage === 7 || project.currentStage === 8) { const route = videoRoute(adapterForProject(project)); lines.push(`- Selected Model: ${route.model}`, `- Adapter Profile: ${route.profile}`, "- Model Selection Status: SELECTED", "- Delivery Surface: STANDARD", `- Prompt Output Template: ${route.template}`, "- Execution Mode: Not Applicable", `- Reference Capacity Audit: ${route.audit}`, "- Long-duration Route: Not Applicable", "- Effective Gateway Limits: UNKNOWN", "- Model Selection Scope: current generation batch"); } return lines.join("\n"); }
function modelRisk(project) { return `Automatic route: ${adapterForProject(project)?.label || "No compatible model"}. ${autoAdapterReason(project)}`; }
function isAdapterConfigured(adapter) { if (!adapter) return false; if (adapter.provider === "prompt") return true; if (adapter.provider === "compatible") return Boolean(compatibleApiKey && compatibleBaseUrl && compatibleModel); return Boolean(openAiApiKey); }
function configuredOpenAi() { return { keyStorage: "memory", routing: "automatic", providers: { openai: { configured: Boolean(openAiApiKey) }, compatible: { configured: Boolean(compatibleApiKey && compatibleBaseUrl && compatibleModel) } }, adapters: modelAdapters.map(({ id, label, provider, model, multimodal, outputMode, stage, description }) => ({ id, label, provider, model: model || null, multimodal, outputMode, stage, description })) }; }
function outputText(response) { return response.output_text || response.output?.flatMap((item) => item.content || []).filter((item) => item.type === "output_text").map((item) => item.text || "").join("\n").trim() || ""; }
async function responseFromOpenAi(input, model = openAiModel) { const response = await fetch("https://api.openai.com/v1/responses", { method: "POST", headers: { "content-type": "application/json", authorization: `Bearer ${openAiApiKey}` }, body: JSON.stringify({ model, input }), signal: AbortSignal.timeout(90_000) }); const body = await response.json().catch(() => ({})); if (!response.ok) throw new Error(body?.error?.message || "OpenAI 请求失败，请检查密钥、网络和 API 项目权限。"); return body; }
async function responseFromCompatible(prompt) { const response = await fetch(`${compatibleBaseUrl.replace(/\/+$/, "")}/chat/completions`, { method: "POST", headers: { "content-type": "application/json", authorization: `Bearer ${compatibleApiKey}` }, body: JSON.stringify({ model: compatibleModel, messages: [{ role: "user", content: prompt }] }), signal: AbortSignal.timeout(90_000) }); const body = await response.json().catch(() => ({})); if (!response.ok) throw new Error(body?.error?.message || "兼容 API 请求失败，请检查地址、密钥和模型名称。"); const text = body.choices?.[0]?.message?.content; if (!text) throw new Error("兼容 API 未返回文本。" ); return String(text); }
async function referenceImageParts(project) { const files = (project.uploads || []).filter((file) => file.mimeType?.startsWith("image/")).slice(0, 4); const parts = []; for (const file of files) { try { const bytes = await readFile(path.join(projectDir(project.id), "uploads", file.storedName)); if (bytes.length <= 8 * 1024 * 1024) parts.push({ type: "input_image", image_url: `data:${file.mimeType};base64,${bytes.toString("base64")}`, detail: "auto" }); } catch { /* Missing local references are skipped without blocking the draft. */ } } return parts; }
function stageAllowsAdapter(project, adapter) { if (adapter.stage === "image" && project.currentStage !== 3) return "Midjourney 提示词包仅在 STATE-03 资产开发阶段可用。"; if (adapter.stage === "video" && project.currentStage < 7) return "视频模型提示词包必须在 STATE-06 确认后、进入 STATE-07 及之后使用。"; return null; }
function referenceNames(project) { const files = project.uploads || []; return files.length ? files.slice(0, 12).map((file) => `${file.kind}：${file.name}`).join("；") : "无已上传参考素材"; }
function externalPrompt(project, adapter) {
  const stage = stages[project.currentStage];
  const prior = project.artifacts?.[stage.id]?.content || "无";
  const route = adapter.id === "built-in-image-prompt" ? "Built-in Image 资产提示词" : adapter.id === "midjourney-prompt" ? "外部 Midjourney 图像提示词" : adapter.id === "seedance-25-prompt" ? "外部 Seedance 2.5 视频提示词" : adapter.id === "minimax-h3-prompt" ? "外部 MiniMax H3 视频提示词" : "文本模型可执行提示词";
  const videoSafety = adapter.id.includes("seedance") || adapter.id.includes("minimax") ? " 如涉及视频，非叙事性音乐：N/A。" : "";
  return `# ${adapter.label} · ${route}

状态：${stage.id} ${stage.label}
工作流：${stage.workflow}
项目：${project.name}

## 可用事实
${project.brief}

## 当前工件草稿
${prior}

## 已上传参考（仅文字说明，未向模型传图）
${referenceNames(project)}

## 提交提示词
基于以上已确认事实，生成或分析当前阶段的“${stage.artifact}”。保持人物身份、故事因果、空间关系与已确认资产一致；不得虚构未提供的参考图内容。${videoSafety}

> 此为提示词交付，不代表已调用 ${adapter.label} 或已生成媒体。`;
}
async function draftForStage(project) { const adapter = adapterForProject(project); if (!adapter) throw new Error("请先为当前步骤选择模型。"); if (!isAdapterAllowed(project.currentStage, adapter)) throw new Error("当前步骤的模型选择不符合 SD Film 工作流。请重新选择。" ); if (adapter.provider === "prompt") return externalPrompt(project, adapter); const stage = stages[project.currentStage]; const prior = project.artifacts?.[stage.id]?.content || "None"; const prompt = `You are the SD Film production assistant. Work only on ${stage.id} (${stage.label}); do not advance the stage or claim user confirmation. Write a concise Chinese ${adapter.multimodal ? "draft" : "prompt package"} for the current artifact, grounded only in the project facts below. Preserve story, assets, and confirmed facts. Do not add non-diegetic background music to any video-prompt-related content.\n\nProject: ${project.name}\nOriginal brief: ${project.brief}\nCurrent workflow: ${stage.workflow}\nArtifact requested: ${stage.artifact}\nCurrent saved draft: ${prior}\nUploaded reference names: ${referenceNames(project)}\n\nReturn only the proposed artifact content, in Chinese, ready for the user to review.`; if (adapter.provider === "compatible") return (await responseFromCompatible(prompt)).slice(0, 12_000); const content = [{ type: "input_text", text: prompt }, ...(await referenceImageParts(project))]; const response = await responseFromOpenAi([{ role: "user", content }], adapter.model); const text = outputText(response); if (!text) throw new Error("模型未返回可保存的文本草稿。"); return text.slice(0, 12_000); }
async function api(req, res, pathname) {
  if (req.method === "GET" && pathname === "/api/health") return send(res, 200, { ok: true });
  if (req.method === "GET" && (pathname === "/api/integrations/openai" || pathname === "/api/integrations/models")) return send(res, 200, configuredOpenAi());
  if (req.method === "POST" && (pathname === "/api/integrations/openai/test" || pathname === "/api/integrations/models/test")) { const { apiKey, adapterId, baseUrl, model } = await readBody(req); const adapter = adapterById(adapterId || "openai-terra"); if (!adapter) return send(res, 400, { error: "不支持的模型适配器。" }); if (adapter.provider === "prompt") return send(res, 200, configuredOpenAi()); const candidateKey = String(apiKey || (adapter.provider === "openai" ? openAiApiKey : compatibleApiKey) || "").trim(); if (candidateKey.length < 20) return send(res, 400, { error: "请输入有效的 API Key。" }); if (adapter.provider === "openai") { const previousKey = openAiApiKey, previousModel = openAiModel; openAiApiKey = candidateKey; openAiModel = adapter.model; try { const result = await responseFromOpenAi("Reply with exactly: connected.", adapter.model); if (!outputText(result)) throw new Error("未获得测试响应。"); return send(res, 200, configuredOpenAi()); } catch (error) { openAiApiKey = previousKey; openAiModel = previousModel; return send(res, 502, { error: error.message || "无法连接 OpenAI。" }); } } const candidateBaseUrl = String(baseUrl || compatibleBaseUrl || "").trim().replace(/\/+$/, ""); const candidateModel = String(model || compatibleModel || "").trim(); try { const parsed = new URL(candidateBaseUrl); if (parsed.protocol !== "https:") throw new Error("兼容 API 地址必须使用 HTTPS。"); } catch (error) { return send(res, 400, { error: error.message || "请输入有效的 HTTPS API 地址。" }); } if (!candidateModel) return send(res, 400, { error: "请输入兼容接口的模型名称。" }); const previous = [compatibleApiKey, compatibleBaseUrl, compatibleModel]; compatibleApiKey = candidateKey; compatibleBaseUrl = candidateBaseUrl; compatibleModel = candidateModel; try { await responseFromCompatible("Reply with exactly: connected."); return send(res, 200, configuredOpenAi()); } catch (error) { [compatibleApiKey, compatibleBaseUrl, compatibleModel] = previous; return send(res, 502, { error: error.message || "无法连接兼容 API。" }); } }
  if (pathname === "/api/integrations/workflow-routes") return send(res, 410, { error: "模型由系统按当前步骤和素材自动识别，无需手动分配。" });
  if (req.method === "GET" && pathname === "/api/projects") return send(res, 200, { projects: await list() });
  if (req.method === "POST" && pathname === "/api/projects") { const { name, brief } = await readBody(req); if (!String(name || "").trim() || !String(brief || "").trim()) return send(res, 400, { error: "项目名称和创意/剧本不能为空。" }); const at = now(); const p = { id: `PROJECT-${randomUUID().slice(0, 8).toUpperCase()}`, name: String(name).trim().slice(0, 60), brief: String(brief).trim().slice(0, 12000), artifacts: {}, uploads: [], modelRoutes: {}, currentStage: 0, completedStages: [], revision: 1, reviewPassed: false, createdAt: at, updatedAt: at, lastCompletedStep: null, lastCheckpoint: "Project initialized", activity: [{ at, message: "STATE-00 Project Setup initialized" }] }; return send(res, 201, exposed(await save(p))); }
  const routeMatch = pathname.match(/^\/api\/projects\/([A-Z0-9-]+)\/model-routes\/(STATE-\d\d)$/);
  if (routeMatch) return send(res, 410, { error: "模型已改为在“模型中心”统一配置；制作步骤会自动按调用方案执行。" });
  const uploadMatch = pathname.match(/^\/api\/projects\/([A-Z0-9-]+)\/uploads$/);
  if (uploadMatch) { const p = await load(uploadMatch[1]); if (!p) return send(res, 404, { error: "找不到该项目。" }); if (req.method !== "POST") return send(res, 405, { error: "不支持的操作。" }); const { name, type, kind, data } = await readBody(req); const fileName = safeFileName(name); const fileKind = ["剧本", "资产", "参考素材"].includes(kind) ? kind : "参考素材"; if (!allowedUploadExtensions.has(path.extname(fileName).toLowerCase())) return send(res, 400, { error: "仅支持文本、文档、图片、视频和音频素材文件。" }); if (typeof data !== "string" || !data) return send(res, 400, { error: "请选择需要上传的文件。" }); const bytes = Buffer.from(data, "base64"); if (!bytes.length || bytes.length > maxUploadBytes) return send(res, 400, { error: "文件为空或超过 50 MB 限制。" }); const uploadId = `UPLOAD-${randomUUID().slice(0, 8).toUpperCase()}`; const storedName = `${uploadId}--${fileName}`; await mkdir(path.join(projectDir(p.id), "uploads"), { recursive: true }); await writeFile(path.join(projectDir(p.id), "uploads", storedName), bytes); const at = now(); p.uploads.unshift({ id: uploadId, name: fileName, storedName, kind: fileKind, mimeType: String(type || "application/octet-stream").slice(0, 120), size: bytes.length, uploadedAt: at }); p.revision += 1; p.activity.unshift({ at, message: `${fileKind} uploaded: ${fileName}` }); return send(res, 201, exposed(await save(p))); }
  const draftMatch = pathname.match(/^\/api\/projects\/([A-Z0-9-]+)\/agent\/draft$/);
  if (draftMatch) { const p = await load(draftMatch[1]); if (!p) return send(res, 404, { error: "找不到该项目。" }); if (p.reviewPassed) return send(res, 409, { error: "项目已完成审核，不能再生成当前阶段草稿。" }); const adapter = adapterForProject(p); if (!adapter) return send(res, 409, { error: "请先为当前步骤选择模型。" }); if (!isAdapterConfigured(adapter)) return send(res, 409, { error: "请先在模型配置中连接该模型提供方。" }); try { const content = await draftForStage(p); const at = now(); const stage = stages[p.currentStage]; p.artifacts[stage.id] = { content, updatedAt: at, source: adapter.id }; p.revision += 1; p.activity.unshift({ at, message: `${stage.id} ${adapter.label} output saved` }); return send(res, 200, exposed(await save(p))); } catch (error) { return send(res, 502, { error: error.message || "生成草稿失败。" }); } }
  const artifactMatch = pathname.match(/^\/api\/projects\/([A-Z0-9-]+)\/artifacts\/(STATE-\d\d)$/);
  if (artifactMatch) { const p = await load(artifactMatch[1]); if (!p) return send(res, 404, { error: "找不到该项目。" }); const stageIndex = stages.findIndex((stage) => stage.id === artifactMatch[2]); if (stageIndex < 0 || stageIndex > p.currentStage) return send(res, 409, { error: "不能编辑尚未开始的阶段。" }); if (stageIndex !== p.currentStage) return send(res, 409, { error: "请先点击“返回此步骤继续”，再修改历史阶段内容。" }); if (req.method !== "POST") return send(res, 405, { error: "不支持的操作。" }); const { content } = await readBody(req); if (!String(content || "").trim()) return send(res, 400, { error: "工件内容不能为空。" }); const at = now(); p.artifacts[artifactMatch[2]] = { content: String(content).trim().slice(0, 12000), updatedAt: at }; p.revision += 1; p.activity.unshift({ at, message: `${artifactMatch[2]} artifact updated` }); return send(res, 200, exposed(await save(p))); }
  const m = pathname.match(/^\/api\/projects\/([A-Z0-9-]+)(?:\/actions\/(confirm|return))?$/); if (!m) return false; const p = await load(m[1]); if (!p) return send(res, 404, { error: "找不到该项目。" });
  if (req.method === "GET" && !m[2]) return send(res, 200, exposed(p));
  if (req.method === "POST" && m[2] === "return") {
    const { stageId } = await readBody(req);
    const stageIndex = stages.findIndex((stage) => stage.id === stageId);
    if (stageIndex < 0) return send(res, 400, { error: "无效的返回步骤。" });
    if (stageIndex >= p.currentStage) return send(res, 409, { error: "只能返回已经通过的历史步骤。" });
    const target = stages[stageIndex];
    p.currentStage = stageIndex;
    p.completedStages = p.completedStages.filter((id) => stages.findIndex((stage) => stage.id === id) < stageIndex);
    p.invalidatedStages = stages.slice(stageIndex).map((stage) => stage.id);
    p.returnRoute = target.id;
    p.recheckScope = p.invalidatedStages.join(", ");
    p.reviewPassed = false;
    p.lastCompletedStep = stageIndex > 0 ? stages[stageIndex - 1].workflow : "None";
    p.lastCheckpoint = stageIndex > 0 ? `${stages[stageIndex - 1].id} remains confirmed` : "Project initialized";
    p.activity.unshift({ at: now(), message: `Returned to ${target.id}; downstream artifacts retained for recheck` });
    p.revision += 1;
    return send(res, 200, exposed(await save(p)));
  }
  if (req.method === "POST" && m[2] === "confirm") {
    const current = stages[p.currentStage];
    p.invalidatedStages = (p.invalidatedStages || []).filter((id) => id !== current.id);
    if (!p.invalidatedStages.length) { p.returnRoute = null; p.recheckScope = null; }
    if (p.currentStage === stages.length - 1) {
      p.reviewPassed = true;
      p.lastCompletedStep = current.workflow;
      p.lastCheckpoint = "STATE-09 Review PASS";
      p.activity.unshift({ at: now(), message: "STATE-09 Review passed" });
    } else {
      p.completedStages = [...new Set([...p.completedStages, current.id])];
      p.lastCompletedStep = current.workflow;
      p.lastCheckpoint = `${current.id} confirmed`;
      p.currentStage += 1;
      p.activity.unshift({ at: now(), message: `${current.id} confirmed; entered ${stages[p.currentStage].id}` });
    }
    p.revision += 1;
    return send(res, 200, exposed(await save(p)));
  }
  return send(res, 405, { error: "不支持的操作。" });
}
const types = { ".html": "text/html; charset=utf-8", ".js": "application/javascript; charset=utf-8", ".css": "text/css; charset=utf-8" };
async function serveFile(res, pathname) { const target = path.resolve(here, `.${pathname === "/" ? "/index.html" : pathname}`); if (!target.startsWith(`${here}${path.sep}`)) return send(res, 403, { error: "禁止访问。" }); try { if (!(await stat(target)).isFile()) throw new Error(); res.writeHead(200, { "content-type": types[path.extname(target)] || "application/octet-stream", "cache-control": "no-store" }); createReadStream(target).pipe(res); } catch { send(res, 404, { error: "页面不存在。" }); } }
async function demo() { if ((await list()).length) return; const at = now(); await save({ id: "PROJECT-DEMO-001", name: "雾港来信", brief: "雨夜的雾港，一封迟到十年的信迫使返乡的苏岑重新面对父亲失踪的真相。", artifacts: {}, uploads: [], currentStage: 1, completedStages: ["STATE-00"], revision: 3, reviewPassed: false, createdAt: at, updatedAt: at, lastCompletedStep: "01_project_setup_workflow.md", lastCheckpoint: "STATE-00 confirmed", activity: [{ at, message: "制作版剧本提案等待确认" }, { at, message: "STATE-00 Project Setup confirmed" }, { at, message: "Project created" }] }); }
await demo(); createServer(async (req, res) => { const url = new URL(req.url, `http://${req.headers.host || "localhost"}`); try { if (url.pathname.startsWith("/api/")) { const done = await api(req, res, url.pathname); return done === false ? send(res, 404, { error: "API 不存在。" }) : done; } return serveFile(res, decodeURIComponent(url.pathname)); } catch (error) { return send(res, 500, { error: error.message || "服务器发生错误。" }); } }).listen(port, "127.0.0.1", () => console.log(`SD Film Web is ready at http://127.0.0.1:${port}`));
