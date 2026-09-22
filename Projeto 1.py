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



    print("\nDigite o Index ou o nome do ativo para ver seu detalhes,'add' para adicionar um ativo, 'del' para remover um ativo. Ou 'edit' para editar um ativo")
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

        novo_ativo = {"nome": nome_ativo, "Principal vulnerabilidade": [principal_vul], "Index": str(len(ativos)+1)}
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
            for i, ativo in enumerate(ativos, start=1): #RE-ENUMERA OS ATIVOS E SALVA
                ativo["Index"] = str(i)
            salvar_ativos(ativos)

        else:
            print("\nAtivo não encontrado!")

    elif entrada == "edit":
        alvo = input("Digite o nome ou Index do ativo que deseja editar: ").capitalize().strip()
        editado = False

        for ativo in ativos:
            if alvo == ativo["Index"] or alvo == ativo["nome"]:
                print(f"Ativo '{ativo["nome"]}' encontrado! ")

                while True:
                    escolha = input("O que deseja editar?\n1. Nome\n2. Lista de vulnerabilidades\n").strip().lower()
                    if escolha == "1" or escolha == "nome":
                        novo_nome = input(f"Por qual nome deseja substituir? Nome atual: {ativo["nome"]}\n").lower().strip()
                        ativo["nome"] = novo_nome
                        print(f"Nome alterado com sucesso! Novo nome: {ativo["nome"]}")
                        print(f"Novas informações do ativo: {ativo}")
                        salvar_ativos(ativos)
                        break

                    elif escolha == "2" or escolha == "lista de vulnerabilidades" or escolha =="lista":
                        substituir = input("Qual operação deseja realizar? \n1. Substituir vulnerabilidade \n2. Adicionar vulnerabilidade\n3. Remover vulnerabilidade\n").strip().lower()

                        if substituir == "1" or substituir == "substituir":
                            print(f"Qual vulnerabilidade deseja subtituir?")

                            for i, vul in enumerate(ativo["Principal vulnerabilidade"], start=1): #FUNÇÃO PRA PRINTAR LISTA FORMATADA | VUL=PRINCIPAL VULNERABILIDADE
                                print (f"{i}.'{vul}'")

                            escolhida = input("-"*25+"> ").strip().lower()
                            posiçao_encontrada = None

                            for index, vul in enumerate(ativo["Principal vulnerabilidade"]):
                                if escolhida == str(index+1) or escolhida == vul.lower(): #+1 PORQUE COMEÇA NO 0
                                    posiçao_encontrada = index
                                    break

                            if posiçao_encontrada is not None:
                                vul_antiga = ativo["Principal vulnerabilidade"][posiçao_encontrada] # ATIVO[CAMPO DICONARIO][INDEX]
                                nova_vul = input(f"Substituir '{vul_antiga}' por qual nova vulnerabilidade? ").strip().capitalize()

                                # Substitui apenas a vulnerabilidade daquela posição específica
                                ativo["Principal vulnerabilidade"][posiçao_encontrada] = nova_vul

                                print(f"\nVulnerabilidade '{vul_antiga}' alterada com sucesso para '{nova_vul}'!")
                                print(f"Novas informações do ativo: {ativo}")
                                salvar_ativos(ativos)
                                break

                        elif substituir == "2" or substituir == "adicionar vulnerabilidade":
                            nova_vul = input(f"Qual vulnerabilidade deseja adicionar? Vulnerabilidades atuais: {ativo["Principal vulnerabilidade"]}\n").capitalize().strip()
                            ativo["Principal vulnerabilidade"].append(nova_vul)
                            print(f"Lista alterada com sucesso! Nova vulnerabilidade: {nova_vul}")
                            print(f"Novas informações do ativo: {ativo}")
                            salvar_ativos(ativos)
                            break

                        elif substituir == "3" or substituir == "remover vulnerabilidade" or substituir == "remover":
                            if len(ativo["Principal vulnerabilidade"]) == 0: #LEN CONFERE SE EXISTE ALGUM DADO NO DICIONARIO (LENGTH)
                                print("Este ativo não possui vulnerabilidades para serem removidas")
                                break

                            print("Qual vulnerabilidade deseja remover?")

                            for i, vul in enumerate(ativo["Principal vulnerabilidade"], start=1): #LISTA ORGANIZADA
                                print (f"{i}.'{vul}'")

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posiçao_encontrada = None

                            for index, vul in enumerate(ativo["Principal vulnerabilidade"]):
                                if escolhida == str(index + 1) or escolhida == vul.lower():
                                    posiçao_encontrada = index
                                    break

                            if posiçao_encontrada is not None:
                                # O recurso .pop() remove o item da lista usando a posição (index) e retorna o item removido
                                vul_removida = ativo["Principal vulnerabilidade"].pop(posiçao_encontrada)
                                print(f"\nVulnerabilidade '{vul_removida}' removida com sucesso!")
                                print(f"Novas informações do ativo: {ativo}")
                                salvar_ativos(ativos)
                                break

                            else:
                                print("Vulnerabilidade não encontrada!")

                        else:
                            print("Opção inválida")

                    else:
                        print("Escolha uma opção válida!\n"+"-"*60)
                        continue







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

            #mais opções de descrições para o ativo | descrições vulnerabilidades