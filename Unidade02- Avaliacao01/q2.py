#Pamela e Rafaela
numInicial = 10
numFinal = 100000
contador = 0
for numero in range(numInicial, numFinal + 1):
    original = numero
    inverso = 0
    while numero > 0:
        digito = numero % 10
        inverso = inverso * 10 + digito
        numero = numero // 10
    if original == inverso:
        contador +=1

print(contador)
