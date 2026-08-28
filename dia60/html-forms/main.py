from flask import Flask, render_template, request, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        password = request.form['password']

        # Devuelve directamente el h1 formateado
        return f"<h1>Name: {nombre} {apellido}, Password: {password}</h1>"

if __name__ == '__main__':
    app.run(debug=True)