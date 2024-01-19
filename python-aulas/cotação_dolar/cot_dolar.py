cotacao_dolar = float(input("Digite a cotação do dólar: "))
valor_dolar = float(input("Digite o valor em dólares: "))

valor_real = valor_dolar * cotacao_dolar

print(f'O valor em reais é: {valor_real:.2f}')