presidentes = {
    'Deodoro':1889,
    'Prudente':1894,
    'Washington':1926,
    'Vargas':1930,
    'Janio':1961
}
print ("tamanho", len(presidentes))
dic_logico = {0: True, 1: False, 3:True}
print ("all", all(dic_logico))
False
print("any", any(dic_logico))
True
sorted(presidentes)
sorted(presidentes, reverse=True)
sorted(presidentes.values())
sorted(presidentes.items())