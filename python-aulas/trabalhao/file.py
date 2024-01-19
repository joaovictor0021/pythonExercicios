##conversor de escalas
def conversor_de_escalas():
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def celsius_para_kelvin(celsius):
        return celsius + 273.15

    def fahrenheit_para_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def fahrenheit_para_kelvin(fahrenheit):
        return (fahrenheit + 459.67) * 5/9

    def kelvin_para_celsius(kelvin):
        return kelvin - 273.15

    def kelvin_para_fahrenheit(kelvin):
        return (kelvin * 9/5) - 459.67

    temperatura = float(input("Digite a temperatura: "))
    scale_thermometric = input("Digite a unidade de temperatura (C, F, K): ").upper()

    if scale_thermometric == 'C':
        temperatura_fahrenheit = celsius_para_fahrenheit(temperatura)
        temperatura_kelvin = celsius_para_kelvin(temperatura)
        print(f"\n{temperatura:.0f} Celsius é equivalente a:")
        print(f"{temperatura_fahrenheit:.2f} Fahrenheit")
        print(f"{temperatura_kelvin:.2f} Kelvin")
        print('')
    elif scale_thermometric == 'F':
        temperatura_celsius = fahrenheit_para_celsius(temperatura)
        temperatura_kelvin = fahrenheit_para_kelvin(temperatura)
        print(f"\n{temperatura:.2f} Fahrenheit é equivalente a:")
        print(f"{temperatura_celsius:.2f} Celsius")
        print(f"{temperatura_kelvin:.2f} Kelvin")
        print('')
    elif scale_thermometric == 'K':
        temperatura_celsius = kelvin_para_celsius(temperatura)
        temperatura_fahrenheit = kelvin_para_fahrenheit(temperatura)
        print(f"\n{temperatura:.2f} Kelvin é equivalente a:")
        print(f"{temperatura_celsius:.2f} Celsius")
        print(f"{temperatura_fahrenheit:.2f} Fahrenheit")
        print('')
    else:
        print("Unidade de temperatura inválida. Use C, F ou K.")

##cotação do dólar
def cotacao_dolar():
    print('Cotação do dólar em reais')
    print('')
    cotacao_dolar = float(input("Digite a o valor da cotação atual em reais: "))
    valor_dolar = float(input("Digite o valor em dólares: "))

    valor_real = valor_dolar * cotacao_dolar

    print(f'O valor em reais é: R$ {valor_real:.2f}')

##estoque médio
def estoque_medio():
    print('Estoque médio')
    print('')
    quant_min = int(input("Digite a quantidade mínima em estoque: "))
    quant_max = int(input("Digite a quantidade máxima em estoque: "))

    estoque_medio = (quant_min + quant_max) / 2

    print(f'O estoque médio da peça é: {estoque_medio}')

##calculadora de IMC
def calc_imc():
    print('Calculadora IMC')
    print('')
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))


    imc = peso / (altura ** 2)

    classificacao = ""
    if imc < 18.5:
        classificacao = "Magreza"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Normal"
    elif 25.0 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc <= 39.9:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade Grave"

    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

##idade em dias
def idade_em_dias():
    print('Idade em ANOS, MESES e DIAS')
    print('')
    anos = int(input("Digite a idade em anos: "))
    meses = int(input("Digite a idade em meses: "))
    dias = int(input("Digite a idade em dias: "))

    idade_em_dias = (anos * 365) + (meses * 30) + dias

    print(f"A idade em dias é: {idade_em_dias} dias")

##media de cinco números
def media_de_cinco_numeros():
    print('Média de 5 números')
    print('')
    soma = 0
    # Loop para ler 5 números
    for i in range(5):
        numero = float(input(f'Digite o {i+1}º número: '))
        soma += numero 

    media = soma / 5

    # Apresenta o resultado
    print(f'A média dos 5 números é: {media}')

##comissão de funcionário
def comissao_de_funcionario():
    print('Pagamento de comissão')
    print('')  
    identificacao_vendedor = input("Digite a sua identificação: ")

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





print('Escolha:\n1 - Escalas Termométricas\n2 - Cotação do Dólar\n3 - Estoque médio\n4 - Calculadora IMC\n5 - Idade em ANOS, MESES e DIAS\n6 - Média de 5 números\n7 - Pagamento de comissão')
print('')
escolha = str(input('Ecolha: '))
print('')
match escolha:
    case '1':
        print('Conversor de escalas termométricas')
        conversor_de_escalas()
    case '2':
        cotacao_dolar()
    case '3':
        estoque_medio()
    case '4':
        calc_imc()
    case '5':
        idade_em_dias()
    case '6':
        media_de_cinco_numeros()
    case '7':
        comissao_de_funcionario()


