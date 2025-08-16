valores = []

while True:
    n = int(input("Digite um valor (-1 para encerrar): "))
    if n == -1:
        break
    valores.append(n)

print("Quantidade de valores lidos:", len(valores))
print("Valores na ordem informada:", valores)
print("Valores na ordem inversa:", valores[::-1])
print("Soma dos valores:", sum(valores))

if valores:
    media = sum(valores) / len(valores)
    print("Média dos valores:", media)
    acima_media = 0
    for v in valores:
        if v > media:
            acima_media += 1
    print("Quantidade de valores acima da média:", acima_media)
else:
    print("Não há valores para calcular média.")