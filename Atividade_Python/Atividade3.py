x = float(input("Digite a nota do primeiro semestre: "))
d = float(input("Digite a nota do semestre semestre: "))
media = (x + d) / 2
if media >= 9:
    print("Voce tirou A")
elif 7.5 <= media < 9:
    print("Voce tirou B")
elif 6.0 <= media < 7.5:
    print("Voce tirou C")
elif 4.0 <= media < 6:
    print("Voce tirou D")
elif media < 4:
    print("Voce tirou E")