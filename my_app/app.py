from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Aplicación corriendo con Docker y App Services de Microsoft Azure!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
