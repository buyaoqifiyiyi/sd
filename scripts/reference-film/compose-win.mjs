#!/usr/bin/env node
/*
 * compose-win.mjs — Windows-safe wrapper around the vendored video-sync `compose`
 * step for the SD Film reference-film study workflow.
 *
 *   node scripts/reference-film/compose-win.mjs <shots.json> --video <片> [--panels panels]
 *     [-o out.mp4] [--chrome <路径>] [--crf 20] [--ease 0.45] [--scale 1]
 *     [--width 1920] [--height 1080] [--panel <比例>]
 *
 * WHY THIS EXISTS
 * ---------------
 * Upstream's `compose` builds an ffmpeg filtergraph that embeds an absolute path
 * inside a filter option: `sendcmd=f='<abs path to motion.cmd>'`. On POSIX that
 * path is `/tmp/x/motion.cmd` and parses fine. On Windows it is
 * `C:\Users\...\motion.cmd`, where the filtergraph parser treats `\` as an escape
 * and `:` as an option separator, so ffmpeg fails with:
 *
 *   [AVFilterGraph] No option name near '\Users\...\motion.cmd'
 *
 * Measured on ffmpeg 9.0.1 / Windows: forward slashes alone are NOT enough —
 * `sendcmd=f='C:/Users/x/motion.cmd'` still fails. The path must be written
 * `C\:/Users/x/motion.cmd` (forward slashes, drive colon backslash-escaped).
 * That is the whole delta this file carries.
 *
 * SCOPE / SINGLE OWNERSHIP
 * ------------------------
 * This is a PATCH, not a reimplementation, and it deliberately stays small:
 *
 *   - `plan`   → delegated to upstream as a subprocess (geometry + layout facts)
 *   - `panels` → NOT implemented here; run upstream `panels` first
 *   - compose  → reimplemented ONLY because the three line-502/505/508 arguments
 *                embed paths/expressions the upstream code cannot parameterise.
 *                The filtergraph structure, the motion plan and the encoding
 *                flags are reproduced from vendor/video-sync/scripts/video-sync.mjs
 *                (composeArgs / motionPlan / ramp / commandFile) and must be kept
 *                in step with it.
 *
 * Panels/motion geometry is read from the browser-measured `<panels>/layout.json`
 * that upstream `panels` writes; the video/panel/stack/crf geometry comes from
 * upstream `plan` so the two never disagree.
 *
 * If the vendored engine is ever replaced, re-diff this file against the new
 * composeArgs before trusting it.
 */

import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const UPSTREAM = join(HERE, 'vendor', 'video-sync', 'scripts', 'video-sync.mjs');

const DEFAULT_EASE = 0.45;
const DEFAULT_ANCHOR_ROW = 1;

/* ------------------------------------------------------------------ */
/* argv                                                               */
/* ------------------------------------------------------------------ */

function flag(rest, name, fallback = null) {
  const i = rest.indexOf(name);
  if (i === -1) return fallback;
  const v = rest[i + 1];
  return v == null || v.startsWith('--') ? true : v;
}

const USAGE = `用法：
  node compose-win.mjs <shots.json> --video <片> [--panels panels] [-o out.mp4]
    [--chrome <路径>] [--crf 20] [--ease ${DEFAULT_EASE}] [--scale 1]
    [--width 1920] [--height 1080] [--panel <比例>]

先跑 vendor 的 panels，它会写下 browser 量出来的 layout.json；本命令只补 compose。`;

/* ------------------------------------------------------------------ */
/* filtergraph path escaping                                          */
/* ------------------------------------------------------------------ */

/**
 * A filesystem path as an ffmpeg filtergraph option value.
 *
 * Not a URL, not a shell quote. Inside a filter description `\` is an escape
 * character and `:` separates an option name from its value, so a Windows path
 * has to be written with forward slashes and an escaped drive colon.
 * POSIX paths already parse and are returned unchanged.
 */
export function filterPath(p) {
  const abs = resolve(p);
  if (!/^[A-Za-z]:[\\/]/.test(abs)) return abs.replace(/\\/g, '/');
  return abs.replace(/\\/g, '/').replace(/^([A-Za-z]):/, '$1\\:');
}

/* ------------------------------------------------------------------ */
/* motion plan — reproduced from vendor video-sync.mjs                */
/* ------------------------------------------------------------------ */

const r2 = (n) => Math.round(Number(n) * 100) / 100;

/** One eased segment: walk a→b over `dur` seconds starting at `start`, then clamp. */
export function ramp(a, b, start, dur) {
  if (a === b || !(dur > 0)) return `${r2(a)}`;
  const lo = Math.min(a, b);
  const hi = Math.max(a, b);
  return `clip(${r2(a)}+${r2(b - a)}*(t-${r2(start)})/${r2(dur)},${r2(lo)},${r2(hi)})`;
}

