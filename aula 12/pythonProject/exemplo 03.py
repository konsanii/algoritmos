from math import pi, pow
def area_circulo(raio):
 PI = 3.141592
 area = PI * pow(raio, 2)
 return area
#...
r = float(input("Digite o raio: "))
print(f"A área do circulo de raio {r} é igual a {area_circulo(r)}")