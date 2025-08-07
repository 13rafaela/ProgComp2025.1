#Pamela e Rafaela
numInicial = 10 # inicio do intervalo
numFinal = 100000 # limite do intervalo
contador = 0 # inicializa o contador dos num palindromos
for numero in range(numInicial, numFinal + 1): # percorre por todos os numeros do intervalo
    # inversão do num
    numOriginal = numero # guarda o numero original
    numInvertido = 0 # inicializa a variavel que vai guardar o numero invertido
    while numero > 0: # extrai cada digito do num( do ultimo ao primeiro) e constroi o num invertido
        digito = numero % 10
        numInvertido = numInvertido * 10 + digito
        numero = numero // 10
        # verificação
    if numOriginal == numInvertido:# compara o num original com o num invertido
        contador +=1 # se forem iguais, incrementa o contador
print(contador)

