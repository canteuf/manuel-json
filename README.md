# Manuel de référence : le format JSON

Manuel en français sur le format JSON pour les développeurs qui l'utilisent au quotidien en JavaScript/TypeScript, en Python et en SQL : normes, validation par schémas, pièges de sécurité, gros volumes et outils.

- `manuel_reference_json.pdf` : le manuel compilé.
- `manuel_reference_json.tex` et `references.bib` : les sources LaTeX.
- `exemples/` : tous les codes du manuel, sous forme de fichiers exécutables et testés.

Le manuel inclut directement les fichiers de `exemples/` : le code imprimé et le code testé sont les mêmes fichiers. Les tests tournent à chaque push grâce à GitHub Actions (`.github/workflows/exemples.yml`).

## Compiler le PDF

```powershell
pdflatex manuel_reference_json.tex
bibtex manuel_reference_json
pdflatex manuel_reference_json.tex
pdflatex manuel_reference_json.tex
```

Auteur : Teufack Doury Cantor.
