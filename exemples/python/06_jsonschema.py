import json
from jsonschema import Draft202012Validator

with open("json/produit.schema.json", encoding="utf-8") as f:
    schema = json.load(f)

# FORMAT_CHECKER active la verification de "format" (desactivee par defaut)
validateur = Draft202012Validator(
    schema, format_checker=Draft202012Validator.FORMAT_CHECKER
)

with open("json/produit.json", encoding="utf-8") as f:
    produit = json.load(f)
print(validateur.is_valid(produit))  # True

invalide = {**produit, "prix": 0, "creeLe": "hier", "couleur": "bleu"}
for erreur in validateur.iter_errors(invalide):
    print(list(erreur.path), erreur.message)
