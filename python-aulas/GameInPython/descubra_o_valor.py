from random import randint

chance = 0
tentativa = 0
pontuacao = 1000
player = str(input("Insira seu username: " ))
fichas = int(input(player + " insira a quantidade de fichas que você possui: "))
pontuacaoPerdeu = 0

print("---------------------------------------------------")
print()
print("                Descubra o valor")
print()
print("---------------------------------------------------")

print()
nivel = input(" Escolha o nível (Fácil, Médio, Difícil): ").lower()
print()
print("---------------------------------------------------")

if nivel == "fácil":
    chance = fichas
    valor_oculto_aleatorio = 'randint(0, 50)'
elif nivel == "médio":
    chance = fichas
    valor_oculto_aleatorio = randint(0, 110)
elif nivel == "difícil":
    chance = fichas
    valor_oculto_aleatorio = randint(0, 300)
else:
    print("Nível inválido. Escolhendo o nível Médio por padrão.")
    chance = fichas
    valor_oculto_aleatorio = randint(0, 110)

print()
print(f"A pontuação inícial é de {pontuacao}")

for i in range(fichas):
    print()
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
