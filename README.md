# Gerenciador de Ativos de TI e Vulnerabilidades

> **1ª Atividade Avaliativa — Cibersegurança**  
> **Instituição:** Universidade Federal de Uberlândia (UFU)  
> **Autor:** Douglas Oliveira de Aquino  
> **Linguagem:** Python 3  

---

## 📋 Sobre o Projeto

Este projeto consiste em uma aplicação baseada em linha de comando (CLI) desenvolvida em Python para gerenciar **ativos de TI** e suas respectivas **vulnerabilidades de segurança**. O sistema permite a persistência dos dados através de um arquivo de armazenamento em formato JSON (`ativos.json`) e atende a todos os critérios de avaliação propostos para a disciplina.

---

## 🛠️ Funcionalidades e Atendimento aos Requisitos

| Requisito | Descrição da Funcionalidade | Status |
| :---: | :--- | :---: |
| **1** | **Interface CLI e Tratamento de Erros:** Menu interativo textual via prompt com validação de entradas inválidas, loops de repetição e prevenção contra falhas de execução. | ✅ |
| **2** | **Categorização de Ativos:** Estrutura para enumeração/classificação dos ativos com códigos identificadores numéricos inteiros. | ✅ |
| **3** | **Cadastro de Ativos (CRUD):** Leitura via prompt e armazenamento persistente em arquivo JSON (`ativos.json`), contendo ID único, nome/hostname, responsável e lista de vulnerabilidades associadas. | ✅ |
| **4** | **Consulta e Busca Organizada:** Pesquisa de ativos na base de dados por ID ou por nome/hostname. | ✅ |
| **5** | **Atualização de Dados (Edit):** Permite alterar nome, responsável e a lista de vulnerabilidades cadastradas. | ✅ |
| **6** | **Remoção de Registros (Del):** Deleção completa de ativos e reordenação/re-enumeração automática do campo `Index` para manter a integridade do banco. | ✅ |
| **7** | **Gestão Detalhada de Vulnerabilidades:** Cadastro de vulnerabilidades contendo obrigatoriamente **Nome/Descrição**, **Tipo/Categoria**, **Severidade** (Baixa, Média, Alta, Crítica) e **Status de Tratamento** (Aberta, Em tratamento, Corrigida, Aceita como risco). | ✅ |
| **8** | **Visualização de Vulnerabilidades:** Exibição detalhada de todas as vulnerabilidades vinculadas ou alerta amigável quando o ativo não possui registros. | ✅ |
| **9** | **Estrutura em Dicionário (Hash Map):** Uso intensivo de estruturas do tipo `dict` e listas dinâmicas em Python para indexação, otimização de busca e persistência em JSON. | ✅ |
| **10** | **Versionamento e Git Flow:** Projeto desenvolvido no GitHub com controle de versão utilizando múltiplas branches (`main` e `dev`) e processo de *merge*. | ✅ |

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   # Nota: Remova os colchetes do link abaixo!
   git clone [https://github.com/Douglas-aquino1105/Primeiro_Projeto]
   cd Primeiro_Projeto
2. **Executar (`Projeto 1.py`)**