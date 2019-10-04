from flask import Flask, render_template, request, redirect
from investimento import Investimento
from carteira_investimento import Carteira_investimento


app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo_pagina = 'Home')


app.run()