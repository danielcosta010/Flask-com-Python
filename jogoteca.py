from flask import Flask, render_template, request

app = Flask(__name__)

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
  return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True)