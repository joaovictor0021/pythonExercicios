valor = int(input("Digite um valor entre 10 e 100: "))

if valor < 10 or valor > 100:
    print("Insira um valor entre 10 e 100")
else:
    for i in range(valor + 1): 
        print(i)