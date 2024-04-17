from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_ganancia_diaria(tasa_anual, monto_inicial):
    # Convertir la tasa anual a tasa diaria
    tasa_diaria = tasa_anual / 365
    
    # Calcular la ganancia diaria
    ganancia_diaria = tasa_diaria * monto_inicial / 100
    
    return ganancia_diaria

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'calcular_diaria' in request.form:
            tasa_anual = float(request.form['tasa_anual'])
            monto_inicial = float(request.form['monto_inicial'])
            ganancia_diaria = calcular_ganancia_diaria(tasa_anual, monto_inicial)
            return render_template('index.html', ganancia_diaria=ganancia_diaria)
        elif 'calcular_total' in request.form:
            ganancia_diaria = float(request.form['ganancia_diaria'])
            dias_total = int(request.form['dias_total'])
            ganancia_total = round(ganancia_diaria * dias_total, 3)
            return render_template('index.html', ganancia_total=ganancia_total)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
