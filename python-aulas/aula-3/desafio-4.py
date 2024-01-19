print("insira um número para saber se ele é negativo ou não")

n1 = int(input("Digite o número "))

if (n1 < 0):
    print(f"O número {n1} é negativo!")
elif (n1 > 0):
    print(f"O número {n1} é positivo!")
elif (n1 == 0):
    print("O número é zero")
else:
    print("Valor desconhecido")