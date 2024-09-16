SECRET_KEY = 'jsw'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:3412@localhost/jogoteca'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '3412',
        servidor = 'localhost',
        database = 'jogoteca'
    )