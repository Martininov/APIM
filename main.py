from flask import Flask, jsonify
from . import understat   # ✅ Import du module local au lieu du package PyPI
import constants

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Understat API est en ligne sur Render"

@app.route("/constants")
def get_constants():
    return jsonify({k: getattr(constants, k) for k in dir(constants) if not k.startswith("__")})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
