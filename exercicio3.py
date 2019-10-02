from alunos import Alunos
from flask import Flask, render_template, request, redirect

pagina_nome = 'LISTA ALUNOS'
# aluno1 = Alunos('Jonathan','Prange', 479997908805)
# aluno2 = Alunos('Maykon','D. Granemann', 47999080511)
# aluno3 = Alunos('Kerolain','Andressa', 47996279827)
# aluno4 = Alunos('Matheus','Nicolas', 47991019683)
# aluno5 = Alunos('Merlaine','Kuhn', 47999522602)
lista_alunos = []



app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome = pagina_nome, lista=lista_alunos)
@app.route('/novo') 
def novo():
    return render_template ('novo.html') 
@app.route('/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    novo_aluno = Alunos(nome, sobrenome, telefone)
    lista_alunos.append(novo_aluno)
    return redirect ('/')   
app.run()

# print('='*50)
# print(aluno1.Nome)
# print(aluno2.nome_completo())
# print ('='*50)