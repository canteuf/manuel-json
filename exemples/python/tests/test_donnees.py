import json
from pathlib import Path

import jsonpatch
import jsonpointer
import pytest

JSON = Path(__file__).resolve().parents[2] / "json"


@pytest.mark.parametrize("fichier", sorted(p.name for p in JSON.glob("*.json")))
def test_fichiers_json_valides(fichier):
    json.loads((JSON / fichier).read_text(encoding="utf-8"))


def test_jsonl_une_valeur_par_ligne():
    lignes = (JSON / "mesures.jsonl").read_text(encoding="utf-8").splitlines()
    assert all(isinstance(json.loads(l), dict) for l in lignes)


def test_json_pointer():
    doc = json.loads((JSON / "contacts.json").read_text(encoding="utf-8"))
    assert jsonpointer.resolve_pointer(doc, "/utilisateurs/0/nom") == "Alice"
    assert jsonpointer.resolve_pointer(doc, "/utilisateurs/0/contacts/email~1pro") == "alice@example.com"


def test_json_patch():
    doc = json.loads((JSON / "commande.json").read_text(encoding="utf-8"))
    patch = json.loads((JSON / "commande.patch.json").read_text(encoding="utf-8"))
    assert jsonpatch.apply_patch(doc, patch) == {
        "statut": "validee", "montant": 15000, "validePar": "Administrateur",
    }


def test_json_patch_test_echoue_annule_tout():
    doc = {"statut": "validee", "brouillon": {}}
    patch = json.loads((JSON / "commande.patch.json").read_text(encoding="utf-8"))
    with pytest.raises(jsonpatch.JsonPatchTestFailed):
        jsonpatch.apply_patch(doc, patch)
    assert doc == {"statut": "validee", "brouillon": {}}  # document intact


def test_json_merge_patch_rfc7396():
    # Algorithme de la RFC 7396, section 2
    def merge(cible, patch):
        if not isinstance(patch, dict):
            return patch
        cible = dict(cible) if isinstance(cible, dict) else {}
        for cle, valeur in patch.items():
            if valeur is None:
                cible.pop(cle, None)
            else:
                cible[cle] = merge(cible.get(cle), valeur)
        return cible

    doc = json.loads((JSON / "commande.json").read_text(encoding="utf-8"))
    assert merge(doc, {"statut": "validee", "brouillon": None}) == {"statut": "validee", "montant": 15000}
