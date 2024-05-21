
Y = 46
valor = Y * 2 + 5
x = []
somar = 0

for numero in range(valor + 1):
    if numero < 2:
        continue
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        x.append(numero)
        somar += numero

print(f"Lista de numeros primos no valor y e {valor}: {x}")
print(f"Soma de todos os numeros e: {somar}")
