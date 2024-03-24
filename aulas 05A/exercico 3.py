x1 = int(input("digite o primeiro lado do triangulo"))
x2 = int(input("digite o segundo lado do triangulo"))
x3 = int(input("digite o terceiro lado do triangulo"))

if x1+x2>x3 and x1+x3>x2 and x2+x3>x1:

 if x1 == x2 and x2 == x3:
    print("parabens esse e um triangulo Equilátero")

 elif x1 == x2 or x1==x3 or x2==x3:
    print("parabens esse e um triangulo isósceles")

 elif x1!=x2 and x1!=x3 and x2!=x3:
    print ("parabens esse e um triangulo escaleno")

else:
    print("não e um triangulo")
