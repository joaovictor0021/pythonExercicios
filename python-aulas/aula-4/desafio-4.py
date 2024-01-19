n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    n1, n2 = n2, n1

for numero in range(n1, n2 + 1):
    if (numero % 2) == 0:
        print(numero)