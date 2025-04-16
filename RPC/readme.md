# EgaPro JSON-RPC API

Ce projet est une API Flask qui expose des méthodes JSON-RPC pour interagir avec une base de données PostgreSQL. L'API permet d'exécuter des requêtes sur la base de données et de retourner les résultats au format JSON.

## Prérequis

- Python 3.x
- PostgreSQL
- Flask
- psycopg2
- flask-jsonrpc


## Utilisation
Démarrer l'application

Pour démarrer l'application Flask, exécutez la commande suivante :

python app.py

L'application sera accessible à l'adresse http://localhost:5000.
Méthodes JSON-RPC
App.hello

    Description : Retourne un message de salutation personnalisé.
    Paramètres :
        name (string) : Le nom à inclure dans le message de salutation.
    Exemple de requête :

{
  "jsonrpc": "2.0",
  "method": "App.hello",
  "params": ["World"],
  "id": 1
}

Exemple de réponse :

    {
      "jsonrpc": "2.0",
      "result": "Hello, World!",
      "id": 1
    }

App.test_query

    Description : Exécute une requête SQL pour récupérer les 10 premières lignes de la table egapro et retourne les résultats.
    Paramètres : Aucun.
    Exemple de requête :

{
  "jsonrpc": "2.0",
  "method": "App.test_query",
  "params": [],
  "id": 2
}

Exemple de réponse :

    {
      "jsonrpc": "2.0",
      "result": [
        ["value1", "value2", "value3"],
        ["value4", "value5", "value6"]
      ],
      "id": 2
    }

## Exemple d'utilisation avec curl
Appeler la méthode App.hello

curl -X POST http://localhost:5000/ -d '{"jsonrpc": "2.0", "method": "App.hello", "params": ["World"], "id": 1}' -H "Content-Type: application/json"

Appeler la méthode App.test_query

curl -X POST http://localhost:5000/ -d '{"jsonrpc": "2.0", "method": "App.test_query", "params": [], "id": 2}' -H "Content-Type: application/json"

Exemple d'utilisation avec Postman

    Configurer une requête POST :

        URL : http://localhost:5000/

        Body : raw avec le type JSON

        Contenu du body pour App.hello :

{
  "jsonrpc": "2.0",
  "method": "App.hello",
  "params": ["World"],
  "id": 1
}

Contenu du body pour App.test_query :

    {
      "jsonrpc": "2.0",
      "method": "App.test_query",
      "params": [],
      "id": 2
    }

Envoyer la requête et vérifier la réponse.
