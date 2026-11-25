// The World Today — Wednesday, 25 November 2026.
//
// Entry point for the news-image-20261125 bounty (Node 22, standard
// library only). The poster lives in this repository as entry.png; this
// program places a byte-identical copy at $MAKEFUN_OUTPUT_DIR/entry.png
// (or /output/entry.png when the variable is unset, which is where the
// grader expects it). It never touches the network and it never modifies
// the image, so two runs always write the same bytes.
//
// Local check:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const source = join(dirname(fileURLToPath(import.meta.url)), "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

if (!existsSync(source)) {
  throw new Error(`entry.png not found next to main.ts: ${source}`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

// The copy must be exact: same size, same bytes. A truncated or partial
// write would fail the gate, so refuse to finish quietly on one.
if (statSync(source).size !== statSync(target).size) {
  throw new Error(`copied entry.png has the wrong size: ${target}`);
}
