# EgaPro API

Ce projet est une API Flask qui permet de récupérer et d'ajouter des données dans une base de données PostgreSQL. L'API utilise Flask-Swagger-UI pour la documentation interactive des endpoints.

## Prérequis

- Python 3.x
- PostgreSQL
- Flask
- psycopg2
- flask-swagger-ui

L'application sera accessible à l'adresse http://localhost:5000.
## Endpoints
### Accueil

    URL : /
    Méthode : GET
    Description : Retourne un message de bienvenue.
    Réponse :

    {
      "message": "Hello, Docker!"
    }

### Récupérer les données d'un SIREN

    URL : /api/egapro/<siren>
    Méthode : GET
    Description : Récupère les données associées à un SIREN spécifique.
    Paramètres :
        siren (path parameter) : Le SIREN pour lequel récupérer les données.
    Réponse :
        Succès :

{
  "siren": "123456789",
  "data": "Données associées au SIREN"
}

Erreur :

        {
          "error": "Donnees non trouvees pour ce SIREN"
        }

### Ajouter des données

    URL : /api/egapro
    Méthode : POST
    Description : Ajoute des données dans la base de données PostgreSQL.
    Corps de la requête :

{
  "siren": "123456789",
  "data": "Nouvelles données"
}

Réponse :

    Succès :

{
  "message": "Données ajoutées avec succès"
}

Erreur :

        {
          "error": "SIREN et données sont nécessaires"
        }

### Documentation Swagger

La documentation interactive de l'API est disponible à l'adresse http://localhost:5000/swagger. Le fichier Swagger YAML est servi à partir de /static/swagger.yml.
