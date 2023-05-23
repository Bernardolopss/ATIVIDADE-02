P = float(input("Informe o peso de peixes(kg): "))

if P > 50:
    E = P - 50
    M = E * 4
else:
    E = 0
    M = 0
print("Excesso de peso: ", E, "kg")
print("Valor da multa: R$", M)
