import sqlite3
from flask import Flask, request, url_for, session, g, redirect,\
    abort, render_template, flash

# configuração
DATABASE = "blog.db"
SECRET_KEY = "pudim"  # chave de criptografia usada pelo flask, não deveria ser salvo no código

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisicao():
    g.bd = conectar_bd() 

@app.teardown_request
def depois_requisicao(exc):
    g.bd.close()    

@app.route('/')
@app.route('/entradas')
def exibir_entradas():
    sql = "select titulo, texto from entradas order by id desc"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo': titulo, 'texto': texto})
    return render_template('exibir_entradas.html', entradas=entradas)

@app.route('/inserir')
def inserir_entrada():
    if not session.get('logado'):
        abort(401)
    sql = "insert into entradas (titulo, texto) values (?,?)"
    g.bd.execute(sql, ,)
    g.bd.commit()
    return redirect(url_for('exibir_entradas'))
