import random

# Configuração de cores
resetCor = '\033[0;0m'  # Retoma a cor padrão
letraNExiste = '\033[40m'     # Fundo preto
letraPosErrado = '\033[43m'   # Fundo amarelo
letraPosCorreta = '\033[42m'  # Fundo verde
# lista com as palavras validas
palavras = [ "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
]
palavra1 = random.choice(palavras).upper()
palavra2 = random.choice (palavras).upper()
#sorteia as palavras da lista
fimdejogo = False # variavel para determinar o fim do jogo quando ele for verdadeiro
tentativas = 7 # num de tentativas
acertou1 = False
acertou2 = False# variaveis para determinar quando o acerto acontece ou nao

print("T   E   R   M   O")
print("-------------------------------------------------------")

# loop pra determinar que enquanto não acabar o jogo e as chances forem maiores que zero, o jogo continua
while not fimdejogo:
    print1 = ""
    print2 = ""
    palpite1 = input("Digite a palavra (5 letras): ").upper()
    
    if len(palpite1) != 5:# validação da quantidade de letras que serão digitadas(ñ aceita a quantidade de letras nem maiores ou menores que 5)
        print("a palavra deve ter 5 letras.")
        continue
    
    if palpite1 not in palavras:# validação para palavras que não estao na lista
        print("palavra invalida! escolha outra.")
        continue
    
    tentativas -=1# contagem de tentativas
    print(f"voce tem {tentativas} tentativas restantes.")
    
    # verifica se o palpite que foi digitado esta na palavra 1 ou na palavra dois
    if palpite1 == palavra1:
        acertou1 = True
        print(f"você acertou a primeira palavra: {palavra1}")
    if palpite1 == palavra2:
        acertou2 = True
        print(f"Voce acertou a segunda palavra:{palavra2}")
    if acertou1 and acertou2:
        print(f"parabéns, você acertou as duas palavras: {palavra1} e {palavra2}")
    
    # determina o nivel de acordo com o acerto do usuario
        if tentativas == 7:
            print("impossivel 😯")
        elif tentativas == 5:
            print("ninja 👌")
        elif tentativas == 4:
            print("impressionante 👏")
        elif tentativas == 3:
            print("interessante 😊")
        elif tentativas == 2:
            print("pode melhorar 🙂")
        elif tentativas == 1:
            print("foi por pouco 😥")
        fimdejogo = True
    elif tentativas == 0:
        print(f"Acabaram as chances. As palavras eram {palavra1} e {palavra2}.")
        fim_do_jogo = True # determina se acabar as chances o jogo acaba
    else:
        # Verificação do palpite na posição das letras da palavra 1
        if acertou1:
            print1 = letraPosCorreta + palavra1 + resetCor
        else:
            i = 0
            for c in palpite1:
                if c in palpite1:
                    if c == palpite1[i]:
                        print1 += (letraPosCorreta + c + resetCor)
                    else:
                        print1 += (letraPosErrado + c + resetCor)
                else:
                    print1 += (letraNExiste + c + resetCor)
                i += 1

        # Verificação do palpite na posição das letras da palavra 2 e determinação das cores em cada posição
        if acertou2:
            print2 = letraPosCorreta + palavra2 + resetCor
        else:
            i = 0
            for c in palpite1:
                if c in palavra2:
                    if c == palavra2[i]:
                        print2 += (letraPosCorreta + c + resetCor)
                    else:
                        print2 += (letraPosErrado + c + resetCor)
                else:
                    print2 += (letraNExiste + c + resetCor)
                i += 1

        # Exibição dos resultados)
        print("Palavra 1:", ''.join(print1))
        print("Palavra 2:", ''.join(print2))
     
   