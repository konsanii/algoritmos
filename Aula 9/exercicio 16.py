from random import randint
m = []
l = []
for y in range(5):
    for x in range(5):
        l.append(randint(1,100))
    m.append(l)
    l = []
soma = 0
qtd = 0
for i in range (0,5,2):
    soma = soma + m[y][x]
    qtd = qtd +1

media = soma / qtd
print(f"{media=}")
