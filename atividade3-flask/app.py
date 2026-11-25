from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)