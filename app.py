from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Saludos a todos desde Dockerfile - Hola a todos "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)