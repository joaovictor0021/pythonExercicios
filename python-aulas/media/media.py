A = float(input('Nota 1: '))
B = float(input('Nota 2: '))
C = float(input('Nota 3: '))
D = float(input('Nota 4: '))

media = (A+B+C+D)/4

if(media >= 9 and media <= 10):
    print(f'Sua nota foi {media} (APROVADO)')
elif(media >= 7 and media < 9):
    print(f'Sua nota foi {media} (APROVADO)')
elif(media >= 5 and media < 7):
    print(f'Sua nota foi {media} (APROVADO)')
elif (media >= 0 and media < 5):
    print(f'Sua nota foi {media} (REPROVADO)')
else:
    print('Digite uma nota entre 0 e 10')
