def calcular_comissao(total_venda):
    if (total_venda >= 1000 and total_venda <= 5000):
        percentual_comissao = 5
        return 0.05 * total_venda, percentual_comissao
    elif (total_venda >= 5001 and total_venda <= 50000):
        percentual_comissao = 10
        return 0.10 * total_venda, percentual_comissao
    elif total_venda > 50000:
        percentual_comissao = 15
        return 0.15 * total_venda, percentual_comissao
    else:
        return 0, 0
    
    
preco_unitario = float(input("Digite o preço unitário da peça: "))
quantidade_vendida = int(input("Digite a quantidade vendida da peça: "))

total_venda = preco_unitario * quantidade_vendida

comissao, percentual_comissao = calcular_comissao(total_venda)

print(f"Preço Unitário: R${preco_unitario:.2f}")
print(f"Quantidade Vendida: {quantidade_vendida}")
print(f"Total da Venda: R${total_venda:.2f}")
print(f"Comissão do Vendedor: R${comissao:.2f} ({percentual_comissao}% de comissão)")

if percentual_comissao == 5:
    print("Bom trabalho!")
elif percentual_comissao == 10:
    print("Ótimo trabalho!")
elif percentual_comissao == 15:
    print("Excelente trabalho!")
else:
    print("Sem comissão. Você não bateu a meta mínima que era vender R$ 1000 em produtos!")