def categorizar_numero(numero):
    if numero > 0:
        return 'positivo'
    elif numero < 0:
        return 'negativo'
    elif numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

def calculadora():
    soma = []
    subtracao = []
    multiplicacao = []
    divisao = []

    while True:
        print('Escolha uma operação:')
        print('+. Adição')
        print('-. Subtração')
        print('x. Multiplicação')
        print('/. Divisão')
        print('5. Ver histórico')
        print('Caso não queira mais calcular digite Sair')
        print('')

        escolha = input('Selecione uma opção: ')
        print('')

        if escolha == "Sair":
            print('Calculadora encerrada')
            break

        if escolha == '5':
            historico = str(input('Você deseja ver o histórico de qual opção:\n+\n-\nx\n/\ntudo\n'))

            if historico == '+':
                print('')
                print(f'O seu histórico de cálculo utilizando o operador de + é:')
                for resultado in soma:
                    categoria = categorizar_numero(resultado)
                    print(f'{resultado.__round__(1)} - {categoria}')

            elif historico == '-':
                print('')
                print(f'O seu histórico de cálculo utilizando o operador de - é:')
                for resultado in subtracao:
                    categoria = categorizar_numero(resultado)
                    print(f'{resultado.__round__(1)} - {categoria}')

            elif historico == 'x':
                print('')
                print(f'O seu histórico de cálculo utilizando o operador de x é:')
                for resultado in multiplicacao:
                    categoria = categorizar_numero(resultado)
                    print(f'{resultado.__round__(1)} - {categoria}')

            elif historico == '/':
                print('')
                print(f'O seu histórico de cálculo utilizando o operador de / é:')
                for resultado in divisao:
                    categoria = categorizar_numero(resultado)
                    print(f'{resultado.__round__(1)} - {categoria}')

            elif historico == 'tudo':
                print('')
                print('Todo o seu histórico de cálculo:')
                print(f'soma {soma}')
                print(f'subtração {subtracao}')
                print(f'multiplicação {multiplicacao}')
                print(f'divisão {divisao}')

        if escolha not in ('+', '-', 'x', '/'):
            print('Escolha inválida tente novamente')
            print('')
            continue

        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('')

        if escolha == '+':
            resultado = num1 + num2
            soma.append(resultado)
        elif escolha == '-':
            resultado = num1 - num2
            subtracao.append(resultado)
        elif escolha == 'x':
            resultado = num1 * num2
            multiplicacao.append(resultado)
        elif escolha == '/':
            if num2 != 0:
                resultado = num1 / num2
                divisao.append(resultado)
            else:
                print('Erro: Divisão por zero')
                continue

        print(f'Resultado: {resultado.__round__(1)}')
        print('')


calculadora()