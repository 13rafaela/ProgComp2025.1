nota1 = int(input('Digite a nota da primeira unidade:'))
nota2 = int(input('Digite a nota da segunda unidade:'))
media =  (nota1 + nota2) // 2
if media >=60:
      print('aprovado(a)')
if media >= 20:
      print('prova final')
      nota_final = float(input('Digite a nota final:'))
      media_final = (media+ nota_final) // 2
      if media_final >= 60:
            print('aprovado')
      else:
            print('reprovado')


