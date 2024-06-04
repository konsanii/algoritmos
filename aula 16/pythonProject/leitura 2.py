with open("texto.txt" , "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print("fim do arquivo")