/** The sendcmd command file: one `time target command 'expr';` per line. */
export function commandFile(commands) {
  return commands.map((c) => `${r2(c.time)} ${c.target} ${c.command} '${c.arg}';`).join('\n');
}

/**
 * Rolling + highlighting as piecewise-linear functions of t, one command per
 * cut. The active shot stays pinned to row `anchorRow + 1`; rolling happens only
 * at cuts and stops after `easeSeconds`. Expressions must stay short — ffmpeg's
 * expression parser gives up around a hundred terms.
 */
export function motionPlan({ shots, rows, view, content, easeSeconds = DEFAULT_EASE, anchorRow = DEFAULT_ANCHOR_ROW, panelHeight = 0 }) {
  const byId = new Map(rows.map((r) => [r.id, r]));
  const row = (s) => byId.get(s.id) ?? { top: 0, height: 0 };
  const slot = Math.min(Math.max(0, Math.round(anchorRow)), Math.max(0, rows.length - 1));
  const anchor = rows[slot] ? rows[slot].top - (rows[0]?.top ?? 0) : 0;
  const maxOffset = Math.max(0, content - view.height);
  const target = (s) => Math.min(maxOffset, Math.max(0, row(s).top - anchor));

  const bands = [...new Set(rows.map((r) => r.height))].sort((a, b) => a - b);
  const bandOf = (s) => Math.max(0, bands.indexOf(row(s).height));
  const tallestRow = Math.max(0, ...rows.map((r) => r.height));
  const parkY = Math.max(panelHeight, view.y + view.height + tallestRow) + 10;
  const screenY = (s, top, offset) => {
    const hi = view.y + view.height - row(s).height;
    return `clip(${view.y}+(${top})-(${offset}),${r2(view.y)},${r2(Math.max(view.y, hi))})`;
  };

  const commands = [];
  shots.forEach((s, i) => {
    const prev = shots[i - 1];
    const start = Number(s.start);
    const span = Math.max(0.001, Number(s.end) - start);
    const ease = Math.min(easeSeconds, span);
    const band = bandOf(s);
    const prevBand = prev ? bandOf(prev) : band;
    const offset = ramp(prev ? target(prev) : target(s), target(s), start, ease);
    const top = ramp(prev ? row(prev).top : row(s).top, row(s).top, start, ease);

    commands.push({ time: start, target: 'crop@win', command: 'y', arg: offset });
    commands.push({ time: start, target: `crop@band${band}`, command: 'y', arg: top });
    commands.push({ time: start, target: `overlay@band${band}`, command: 'y', arg: screenY(s, top, offset) });

    bands.forEach((_, j) => {
      if (j === band) return;
      commands.push({ time: j === prevBand ? start + ease : start, target: `overlay@band${j}`, command: 'y', arg: `${r2(parkY)}` });
    });
  });

  const first = shots[0];
  return {
    commands,
    bands,
    parkY,
    initial: {
      offset: first ? target(first) : 0,
      top: first ? row(first).top : 0,
      screenY: view.y + (first ? row(first).top - target(first) : 0),
      band: first ? bandOf(first) : 0,
    },
    rowHeight: Math.max(...rows.map((r) => r.height), 1),
    maxOffset,
    anchor,
    anchorRow: slot,
    easeSeconds,
  };
}

/* ------------------------------------------------------------------ */
/* filtergraph — upstream composeArgs with filterPath on the 3 path sites */
/* ------------------------------------------------------------------ */

export function composeArgs({ video, still, listDim, listLit, out, layout, motion, view, commands, hasAudio }) {
  const { width: vw, height: vh } = layout.video;
  const { width: pw, height: ph } = layout.panel;
  const { bands, parkY, initial } = motion;
  const chain = [
    `[0:v]scale=${vw}:${vh}:flags=lanczos,setsar=1,fps=${layout.fps}[v]`,
    // ⚠ the fixed line: sendcmd's option value is a path inside a filtergraph
    `[1:v]scale=${pw}:${ph},setsar=1,fps=${layout.fps},sendcmd=f='${filterPath(commands)}'[base]`,
    `[2:v]fps=${layout.fps},crop@win=w=${view.width}:h=${view.height}:x=${view.x}:y=${initial.offset}[win]`,
    `[3:v]fps=${layout.fps}${bands.length > 1 ? `,split=${bands.length}${bands.map((_, i) => `[lit${i}]`).join('')}` : '[lit0]'}`,
    ...bands.map((h, i) => `[lit${i}]crop@band${i}=w=${view.width}:h=${h}:x=${view.x}:y=${initial.top}[band${i}]`),
    `[base][win]overlay@win=x=${view.x}:y=${view.y}[p0]`,
    ...bands.map((h, i) => `[p${i}][band${i}]overlay@band${i}=x=${view.x}:y=${i === initial.band ? initial.screenY : parkY}[p${i + 1}]`),
    `[v][p${bands.length}]${layout.stack}=inputs=2[out]`,
  ];

  const args = [
    '-v', 'error', '-y',
    '-i', video,
    '-loop', '1', '-i', still,
    '-loop', '1', '-i', listDim,
    '-loop', '1', '-i', listLit,
    '-filter_complex', chain.join(';'),
    '-map', '[out]',
  ];
  if (hasAudio) args.push('-map', '0:a', '-c:a', 'aac', '-b:a', '160k');
  args.push('-c:v', 'libx264', '-preset', 'medium', '-crf', String(layout.crf), '-pix_fmt', 'yuv420p',
    '-movflags', '+faststart', '-shortest', out);
  return args;
}

