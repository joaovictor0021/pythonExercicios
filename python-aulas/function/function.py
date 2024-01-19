print("Função simples")
def saudacao():
    print("Olá, boa noite!")

saudacao()

print("Função com parametros")

def saudacao_alunos(alunoName):
    print(f"boa noite, {alunoName}")


saudacao_alunos("João")

def tuma_aluno(aluno, turma):
    print(f"O aluno {aluno} é da turma {turma}")

tuma_aluno("João", 3001)



print("Função com return")

def soma(x, y):
    return x + y

print(f"2 + 5 = {soma(2, 5)}")


def multiplique(x, y):
    resultado = x * y
    return resultado


print(f"10 x 8 = {multiplique(10, 8)}")
