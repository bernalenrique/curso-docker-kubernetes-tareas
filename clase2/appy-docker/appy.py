import os
from flask import Flask, jsonify

app = Flask(__name__)

# --- Endpoint 1
@app.route('/')
def home():
    return "Hola, este es el endpoint 1 \n"

# --- Endpoint 2
@app.route('/apiinfo')
def info():
    return jsonify({
        "mensaje": "Este es el endpoint 2, adios",
        "status": "ok",
        "puerto": os.environ.get("PORT", 5000)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    #host='0.0.0.0' permite la conexión desde el exterior del contenedor
    app.run(debug=True, host='0.0.0.0', port=port)
