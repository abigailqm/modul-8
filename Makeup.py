from flask import Flask, render_template, request


app = Flask(__name__)

# Halaman pertama
@app.route('/')
def index():
    return render_template('Front.html')

# Halaman kedua
@app.route('/<size>')
def lights(size):
    return render_template(
                            'Makeup.html'
                           )

app.run(debug=True)