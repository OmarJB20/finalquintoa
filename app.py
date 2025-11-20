from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicación desplegada con Docker  funcionando correctamente - Saludos a todos !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)

    
