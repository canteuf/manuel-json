import json
from dataclasses import dataclass


@dataclass
class Coordonnees:
    lat: float
    lon: float


def vers_coordonnees(d: dict):
    # Appelee pour chaque objet JSON decode, des plus profonds aux plus externes
    if d.keys() == {"lat", "lon"}:
        return Coordonnees(**d)
    return d


texte = '{"ville": "Libreville", "point": {"lat": 0.4162, "lon": 9.4673}}'
resultat = json.loads(texte, object_hook=vers_coordonnees)
print(resultat["point"])  # Coordonnees(lat=0.4162, lon=9.4673)
