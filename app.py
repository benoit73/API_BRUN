import psycopg2
from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, "/rpc/")

DB_CONFIG = psycopg2.connect(
    host="bdd",
    # host="10.74.16.190",
    database="mydatabase",  
    user="root",
    password="root"
)

@jsonrpc.method("App.hello")
def hello(name: str) -> str:
    return f"Hello, {name}!"

@jsonrpc.method("App.test_query")
def test_query() -> list:
    try:
        with DB_CONFIG.cursor() as cursor:
            cursor.execute("SELECT * FROM egapro LIMIT 10;")
            result = cursor.fetchall()
        return result
    except Exception as e:
        return [str(e)]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
