import psycopg2
from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, "/api")

DB_CONFIG = psycopg2.connect(
    host="bdd",    
    database="mydatabase",  
    user="root",
    password="root"
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
