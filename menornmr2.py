n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

menor = n1  

if n2 < menor:
    menor = n2  
if 3 < menor:
    menor = n3  

print("O menor número é:", menor)
