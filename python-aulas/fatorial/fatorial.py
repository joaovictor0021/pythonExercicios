numero = int(input('Digite um numero'))

indice = 1

f = 1

while indice <= numero:
    f = f*indice
    indice += 1

print('Fatorial While', numero,'! é', f)


resultado = 1

## Com For
for n in range(1, numero + 1):
    resultado *= n

print('Fatorial FOR', resultado)