function lireJSON(texte) {
  try {
    return { ok: true, valeur: JSON.parse(texte) };
  } catch (err) {
    if (err instanceof SyntaxError) return { ok: false, erreur: err.message };
    throw err; // toute autre erreur n'est pas un probleme de syntaxe
  }
}

console.log(lireJSON('{"a": 1}').ok);         // true
console.log(lireJSON("{'a': 1}").ok);         // false
console.log(lireJSON("<!DOCTYPE html>").ok);  // false

// Avec fetch : verifier le statut et le type de contenu avant .json()
async function lireReponse(reponse) {
  if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
  const type = reponse.headers.get("content-type") ?? "";
  if (!type.includes("json")) {
    const debut = (await reponse.text()).slice(0, 40);
    throw new Error(`Reponse non JSON (${type}) : ${debut}`);
  }
  return reponse.json();
}

// Simulation d'un serveur qui renvoie une page HTML au lieu de JSON
const pageErreur = new Response("<!DOCTYPE html><h1>Maintenance</h1>", {
  headers: { "content-type": "text/html" },
});
try {
  await lireReponse(pageErreur); // en vrai : await lireReponse(await fetch(url))
} catch (err) {
  console.log(err.message);
  // Reponse non JSON (text/html) : <!DOCTYPE html><h1>Maintenance</h1>
}
