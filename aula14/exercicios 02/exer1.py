def animais(cabecas, pernas):
    coelhos = (pernas - 2*cabecas)/2
    patos = cabecas - coelhos

    return patos, coelhos

cabecas = 46
pernas = 141

patos, coelhos = animais(cabecas, pernas)

print("o cercado tem ", str(int(patos)),   "patos e ", str(int(coelhos)),  "coelhos")

