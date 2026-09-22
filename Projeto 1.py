import json


# FUNÇÃO PARA INICIAR O ARQUIVO NA MEMÓRIA
def carregar_ativos():
    try:
        with open("ativos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# FUNÇÃO PARA SALVAR AS MUDANÇAS FEITAS NA MEMÓRIA PARA O ARQUIVO
def salvar_ativos(lista):
    with open("ativos.json", "w", encoding="utf-8") as file:
        json.dump(lista, file, indent=4, ensure_ascii=False)  # ENSURE ASCII FAZ OS ACENTOS FUNCIONAREM


ativos = carregar_ativos()  # INICIA O ARQUIVO NA MEMÓRIA

rodando = True
while rodando == True:

    print(
        "\nDigite o Index ou o nome do ativo para ver seu detalhes,'add' para adicionar um ativo, 'del' para remover um ativo. Ou 'edit' para editar um ativo")
    print("Para sair digite 'quit'\n")

    for item in ativos:
        print(item["Index"], "-", item["nome"])

    entrada = input("\n" + "-" * 25 + "> ").strip().lower()
    print("-" * 60)

    if entrada == "quit":
        print("Programa finalizado com sucesso!")
        rodando = False
        break

    elif entrada == "add" or entrada == "0":  # CRIAÇÃO DE NOVO ATIVO
        print("Adicionando um novo ativo!")
        nome_ativo = input(f"Qual o nome do ativo que deseja adicionar? ").capitalize().strip()
        principal_vul = input(f"Qual a principal vulnerabilidade de tal ativo? ").capitalize().strip()
        responsavel_ativo = input("Qual o responsável pelo ativo? ").capitalize().strip()

        if responsavel_ativo == "":
            responsavel_ativo = "Não atribuído"

        novo_ativo = {"nome": nome_ativo, "Principal vulnerabilidade": [principal_vul],
                      "Responsavel": [responsavel_ativo], "Index": str(len(ativos) + 1)}
        ativos.append(novo_ativo)
        print(f"\nAtivo '{nome_ativo}' adicionado com sucesso")
        print(f"Dados do ativo: {novo_ativo}\n")

        salvar_ativos(ativos)

    elif entrada == "del" or entrada == "remove":
        alvo = input("Digite o Index ou o nome do ativo que deseja remover: ").strip().lower()
        removido = False

        for ativo in ativos:
            if alvo == ativo["Index"] or alvo == ativo["nome"].lower():
                ativos.remove(ativo)
                removido = True
                print(f"Ativo '{ativo['nome']}' removido com sucesso!")
                break

        if removido:
            for i, ativo in enumerate(ativos, start=1):  # RE-ENUMERA OS ATIVOS E SALVA
                ativo["Index"] = str(i)
            salvar_ativos(ativos)

        else:
            print("\nAtivo não encontrado!")

    elif entrada == "edit":
        alvo = input("Digite o nome ou Index do ativo que deseja editar: ").strip().lower()
        editado = False

        for ativo in ativos:
            if alvo == ativo["Index"] or alvo == ativo["nome"].lower():
                print(f"Ativo '{ativo['nome']}' encontrado! ")

                while True:
                    escolha = input(
                        "\nO que deseja editar?\n1. Nome\n2. Lista de vulnerabilidades\n3. Responsável\n> ").strip().lower()

                    if escolha == "1" or escolha == "nome":
                        novo_nome = input(
                            f"Por qual nome deseja substituir? Nome atual: {ativo['nome']}\n> ").capitalize().strip()
                        if novo_nome != "":
                            ativo["nome"] = novo_nome
                            print(f"Nome alterado com sucesso! Novo nome: {ativo['nome']}")
                            print(f"Novas informações do ativo: {ativo}")
                            salvar_ativos(ativos)
                        break

                    elif escolha == "2" or escolha == "lista de vulnerabilidades" or escolha == "lista":
                        substituir = input(
                            "Qual operação deseja realizar? \n1. Substituir vulnerabilidade \n2. Adicionar vulnerabilidade\n3. Remover vulnerabilidade\n> ").strip().lower()

                        if substituir == "1" or substituir == "substituir":
                            print(f"Qual vulnerabilidade deseja substituir?")

                            for i, vul in enumerate(ativo["Principal vulnerabilidade"],
                                                    start=1):  # FUNÇÃO PRA PRINTAR LISTA FORMATADA | VUL=PRINCIPAL VULNERABILIDADE
                                print(f"{i}.'{vul}'")

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posiçao_encontrada = None

                            for index, vul in enumerate(ativo["Principal vulnerabilidade"]):
                                if escolhida == str(index + 1) or escolhida == vul.lower():  # +1 PORQUE COMEÇA NO 0
                                    posiçao_encontrada = index
                                    break

                            if posiçao_encontrada is not None:
                                vul_antiga = ativo["Principal vulnerabilidade"][
                                    posiçao_encontrada]  # ATIVO[CAMPO DICIONARIO][INDEX]
                                nova_vul = input(
                                    f"Substituir '{vul_antiga}' por qual nova vulnerabilidade? ").strip().capitalize()

                                # Substitui apenas a vulnerabilidade daquela posição específica
                                ativo["Principal vulnerabilidade"][posiçao_encontrada] = nova_vul

                                print(f"\nVulnerabilidade '{vul_antiga}' alterada com sucesso para '{nova_vul}'!")
                                print(f"Novas informações do ativo: {ativo}")
                                salvar_ativos(ativos)
                                break
                            else:
                                print("Vulnerabilidade não encontrada!")

                        elif substituir == "2" or substituir == "adicionar vulnerabilidade" or substituir == "adicionar":
                            nova_vul = input(
                                f"Qual vulnerabilidade deseja adicionar? Vulnerabilidades atuais: {ativo['Principal vulnerabilidade']}\n> ").capitalize().strip()
                            ativo["Principal vulnerabilidade"].append(nova_vul)
                            print(f"Lista alterada com sucesso! Nova vulnerabilidade: {nova_vul}")
                            print(f"Novas informações do ativo: {ativo}")
                            salvar_ativos(ativos)
                            break

                        elif substituir == "3" or substituir == "remover vulnerabilidade" or substituir == "remover":
                            if len(ativo[
                                       "Principal vulnerabilidade"]) == 0:  # LEN CONFERE SE EXISTE ALGUM DADO NO DICIONARIO (LENGTH)
                                print("Este ativo não possui vulnerabilidades para serem removidas")
                                break

                            print("Qual vulnerabilidade deseja remover?")

                            for i, vul in enumerate(ativo["Principal vulnerabilidade"], start=1):  # LISTA ORGANIZADA
                                print(f"{i}.'{vul}'")

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

                    elif escolha == "3" or escolha == "responsavel" or escolha == "responsável":
                        lista_resp = ativo.get("Responsavel", ["Não atribuído"]) #.get SERVE PARA BUSCAR SEM QUEBRAR O PROGRAMA CASO DÊ ERRO
                        op_resp = input(
                            "Qual operação deseja realizar no responsável? \n1. Substituir responsável \n2. Adicionar responsável\n3. Remover responsável\n> ").strip().lower()

                        if op_resp == "1" or op_resp == "substituir":
                            print("Qual responsável deseja substituir?")
                            for i, resp in enumerate(lista_resp, start=1):
                                print(f"{i}.'{resp}'")

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posiçao_encontrada = None

                            for index, resp in enumerate(lista_resp):
                                if escolhida == str(index + 1) or escolhida == resp.lower():
                                    posiçao_encontrada = index
                                    break

                            if posiçao_encontrada is not None:
                                resp_antigo = lista_resp[posiçao_encontrada]
                                novo_resp = input(f"Substituir '{resp_antigo}' por qual nome? ").strip().capitalize()
                                lista_resp[posiçao_encontrada] = novo_resp
                                ativo["Responsavel"] = lista_resp

                                print(f"\nResponsável '{resp_antigo}' alterado com sucesso para '{novo_resp}'!")
                                print(f"Novas informações do ativo: {ativo}")
                                salvar_ativos(ativos)
                                break
                            else:
                                print("Responsável não encontrado!")

                        elif op_resp == "2" or op_resp == "adicionar":
                            novo_resp = input(
                                f"Qual responsável deseja adicionar? Responsáveis atuais: {lista_resp}\n> ").capitalize().strip()
                            if "Responsavel" not in ativo or not isinstance(ativo["Responsavel"], list):
                                ativo["Responsavel"] = []
                            ativo["Responsavel"].append(novo_resp)

                            print(f"Lista alterada com sucesso! Novo responsável: {novo_resp}")
                            print(f"Novas informações do ativo: {ativo}")
                            salvar_ativos(ativos)
                            break

                        elif op_resp == "3" or op_resp == "remover":
                            if len(lista_resp) == 0:
                                print("Este ativo não possui responsáveis para serem removidos.")
                                break

                            print("Qual responsável deseja remover?")
                            for i, resp in enumerate(lista_resp, start=1):
                                print(f"{i}.'{resp}'")

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posiçao_encontrada = None

                            for index, resp in enumerate(lista_resp):
                                if escolhida == str(index + 1) or escolhida == resp.lower():
                                    posiçao_encontrada = index
                                    break

                            if posiçao_encontrada is not None:
                                resp_removido = lista_resp.pop(posiçao_encontrada)
                                if len(lista_resp) == 0:
                                    lista_resp.append("Não atribuído")
                                ativo["Responsavel"] = lista_resp

                                print(f"\nResponsável '{resp_removido}' removido com sucesso!")
                                print(f"Novas informações do ativo: {ativo}")
                                salvar_ativos(ativos)
                                break
                            else:
                                print("Responsável não encontrado!")

                        else:
                            print("Opção inválida!")

                    else:
                        print("Escolha uma opção válida!\n" + "-" * 60)
                        continue

                editado = True
                break

        if not editado:
            print("Ativo não encontrado!")

    else:
        encontrado = False
        for ativo in ativos:
            if entrada == ativo["nome"].lower() or entrada == ativo["Index"]:
                print(f"Ativo: {ativo['nome']}")
                print(f"Principal vulnerabilidade: {ativo['Principal vulnerabilidade']}")
                print(f"Responsável: {ativo.get('Responsavel', ['Não atribuído'])}")
                print(f"Index: {ativo['Index']}")
                print("-" * 60)
                encontrado = True
                break
        if encontrado == False:
            print("Opção inválida! Tente novamente.")
            print("-" * 60)
            continue

    loop2 = True
    while loop2 == True:  # LOOP PARA EVITAR Q O PROGRAMA SAIA DE UMA PERGUNTA PARA OUTRA (PERGUNTA DO INICIO DO PROGRAMA)
        continuar = input(f"Pressione 'enter' para continuar ou 'quit' para fechar o programa ").strip().lower()
        if continuar == "quit":
            rodando = False
            loop2 = False

        elif continuar == "":
            loop2 = False

        else:
            print("Selecione uma opção válida")