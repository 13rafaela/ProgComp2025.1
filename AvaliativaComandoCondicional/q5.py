minutos = int(input('Número de minutos que o veículo permaneceu no estacionamento: '))

horas = minutos / 60
if horas != int(horas):  
    horas = int(horas) + 1
else:
    horas = int(horas)

if horas <= 2:
    valor = horas * 8
if horas <= 4:
    valor = 2 * 8 + (horas - 2) * 5
if horas <= 12:
    valor = 2 * 8 + 2 * 5 + (horas - 4) * 3
else:
    valor = 30  

print('Valor a ser pago: R$',valor)