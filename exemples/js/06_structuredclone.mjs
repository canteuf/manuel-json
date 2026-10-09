const original = {
  nom: "Rapport",
  creeLe: new Date("2026-10-08T22:00:00Z"),
  tags: new Set(["json", "manuel"]),
  note: undefined,
};

// Copie par aller-retour JSON : types perdus sans avertissement
const copieJSON = JSON.parse(JSON.stringify(original));
console.log(typeof copieJSON.creeLe); // string
console.log(copieJSON.tags);          // {}
console.log("note" in copieJSON);     // false

// structuredClone conserve Date, Set, Map et les valeurs undefined
const copie = structuredClone(original);
console.log(copie.creeLe instanceof Date);     // true
console.log(copie.tags.has("json"));           // true
console.log(copie.creeLe !== original.creeLe); // true : vraie copie
