"""
While / ELse
contadores
acumuladores
"""
#  CONTADOR
contador = 50

while contador <= 100:
    print(contador)
    contador += 1

#  ACUMULADOR
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('CHeguei no else.')