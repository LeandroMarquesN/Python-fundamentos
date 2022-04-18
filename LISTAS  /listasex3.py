"""
    listas em Python
    fatiamento 
    append,insert,pop,del,clear,extend,+
    min,max
aula de3 lista :

https://www.youtube.com/watch?v=CSTb7pLsLZE&list=PLbIBj8vQhvm3l_9X_mFVnvBJ7rh2A6lor&index=16&ab_channel=Ot%C3%A1vioMiranda

"""
#indice  0   1   2   3   5
"""
Os indices possuem valores negativos tambem
0 1 2 3
0 -1 -2 -3
"""
"""
listas possuem tambem o fatiamento 
onde temos a composição:

[0star,5stop,1+step]
issso sguinifiva que queremos que
comece no 0 , pare no 5 , e receba o incremento de  1 

"""
lista =['A','Banana','C','D','E',10.5, 'oi']
"""
mostrando os 3 primeiro elemntos da lista
"""
print('Mostrando os 3 primeiros elementos da lista\n')
print(lista[0:3:1])
print('Ou podemos escreve a lista apartir do elemento 3 assim :\n')
print(lista[:3])
print('Ou podemos escrever a lista do elemento 3 ao final desta maneira \n')
print(lista[3:])

print('mostrando o elemnto 2 ao 4\n')
print(lista[1:4:1])

"""
quando omitimos os parametros do fatiamento 
po padraão vem: [começo = 0 : final =tamanho da lista:  o step =1]

"""
print('Exibir elementos da lista pulando de 2 em dois')
print(lista[::2])

"""
para inverte a lsiat podemos utilizar o -1 no passo e assim vamos invertela
"""
print('Invertendo a lista com o comando print(lista[::-1])\n')
print(lista[::-1])