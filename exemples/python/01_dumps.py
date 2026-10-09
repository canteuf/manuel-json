import json

donnees = {
    "utilisateur": "Hélène",
    "actif": True,
    "scores": [19.5, 18.0, 20.0],
    "meta": {"version": 2, "client": "web"},
}

# Lisible : indentation, accents conserves, cles triees
print(json.dumps(donnees, indent=2, ensure_ascii=False, sort_keys=True))

# Par defaut, les caracteres non ASCII sont echappes
print(json.dumps({"utilisateur": "Hélène"}))  # {"utilisateur": "H\u00e9l\u00e8ne"}

# Compact : aucun espace apres les separateurs
print(json.dumps(donnees["meta"], separators=(",", ":")))  # {"version":2,"client":"web"}

# NaN : interdit par la grammaire JSON, mais produit par defaut en Python
print(json.dumps(float("nan")))  # NaN
try:
    json.dumps(float("nan"), allow_nan=False)
except ValueError as erreur:
    print("Refuse :", erreur)
