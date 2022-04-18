"""
    listas em Python
    fatiamento 
    append,insert,pop,del,clear,extend,+
    min,max

"""
#indice  0   1   2   3   5
"""
Os indices possuem valores negativos tambem
0 1 2 3
0 -1 -2 -3
"""
import string


lista =['A','Banana','C','D','E',10.5, 'oi']
# ind-   5      4     3   2   1   0     -1
"""
Aqui estamos querendo acessar o elemento do indice -1 da nossa lista!

"""
print(lista[-1])

print(lista[6])

print('\n O Elemento -1 e o 6 são respectivamentes o mesmo elemnto ')
print(lista)

"""
atribuindo outro valor para o elemento 6 
inves de oi  agora vai ser tchau mas poderiamos mudar para qualquer outro tipo primitivo
"""
lista[6] = 'thcau'

print(lista[6])

