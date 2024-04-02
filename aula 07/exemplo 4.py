soma = 0
idade = 100
qtd = 0
while idade != 0:
    idade = int(input(f"Entre com a idade {qtd+1}:"))
    if idade != 0:
        soma = soma+idade
        qtd = qtd+1
        media = soma /qtd
        print(f"A media das {qtd} idades é: {media:5.2f} anos.")