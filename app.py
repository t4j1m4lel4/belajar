from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Hello from Flask on Termux!</h1><p>Proyek 2: Web Server Mini</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
