identificacao_vendedor = input("Digite a identificação do vendedor: ")

codigo_peca = input("Digite o código da peça: ")
preco_unitario = float(input("Digite o preço unitário da peça: "))
quantidade_vendida = int(input("Digite a quantidade vendida da peça: "))

total_venda = preco_unitario * quantidade_vendida

comissao = 0.05 * total_venda

print(f"\nVendedor: {identificacao_vendedor}")
print(f"Código da Peça: {codigo_peca}")
print(f"Preço Unitário: R${preco_unitario:.2f}")
print(f"Quantidade Vendida: {quantidade_vendida}")
print(f"Total da Venda: R${total_venda:.2f}")
print(f"Comissão do Vendedor: R${comissao:.2f}")