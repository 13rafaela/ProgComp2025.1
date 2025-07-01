import random
IstNomes = ['Lya','Eduarda','Giovana']
IstNotas = []
aprovados= []
for i in range(0,3):
    IstNotas.append(random.randint(0,100))

for i in range(len(IstNomes)):
    if IstNotas[i] >=60:
        aprovados.append(IstNomes[i])
print(f'lista de aprovados: {aprovados}')
print(f'notas: {IstNotas}')

    
        
    

