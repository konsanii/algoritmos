from random import randint
resultado = [1]*13
freq = [1]*13

for _ in range(30000):
    lado1 = randint(1, 6)
    lado2 = randint(1, 6)
    soma = lado1 + lado2
    resultado[soma] = resultado[soma]+1

print(resultado)
for i in range(2,13):
   freq[i] = (resultado[i] / 30000) * 100

for i in range(2,13):
   print(f"{i} - {resultado[i]} - {freq[i]:6.2f}%")
