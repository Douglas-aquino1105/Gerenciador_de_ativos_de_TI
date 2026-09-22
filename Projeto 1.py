import json


# FUNÇÃO PARA CRIAR A ESTRUTURA DETALHADA DA VULNERABILIDADE
def criar_vulnerabilidade():
    print("\n--- Cadastro de Vulnerabilidade ---")
    nome = input("Nome da vulnerabilidade: ").strip().capitalize()
    tipo = input("Categoria/Tipo (ex: Software, Hardware, Rede): ").strip().capitalize()
    sev = input("Severidade (Baixa, Média, Alta, Crítica): ").strip().capitalize()
    status = input("Status (Aberta, Em tratamento, Corrigida, Aceita como risco): ").strip().capitalize()

    return {
        "Nome": nome,
        "tipo": tipo,
        "severidade": sev,
        "status": status
    }


# FUNÇÃO PARA EXIBIR VULNERABILIDADES (COMPATÍVEL COM STRINGS ANTIGAS E DICIONÁRIOS NOVOS)
def exibir_vulnerabilidades(lista_vulns):
    for i, vul in enumerate(lista_vulns, start=1):
        if isinstance(vul, dict): #RETORNA TRUE SE FOR DO TIPO ESPECIFICADO, EX: VUL É UM DICIONARIO? TRUE/FALSE
            nome_vuln = vul.get("Nome", vul.get("descrição", "Sem nome")) #TENTA PEGAR O NOME PELO NOME->DESCRIÇÃO->ATRIBUI "SEM NOME"
            print(
                f"{i}. Nome: {nome_vuln} | Tipo: {vul.get('tipo', 'N/A')} | Severidade: {vul.get('severidade', 'N/A')} | Status: {vul.get('status', 'N/A')}")
        else:
            print(f"{i}. {vul}")


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
        json.dump(lista, file, indent=4, ensure_ascii=False)


ativos = carregar_ativos()

