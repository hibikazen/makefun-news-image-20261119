// Entry point for the news-image-20261119 bounty.
//
// The front page is rendered ahead of time by render.py and shipped as
// entry.png. This program only copies it to the output directory, so both
// graded runs write exactly the same bytes. No network, no randomness,
// no dependencies beyond the Node standard library.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = join(repoRoot, "entry.png");

if (!existsSync(source)) {
  throw new Error(`entry image missing: ${source}`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, "entry.png"));