/* ------------------------------------------------------------------ */
/* main                                                              */
/* ------------------------------------------------------------------ */

function probeHasAudio(video) {
  try {
    const out = execFileSync('ffprobe', ['-v', 'error', '-select_streams', 'a', '-show_entries', 'stream=codec_type', '-of', 'csv=p=0', video], { encoding: 'utf8' });
    return out.trim().length > 0;
  } catch {
    return false;
  }
}

function main(argv) {
  if (!argv.length || argv.includes('--help') || argv.includes('-h')) {
    process.stdout.write(`${USAGE}\n`);
    return;
  }
  const shotsPath = argv[0];
  if (shotsPath.startsWith('--')) throw new Error('第一个参数要是 shots.json');

  const doc = JSON.parse(readFileSync(shotsPath, 'utf8'));
  const video = flag(argv, '--video');
  if (typeof video !== 'string') throw new Error('要 --video <片>');
  if (!existsSync(video)) throw new Error(`--video 指的文件不存在：${video}`);
  if (!existsSync(UPSTREAM)) throw new Error(`找不到上游引擎：${UPSTREAM}`);

  const panelDir = typeof flag(argv, '--panels') === 'string' ? flag(argv, '--panels')
    : typeof flag(argv, '--out') === 'string' ? flag(argv, '--out') : 'panels';
  const layoutPath = join(panelDir, 'layout.json');
  if (!existsSync(layoutPath)) {
    throw new Error(`没有 ${layoutPath}——先跑 vendor 的 panels（它才会用浏览器量出行位置）`);
  }
  const measured = JSON.parse(readFileSync(layoutPath, 'utf8'));

  // Geometry comes from upstream `plan` so compose and panels cannot disagree.
  const passThrough = ['--panel', '--width', '--height', '--scale', '--crf'];
  const planArgs = [UPSTREAM, 'plan', resolve(shotsPath), '--video', video];
  for (const name of passThrough) {
    const v = flag(argv, name);
    if (typeof v === 'string') planArgs.push(name, v);
  }
  const layout = JSON.parse(execFileSync('node', planArgs, { encoding: 'utf8' }));

  const still = join(panelDir, 'static.png');
  const listDim = join(panelDir, 'list-dim.png');
  const listLit = join(panelDir, 'list-lit.png');
  for (const f of [still, listDim, listLit]) {
    if (!existsSync(f)) throw new Error(`缺面板图 ${f}——重跑 vendor 的 panels`);
  }

  const view = measured.view;
  const rows = measured.rows;
  if (!Array.isArray(rows) || !rows.length) throw new Error('layout.json 里没有 rows，面板可能没渲成功');
  const content = measured.tallHeight ?? measured.content;

  const ease = typeof flag(argv, '--ease') === 'string' ? Number(flag(argv, '--ease')) : DEFAULT_EASE;
  const motion = motionPlan({ shots: doc.shots, rows, view, content, easeSeconds: ease, panelHeight: measured.panel?.height ?? 0 });

  const cmdFile = join(panelDir, 'motion.cmd');
  writeFileSync(cmdFile, commandFile(motion.commands));

  const out = typeof flag(argv, '-o') === 'string' ? flag(argv, '-o')
    : typeof flag(argv, '--out') === 'string' ? flag(argv, '--out')
    : `${(doc.source ?? 'out').replace(/\.[^.]+$/, '')}-sync.mp4`;

  const args = composeArgs({
    video: resolve(video), still: resolve(still), listDim: resolve(listDim), listLit: resolve(listLit), out,
    layout, motion, view, commands: resolve(cmdFile), hasAudio: probeHasAudio(video),
  });

  execFileSync('ffmpeg', args, { stdio: ['ignore', 'ignore', 'inherit'] });

  process.stderr.write(`[compose-win] ${out} — ${layout.output.width}×${layout.output.height} / ${doc.meta?.durationSeconds ?? '?'}s / ${layout.stack === 'vstack' ? '画面在上' : '画面在左'}\n`);
  process.stderr.write(`[compose-win] 当前镜头钉在第 ${motion.anchorRow + 1} 行，切点处滚 ${motion.easeSeconds}s 到位后停住（${motion.commands.length} 条命令 / ${motion.bands.length} 层高亮）\n`);
}

try {
  main(process.argv.slice(2));
} catch (err) {
  process.stderr.write(`${err.message}\n`);
  process.exitCode = 1;
}
