num = int(input("Digite um número (0 a 9999): "))
if num < 0 or num > 9999:
    print("Número inválido! Digite um valor entre 0 e 9999.")
else:
    if num < 10:
        soma = num
    if num < 100:
        dez = num // 10
        uni = num % 10
        soma = dez + uni
if num < 1000:
        cen = num // 100
        dez = (num % 100) // 10
        uni = num % 10
        soma = cen + dez + uni
else:
        mi = num // 1000
        cen = (num % 1000) // 100
        dez = (num % 100) // 10
        uni = num % 10
        soma = mi + cen + dez + uni
    
print("A soma dos algarismos é:", soma)







