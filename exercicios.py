# crie um template desta maniera

# *
# **
# ***
# ****
# *****
# ******

# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')
# print('******')

#para cada i em um intervalo de 0 a 10 10 escluido
for i in range(1, 10):
  print('*' * i)
for i in range(10, 0, -1):
  print('*' * i)


dev = 'python'

if dev == 'java':
  print('Se é loco jão')
elif dev == 'python':
  print('Menos loco jão')
elif dev == 'html':
  print('Nem é programação')
else:
  print('Qualquer outra coisa')

nomes = [
  {
    'nome': 'João',
    'idade': '25'
  },
  {
    'nome': 'Maria',
    'idade': '30'
  },
  {
    'nome': 'Pedro',
    'idade': '35'
  }
]

for d in nomes:
  print(f"{d['nome']} tem {d['idade']} anos")