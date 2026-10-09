function safeStringify(obj, space) {
  const ancetres = [];
  return JSON.stringify(obj, function (cle, valeur) {
    if (typeof valeur !== "object" || valeur === null) return valeur;
    // "this" est l'objet qui contient la cle en cours :
    // on retire de la pile les objets qui ne sont plus des ancetres.
    while (ancetres.length > 0 && ancetres.at(-1) !== this) {
      ancetres.pop();
    }
    if (ancetres.includes(valeur)) return "[Reference circulaire]";
    ancetres.push(valeur);
    return valeur;
  }, space);
}

const noeud = { nom: "racine", enfant: {} };
noeud.enfant.parent = noeud; // cycle
console.log(safeStringify(noeud));
// {"nom":"racine","enfant":{"parent":"[Reference circulaire]"}}

const x = { n: 1 };
console.log(safeStringify({ a: x, b: x })); // objet partage, pas de cycle
// {"a":{"n":1},"b":{"n":1}}