rodando = True
while rodando == True:

    print(
        "\nDigite o Index ou o nome do ativo para ver seu detalhes, 'add' para adicionar, 'del' para remover ou 'edit' para editar.")
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
        nome_ativo = input("Qual o nome do ativo que deseja adicionar? ").strip().capitalize()
        responsavel_ativo = input("Qual o responsável pelo ativo? ").strip().capitalize()

        if responsavel_ativo == "":
            responsavel_ativo = "Não atribuído"

        # Chama a função para coletar a vulnerabilidade com os 4 campos requeridos
        vuln_inicial = criar_vulnerabilidade()

        novo_ativo = {
            "nome": nome_ativo,
            "Principal vulnerabilidade": [vuln_inicial],
            "Responsavel": [responsavel_ativo],
            "Index": str(len(ativos) + 1)
        }
        ativos.append(novo_ativo)
        print(f"\nAtivo '{nome_ativo}' adicionado com sucesso!")
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
            for i, ativo in enumerate(ativos, start=1):
                ativo["Index"] = str(i)
            salvar_ativos(ativos)
        else:
            print("\nAtivo não encontrado!")

    elif entrada == "edit":
        alvo = input("Digite o nome ou Index do ativo que deseja editar: ").strip().lower()
        editado = False

        for ativo in ativos:
            if alvo == ativo["Index"] or alvo == ativo["nome"].lower():
                print(f"Ativo '{ativo['nome']}' encontrado!")

                while True:
                    escolha = input(
                        "\nO que deseja editar?\n1. Nome\n2. Lista de vulnerabilidades\n3. Responsável\n> ").strip().lower()

                    if escolha == "1" or escolha == "nome":
                        novo_nome = input(
                            f"Por qual nome deseja substituir? Nome atual: {ativo['nome']}\n> ").strip().capitalize()
                        if novo_nome != "":
                            ativo["nome"] = novo_nome
                            print(f"\nNome alterado com sucesso! Novo nome: {ativo['nome']}")
                            salvar_ativos(ativos)
                        break

                    elif escolha == "2" or escolha == "lista de vulnerabilidades" or escolha == "lista":
                        substituir = input(
                            "\nQual operação deseja realizar? \n1. Substituir vulnerabilidade \n2. Adicionar vulnerabilidade\n3. Remover vulnerabilidade\n> ").strip().lower()

                        if substituir == "1" or substituir == "substituir":
                            if len(ativo["Principal vulnerabilidade"]) == 0:
                                print("\nEste ativo não possui vulnerabilidades registradas para substituir.")
                                break

                            print("\nQual vulnerabilidade deseja substituir?")
                            exibir_vulnerabilidades(ativo["Principal vulnerabilidade"])

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posicao_encontrada = None

                            for index, vul in enumerate(ativo["Principal vulnerabilidade"]):
                                nome_vul = vul.get("Nome", vul.get("descrição", vul)) if isinstance(vul, dict) else vul
                                if escolhida == str(index + 1) or escolhida == str(nome_vul).lower():
                                    posicao_encontrada = index
                                    break

                            if posicao_encontrada is not None:
                                print("\nDigite os novos dados para esta vulnerabilidade:")
                                nova_vuln = criar_vulnerabilidade()
                                ativo["Principal vulnerabilidade"][posicao_encontrada] = nova_vuln

                                print(f"\nVulnerabilidade atualizada com sucesso!")
                                salvar_ativos(ativos)
                                break
                            else:
                                print("Vulnerabilidade não encontrada!")

                        elif substituir == "2" or substituir == "adicionar vulnerabilidade" or substituir == "adicionar":
                            nova_vuln = criar_vulnerabilidade()
                            ativo["Principal vulnerabilidade"].append(nova_vuln)
                            print(f"\nNova vulnerabilidade adicionada com sucesso!")
                            salvar_ativos(ativos)
                            break

                        elif substituir == "3" or substituir == "remover vulnerabilidade" or substituir == "remover":
                            if len(ativo["Principal vulnerabilidade"]) == 0:
                                print("\nEste ativo não possui vulnerabilidades registradas para remover.")
                                break

                            print("\nQual vulnerabilidade deseja remover?")
                            exibir_vulnerabilidades(ativo["Principal vulnerabilidade"])

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posicao_encontrada = None

                            for index, vul in enumerate(ativo["Principal vulnerabilidade"]):
                                nome_vul = vul.get("Nome", vul.get("descrição", vul)) if isinstance(vul, dict) else vul
                                if escolhida == str(index + 1) or escolhida == str(nome_vul).lower():
                                    posicao_encontrada = index
                                    break

                            if posicao_encontrada is not None:
                                vul_removida = ativo["Principal vulnerabilidade"].pop(posicao_encontrada)
                                nome_removido = vul_removida.get("Nome", vul_removida.get("descrição",
                                                                                          vul_removida)) if isinstance(
                                    vul_removida, dict) else vul_removida
                                print(f"\nVulnerabilidade '{nome_removido}' removida com sucesso!")
                                salvar_ativos(ativos)
                                break
                            else:
                                print("Vulnerabilidade não encontrada!")

                        else:
                            print("Opção inválida!")

                    elif escolha == "3" or escolha == "responsavel" or escolha == "responsável":
                        lista_resp = ativo.get("Responsavel", ["Não atribuído"])
                        op_resp = input(
                            "\nQual operação deseja realizar no responsável? \n1. Substituir responsável \n2. Adicionar responsável\n3. Remover responsável\n> ").strip().lower()

                        if op_resp == "1" or op_resp == "substituir":
                            print("\nQual responsável deseja substituir?")
                            for i, resp in enumerate(lista_resp, start=1):
                                print(f"{i}. '{resp}'")

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posicao_encontrada = None

                            for index, resp in enumerate(lista_resp):
                                if escolhida == str(index + 1) or escolhida == resp.lower():
                                    posicao_encontrada = index
                                    break

                            if posicao_encontrada is not None:
                                resp_antigo = lista_resp[posicao_encontrada]
                                novo_resp = input(f"Substituir '{resp_antigo}' por qual nome? ").strip().capitalize()
                                lista_resp[posicao_encontrada] = novo_resp
                                ativo["Responsavel"] = lista_resp

                                print(f"\nResponsável '{resp_antigo}' alterado com sucesso para '{novo_resp}'!")
                                salvar_ativos(ativos)
                                break
                            else:
                                print("Responsável não encontrado!")

                        elif op_resp == "2" or op_resp == "adicionar":
                            novo_resp = input(
                                f"Qual responsável deseja adicionar? Responsáveis atuais: {lista_resp}\n> ").strip().capitalize()
                            if "Responsavel" not in ativo or not isinstance(ativo["Responsavel"], list):
                                ativo["Responsavel"] = []
                            ativo["Responsavel"].append(novo_resp)

                            print(f"\nNovo responsável '{novo_resp}' adicionado com sucesso!")
                            salvar_ativos(ativos)
                            break

                        elif op_resp == "3" or op_resp == "remover":
                            if len(lista_resp) == 0:
                                print("Este ativo não possui responsáveis para serem removidos.")
                                break

                            print("\nQual responsável deseja remover?")
                            for i, resp in enumerate(lista_resp, start=1):
                                print(f"{i}. '{resp}'")

                            escolhida = input("-" * 25 + "> ").strip().lower()
                            posicao_encontrada = None

                            for index, resp in enumerate(lista_resp):
                                if escolhida == str(index + 1) or escolhida == resp.lower():
                                    posicao_encontrada = index
                                    break

                            if posicao_encontrada is not None:
                                resp_removido = lista_resp.pop(posicao_encontrada)
                                if len(lista_resp) == 0:
                                    lista_resp.append("Não atribuído")
                                ativo["Responsavel"] = lista_resp

                                print(f"\nResponsável '{resp_removido}' removido com sucesso!")
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

    else:  # EXIBIÇÃO DE DETALHES DO ATIVO
        encontrado = False
        for ativo in ativos:
            if entrada == ativo["nome"].lower() or entrada == ativo["Index"]:
                print(f"Ativo: {ativo['nome']}")
                print("Vulnerabilidades registradas:")
                exibir_vulnerabilidades(ativo["Principal vulnerabilidade"])
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
    while loop2 == True:
        continuar = input(f"Pressione 'enter' para continuar ou 'quit' para fechar o programa ").strip().lower()
        if continuar == "quit":
            rodando = False
            loop2 = False
        elif continuar == "":
            loop2 = False
        else:
            print("Selecione uma opção válida")