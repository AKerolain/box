from flask import Flask, render_template

app = Flask(__name__)
nome_app = "Mercado Tech"
@app.route('/')
def inicio():
    return render_template ('index.html')

app.run()    