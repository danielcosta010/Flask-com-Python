from jogoteca import app
from flask import redirect, render_template, request, session, flash, url_for
from helpers import FormularioUsuario
from models import Usuarios

@app.route('/login')
def login():
  proxima = request.args.get('proxima')
  form = FormularioUsuario()
  return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
  form = FormularioUsuario(request.form)
  usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
  if usuario:
    if form.senha.data == usuario.senha:
      session['usuario_logado'] = usuario.nickname
      flash(usuario.nickname + ' logado com sucesso!')
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