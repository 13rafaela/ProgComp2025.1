dados = {}  # Dicionário para armazenar os CPFs e suas listas de MACs

# Validação de CPF
def cpf_valido(cpf):
    # Remove pontos e traços
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")

    # Verifica se tem 11 dígitos numéricos
    if len(cpf) != 11:
        return False
    for caractere in cpf:
        if caractere < "0" or caractere > "9":
            return False

    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
    todos_iguais = True
    for i in range(1, 11):
        if cpf[i] != cpf[0]:
            todos_iguais = False
    if todos_iguais:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    dv1 = 11 - resto
    if dv1 >= 10:
        dv1 = 0
    if dv1 != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    dv2 = 11 - resto
    if dv2 >= 10:
        dv2 = 0
    if dv2 != int(cpf[10]):
        return False

    return True

# Validação do MAC address no formato XX:XX:XX:XX:XX:XX
def mac_valido(mac):
    partes = mac.split(":")
    if len(partes) != 6:
        return False

    letras = "0123456789ABCDEFabcdef"
    for parte in partes:
        if len(parte) != 2:
            return False
        for caractere in parte:
            if caractere not in letras:
                return False
    return True

# Cadastra um novo CPF no sistema
def cadastrar_cpf():
    cpf = input("Digite o CPF: ")
    if cpf_valido(cpf) == False:
        print("CPF inválido.")
        return
    if cpf in dados:
        print("CPF já cadastrado.")
    else:
        dados[cpf] = []
        print("CPF cadastrado com sucesso.")

# Adiciona um MAC address a um CPF existente
def adicionar_mac():
    cpf = input("Digite o CPF: ")
    if cpf in dados:
        mac = input("Digite o MAC address (formato XX:XX:XX:XX:XX:XX): ")
        if mac_valido(mac) == False:
            print("MAC inválido.")
            return
        if mac in dados[cpf]:
            print("MAC já cadastrado para este CPF.")
        else:
            dados[cpf].append(mac)
            print("MAC adicionado com sucesso.")
    else:
        print("CPF não encontrado.")

# Remove um MAC de um CPF
def remover_mac():
    cpf = input("Digite o CPF: ")
    if cpf in dados:
        mac = input("Digite o MAC a ser removido: ")
        if mac in dados[cpf]:
            dados[cpf].remove(mac)
            print("MAC removido com sucesso.")
        else:
            print("MAC não encontrado.")
    else:
        print("CPF não encontrado.")

# Remove o CPF, se não houver MACs vinculados
def remover_cpf():
    cpf = input("Digite o CPF: ")
    if cpf in dados:
        if len(dados[cpf]) == 0:
            del dados[cpf]
            print("CPF removido com sucesso.")
        else:
            print("CPF não pode ser removido, há MACs vinculados.")
    else:
        print("CPF não encontrado.")

# Lista todos os CPFs cadastrados
def listar_cpfs():
    print("CPFs cadastrados:")
    for cpf in dados:
        print(cpf)

# Lista todos os MACs vinculados a um CPF
def listar_macs():
    cpf = input("Digite o CPF: ")
    if cpf in dados:
        print("MACs cadastrados:")
        for mac in dados[cpf]:
            print(mac)
    else:
        print("CPF não encontrado.")

# Salva os dados em um arquivo texto
def salvar_dados():
    nome = input("Nome do arquivo para salvar: ")
    arq = open(nome, "w")
    for cpf in dados:
        linha = cpf + ":"
        for i in range(len(dados[cpf])):
            linha = linha + dados[cpf][i]
            if i < len(dados[cpf]) - 1:
                linha = linha + ","
        arq.write(linha + "\n")
    arq.close()
    print("Dados salvos com sucesso.")

# Carrega os dados de um arquivo texto
def carregar_dados():
    nome = input("Nome do arquivo para carregar: ")
    try:
        arq = open(nome, "r")
        for linha in arq:
            linha = linha.strip()
            partes = linha.split(":")
            cpf = partes[0]
            if len(partes) > 1:
                macs = partes[1].split(",")
            else:
                macs = []
            dados[cpf] = macs
        arq.close()
        print("Dados carregados com sucesso.")
    except:
        print("Erro ao ler o arquivo.")

# Menu principal do programa
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar CPF")
        print("2 - Adicionar MAC")
        print("3 - Remover MAC")
        print("4 - Remover CPF")
        print("5 - Listar CPFs")
        print("6 - Listar MACs")
        print("7 - Salvar dados")
        print("8 - Carregar dados")
        print("9 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cpf()
        elif opcao == "2":
            adicionar_mac()
        elif opcao == "3":
            remover_mac()
        elif opcao == "4":
            remover_cpf()
        elif opcao == "5":
            listar_cpfs()
        elif opcao == "6":
            listar_macs()
        elif opcao == "7":
            salvar_dados()
        elif opcao == "8":
            carregar_dados()
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Inicia o programa
menu()
