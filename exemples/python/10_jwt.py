import base64
import json

# en-tete . charge utile . signature (jeton de demonstration)
jeton = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ".eyJzdWIiOiI0MiIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc5MTUwMDAwMH0"
    ".7G4nli0DKe1i4y7RFj9X7dYdcuCgXs4a5yftUsM9cvU"
)


def decoder(segment: str) -> dict:
    remplissage = "=" * (-len(segment) % 4)  # Base64URL omet les "="
    return json.loads(base64.urlsafe_b64decode(segment + remplissage))


entete, charge_utile, _signature = jeton.split(".")
print(decoder(entete))        # {'alg': 'HS256', 'typ': 'JWT'}
print(decoder(charge_utile))  # {'sub': '42', 'role': 'admin', 'exp': 1791500000}
# Aucune cle n'a ete necessaire : la charge utile est lisible par tous.
