#aqui vamos testar as funcoes..
from fu import segundos

h = int(input("digite a quantidade de horas"))
m = int(input("digite a quantidade de minutos"))
s = int(input("digite a quantidade de segundos"))

print(f"o total de segundos e {segundos(h, m, s)}")