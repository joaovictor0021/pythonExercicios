opcao = input('Deseja utilizar o tradutor? ')
print('Opções de palavras para tarduzir:\n1- Casa\n2- Fogo\n3- Cachorro\n4- Avião\n5- Água\n6- Mesa\n7- Trabalho\n8- Chuva\n9- Óculos\n10- Cabo\n11- Deus\n')

palavra = input('Escolha um número para traduzir: ')

while opcao != 'n':
    match palavra:
        case '1':
            print('Casa em Inglês: House')
            print('Casa em Espanhol: Hogar')
            print('Casa em Francês: Maison')
            break
        case '2':
            print('Fogo em Inglês: Fire')
            print('Fogo em Espanhol: Fuego')
            print('Fogo em Francês: Feu')
            break
        case '3':
            print('Cachorro em Inglês: Dog')
            print('Cachorro em Espanhol: Cachorro')
            print('Cachorro em Francês: Chiot')
            break
        case '4':
            print('Avião em Inglês: Plane')
            print('Avião em Espanhol: Avión')
            print('Avião em Francês: Avión')
            break
        case '5':
            print('Água em Inglês: Water')
            print('Água em Espanhol: Agua')
            print('Água em Francês: Eau')
            break
        case '6':
            print('Mesa em Inglês: Table')
            print('Mesa em Espanhol: Mesa')
            print('Mesa em Francês: Tableau')
            break
        case '7':
            print('Trabalho em Inglês: Work')
            print('Trabalho em Espanhol: Trabajar')
            print('Trabalho em Francês: Travail')
            break
        case '8':
            print('Chuva em Inglês: Rain')
            print('Chuva em Espanhol: Lluvia')
            print('Chuva em Francês: Pluie')
            break
        case '9':
            print('Óculos em Inglês: Glasses')
            print('Óculos em Espanhol: Anteojos')
            print('Óculos em Francês: Lunettes')
            break
        case '10':
            print('Cabo em Inglês: Cable')
            print('Cabo em Espanhol: Cable')
            print('Cabo em Francês: Câble')
            break
        case '11':
            print('Deus em Inglês: God')
            print('Deus em Espanhol: Dios')
            print('Deus em Francês: Dieu')
            break
    


        