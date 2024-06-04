arquivo=open("texto.txt", "r", encoding="utf-8")
for linha in arquivo:
      print (linha.strip())
arquivo.close()
