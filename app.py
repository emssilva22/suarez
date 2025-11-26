from flask import Flask, request, jsonify

app = Flask(__name__)


HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mini IA – Flask App</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #4f46e5, #6366f1);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 18px;
            backdrop-filter: blur(12px);
            max-width: 450px;
            width: 90%;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.25);
        }
        h1 {
            margin-bottom: 10px;
            font-size: 28px;
        }
        p {
            font-size: 16px;
            line-height: 1.4;
        }
        .btn {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 20px;
            background: #ffffff;
            color: #4f46e5;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }
        .btn:hover {
            background: #e0e0ff;
        }
        .endpoints {
            margin-top: 20px;
            text-align: left;
            font-size: 14px;
        }
        .endpoints code {
            background: rgba(255, 255, 255, 0.2);
            padding: 4px 6px;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Mini IA Flask</h1>
        <p>
            Bienvenido a tu servicio desplegado con CI/CD.  
            Este proyecto demuestra una API simple con IA simulada.
        </p>

        <div class="endpoints">
            <h3>📌 Endpoints:</h3>
            <p>GET → <code>/</code></p>
            <p>POST → <code>/saludar</code></p>
            <p>POST → <code>/ia</code></p>
        </div>
    </div>
</body>
</html>
"""

# --- Simulador sencillo de IA ---
def mini_ia(texto: str) -> str:
    texto = texto.lower()

    if any(p in texto for p in ["hola", "buenas", "hey"]):
        return "Parece que estás saludando 👋"
    if "adios" in texto or "bye" in texto:
        return "Parece que te estás despidiendo 👋"
    if "ayuda" in texto or "soporte" in texto:
        return "Detecté que necesitas ayuda 🛠️"
    if "comprar" in texto:
        return "Parece una intención de compra 🛒"

    return "No entendí muy bien, pero estoy aprendiendo 🤖"


@app.get("/")
def home():
    return HTML_PAGE


@app.post("/saludar")
def saludar():
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre", "")

    if not nombre:
        return jsonify({"error": "Debes enviar un nombre"}), 400

    return jsonify({
        "mensaje": f"Hola {nombre} 😄",
        "detalle": "Gracias por probar la API"
    })


@app.post("/ia")
def ia():
    data = request.get_json(silent=True) or {}
    texto = data.get("texto", "")

    if not texto:
        return jsonify({"error": "Debes enviar un texto"}), 400

    resultado = mini_ia(texto)

    return jsonify({
        "input": texto,
        "resultado": resultado,
        "modelo": "mini-ia-v1"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
