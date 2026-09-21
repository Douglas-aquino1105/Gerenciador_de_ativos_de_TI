import json

#FUNÇÃO PARA INICIAR O ARQUIVO NA MEMÓRIA
def carregar_ativos():
    try:
        with open("ativos.json", "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#FUNÇÃO PARA SALVAR AS MUDANÇAS FEITAS NA MEMÓRIA PARA O ARQUIVO
def salvar_ativos(lista):
    with open("ativos.json", "w", encoding = "utf-8") as file:
        json.dump(lista, file, indent = 4, ensure_ascii = False) #ENSURE ASCII FAZ OS ACENTOS FUNCIONAREM


ativos = carregar_ativos() #INICIA O ARQUIVO NA MEMÓRIA

rodando = True
while rodando == True:



    print("\nDigite o Index ou o nome do ativo para ver seu detalhes,'add' para adicionar um ativo, ou 'del' para remover um ativo.")
    print("Para sair digite 'quit'\n")

    for item in ativos:
        print(item["Index"],"-", item["nome"])

    entrada = input("\n"+"-"*25+"> ").strip().lower()
    print("-" * 60)

    if entrada == "quit":
        print("Programa finalizado com sucesso!")
        rodando = False
        break

    elif entrada == "add" or entrada == "0": #CRIAÇÃO DE NOVO ATIVO
        print("Adicionando um novo ativo!")
        nome_ativo = input(f"Qual o nome do ativo que deseja adicionar? ").capitalize().strip()
        principal_vul = input(f"Qual a principal vulnerabilidade de tal ativo? ").capitalize().strip()

        novo_ativo = {"nome": nome_ativo, "Principal vulnerabilidade": principal_vul, "Index": str(len(ativos)+1)}
        ativos.append(novo_ativo)
        print(f"\nAtivo '{nome_ativo}' adicionado com sucesso")
        print(f"Dados do ativo: {novo_ativo}\n")

        salvar_ativos(ativos)

    elif entrada == "del" or entrada == "remove":
        alvo = input("Digite o Index ou o nome do ativo que deseja remover: ").strip().lower()
        removido = False

        for ativo in ativos:
            if alvo == ativo["Index"] or alvo == ativo["nome"]:
                ativos.remove(ativo)
                removido = True
                print(f"Ativo '{ativo["nome"]}' removido com sucesso!")
                break

        if removido:
            for i, ativo in enumerate(ativos, start=1):
                ativo["Index"] = str(i)
            salvar_ativos(ativos)

        else:
            print("\nAtivo não encontrado!")

    else:
        encontrado = False
        for ativo in ativos:
            if entrada == ativo["nome"].lower() or entrada == ativo["Index"]:
                print(f"Ativo: {ativo['nome']}")
                print(f"Principal vulnerabilidade: {ativo['Principal vulnerabilidade']}")
                print(f"Index: {ativo['Index']}")
                print("-" * 60)
                encontrado = True
                break
        if encontrado == False:
            print("Opção inválida! Tente novamente.")
            print("-" * 60)
            continue

    loop2 = True
    while loop2 == True: #LOOP PARA EVITAR Q O PROGRAMA SAIA DE UMA PERGUNTA PARA OUTRA (PERGUNTA DO INICIO DO PROGRAMA)
        continuar = input(f"Pressione 'enter' para continuar ou 'quit' para fechar o programa ").strip().lower()
        if continuar == "quit":
            rodando = False
            loop2 = False

        elif continuar == "":
            loop2 = False

        else:
            print("Selecione uma opção válida")