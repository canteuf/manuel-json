const utilisateur = {
  id: 101,
  nom: "Martin",
  motDePasseHash: "9f8379c92f3402",
  secretBancaire: "GA21-0000-0000",
  roles: ["editeur", "visiteur"],
};

// 1. Liste blanche : seules les proprietes nommees sont serialisees
console.log(JSON.stringify(utilisateur, ["id", "nom"]));
// {"id":101,"nom":"Martin"}

// 2. Fonction replacer : renvoyer undefined supprime la cle
const masque = JSON.stringify(utilisateur, (cle, valeur) => {
  const c = cle.toLowerCase();
  if (c.includes("secret") || c.includes("hash")) return undefined;
  return valeur;
});
console.log(masque);
// {"id":101,"nom":"Martin","roles":["editeur","visiteur"]}

// 3. Troisieme parametre : indentation de 2 espaces
console.log(JSON.stringify({ a: 1, b: [true, null] }, null, 2));
