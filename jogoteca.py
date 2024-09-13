from flask import Flask, redirect, render_template, request, session, flash


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

@app.route('/')
def index():
  return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
  return render_template('novo.html', titulo='Cadastre um novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome, categoria, console)
  lista.append(jogo)
  return redirect('/')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
  if '1234' == request.form['senha']:
    session['usuario_logado'] = request.form['usuario']
    flash(session['usuario_logado'] + ' logado com sucesso!')
    return redirect('/')
  else: 
    flash('Usuario ou senha incorreta.')
    return redirect('/login')
  
@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout realizado com secesso!')
  return redirect('/')
    

app.run(debug=True)