from flask import Flask, render_template, request, redirect, session, flash, url_for
import math

app = Flask(__name__)

class Resultado():
    def __init__(self, primeiro_numero, segundo_numero, primos):
        self.primeiro_numero = str(primeiro_numero)
        self.segundo_numero = str(segundo_numero)
        self.primos = primos[0]

lista = []

import math

def lista_numeros(lim):
    lista = []

    for index in range(2, lim):
        lista.append(index)

    return lista

def remove_zeros(lista, menor):
    lista2 = []

    for index in range(len(lista)):
        if lista[index] and lista[index] > menor:
            lista2.append(lista[index])

    return lista2

def calculaPrimosEntre(maior, menor):

    lista = lista_numeros(maior)
    limite = int(math.sqrt(maior))

    for index1 in range(0, limite):
        if not lista[index1]:
            continue

        for index2 in range(index1 + 1, maior - 2):
            if lista[index2] and (not (lista[index2] % lista[index1])):
                lista[index2] = 0

    return remove_zeros(lista, menor)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/inserir')
def index():
    return render_template('novo.html')

@app.route('/resultado')
def mostrar():
    return render_template('lista.html', titulo='Lista', lista=lista)

@app.route('/redirecionar', methods=['POST', ])
def redirecionar():
    return redirect(url_for('index'))


@app.route('/criar', methods=['POST', 'GET'])
def criar():
    error = None
    aux = 0
    primeiro_numero = request.form['primeiro_numero']
    segundo_numero = request.form['segundo_numero']

    if primeiro_numero == "" or segundo_numero == "":
        error = "Você não digitou um número em algum campo."
        return render_template('novo.html', error=error)
    else:

        primeiro_numero = int(primeiro_numero)
        segundo_numero = int(segundo_numero)

        if segundo_numero < primeiro_numero:
            aux = primeiro_numero
            primeiro_numero = segundo_numero
            segundo_numero = aux

        primos = calculaPrimosEntre(segundo_numero, primeiro_numero)
        primos = [str(x) for x in primos]
        primos = [', '. join(primos)]
        resultado = Resultado(primeiro_numero, segundo_numero, primos)
        lista.append(resultado)
        return redirect(url_for('mostrar'))
    
    return render_template('novo.html', error=error)


app.run()