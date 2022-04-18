"""
 (while) com o comando (else) 

"""

contador = 1
acumulador = 1

while contador <= 5:
    print(f'       Este é o contador {contador} e este é o acumulado que está dando = {acumulador} ')

    if contador == 2:
        contador += +2 # se não colocarmos essa linha vamos cair em um loop infinito
        print('  chegou no ponto de parada onde pulou o contador 3')
        continue

    acumulador += contador # acumulador = acumulador + contador
    contador += 1
else:
    print('   Essa menssagem so vai aparecer caso a condição do laço seja satisfeita')

print('acabou')