from flask import Flask
from spyne import Application, rpc, ServiceBase, Iterable, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import psycopg2

# Service SOAP avec Spyne
class EgaProService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def get_egapro_data(ctx):
        conn = psycopg2.connect(
            host="bdd",           # Nom d'hôte du conteneur PostgreSQL
            database="mydatabase",
            user="root",
            password="root"
        )
        cur = conn.cursor()
        cur.execute("SELECT id, field_1, field_2 FROM egapro_data")
        rows = cur.fetchall()
        for row in rows:
            yield f"ID: {row[0]}, Field 1: {row[1]}, Field 2: {row[2]}"
        cur.close()
        conn.close()

# Configuration de Spyne
soap_app = Application(
    [EgaProService],
    tns='http://example.com/egapro',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

# Flask
flask_app = Flask(__name__)

# Intégration Spyne via DispatcherMiddleware
flask_app.wsgi_app = DispatcherMiddleware(flask_app.wsgi_app, {
    '/soap': WsgiApplication(soap_app)
})

if __name__ == "__main__":
    flask_app.run(debug=True, host="0.0.0.0")
