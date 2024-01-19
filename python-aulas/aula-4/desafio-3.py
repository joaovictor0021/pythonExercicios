print("Tabuada de multiplicação")

number = int(input("Insira um número "))

for i in range(1, 11):
    resultado = number * i

    print(number, "x", i, "=", resultado)
