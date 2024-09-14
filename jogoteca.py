from flask import Flask, redirect, render_template, request, session, flash, url_for


app = Flask(__name__)
app.secret_key = 'jsw'

class Jogo:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

jogo_1 = Jogo('Skyline', 'Guerra aerea', 'PS3')
jogo_2 = Jogo('Pacman', 'coleções', 'Atari')
jogo_3 = Jogo('Street Fighter', 'Luta', 'Nintendo')
lista = [jogo_1, jogo_2, jogo_3]

class Usuario:
  def __init__(self, nome, nickname, senha):
    self.nome = nome
    self.nickname = nickname
    self.senha = senha

usuario1 = Usuario('Daniel', 'Dan', '1234')
usuario2 = Usuario('Polliana', 'Pol', '4321')
usuario3 = Usuario('Isabella', 'Bella', '6789')

usuarios= {
  usuario1.nome: usuario1,
  usuario2.nome: usuario2,
  usuario3.nome: usuario3
}

@app.route('/')
def index():
  return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect(url_for('login', proxima=url_for('novo')))
  return render_template('novo.html', titulo='Cadastre um novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome, categoria, console)
  lista.append(jogo)
  return redirect(url_for('index'))

@app.route('/login')
def login():
  proxima = request.args.get('proxima')
  return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
  if request.form['usuario'] in usuarios:
    usuario = usuarios[request.form['usuario']]
    if request.form['senha'] == usuario.senha:
      session['usuario_logado'] = usuario.nome
      flash(usuario.nome + ' logado com sucesso!')
      proxima_pagina = request.form['proxima']
      return redirect(proxima_pagina)    
    else:
      flash('Usuario ou senha incorretos')
      return redirect(url_for('login'))
  else: 
    flash('Usuario ou senha incorretos.')
    return redirect(url_for('login'))
  
@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout realizado com secesso!')
  return redirect(url_for('index'))
    

app.run(debug=True)