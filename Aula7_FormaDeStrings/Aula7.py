nome = 'Kawan'
idade = 27
altura = 1.75
peso = 75
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))