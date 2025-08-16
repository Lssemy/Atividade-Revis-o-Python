import requests

nomes_moedas = {
    "USD": "dólares americanos",
    "EUR": "euros",
    "GBP": "libras esterlinas",
    "JPY": "ienes japoneses",
    "ARS": "pesos argentinos",
    "CAD": "dólares canadenses",
    "AUD": "dólares australianos",
    "CHF": "francos suíços",
    "CNY": "yuans chineses"
}

sigla = input("Digite a sigla da moeda desejada (ex: USD, EUR, GBP): ").strip().upper()

url = "https://api.exchangerate-api.com/v4/latest/BRL"
try:
    resposta = requests.get(url)
    dados = resposta.json()
    taxas = dados.get("rates", {})
    if sigla in taxas:
        valor = taxas[sigla]
        nome = nomes_moedas.get(sigla, sigla)
        print(f"1 Real vale {valor:.4f} {nome}.")
        if valor != 0:
            print(f"1 {nome} vale {1/valor:.4f} reais.")
        else:
            print("Não foi possível calcular a cotação inversa.")
    else:
        print("Moeda não encontrada na base de dados da API.")
except Exception as e:
    print("Erro ao consultar a API:", e)