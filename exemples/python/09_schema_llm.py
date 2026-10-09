import json

from pydantic import BaseModel, Field


class Facture(BaseModel):
    fournisseur: str
    montant_total: float = Field(ge=0)
    devise: str = Field(pattern=r"^[A-Z]{3}$")
    lignes: list[str]


# 1. Le JSON Schema est genere a partir du modele Python
schema = Facture.model_json_schema()
print(json.dumps(schema["required"]))
# ["fournisseur", "montant_total", "devise", "lignes"]

# 2. Corps de requete pour un modele local servi par Ollama (POST /api/chat)
requete = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Extrais la facture suivante : ..."}],
    "format": schema,  # la reponse devra respecter ce schema
    "stream": False,
}

# 3. La reponse se valide comme n'importe quelle donnee externe
reponse = '{"fournisseur": "Papeterie du Centre", "montant_total": 15000, "devise": "XAF", "lignes": ["2 cahiers", "1 stylo"]}'
facture = Facture.model_validate_json(reponse)
print(facture.montant_total, facture.devise)  # 15000.0 XAF
