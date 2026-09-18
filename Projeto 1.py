
rodando = True

while rodando == True:

    ativos = [

        {"nome": "Computadores", "Principal vulnerabilidade": "Roubo", "Número": "1"},
        {"nome": "Servidores", "Principal vulnerabilidade": "Fogo", "Número": "2"},
        {"nome": "Carros", "Principal vulnerabilidade": "Roubo", "Número": "3"},
        {"nome": "Teclados", "Principal vulnerabilidade": "Roubo", "Número": "4"},

    ]

    print("Selecione um ativo para ver seu detalhes. Ou 'add' para adicionar um ativo")

    for item in ativos:
        print(item["Número"],"-", item["nome"])

    entrada = input("Digite o número ou o nome do ativo (ou 'quit' para sair): ").strip().lower()
    print("-" * 60)

    if entrada == "quit":
        print("Programa finalizado com sucesso!")
        rodando = False
        break

    encontrado = False
    for ativo in ativos:
        if entrada == ativo["nome"].lower() or entrada == ativo["Número"]:
            print(f"Ativo: {ativo['nome']}")
            print(f"Principal vulnerabilidade: {ativo['Principal vulnerabilidade']}")
            print("-" * 60)
            encontrado = True
            break
    if encontrado == False:
        print("Opção inválida! Tente novamente.")
        print("-" * 60)

    if entrada == "add" or 0:
        print("Adicionando um novo ativo!")
        nome_ativo = input(f"Qual o nome do ativo que deseja adicionar? ")
        principal_vul = input(f"Qual a principal vulnerabilidade de tal ativo? ")

        novo_ativo = {"nome": nome_ativo, "Principal vulnerabilidade": principal_vul}
        ativos.append(novo_ativo)

    for item in ativos:
        print(item)
