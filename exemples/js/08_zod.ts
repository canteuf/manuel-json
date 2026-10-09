import { z } from "zod";

const SchemaUtilisateur = z.object({
  id: z.number().int().positive(),
  email: z.email(),
  roles: z.array(z.string()).min(1),
  derniereConnexion: z.iso.datetime().optional(),
});

// Le type TypeScript est deduit du schema : une seule source de verite
type Utilisateur = z.infer<typeof SchemaUtilisateur>;

function lireUtilisateur(texte: string): Utilisateur {
  return SchemaUtilisateur.parse(JSON.parse(texte));
}

const ada = lireUtilisateur('{"id": 7, "email": "ada@example.com", "roles": ["admin"]}');
console.log(ada.email); // ada@example.com

const resultat = SchemaUtilisateur.safeParse({ id: -1, email: "ada", roles: [] });
if (!resultat.success) {
  console.log(resultat.error.issues.map((i) => i.path.join(".")));
  // [ 'id', 'email', 'roles' ]
}
