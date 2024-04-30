idade_por_sobrenome = {}

for _ in range(3):
    sobrenome = input("digite o sobrenome de pessoas")
    idade = int(input("digite a idade de pessoas"))
    idade_por_sobrenome[sobrenome] = idade

sobrenome_mais_velho = max(idade_por_sobrenome, key=idade_por_sobrenome.get)
print(f"\n0 sobrenome das pessoas mais velhas é:){sobrenome_mais_velho}")




