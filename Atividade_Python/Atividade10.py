import requests

cep = input("Digite o CEP do destino: ")
api = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(api)
dados = response.json()

print(f"Bairro: {dados['bairro']}, {dados['localidade']} - {dados['uf']}")

if dados["localidade"] != "São Paulo":
    print("Destino fora da cidade de São Paulo (cidades vizinhas).")
else:
    prefixo = int(cep[:2])

    if prefixo == 1:
        print("Região: Centro de São Paulo")
    elif prefixo == 2:
        print("Região: Zona Norte de São Paulo")
    elif prefixo in [3, 4]:
        print("Região: Zona Leste de São Paulo")
    elif prefixo in [5, 6]:
        print("Região: Zona Sul de São Paulo")
    elif prefixo == 5:  
        print("Região: Zona Oeste de São Paulo")
    else:
        print("Não foi possível identificar a zona.")