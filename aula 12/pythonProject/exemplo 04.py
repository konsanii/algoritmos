
from math import pow
def potencia(numero, expoente = 2):
 """ Função que calcula a potencia de um número.
 Valor de Entrada:
 numero = numero a ser calculado (elevado a potencia) (float)
 expoente = expoente utilizado no cálculo (inteiro)
 Resultado:
 Resultado do cálculo (float)"""

 resultado = pow(numero, expoente)
 return resultado
#...
n = float(input("Digite o numero: "))
e = int(input("Expoente: "))
print(f"Valor com expoente: {potencia(n,e)}")

potencia(expoente= e,numero= n)

print(f"Valor sem o expoente: {potencia(n)}")

print(help(potencia))