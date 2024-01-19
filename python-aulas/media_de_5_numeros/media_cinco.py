soma = 0

# Loop para ler 5 números
for i in range(5):
    numero = float(input(f'Digite o {i+1}º número: '))
    soma += numero 

media = soma / 5

# Apresenta o resultado
print(f'A média dos 5 números é: {media}')