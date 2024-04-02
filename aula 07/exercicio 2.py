maior_imc=0
menor_imc=100
soma_altura=0
soma_peso = 0
for k in range(1,6):
    altura = float(input(f"entre com a altura {k}:"))
    peso = float(input(f"entre com a peso {k}:"))
    imc = peso/(altura * altura)
    if imc> maior_imc:
        maior_imc = imc
    if imc<maior_imc:
        menor_imc = imc
    soma_altura = soma_altura * soma_altura
    soma_peso = soma_peso* soma_peso
peso_medio = soma_peso / 5
altura_medio = altura_peso / 5
print("resultado")