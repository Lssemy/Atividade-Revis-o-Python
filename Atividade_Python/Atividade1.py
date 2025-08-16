def descontogas(lgas, litros, preco):
    if litros <= 20:
        desconto = lgas * 0.04
    else:
        desconto = lgas * 0.06

    valorf = preco - desconto
    return valorf


def descontoalcool(lalco, litros, preco):
    if litros <= 20:
        desconto = lalco * 0.03
    else:
        desconto = lalco * 0.05

    valorf = preco - desconto
    return valorf

lalco = 2.50
lgas = 1.90

opcao = input("Digite qual opção deseja abastecer (G/A): ").upper()
litros = float(input("Digite a quantidade de litros desejada: "))

if opcao == "G":
    preco = lgas * litros
    print(f"O valor da gasolina sem desconto: R$ {preco:.2f}")
    print(f"O valor da gasolina com desconto: R$ {descontogas(lgas, litros, preco):.2f}")

elif opcao == "A":
    preco = lalco * litros
    print(f"O valor do alcool sem desconto: R$ {preco:.2f}")
    print(f"O valor do alcool com desconto: R$ {descontoalcool(lalco, litros, preco):.2f}")

else:
    print("Opção inválida!")