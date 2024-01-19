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