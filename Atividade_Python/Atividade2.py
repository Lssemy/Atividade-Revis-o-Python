x = int(input("digite o valor a ser sacado:"))
n100= x //100
valor_restante = x % 100
n50 = valor_restante // 50
valor_restante = valor_restante % 50
n10 = valor_restante // 10
valor_restante = valor_restante % 10
n5 = valor_restante // 5
valor_restante = valor_restante % 5
n1 = valor_restante // 1
print(f"Notas de 100: {n100}")
print(f"Notas de 50: {n50}")
print(f"Notas de 10: {n10}")
print(f"Notas de 5: {n5}")
print(f"Notas de 1: {n1}")