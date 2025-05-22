numero = int(input('Digite um número de o á 1000:'))
if numero > 1000:
    print('numero inválido!')
else:
    mi = numero // 1000
    cen = (numero % 1000) // 100
    dez = (numero % 100) // 10
    uni = numero % 10
    soma = mi + cen + dez + uni
    print ( 'A soma dos algarismos é:' , soma)
