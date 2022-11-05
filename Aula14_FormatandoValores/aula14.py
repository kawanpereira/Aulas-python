"""
Formatando valores com modificadores

:s - Texto
:d - Inteiros
:f - Float
:.(Número)f - quantidade de casas décimais
:(caractere)(< ou > ou ^)(quantidade)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisão = num1 / num2
print('{:.2f}'.format(divisão))
print(f'{divisão:.2f}')

num3 = 1
print(f'{num3:0>10}')  #posso usar o < ou ^

num4 = 12
print(f'{num4:0<10}')

num5 = 123
print(f'{num5:0^10}')


nome = 'Kawan Pereira'
nome_formatado = '{:@>20}'.format(nome)
print(nome_formatado)

gato = 'konan'
print(gato.lower()) # tudo minusculo
print(gato.upper()) # tudo maiusculo
print(gato.title()) # primeiras letras maiusculas