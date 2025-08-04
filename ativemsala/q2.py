numInicial = 10
numFinal = 100000 # valores estipulados
contador  = 0 # variavel para contar
for numero in range(numInicial,numFinal + 1):
    original = numero
    invertido = 0
    while numero >0:
        ultimoDigito = numero % 10
        invertido = invertido * 10 + ultimoDigito
        numero = numero //10

    if original == invertido:
        contador += 1
print(contador)
