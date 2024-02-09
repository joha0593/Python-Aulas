altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2 )
print("IMC: ", round(imc,2))


# Entrada dos dados
peso = float(input("Digite o seu peso (kg):"))
altura = float(input("Digite a sua altura (m):"))

# Processamento
imc = peso/(altura ** 2)

# Classificacao do resultado
if imc < 18.5:
  resultado = "baixo peso"

elif imc >= 18.5 and imc < 25:
    resultado = "peso adequado"

elif imc >= 18.5 and imc < 30:
    resultado = "sobrepeso"

else:
  resultado = "obesidade"

# Saida do dado
print(f"O seu IMC esta em {round(imc,2)}, classificando-o como {resultado}.")