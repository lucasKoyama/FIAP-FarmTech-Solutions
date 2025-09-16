import csv


dados = []


def calcular_insumo(area, cultura):
    insumo = 0
    match cultura:
        case "Soja":
            insumo = area * 100
        case "Café":
            insumo = area * 500
    return insumo


def entrada_de_dados():
    cultura = input("Escolha a cultura desejada:\n " "1. Soja\n " "2. Café\n" "opção: ")
    if cultura == "1":
        cultura = "Soja"
    elif cultura == "2":
        cultura = "Café"
    comprimento = float(input("Insira o valor do comprimento da área em metros: "))
    largura = float(input("Insira o valor da largura da área em metros: "))
    area = comprimento * largura
    insumo = calcular_insumo(area, cultura)

    linha = [cultura, comprimento, largura, area, insumo]
    dados.append(linha)


def saida_de_dados():
    global dados
    for l in range(0, len(dados)):
        print(
            f"{l+1}. {dados[l][0]}, comprimento = {dados[l][1]}, largura = {dados[l][2]}, area = {dados[l][3]}, insumo = {dados[l][4]}"
        )


def atualizar_dados():
    global dados
    saida_de_dados()

    linha_alterada = int(input("Insira o número da linha que deseja alterar: "))
    coluna_alterada = input(
        "Insira o número da coluna que deseja alterar:\n"
        "1. cultura\n"
        "2. comprimento\n"
        "3. largura\n"
        "Insira a coluna: "
    )

    match coluna_alterada:
        case "1":  # cultura
            cultura = input("Insira o novo valor:\n1. Soja\n2. Café")
            dados[linha_alterada - 1][0] = "Soja" if cultura == "1" else "Café"
        case "2":  # comprimento
            dados[linha_alterada - 1][1] = float(input("Insira o novo valor: "))
        case "3":  # largura
            dados[linha_alterada - 1][2] = float(input("Insira o novo valor: "))

    area = dados[linha_alterada - 1][1] * dados[linha_alterada - 1][2]
    insumo = calcular_insumo(area, dados[linha_alterada - 1][0])
    dados[linha_alterada - 1][3] = area
    dados[linha_alterada - 1][4] = insumo


def deletar_dados():
    global dados
    saida_de_dados()

    opcao = input(
        "Escolha  opção para realizar a deleção:\n"
        "1. Deletar uma linha\n"
        "2. Deletar tudo\n"
        "Opção: "
    )
    match opcao:
        case "1":
            linha_excluida = int(input("Insira o número da linha que deseja excluir:"))
            del dados[linha_excluida - 1]
        case "2":
            dados = []


def exportar_dados():
    global dados
    if not dados:
        print("Não há dados para exportar.")
        return
    with open("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Cultura", "Comprimento", "Largura", "Área", "Insumo"])
        escritor.writerows(dados)


while True:
    menu = input(
        "escolha a opção:\n"
        "1. entrada de dados\n"
        "2. saída de dados\n"
        "3. atualizar dados\n"
        "4. deletar dados\n"
        "5. sair\n"
        "opção: "
    )
    print("\n")
    match menu:
        case "1":
            entrada_de_dados()
        case "2":
            saida_de_dados()
        case "3":
            atualizar_dados()
        case "4":
            deletar_dados()
        case "5":
            exportar_dados()
            print("Finalizando o programa...")
            break
    print("\n")
