from flask import Flask, jsonify, request, send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_swagger_ui import get_swaggerui_blueprint
import os 

#Initialisation de Flask
app = Flask(__name__)

# Définir le chemin vers le fichier Swagger YAML
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yml'  # Le fichier Swagger est placé dans /static

# Configuration de Flask-Swagger-UI
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "EgaPro API"
    }
)

# Enregistrer Swagger-UI avec Flask
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Configuration de la connexion à PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',   # Le nom d'hôte de la base de données PostgreSQL
        database='egapro',  # Nom de la base de données
        user='your_user',   # Votre utilisateur PostgreSQL
        password='your_password'  # Votre mot de passe PostgreSQL
    )
    return conn
 
@app.route("/")
def home():
    return jsonify({"message": "Hello, Docker!"})

# Route pour récupérer les données d'un SIREN
@app.route('/api/egapro/<siren>', methods=['GET'])
def get_egapro_data(siren):
    # Se connecter à la base de données PostgreSQL
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Exécuter la requête pour récupérer les données du SIREN
    cursor.execute('SELECT * FROM egapro_data WHERE siren = %s', (siren,))
    row = cursor.fetchone()  # Récupérer une ligne de résultats

    # Si des données sont trouvées pour ce SIREN, les retourner
    if row:
        result = {
            'siren': row['siren'],
            'data': row['data']
        }
        conn.close()
        return jsonify(result), 200
    else:
        # Si aucun résultat trouvé, retourner une erreur 404
        conn.close()
        return jsonify({'error': 'Données non trouvées pour ce SIREN'}), 404

# Route pour ajouter des données dans la base de données PostgreSQL
@app.route('/api/egapro', methods=['POST'])
def add_egapro_data():
    # Récupérer les données JSON envoyées par le client
    data = request.get_json()
    
    siren = data.get('siren')
    data_value = data.get('data')

    if not siren or not data_value:
        return jsonify({'error': 'SIREN et données sont nécessaires'}), 400

    # Se connecter à la base de données PostgreSQL
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ajouter les données dans la table egapro_data
    cursor.execute('INSERT INTO egapro_data (siren, data) VALUES (%s, %s)', (siren, data_value))
    conn.commit()  # Valider la transaction
    conn.close()

    return jsonify({'message': 'Données ajoutées avec succès'}), 201
 
# Route pour servir le fichier Swagger.yml (si vous ne voulez pas le stocker statiquement dans Flask)
@app.route('/static/swagger.yml')
def swagger_yml():
    return send_from_directory(os.getcwd(), 'swagger.yml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)