
rodando = True

while rodando == True:

    ativos = [

        {"nome": "Computadores", "Principal vulnerabilidade": "Roubo", "Index": "1"},
        {"nome": "Servidores", "Principal vulnerabilidade": "Fogo", "Index": "2"},
        {"nome": "Carros", "Principal vulnerabilidade": "Roubo", "Index": "3"},
        {"nome": "Teclados", "Principal vulnerabilidade": "Roubo", "Index": "4"},

    ]

    print("Selecione um ativo para ver seu detalhes. Ou 'add' para adicionar um ativo")

    for item in ativos:
        print(item["Index"],"-", item["nome"])

    entrada = input("Digite o Index ou o nome do ativo (ou 'quit' para sair): ").strip().lower()
    print("-" * 60)

    if entrada == "quit":
        print("Programa finalizado com sucesso!")
        rodando = False
        break

    elif entrada == "add" or 0:            #CRIAÇÃO DE NOVO ATIVO
        print("Adicionando um novo ativo!")
        nome_ativo = input(f"Qual o nome do ativo que deseja adicionar? ")
        principal_vul = input(f"Qual a principal vulnerabilidade de tal ativo? ")

        novo_ativo = {"nome": nome_ativo, "Principal vulnerabilidade": principal_vul, "Index": str(len(ativos)+1)}
        ativos.append(novo_ativo)
        print(f"\nAtivo '{nome_ativo}' adicionado com sucesso")
        print(f"Dados do ativo: {novo_ativo}\n")

        # for item in ativos: ##########################temporário, existe apenas para checagem
        #     print(item)
        #     print("-"*60)

    else:
        encontrado = False
        for ativo in ativos:
            if entrada == ativo["nome"].lower() or entrada == ativo["Index"]:
                print(f"Ativo: {ativo['nome']}")
                print(f"Principal vulnerabilidade: {ativo['Principal vulnerabilidade']}")
                print("-" * 60)
                encontrado = True
                break
        if encontrado == False:
            print("Opção inválida! Tente novamente.")
            print("-" * 60)
            continue

    loop2 = True
    while loop2 == True:             #LOOP PARA EVITAR Q O PROGRAMA SAIA DE UMA PERGUNTA PARA OUTRA (PERGUNTA DO INICIO DO PROGRAMA)
        continuar = input(f"Pressione 'enter' para continuar ou 'quit' para fechar o programa ").strip().lower()
        if continuar == "quit":
            rodando = False
            loop2 = False

        elif continuar == "":
            loop2 = False

        else:
            print("Selecione uma opção válida")