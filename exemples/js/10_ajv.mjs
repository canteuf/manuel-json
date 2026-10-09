import { readFileSync } from "node:fs";
import Ajv2020 from "ajv/dist/2020.js";
import addFormats from "ajv-formats";

const ajv = new Ajv2020({ allErrors: true });
addFormats(ajv); // sans cette ligne, "format" n'est pas verifie

const schema = JSON.parse(readFileSync("json/produit.schema.json", "utf8"));
const valider = ajv.compile(schema);

const produit = JSON.parse(readFileSync("json/produit.json", "utf8"));
console.log(valider(produit)); // true

const invalide = { ...produit, prix: 0, creeLe: "hier", couleur: "bleu" };
console.log(valider(invalide)); // false
for (const e of valider.errors) {
  console.log(e.instancePath || "(racine)", e.message);
}
