from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_mysqldb import MySQL
from dao import EstabelecimentoDao, UsuarioDao
from models import Estabelecimento, Usuario

app = Flask(__name__)
app.secret_key = 'lorena'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "programa"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

estab_dao = EstabelecimentoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    dado = estab_dao.listar()
    return render_template('lista.html', titulo='Estabelecimentos', elista=dado)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
       return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Estabelecimento')


@app.route('/criar', methods = ['POST',])
def criar():
    rz_social = request.form['rz_social']
    cnpj = request.form['cnpj']
    email = request.form['email']
    endereco = request.form['endereco']
    cidade = request.form['cidade']
    estado = request.form['estado']
    telefone = request.form['telefone']
    dtcadastro = request.form['dtcadastro']
    categoria = request.form['categoria']
    status = request.form['status']
    agencia = request.form['agencia']
    conta = request.form['conta']
    etb = Estabelecimento(rz_social, cnpj, email, endereco, cidade, estado, telefone, dtcadastro,categoria, status, agencia,conta)
    estab_dao.salvar(etb)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else :
        flash('Não logado, tente de novo!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('sessao encerrada')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    dados_estab = estab_dao.busca_por_id(id)
    return render_template('editar.html', titulo = 'Editando Estabelecimento', dados_estab=dados_estab)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    rz_social = request.form['rz_social']
    cnpj = request.form['cnpj']
    email = request.form['email']
    endereco = request.form['endereco']
    cidade = request.form['cidade']
    estado = request.form['estado']
    telefone = request.form['telefone']
    dtcadastro = request.form['dtcadastro']
    categoria = request.form['categoria']
    status = request.form['status']
    agencia = request.form['agencia']
    conta = request.form['conta']
    etb = Estabelecimento(rz_social, cnpj, email, endereco, cidade, estado, telefone, dtcadastro,categoria, status, agencia,conta,id=request.form['id'] )
    estab_dao.salvar(etb)
    return redirect(url_for('index'))



@app.route('/deletar/<int:id>')
def deletar(id):
    estab_dao.deletar(id)
    flash('O estabelecimento foi removido com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)