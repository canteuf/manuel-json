const INTERDITES = new Set(["__proto__", "constructor", "prototype"]);

// Fusion recursive ; avec protegee = false, elle reproduit l'erreur courante
function fusion(cible, source, protegee) {
  for (const cle of Object.keys(source)) {
    if (protegee && INTERDITES.has(cle)) continue;
    if (typeof source[cle] === "object" && source[cle] !== null) {
      cible[cle] ??= {};
      fusion(cible[cle], source[cle], protegee);
    } else {
      cible[cle] = source[cle];
    }
  }
  return cible;
}

const entree = JSON.parse('{"__proto__": {"admin": true}}');
console.log(Object.keys(entree)); // [ '__proto__' ] : simple propriete

fusion({}, entree, false);
console.log({}.admin); // true : le prototype de TOUS les objets est modifie
delete Object.prototype.admin; // nettoyage pour la suite de l'exemple

fusion({}, entree, true);
console.log({}.admin); // undefined : les cles dangereuses sont ignorees
