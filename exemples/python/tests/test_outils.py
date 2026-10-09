import os
import shutil
import subprocess

import pytest

SQL_URL = os.environ.get("DATABASE_URL")


@pytest.mark.skipif(shutil.which("jq") is None, reason="jq n'est pas installe")
@pytest.mark.parametrize("filtre, fichier, attendu", [
    (".profil.prenom", "json/utilisateur.json", '"Ada"'),
    ("-r .roles[]", "json/utilisateur.json", "chercheuse\npionniere\nadmin"),
    ('.utilisateurs[] | select(.statut == "actif") | .nom', "json/utilisateurs.json", '"Ada"\n"Katherine"\n"Margaret"'),
    ("-c .coordonnees", "json/utilisateur.json", '{"latitude":51.5074,"longitude":-0.1278}'),
    ("-s length", "json/mesures.jsonl", "4"),
])
def test_jq(filtre, fichier, attendu, lancer):
    options = filtre.split(" ", 1) if filtre.startswith("-") else [filtre]
    assert lancer("jq", *options, fichier).strip() == attendu


def test_json_tool(lancer, python_exe):
    sortie = lancer(python_exe, "-m", "json.tool", "json/utilisateur.json")
    assert '"prenom": "Ada"' in sortie


@pytest.mark.skipif(not SQL_URL or shutil.which("psql") is None,
                    reason="definir DATABASE_URL (base de test uniquement)")
def test_sql_jsonb(lancer):
    lancer("psql", SQL_URL, "-q", "-c", "DROP SCHEMA IF EXISTS manuel_json CASCADE")
    sortie = lancer("psql", SQL_URL, "-v", "ON_ERROR_STOP=1", "-f", "sql/jsonb.sql")
    for morceau in ["Libreville", "Port-Gentil", '{"a": 3, "b": 1}', '{"b": 1, "a": 2, "a": 3}']:
        assert morceau in sortie
    lancer("psql", SQL_URL, "-q", "-c", "DROP SCHEMA IF EXISTS manuel_json CASCADE")
