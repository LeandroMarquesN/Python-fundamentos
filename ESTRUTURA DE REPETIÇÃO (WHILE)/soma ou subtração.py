"""
        & Calculando a soma ou subtração de dois numeros até o usuaria mandar parar &


"""


from sunau import AUDIO_FILE_ENCODING_LINEAR_16


resp = 's'

while 's':
    n1 = input('Digite um numero \n')
    n2 = input('Digite outro numero \n')
    operador = input('Ecolha um operador para o calculo (+) ou (-)\n')
# ===validação dos dados =====
# nesta linha estou pergutando se n1 não é numero ou n2 não é numero  !! então ele exibe a menssagem na tela!
    if not n1.isnumeric() or not n2.isnumeric():
        print('digite um numero valido \n')
        continue

# converção do tipo
    n1 = int(n1)
    n2 = int(n2)
# calculando
    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1-n2)
    else:
        print('Operador invalido')

    resp = input("Quer continuar ? [s/n]\n")

#== Aqui temos uma condição para sair da estrutura de repetição
# se a resposta do usuario  for "n" ou  não  ou nao ou "N" ele o comando break entra em ação e sai do laço
    if resp == 'n'or resp=='N' or resp=='nao' or resp =='Nao' or resp =='não' or resp =='Não':
        break
    
print("Acabou")