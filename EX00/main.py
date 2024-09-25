def pes_para_metros(pes):
    return pes * 0,3048

def metros_para_pes(metros):
    return metros * 3.281

def jardas_para_metros(jardas):
    return jardas * 0.9144

def jardas_para_pes(jardas):
    metros = jardas_para_metros(jardas)
    return metros_para_pes(metros)


def converter():
    print("Escolha o tipo de conversão:")
    print("1: Pés para Metros")
    print("2: Metros para Pés")
    print("3: Jardas para Metros")
    print("4: Jardas para Pés")

    escolha = int(input("Digite o número correspondente à conversão desejada: "))

    if escolha == 1:
        valor = float(input("Digite o valor em pés: "))
        resultado = pes_para_metros(valor)
        print(f"{valor} pés é igual a {resultado:.4f} metros")

    elif escolha == 2:
        valor = float(input("Digite o valor em metros: "))
        resultado = metros_para_pes(valor)
        print(f"{valor} metros é igual a {resultado:.4f} pés")

    elif escolha == 3:
        valor = float(input("Digite o valor em jardas: "))
        resultado = jardas_para_metros(valor)
        print(f"{valor} jardas é igual a {resultado:.4f} metros")

    elif escolha == 4:
        valor = float(input("Digite o valor em jardas: "))
        resultado = jardas_para_pes(valor)
        print(f"{valor} jardas é igual a {resultado:.4f} pés")

    else:
        print("Opção inválida!")

converter()