peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = peso / (altura * altura)

print(f"Seu IMC é:", imc)

if imc < 18.5:
    print("Classificação: Abaixo do peso")
if imc < 25:
    print("Classificação: Peso normal")
if imc < 30:
    print("Classificação: Sobrepeso")
if imc < 35:
    print("Classificação: Obesidade grau 1")
if imc < 40:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3 (mórbida)")
