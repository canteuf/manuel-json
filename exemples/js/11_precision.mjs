const texte = '{"id": 9007199254740993, "idTexte": "9007199254740993"}';
const donnees = JSON.parse(texte);

console.log(donnees.id);                       // 9007199254740992 : valeur faussee
console.log(Number.isSafeInteger(donnees.id)); // false
console.log(BigInt(donnees.idTexte));          // 9007199254740993n : intacte
