from pathlib import Path

import pytest

DOSSIER = Path(__file__).resolve().parents[1]

ATTENDUS = {
    "01_dumps.py": ['"utilisateur": "Hélène"', r"H\u00e9l\u00e8ne", '{"version":2,"client":"web"}', "NaN", "Refuse :"],
    "02_erreurs.py": ["Ligne ", "colonne "],
    "03_encodeur.py": ['"montant": "149.99"', '"emiseLe": "2026-10-08T22:00:00"', '"statut": "payee"'],
    "04_object_hook.py": ["Coordonnees(lat=0.4162, lon=9.4673)"],
    "05_pydantic.py": ['"tags":[],"bloque":false', "2 erreurs : ['id', 'email']"],
    "06_jsonschema.py": ["True", "['prix']", "'hier' is not a 'date-time'", "'couleur' was unexpected"],
    "07_ijson.py": ["Comptes actifs : 3"],
    "08_jsonl.py": ["4 mesures", "{'A': 22.5, 'B': 19.5}"],
    "09_schema_llm.py": ['["fournisseur", "montant_total", "devise", "lignes"]', "15000.0 XAF"],
    "10_jwt.py": ["{'alg': 'HS256', 'typ': 'JWT'}", "'role': 'admin'"],
    "11_doublons.py": ["{'role': 'admin'}", "Cles en double : ['role']"],
}


@pytest.mark.parametrize("script", sorted(ATTENDUS))
def test_exemple(script, lancer, python_exe):
    sortie = lancer(python_exe, f"python/{script}")
    for morceau in ATTENDUS[script]:
        assert morceau in sortie, f"{morceau!r} absent de :\n{sortie}"


def test_chaque_exemple_a_un_test():
    scripts = {p.name for p in DOSSIER.glob("[0-9][0-9]_*.py")}
    assert scripts == set(ATTENDUS)
