notas = []

for i in range(4):
    nt = float(input(f"Informe a {i+1} nota: "))
    while nt < 0 or nt > 10:
        nt = float(input("Nota inválida, tente denovo: "))
    notas.append(nt)

med = sum(notas)/len(notas)

if med < 4:
    situacao = "Reprovado"
elif med < 8:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"
