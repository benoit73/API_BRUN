# 🐳 API_BRUN - Multi-API avec Docker Compose

Ce projet contient un ensemble de services API (REST, RPC, SOAP) basés sur Flask, déployés avec Docker Compose. Il inclut également une base de données PostgreSQL, un reverse proxy Nginx et une interface d'administration PgAdmin.


### ✅ Prérequis

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 🔧 Lancer les services
docker-compose build --no-cache
docker-compose up

### Les services suivants seront disponibles :
Service	URL
REST API	http://localhost/rest/
RPC API	http://localhost/rpc/
SOAP API	http://localhost/soap/
PgAdmin	http://localhost:5050

### 🌐 Nginx

Nginx sert de reverse proxy vers les trois services sur les chemins :

    /rest/ → Service REST

    /rpc/ → Service RPC

    /soap/ → Service SOAP

### 🛠️ Développement

Chaque service est un conteneur indépendant basé sur une image Python. Les dépendances sont installées via pip dans les Dockerfiles.
### 📂 Volumes et Réseau

    Volume : postgres_data

    Réseau : myNetwork (tous les services sont sur ce réseau)

### 🧠 Identifiants PgAdmin

    Email : root@root.root

    Mot de passe : root

Ajoutez un serveur dans PgAdmin :

    Nom : Postgres

    Hôte : bdd

    Port : 5432

    Utilisateur : root

### Routes disponibles
Les routes disponibles sont répertoriées dans les différents dossiers des API, dans les readme respectifs.
