from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return render_template('result.html', message='Действительные корни отсутствуют')
        elif discriminant == 0:
            x = -b / (2*a)
            return render_template('result.html', message=f'Уравнение имеет единственный корень: {x}')
        else:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            return render_template('result.html', message=f'Уравнение имеет два корня: {x1}, {x2}')
    return render_template('index.html')
def main():
    app.run(debug=True)