# Exemples exécutables du manuel JSON

Chaque fichier correspond à un bloc de code du manuel. Toutes les commandes se lancent depuis ce dossier `exemples/`, car les scripts lisent les données de `json/` par chemin relatif.

## Python (3.10 ou plus récent)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r python\requirements.txt
python python\01_dumps.py
pytest python\tests
```

Si PowerShell refuse d'exécuter `Activate.ps1`, autorisez les scripts locaux une fois pour votre compte :

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## JavaScript et TypeScript (Node.js 22 ou plus récent)

```powershell
cd js
npm install
npm test
npm run typecheck
```

Pour lancer un exemple seul depuis `exemples/` : `node js\01_replacer.mjs`. Pour un fichier TypeScript, depuis `js/` : `npx tsx 08_zod.ts`.

## SQL (PostgreSQL 13 ou plus récent)

Le test SQL ne s'exécute que si la variable `DATABASE_URL` pointe vers une base. Utilisez une base locale ou de test, jamais une base de production : le test crée puis supprime le schéma `manuel_json`.

```powershell
$env:DATABASE_URL = "postgresql://postgres:motdepasse@localhost:5432/postgres"
pytest python\tests\test_outils.py
```

## Organisation

| Dossier | Contenu |
|---|---|
| `json/` | Documents JSON, JSON Lines, schéma et JSON Patch utilisés par le manuel |
| `python/` | Exemples Python et tests `pytest` |
| `js/` | Exemples JavaScript (`.mjs`) et TypeScript (`.ts`), tests `node:test` |
| `sql/` | Exemple PostgreSQL `jsonb` |
