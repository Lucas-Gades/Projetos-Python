import json
from datetime import datetime

l_profissionais = []
l_visitantes = []
dict_visitas = {}


class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.nome = nome
        self.especialidade = especialidade
        self.sala = sala


class Visitante:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Visita:
    def __init__(self, visitante, profissional, data_entrada):
        self.visitante = visitante
        self.profissional = profissional
        self.data_entrada = data_entrada


def cadastrar_profissional():
    while True:
        nome = input("Nome do profissional: ").strip().upper()
        if len(nome) > 0 and nome.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido. Digite um nome válido.")

    while True:
        especialidade = input("Especialidade do profissional: ").strip().upper()
        if len(especialidade) > 0 and especialidade.replace(" ", "").isalpha():
            break
        else:
            print("Especialidade inválida. Digite uma especialidade válida.")

    while True:
        sala = input("Sala do profissional: ").strip()
        if sala.isdigit():
            break
        else:
            print("Sala inválida. Digite apenas números.")

    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)

    with open("profissionais.txt", "a") as arquivo:
        arquivo.write(f"{nome}:{especialidade}:{sala}\n")

    print("Profissional cadastrado com sucesso.")


def cadastrar_visitante():
    while True:
        nome = input("Nome do visitante: ").strip().upper()
        if len(nome) > 0 and nome.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido. Digite um nome válido.")

    while True:
        documento = input("Documento do visitante: ").strip()
        if documento.isdigit():
            break
        else:
            print("Documento inválido. Digite apenas números.")

    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)

    with open("visitantes.txt", "a") as arquivo:
        arquivo.write(f"{nome}:{documento}\n")
    print("Visitante cadastrado com sucesso.")



def localizar_profissional():
    opcao = input("Deseja localizar o profissional por nome (N) ou especialidade (E)? ").upper()
    while opcao not in ['N', 'E']:
        print("Opção inválida. Digite 'N' para nome ou 'E' para especialidade.")
        opcao = input("Deseja localizar o profissional por nome (N) ou especialidade (E)? ").upper()

    if opcao == 'N':
        nome = input("Digite o nome do profissional: ").upper()
        print("Lista de profissionais com o nome:", nome)
        encontrado = False
        for profissional in l_profissionais:
            if profissional.nome.upper().startswith(nome):
                print("Nome: ", profissional.nome)
                print("Especialidade: ", profissional.especialidade)
                print("Sala: ", profissional.sala)
                encontrado = True
        if not encontrado:
            print("Nenhum profissional encontrado.")
    else:
        print("Lista de especialidades:")
        especialidades = set(profissional.especialidade for profissional in l_profissionais)
        for especialidade in especialidades:
            print(especialidade)
        especialidade = input("Digite a especialidade do profissional: ").upper()
        encontrado = False
        for profissional in l_profissionais:
            if especialidade == profissional.especialidade.upper():
                print("Nome: ", profissional.nome)
                print("Especialidade: ", profissional.especialidade)
                print("Sala: ", profissional.sala)
                encontrado = True
        if not encontrado:
            print("Nenhum profissional encontrado.")


def registrar_visita():
    print("\nLista de profissionais:")
    for i, profissional in enumerate(l_profissionais):
        print(f"{i+1}. {profissional.nome}")

    escolha_profissional = input("Escolha o número do profissional: ")
    while not escolha_profissional.isdigit() or int(escolha_profissional) < 1 or int(escolha_profissional) > len(l_profissionais):
        print("Opção inválida. Digite novamente.")
        escolha_profissional = input("Escolha o número do profissional: ")

    profissional = l_profissionais[int(escolha_profissional)-1]

    print("Lista de visitantes:")
    for i, visitante in enumerate(l_visitantes):
        print(f"{i+1}. {visitante.nome}")

    escolha_visitante = input("Escolha o número do visitante: ")
    while not escolha_visitante.isdigit() or int(escolha_visitante) < 1 or int(escolha_visitante) > len(l_visitantes):
        print("Opção inválida. Digite novamente.")
        escolha_visitante = input("Escolha o número do visitante: ")

    visitante = l_visitantes[int(escolha_visitante)-1]

    data_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if visitante.documento not in dict_visitas:
        dict_visitas[visitante.documento] = []
    dict_visitas[visitante.documento].append({
        "nome_profissional": profissional.nome,
        "hora_entrada": data_entrada,
        "sala": profissional.sala
    })

    print("Visita registrada com sucesso.")


def relatorio_conferencia():
    print("Lista de profissionais:")
    for i, profissional in enumerate(l_profissionais):
        print(f"{i+1} - {profissional.nome}:{profissional.especialidade}")

    escolha = int(input("Digite o número do profissional: "))
    while escolha < 1 or escolha > len(l_profissionais):
        print("Opção inválida. Digite um número válido.")
        escolha = int(input("Digite o número do profissional: "))

    profissional_escolhido = l_profissionais[escolha - 1]
    print("\nRelatório de conferência:")

    encontrado = False
    for documento, visitas in dict_visitas.items():
        for visita in visitas:
            if visita["nome_profissional"].upper() == profissional_escolhido.nome.upper():
                for visitante in l_visitantes:
                    if visitante.documento == documento:
                       encontrado = True
                       nome_visitante = visitante.nome
                       data_entrada = visita["hora_entrada"]
                       print("Nome visitante: ", nome_visitante)
                       print("Data e hora de entrada: ", data_entrada)
                       print()

    if encontrado:
        print("Fim do relatório.")
    else:
        print("Não há visitantes registrados para esse profissional.")


def gerar_arquivo_registros():
    data_atual = datetime.now().strftime("%Y-%m-%d")
    nome_arquivo = f"registros_{data_atual}.json"
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dict_visitas, arquivo)
    print(f"Arquivo {nome_arquivo} gerado com sucesso.")


def ler_arquivos():
    try:
        with open("profissionais.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, especialidade, sala = linha.strip().split(":")
                profissional = Profissional(nome, especialidade, sala)
                l_profissionais.append(profissional)
    except FileNotFoundError:
        print("Arquivo 'profissionais.txt' não encontrado.")

    try:
        with open("visitantes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, documento = linha.strip().split(":")
                visitante = Visitante(nome, documento)
                l_visitantes.append(visitante)
    except FileNotFoundError:
        print("Arquivo 'visitantes.txt' não encontrado.")
    print("Arquivos lidos com sucesso!")


ler_arquivos()

while True:
    print("\n*** SISTEMA DE CONTROLE DE VISITAS ***")
    print("1 - CADASTRAR PROFISSIONAL")
    print("2 - CADASTRAR VISITANTE")
    print("3 - LOCALIZAR PROFISSIONAL")
    print("4 - REGISTRAR VISITA")
    print("5 - RELATÓRIO DE CONFERÊNCIA")
    print("6 - GERAR ARQUIVO DE REGISTROS")
    print("7 - LER ARQUIVOS")
    print("0 - SAIR")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_profissional()
    elif opcao == "2":
        cadastrar_visitante()
    elif opcao == "3":
        localizar_profissional()
    elif opcao == "4":
        registrar_visita()
    elif opcao == "5":
        relatorio_conferencia()
    elif opcao == "6":
        gerar_arquivo_registros()
    elif opcao == "7":
        ler_arquivos()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite um número válido.")
