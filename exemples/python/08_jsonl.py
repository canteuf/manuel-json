import json

import pandas as pd

# Lecture ligne par ligne : chaque ligne est un document JSON complet
with open("json/mesures.jsonl", encoding="utf-8") as f:
    mesures = [json.loads(ligne) for ligne in f if ligne.strip()]
print(len(mesures), "mesures")  # 4 mesures

# pandas lit directement le JSON Lines dans un DataFrame
df = pd.read_json("json/mesures.jsonl", lines=True)
print(df.groupby("capteur")["valeur"].mean().to_dict())  # {'A': 22.5, 'B': 19.5}

# Ajouter un enregistrement = ajouter une ligne (mode "a"), sans relire le fichier :
# with open("mesures.jsonl", "a", encoding="utf-8") as f:
#     f.write(json.dumps({"capteur": "A", "valeur": 22.0}) + "\n")
