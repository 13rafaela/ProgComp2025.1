import random
IstNomes = ['Lya','Eduarda','Giovana'] # adicionar os nomes que galileu colocou no grupo
IstNotas = []
aprovados= []
for i in range(0,3): #adicionar 3 notas dentro de um elemento(sendo 3 elementos tambem)
    IstNotas.append(random.randint(0,100))

for i in range(len(IstNomes)):
    if IstNotas[i] >=60:# colocar a media das notas e não as notas
        aprovados.append(IstNomes[i])
print(f'lista de aprovados: {aprovados}')
print(f'notas: {IstNotas}')
# calcular a media das tres notas

        
    

