from flask import Flask, render_template, request, redirect, session, flash, url_for
import math

app = Flask(__name__)

class Resultado():
    def __init__(self, primeiro_numero, segundo_numero, primos):
        self.primeiro_numero = str(primeiro_numero)
        self.segundo_numero = str(segundo_numero)
        self.primos = primos[0]

lista = []

def ehPrimo(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    elif ( n %2 == 0):
        return False
    
    for k in range (3, math.floor(math.sqrt(n))+1, 2):
        if (n %k == 0):
            return False
    return True

def calculaPrimosEntre(x, y):
    lista_primos = []
    if (x % 2 != 0):
        for i in range(x, y+1):
            resultado = ehPrimo(i)
            if resultado == True:
                lista_primos.append(i)
            i += 2
            
    else:
        for i in range(x, y+1):
            resultado = ehPrimo(i)
            if resultado == True:
                lista_primos.append(i)
            i += 1

    return lista_primos

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

        primos = calculaPrimosEntre(primeiro_numero, segundo_numero)
        primos = [str(x) for x in primos]
        primos = [', '. join(primos)]
        resultado = Resultado(primeiro_numero, segundo_numero, primos)
        lista.append(resultado)
        return redirect(url_for('mostrar'))
    
    return render_template('novo.html', error=error)


app.run()

