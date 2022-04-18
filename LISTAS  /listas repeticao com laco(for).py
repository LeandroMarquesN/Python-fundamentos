"""
    listas em Python
    fatiamento 


    funções : append = inserir no final o valor,insert = iseri o valor no inicio
    pop = remove o ultimo elemto da lista
    del = deleta um elemento ou uma fatia
    clear = limpa a lista
             
    extend,+ = junta a lista com outra
    min,max
aula de3 lista :

https://www.youtube.com/watch?v=CSTb7pLsLZE&list=PLbIBj8vQhvm3l_9X_mFVnvBJ7rh2A6lor&index=16&ab_channel=Ot%C3%A1vioMiranda

"""
# tttalizando os  os valores  dos indices e mostrando na tela
total = 0
l4 = [10,20,30,40,50,60]

for indice in l4:
    cont = 0
    total = total + indice # ou soma+=indice
    print(f'indice {cont} possui o valor =>  {total}')
    cont= cont + 1

