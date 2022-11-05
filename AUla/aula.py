nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)
idade_minima = 18
idade_maxima = 35


if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} não pode pegar o empréstimo. ')