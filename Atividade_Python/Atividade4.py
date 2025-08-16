gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
notas = []

print("Bem-vindo! Vamos corrigir a prova de 10 questões.")

while True:
    acertos = 0
    for i in range(10):
        resp = input(f"Questão {i+1}: ").strip().upper()
        while resp not in ['A', 'B', 'C', 'D', 'E']:
            resp = input("Resposta inválida! Digite A, B, C, D ou E: ").strip().upper()
        if resp == gabarito[i]:
            acertos += 1
    notas.append(acertos)
    print(f"Você acertou {acertos} de 10.")
    if input("Outro aluno? (S/N): ").strip().upper() != 'S':
        break

if notas:
    print("\nResumo da turma:")
    print(f"Maior nota: {max(notas)}/10")
    print(f"Menor nota: {min(notas)}/10")
    print(f"Total de alunos: {len(notas)}")
    print(f"Média da turma: {sum(notas)/len(notas):.1f}/10")
else:
    print("Ninguém respondeu a prova.")