
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))

@app.get("/healthz")
def healthz():
    return "ok", 200

@app.get("/")
def root():
    return jsonify({
        "service": "python-app",
        "message": "Hello from Python/Flask!",
        "path_hint": "Access via /python/",
        "headers": dict(request.headers)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
