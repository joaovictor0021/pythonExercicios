anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

idade_em_dias = (anos * 365) + (meses * 30) + dias

print(f"A idade em dias é: {idade_em_dias} dias")