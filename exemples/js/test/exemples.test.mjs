// Lance chaque exemple depuis le dossier exemples/ et verifie sa sortie.
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const dossierJs = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const dossierExemples = path.dirname(dossierJs);
const chargeurTs = import.meta.resolve("tsx");

const attendus = {
  "01_replacer.mjs": ['{"id":101,"nom":"Martin"}', '"roles":["editeur","visiteur"]}'],
  "02_tojson.mjs": ['{"prix":{"valeur":"49.90","devise":"EUR"}}', '"2026-10-08T22:00:00.000Z"'],
  "03_cycles.mjs": ['"parent":"[Reference circulaire]"', '{"a":{"n":1},"b":{"n":1}}'],
  "04_reviver.mjs": ["true\n2026"],
  "05_erreurs_parse.mjs": ["true\nfalse\nfalse", "Reponse non JSON (text/html)"],
  "06_structuredclone.mjs": ["string\n{}\nfalse\ntrue\ntrue\ntrue"],
  "07_types_json.ts": ['{"nom":"Ada","roles":["admin"],"actif":true,"titre":null}'],
  "08_zod.ts": ["ada@example.com", "[ 'id', 'email', 'roles' ]"],
  "09_zod_vers_schema.ts": ['"exclusiveMinimum": 0', '"additionalProperties": false'],
  "10_ajv.mjs": ["true\nfalse", "/prix must be > 0", 'must match format "date-time"'],
  "11_precision.mjs": ["9007199254740992\nfalse\n9007199254740993n"],
  "12_pollution.mjs": ["[ '__proto__' ]\ntrue\nundefined"],
};

function lancer(fichier) {
  const args = fichier.endsWith(".ts") ? ["--import", chargeurTs] : [];
  return execFileSync(process.execPath, [...args, path.join("js", fichier)], {
    cwd: dossierExemples,
    encoding: "utf8",
  });
}

for (const [fichier, morceaux] of Object.entries(attendus)) {
  test(fichier, () => {
    const sortie = lancer(fichier);
    for (const m of morceaux) assert.ok(sortie.includes(m), `"${m}" absent de :\n${sortie}`);
  });
}

test("chaque exemple a un test", () => {
  const fichiers = readdirSync(dossierJs).filter((f) => /^\d\d_.*\.(mjs|ts)$/.test(f));
  assert.deepEqual(fichiers.sort(), Object.keys(attendus).sort());
});
