qtd = 0
frase = input("digite uma frase")
for letra in frase:
  if (letra =="a") or (letra=="A") or (letra =="ã"):
      qtd = qtd + 1
print(f"existe{qtd} 'a' na frase.")
