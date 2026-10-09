import json

texte = '{"role": "lecteur", "role": "admin"}'
print(json.loads(texte))  # {'role': 'admin'} : la derniere valeur gagne


def sans_doublons(paires: list[tuple]) -> dict:
    # Recoit les paires (cle, valeur) dans l'ordre, doublons compris
    cles = [cle for cle, _ in paires]
    doublons = sorted({c for c in cles if cles.count(c) > 1})
    if doublons:
        raise ValueError(f"Cles en double : {doublons}")
    return dict(paires)


try:
    json.loads(texte, object_pairs_hook=sans_doublons)
except ValueError as erreur:
    print(erreur)  # Cles en double : ['role']
