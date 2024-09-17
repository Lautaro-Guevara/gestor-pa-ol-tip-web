from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entrega-epp')
def entrega_epp():
    return render_template('entrega-epp.html')

@app.route("/ejemplo")
def ejemplo():
    return render_template("ejemplo.html")

if __name__ == "__main__":
    app.run(debug=True)
