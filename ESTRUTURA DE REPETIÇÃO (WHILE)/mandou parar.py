"""
Neste programa estamo susando a estrutura de repetição (while)

onde dentro dela temos a estrutura de condição simples
que usaremos para  interromper o laço.

onde a variavel resp começa com 's' ou verdadeiro
e so termina quando o usuario informa que quer parar
digitando 'n' ou 'N' usamos tambem o operador logico 
(or) o (ou) pois queremos o 'n' ou o 'N'

se ele escolher 'n' vamos mandar parar como o comando (break) o (pare)
se escolher 's' vamos repetir a estrutura while até ele digita 'n'

"""

resp = 's'

while True:
    num =int(input('Digite um numero \n'))
    resp = str(input('Quer continuar ? [s/n]\n'))

    if resp == 'n' or resp =='N':
        break
print('Usuario mandou parar\n')