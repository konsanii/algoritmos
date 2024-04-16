from random import randint
resultado = [0]*7
freq = [0]*7
print(resultado)
for _ in range(6000):
    lado = randint(1, 6)
    resultado[lado]=resultado[lado]+1

print(resultado)

for i in range(1,7):
   freq[i] = (resultado[i] / 6000) * 100

for i in range(1,7):
   print(f"{i} - {resultado[i]} - {freq[i]:6.2f}%")
