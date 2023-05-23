idcpol = float(input("digite o indice de poluição medido: "))

if idcpol <= 0.25:
    print("indice de poluição aceitável")
elif idcpol <= 0.3:
    print("indústrias do primeiro grupo devem suspender suas atividades.")
elif idcpol <= 0.4:
    print("indústrias do primeiro e segundo grupo devem suspender suas atividades.")
else:
    print("todos os grupos devem paralisar suas atividades imediatamente.")
