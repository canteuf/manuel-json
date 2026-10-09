from pydantic import BaseModel, EmailStr, Field, ValidationError


class Utilisateur(BaseModel):
    id: int = Field(gt=0)
    nom: str
    email: EmailStr
    tags: list[str] = []
    bloque: bool = False


texte = '{"id": 42, "nom": "Bob", "email": "bob@example.com"}'
bob = Utilisateur.model_validate_json(texte)  # analyse et validation en une passe
print(bob.model_dump_json())
# {"id":42,"nom":"Bob","email":"bob@example.com","tags":[],"bloque":false}

try:
    Utilisateur.model_validate_json('{"id": 0, "nom": "Bob", "email": "bob"}')
except ValidationError as erreur:
    print(erreur.error_count(), "erreurs :", [e["loc"][0] for e in erreur.errors()])
    # 2 erreurs : ['id', 'email']
