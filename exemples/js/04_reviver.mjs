const texte = '{"nom":"Rapport","genereLe":"2026-10-08T22:00:00.000Z"}';

// Dates ISO 8601 en UTC uniquement (suffixe Z), millisecondes facultatives
const dateISO = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z$/;

const donnees = JSON.parse(texte, (cle, valeur) => {
  if (typeof valeur === "string" && dateISO.test(valeur)) {
    return new Date(valeur);
  }
  return valeur;
});

console.log(donnees.genereLe instanceof Date); // true
console.log(donnees.genereLe.getUTCFullYear()); // 2026
