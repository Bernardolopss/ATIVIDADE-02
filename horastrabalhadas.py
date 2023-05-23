C = int(input("digite o código do operário: "))
N = int(input("digite o numero de horas trabalhadas: "))

if N > 50:
    E = (N - 50) * 20
    salariottl = 50 * 10 + E
else:
    E = 0
    salariottl = N * 10

print("salario total: R$".format(salariottl))
print("salario excedente: R$".format(E))
