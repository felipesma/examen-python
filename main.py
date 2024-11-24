from itertools import filterfalse

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculocompra', methods=['GET', 'POST'])
def calculoCompra():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidadpintura = int(request.form['cantidadpintura'])
        totalpinturas = 9000 * cantidadpintura

        if 18 <= edad <= 30:
            descuento = totalpinturas * 0.15
        elif edad > 30:
            descuento = totalpinturas * 0.25
        else:
            descuento = 0

        totalcompra = totalpinturas - descuento

        return render_template('calculocompra.html', nombre=nombre, totalpinturas=totalpinturas, descuento=int(descuento), totalcompra=int(totalcompra))
    return render_template('calculocompra.html')

@app.route('/iniciosesion', methods=['GET', 'POST'])
def inicioSesion():
    usuarios = {
        'juan': {
            'rol': 'administrador',
            'contrasenha': 'admin'
        },
        'pepe': {
            'rol': 'usuario',
            'contrasenha': 'user'
        }
    }
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        contrasenha = str(request.form['contrasenha'])

        if nombre in usuarios and usuarios[nombre]['contrasenha'] == contrasenha:
            return render_template('iniciosesion.html', rol=usuarios[nombre]['rol'], nombre=nombre)
        else:
            return render_template('iniciosesion.html', error=True)
    return render_template('iniciosesion.html')


if __name__ == '__main__':
    app.run(debug=True)