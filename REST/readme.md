📬 Routes de l'API
GET /api/egapro/<siren>

Récupère les données associées à un SIREN.

Réponse :

{
  "siren": "123456789",
  "data": "..."
}

POST /api/egapro

Ajoute des données pour un SIREN.

Corps de la requête :

{
  "siren": "123456789",
  "data": "contenu à insérer"
}