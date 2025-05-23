print("=== Calculadora de Dias entre Datas ===")
print("Data inicial:")
dia1 = int(input("Dia: "))
mes1 = int(input("Mês: "))

print("Data final:")
dia2 = int(input("Dia: "))
mes2 = int(input("Mês: "))
if mes1 < 1 or mes1 > 12 or mes2 < 1 or mes2 > 12:
    print("Erro: Mês inválido (deve ser entre 1 e 12)")
else:
    if mes1 == 2:
        dias_mes1 = 28
    if mes1 == 4 or mes1 == 6 or mes1 == 9 or mes1 == 11:
        dias_mes1 = 30
    else:
        dias_mes1 = 31
    if mes2 == 2:
        dias_mes2 = 28
    if mes2 == 4 or mes2 == 6 or mes2 == 9 or mes2 == 11:
        dias_mes2 = 30
    else:
        dias_mes2 = 31

    if dia1 < 1 or dia1 > dias_mes1:
        print("Erro: Dia inicial inválido para mês", mes1)
    if dia2 < 1 or dia2 > dias_mes2:
        print("Erro: Dia final inválido para mês", mes2)
    else:
        if mes2 < mes1 or (mes2 == mes1 and dia2 < dia1):
            print("Erro: Data final deve ser após data inicial")
        else:
            if mes1 == mes2:
                total = dia2 - dia1
            else:
                total = dias_mes1 - dia1
                if mes2 > mes1 + 1:
                    if mes1 == 1:  # Janeiro
                        if mes2 > 2: total += 28  # Fevereiro
                        if mes2 > 3: total += 31  # Março
                        if mes2 > 4: total += 30  # Abril
                        if mes2 > 5: total += 31  # Maio
                        if mes2 > 6: total += 30  # Junho
                        if mes2 > 7: total += 31  # Julho
                        if mes2 > 8: total += 31  # Agosto
                        if mes2 > 9: total += 30  # Setembro
                        if mes2 > 10: total += 31  # Outubro
                        if mes2 > 11: total += 30  # Novembro
                    if mes1 == 2:  # Fevereiro
                        if mes2 > 3: total += 31  # Março
                        if mes2 > 4: total += 30  # Abril
                        if mes2 > 5: total += 31  # Maio
                        if mes2 > 6: total += 30  # Junho
                        if mes2 > 7: total += 31  # Julho
                        if mes2 > 8: total += 31  # Agosto
                        if mes2 > 9: total += 30  # Setembro
                        if mes2 > 10: total += 31  # Outubro
                        if mes2 > 11: total += 30  # Novembro
                        if mes2 > 12: total += 31  # Dezembro
                total += dia2
            print("Total de dias entre as datas:", total)

