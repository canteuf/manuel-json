-- Schema dedie aux exemples, pour ne rien melanger avec vos propres tables
CREATE SCHEMA IF NOT EXISTS manuel_json;
SET search_path TO manuel_json;

CREATE TABLE commandes (
  id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  client  text  NOT NULL,
  details jsonb NOT NULL
);

INSERT INTO commandes (client, details) VALUES
  ('Ada',   '{"livraison": {"ville": "Libreville"}, "articles": ["cahier", "stylo"], "express": true}'),
  ('Grace', '{"livraison": {"ville": "Douala"}, "articles": ["cartable"], "express": false}');

-- -> renvoie du jsonb, ->> renvoie du texte
SELECT client,
       details -> 'livraison' ->> 'ville'        AS ville,
       jsonb_array_length(details -> 'articles') AS nb_articles
FROM commandes;

-- @> teste si le document contient un fragment ; un index GIN l'accelere
CREATE INDEX commandes_details_idx ON commandes USING GIN (details);
SELECT client FROM commandes WHERE details @> '{"express": true}';

-- Modifier une valeur imbriquee sans reecrire le reste du document
UPDATE commandes
SET details = jsonb_set(details, '{livraison,ville}', '"Port-Gentil"')
WHERE client = 'Ada';
SELECT details -> 'livraison' ->> 'ville' AS ville FROM commandes WHERE client = 'Ada';

-- json garde le texte tel quel ; jsonb le normalise (derniere cle dupliquee gardee)
SELECT '{"b": 1, "a": 2, "a": 3}'::json  AS texte_json,
       '{"b": 1, "a": 2, "a": 3}'::jsonb AS texte_jsonb;
