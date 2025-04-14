from flask import Flask
from spyne import Application, rpc, ServiceBase, Iterable, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.flask import FlaskApplication
import psycopg2

# Initialisation de l'application Flask
app = Flask(__name__)

# Connexion à la base de données PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="bdd",    # Le nom d'hôte de la base de données PostgreSQL
        database="mydatabase",  # Nom de la base de données
        user="root",            # Nom d'utilisateur PostgreSQL
        password="root"         # Mot de passe PostgreSQL
    )
    return conn

# Service SOAP avec Spyne
class EgaProService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def get_egapro_data(ctx):
        # Se connecter à la base de données PostgreSQL
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Exécuter une requête pour récupérer les données
        cur.execute("SELECT id, field_1, field_2 FROM egapro_data")
        rows = cur.fetchall()

        # Retourner les données sous forme de chaîne
        for row in rows:
            yield f"ID: {row[0]}, Field 1: {row[1]}, Field 2: {row[2]}"

        # Fermer la connexion
        cur.close()
        conn.close()

# Configurer l'application SOAP
soap_app = Application([EgaProService],
                       tns='http://example.com/egapro',
                       in_protocol=Soap11(),
                       out_protocol=Soap11())

# Créer l'application Flask-Spyne
soap_service = FlaskApplication(soap_app, app)

# Ajouter le service SOAP à une route
@app.route('/', methods=['POST'])
def soap():
    return soap_service()

if __name__ == "__main__":
    app.run(debug=True)
