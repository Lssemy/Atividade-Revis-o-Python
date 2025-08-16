def ler_float(msg, default):
    s = input(msg).strip()
    return float(s.replace(",", ".")) if s else float(default)

salario_inicial = ler_float("Salário inicial (Enter = 1000): ", "1000")
ano_final = int(input("Calcular até que ano? (Enter = 2025): ").strip() or "2025")
modo = input(
    "\nModo de simulação:\n"
    "  E - Enunciado  : percentual dobra todo ano\n"
    "  C - Com teto   : dobro limitado por um teto anual\n"
    "  R - Realista   : percentual fixo anual\n"
    "Escolha (E/C/R) [C]: "
).strip().upper() or "C"

perc_1996 = 0.015
salario = salario_inicial * (1 + perc_1996)
print(f"1995: R$ {salario_inicial:.2f}")
print(f"1996: R$ {salario:.2f} (+{perc_1996*100:.2f}%)")

percentual = perc_1996
if modo == "C":
    teto = ler_float("Teto anual em % (Enter = 10): ", "10") / 100
if modo == "R":
    fixo = ler_float("Percentual fixo anual em % (Enter = 3): ", "3") / 100
    percentual = fixo

for ano in range(1997, ano_final + 1):
    if modo == "E":
        percentual *= 2
    elif modo == "C":
        percentual = min(percentual * 2, teto)
    salario *= (1 + percentual)
    print(f"{ano}: R$ {salario:.2f} (+{percentual*100:.2f}%)")

print(f"\nSalário estimado em {ano_final}: R$ {salario:.2f}")