n = int(input("digite o valor de n"))
e = 0
k = 1
while k <= n:
    e = e + 2**k
    k = k +1
    print(f"o valor de E = {e}")
