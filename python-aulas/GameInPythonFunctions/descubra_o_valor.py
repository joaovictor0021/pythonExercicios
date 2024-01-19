from random import randint

def obter_info_jogador():
    player = str(input("Insira seu username: "))
    fichas = int(input(player + " insira a quantidade de fichas que você possui: "))
    return player, fichas

def definir_nivel():
    print("---------------------------------------------------")
    print()
    print("                Descubra o valor")
    print()
    print("---------------------------------------------------")
    print()
    nivel = input(" Escolha o nível (Fácil, Médio, Difícil): ").lower()
    print()
    print("---------------------------------------------------")
    return nivel

def obter_valor_oculto_aleatorio(nivel, fichas):
    if nivel == "Fácil":
        return fichas, randint(0, 50)
    elif nivel == "Médio":
        return fichas, randint(0, 110)
    elif nivel == "Difícil":
        return fichas, randint(0, 300)
    else:
        print("Nível inválido. Escolhendo o nível Médio por padrão.")
        return fichas, randint(0, 110)

def mostrar_pontuacao_inicial(pontuacao):
    print()
    print(f"A pontuação inícial é de {pontuacao}")

def jogar_novamente():
    return input("Deseja jogar novamente? (Sim / Não): ").lower() == 'sim'

def jogo():
    player, fichas = obter_info_jogador()
    nivel = definir_nivel()
    fichas, valor_oculto_aleatorio = obter_valor_oculto_aleatorio(nivel, fichas)
    pontuacao = 1000
    pontuacaoPerdeu = 0

    mostrar_pontuacao_inicial(pontuacao)

    for tentativa in range(fichas):
        print()
        print(f"Você tem {fichas - tentativa} chances")
        print()
        valor_usuario = int(input("Tente acertar o valor oculto: "))
        tentativa += 1

        diferenca = abs(valor_oculto_aleatorio - valor_usuario)
        margem = 5

        if valor_usuario == valor_oculto_aleatorio:
            print()
            print(f"Parabéns, você descobriu o valor oculto que era {valor_oculto_aleatorio} e sua pontuação foi de {pontuacao}")
            print()
            break
        elif diferenca <= margem:
            print("Você está muito perto de acertar")
        elif valor_oculto_aleatorio < valor_usuario:
            print("O valor oculto é menor!")
        elif valor_oculto_aleatorio > valor_usuario:
            print("O valor oculto é maior!")

        pontuacao -= 75

    else:
        print()
        print("---------------------------------------------------")
        print()
        print("Suas chances acabaram " + player)
        print()
        print(f"O valor oculto era {valor_oculto_aleatorio}")
        print()
        print(f"Sua pontuação final foi {pontuacaoPerdeu} pontos")
        print()
        print("---------------------------------------------------")

    if jogar_novamente():
        jogo()

jogo()