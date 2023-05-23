num = int(input("Digite um número: "))

if num == 1:
    print(f"{num} não é número primo")
else:
    for i in range(2, num//2+1):
        if num % i == 0:
            print(num, "não é número primo")
            break
    else:
        print(num, "número primo")
