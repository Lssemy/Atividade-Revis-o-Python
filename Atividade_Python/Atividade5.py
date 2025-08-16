cardapio = {
    100: {"nome": "Cachorro Quente", "preco": 1.20},
    101: {"nome": "Bauru Simples", "preco": 1.30},
    102: {"nome": "Bauru com ovo", "preco": 1.50},
    103: {"nome": "Hamburguer", "preco": 1.20},
    104: {"nome": "Cheeseburguer", "preco": 1.30},
    105: {"nome": "Refrigerante", "preco": 1.00}
}

total_geral = 0

while True: 
    x = int(input("Digite o código do produto desejado: "))
    if x not in cardapio:
        print("Código não encontrado. Tente novamente.")
        continue

    z = int(input("Digite a quantidade do produto desejado: ")) 

    preco = cardapio[x]["preco"]
    valor = preco * z
    total_geral += valor

    j = input("Deseja pedir mais alguma coisa? (s/n): ").lower()

    if j == "s":
        continue
    elif j == "n":
        print(f"Obrigado por comprar conosco! Valor final: R$ {total_geral}")
        break
    else:
        print("Opção inválida. Digite apenas 's' ou 'n'.")