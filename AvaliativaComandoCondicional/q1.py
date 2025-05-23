num = int(input('Digite um número de 0 á 1000: '))
while num > 1000:
    print("Numero inválido!")
    num = int(input('Digite um número de 0 á 1000: '))
	
soma = 0
algarismo = num
while algarismo > 0:
    digito = algarismo % 10 
    soma += digito 
    algarismo = algarismo // 10 
print('A soma dos algarismos é igual a: ', soma)







