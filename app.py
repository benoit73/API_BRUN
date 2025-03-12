from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, "/api")

@jsonrpc.method("App.hello")
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
