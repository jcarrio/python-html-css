import sqlite3
from flask import Flask, request, session, g, redirect,\
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
    return render_template('exibir_entradas.html', mensagem="Olá pessoas!", img="https://s3.amazonaws.com/media.wikiaves.com.br/images/4803/3084192_80b99ac1790d8306ff375024dae8cbf2.jpg")

@app.route('/hello')
def pagina_inicial():
    return "<h1 style='color: green;'>Hello World</h1>"
