with open ('idades.txt', 'r', encoding="utf-8") as arquivoEntrada:
    linhas = arquivoEntrada.readlines()

idades=[]
sexos=[]
total_idades=0.0
for linha in linhas:
    campos = linha.split(",")
    idade = int(campos[0])
    sexo = campos[1]
    idades.append(idade)
    sexos.append(sexo[0])
    total_idades += idade


n_f = 0
n_m = 0
total_idade_f = 0.0
total_idade_m = 0.0

for i in range(len(idades)):
    if sexos[i] == 'F':
        n_f += 1
        total_idade_f += idades[i]
    else:
        n_m += 1
        total_idade_m += idades[i]
idade_media_f = total_idade_f / n_f
idade_media_m = total_idade_m / n_m

print(f"Idade Média das Mulheres é: {idade_media_f}")
print(f"Idade Média dos Homens é: {idade_media_m}")
print(f"Idade Média Geral é : {total_idades / len(idades)}")

