
ativos = [

    {"nome": "Computadores", "Principal vulnerabilidade": "Roubo", "Número": "1" },
    {"nome": "Servidores", "Principal vulnerabilidade": "Fogo", "Número": "2"  },
    {"nome": "Carros", "Principal vulnerabilidade": "Roubo", "Número": "3"  },
    {"nome": "Teclados", "Principal vulnerabilidade": "Roubo", "Número": "4"  },

]

rodando = True

while rodando == True:
    print("Selecione um ativo para ver seu detalhes.")
    print("1. Computadores")
    print("2. Servidores")
    print("3. Carros")
    print("4. Teclados")
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