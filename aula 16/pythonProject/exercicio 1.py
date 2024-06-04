# Abre o arquivo para leitura
# arquivoEntrada = open('entrada_ex1.txt', 'r')
# Coloca todas as linhas em memoria
# linhas = arquivoEntrada.readlines()
# Fecha o arquivo
# arquivoEntrada.close()

# De forma Pythonica
with open('usuarios.txt', 'r') as arquivoEntrada:
    linhas = arquivoEntrada.readlines()

usuarios = []
espacosUtilizados = []
espacoTotal = 0.0
for linha in linhas:
    campos = linha.split()
    usuario = campos[0]
    espacoUtilizado = int(campos[1])
    usuarios.append(usuario)
    espacosUtilizados.append(espacoUtilizado)
    espacoTotal += espacoUtilizado

# Cria a Relatórios
print('----------------------------------------------------------------')
print('ACME Inc.               Uso do espaco em disco pelos usuarios')
print('----------------------------------------------------------------')
print('Nr.  Usuario        Espaco utilizado     %% do uso')
for i in range(0, len(usuarios)):
    espacoMB = espacosUtilizados[i] / (1024.0 * 1024.0)
    percentualUso = espacosUtilizados[i] / espacoTotal
    perc = percentualUso * 100
    print(f'{i+1:2d} - {usuarios[i]:11s} -  {espacoMB:13.2f} MB   - {perc:7.2f}%')


print(f'\nEspaco total ocupado: {(espacoTotal / (1024.0 * 1024.0)):.2f} MB')
space = (espacoTotal / len(usuarios) / (1024.0 * 1024.0))
print(f'Espaco medio ocupado: {space:.2f} MB')
print('----------------------------------------------------------------')