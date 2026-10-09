import json
import uuid
from datetime import datetime, date
from decimal import Decimal
from enum import Enum


class Statut(Enum):
    PAYEE = "payee"


class EncodeurEtendu(json.JSONEncoder):
    # Appelee uniquement pour les objets que json ne sait pas serialiser
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if isinstance(obj, Decimal):
            return str(obj)  # float(obj) perdrait de la precision
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)


facture = {
    "id": uuid.UUID("6f1c2a9e-3b4d-4e5f-8a7b-1c2d3e4f5a6b"),
    "emiseLe": datetime(2026, 10, 8, 22, 0),
    "montant": Decimal("149.99"),
    "statut": Statut.PAYEE,
}
print(json.dumps(facture, cls=EncodeurEtendu))
