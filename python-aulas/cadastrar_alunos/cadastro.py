from random import randint

print('Cadastar alunos')
print('')
print('Informações pessoais do aluno:')
print('')

n_random = randint(0, 2000)
print('Sua matricula é:', randint(0, 2000))
print('')
nome = str(input('Nome: '))
sobrenome = str(input('Sobrenome: '))
idade = int(input('Idade: '))
email = str(input('Email: '))
renda_familiar = float(input('Renda familiar mensal: '))
filiacao = str(input('Filiação: '))
cpf = str(input('CPF: '))
grau_escolaridade = str(input('Grau de escolaridade:\nPré-escolar\nFundamental 1\nFundamental 2\nEnsino Médio\n\n '))



def verificar_idade_nota(idade):
        if (idade >= 16):
            nota_enem = float(input('Nota do enem: '))
        else:
            print('Não tem idade para fazer a prova do ENEM')
            return
        
        if (nota_enem >= 600 and nota_enem <= 1000):
            print('Passou com a média alta')
            return
        elif (nota_enem > 500 and nota_enem < 600):
            print('Passou na media')
            return
        elif (nota_enem >= 0 and nota_enem < 500):
            print('Media baixa')      
            return
        else:
            print('Média indefinida')
            return     

def verificar_renda(renda_familiar):
     salario_minimo = 1412

     if (renda_familiar < salario_minimo):
        print('Ganhou uma bolsa de 100%')
        return
     elif (renda_familiar >= salario_minimo and renda_familiar < salario_minimo * 2):
        print('Ganhou uma bolsa de 50%')
        return
     elif (renda_familiar >= salario_minimo * 3):
        print('Ganhou uma bolsa de 30%')
        return
     else:
        print('Ganhou uma bolsa de 10%')
        return
     
     
def verificar_progresso(idade, grau_escolaridade):
    if idade < 6 and grau_escolaridade == "Pré-escolar":
        return "Adiantado"
    elif 6 <= idade <= 10 and grau_escolaridade == "Fundamental 1":
        return "No tempo certo"
    elif 11 <= idade <= 14 and grau_escolaridade == "Fundamental 2":
        return "No tempo certo"
    elif idade > 14 and grau_escolaridade == "Ensino Médio":
        return "No tempo certo"
    else:
        return "Atrasado"

# Exemplo de uso:
verificar_progresso(idade, grau_escolaridade)
verificar_idade_nota(idade)
verificar_renda(renda_familiar)



# Abre o arquivo em modo de escrita
with open('dados_alunos.txt', 'w') as arquivo:
    # Escreve as informações pessoais do aluno no arquivo
    arquivo.write(f'Matricula: {n_random}\n')
    arquivo.write(f'Nome: {nome}\n')
    arquivo.write(f'Sobrenome: {sobrenome}\n')
    arquivo.write(f'Idade: {idade}\n')
    arquivo.write(f'Email: {email}\n')
    arquivo.write(f'Renda Familiar: {renda_familiar}\n')
    arquivo.write(f'Filiação: {filiacao}\n')
    arquivo.write(f'CPF: {cpf}\n')
    arquivo.write(f'Grau de Escolaridade: {grau_escolaridade}\n')

    # Chama as funções para verificar idade, nota, renda e progresso e escreve os resultados no arquivo
    arquivo.write(f'Progresso: {verificar_progresso(idade, grau_escolaridade)}\n')
    verificar_idade_nota(idade)
    verificar_renda(renda_familiar)

print('Dados gravados com sucesso no arquivo dados_alunos.txt')
