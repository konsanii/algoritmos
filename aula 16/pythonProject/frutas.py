with open("frutas.txt", "w", encoding="utf-8") as arquivo:
    while True:
        frutas = input("digite um fruta:")
        if frutas.lower() == "sair":
            break
        else:
            arquivo.write(frutas)
            arquivo.write("\n")