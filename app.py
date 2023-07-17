from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    nome = request.args.get('name')
    if nome:
        return redirect(f"/{nome}")
    elif not nome:
       return render_template("inicial.html")

@app.route("/will")
def will():
   return render_template("will2.html")


@app.route("/rena")
def rena():
   return render_template("rena2.html")

@app.route("/ambos")
def ambos():
   return render_template("ambos2.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
