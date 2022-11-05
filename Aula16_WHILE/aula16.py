"""
while em Python
utilizando para realizar ações enquanto
uma condição for verdadeira.
"""
#  while True:
#    nome = input("qual o seu nome? ")
#    print(f'Olá {nome}!')

#  x = 0
#  while x < 10:
#    print(x)
#    x = x + 1

#  print('Acabou!')

x = 0 #  coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'(X vale {x}, e Y vale {y})')
        y += 1
    x +=1 # x = x + 1

print('Acabou!')