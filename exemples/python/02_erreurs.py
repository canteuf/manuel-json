import json

texte = '{\n  "nom": "Ada",\n  "age": 36,\n}'  # virgule en trop

try:
    json.loads(texte)
except json.JSONDecodeError as erreur:
    # JSONDecodeError herite de ValueError et indique la position exacte
    print(f"Ligne {erreur.lineno}, colonne {erreur.colno} : {erreur.msg}")
