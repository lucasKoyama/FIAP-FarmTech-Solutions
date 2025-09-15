dados = []

def calcular_insumo(area,cultura):
    insumo = 0
    match cultura:
        case "1":
            insumo = area * 100
        case "2":
            insumo = area * 500
    return insumo

def entrada_de_dados():
    cultura = input("escolha a cultura desejada:\n "
          "1. Soja\n "
          "2. Café\n"
            "opção: ")
    comprimento = float(input("insira o valor do comprimento da área em metros: "))
    altura = float(input("insira o valor da altura da área em metros: "))
    area = comprimento * altura
    insumo= calcular_insumo(area,cultura)

    linha = [cultura, comprimento, altura, area, insumo]
    dados.append(linha)
def saida_de_dados():
    global dados
    for l in dados:
        print(f"{"soja" if l[0] == "1" else "cafe"}, comprimento = {l[1]}, altura = {l[2]}, area = {l[3]}, insumo = {l[4]}")


def atualizar_dados():
    global dados
    saida_de_dados()
    linha_alterada = int(input("digite o número da linha que deseja alterar:"))

    coluna_alterada = int(input("digite o número da coluna que deseja alterar"))
    dados[linha_alterada][coluna_alterada] = input("digite o novo valor")


def deletar_dados():
    print("deletando dados")
while True:
    menu = input(
        "escolha a opção:\n"
        "1.entrada de dados\n"
        "2.saída de dados\n"
        "3.atualizar dados\n"
        "4.deletar dados\n"
        "5.sair\n"
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
        case "5": break
    print("\n")