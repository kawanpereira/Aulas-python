"""
Operadores Lógicos
and, or , not(inverte o valor)
in(se existe a letra ou número) e not in(se não existe)
"""
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'kawan'
senha_bd  = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuario ou senha inválidos! ')