from decorator import *
from flask import Flask, render_template, redirect, url_for
from random import choice


app = Flask(__name__)


@app.route('/')
def principal():
    return redirect(url_for("fabricav2"))

@app.route('/fabricav1')
def fabricav1():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()

    productos = []

    productos.append(arma)
    productos.append(escudo)
    return render_template("productos.html", productos = productos)

@app.route('/fabricav2')
def fabricav2():

    objeto = ComponenteConcreto()

    decoradores = [DecoradorConcretoHumanos(objeto), DecoradorConcretoOrcos(objeto)]
    fabrica = choice(decoradores)
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()
    cuerpo = fabrica.crear_cuerpo()
    montura = fabrica.crear_montura()

    productos = []

    productos.append(arma)
    productos.append(escudo)
    productos.append(cuerpo)
    productos.append(montura)

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)
