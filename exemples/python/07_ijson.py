import ijson

# ijson lit le fichier par morceaux : un seul utilisateur en memoire a la fois
with open("json/utilisateurs.json", "rb") as f:
    actifs = sum(
        1 for u in ijson.items(f, "utilisateurs.item") if u["statut"] == "actif"
    )

print(f"Comptes actifs : {actifs}")  # Comptes actifs : 3
