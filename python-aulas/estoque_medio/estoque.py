quant_min = int(input("Digite a quantidade mínima em estoque: "))
quant_max = int(input("Digite a quantidade máxima em estoque: "))

estoque_medio = (quant_min + quant_max) / 2

print(f'O estoque médio da peça é: {estoque_medio}')