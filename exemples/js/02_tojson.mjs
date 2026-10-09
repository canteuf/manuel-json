class Montant {
  constructor(centimes, devise) {
    this.centimes = centimes;
    this.devise = devise;
  }

  // Appelee automatiquement par JSON.stringify
  toJSON() {
    return { valeur: (this.centimes / 100).toFixed(2), devise: this.devise };
  }
}

console.log(JSON.stringify({ prix: new Montant(4990, "EUR") }));
// {"prix":{"valeur":"49.90","devise":"EUR"}}

// Date possede deja une methode toJSON qui appelle toISOString
console.log(JSON.stringify({ le: new Date(Date.UTC(2026, 9, 8, 22)) }));
// {"le":"2026-10-08T22:00:00.000Z"}
