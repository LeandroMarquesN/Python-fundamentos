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
l1 =[1,2,3]
l2 =['a','b','c']
l3 = l1 + l2
# função extend = extendi uma lista pra outra lista ja existente
l2.extend(l3)

print('lista 1 ',l1,"\n")
print('lista 2 ',l2,"\n")
print("lista 3 é a junção da lista 1 e 2 \n",l3,'\n'
)
print("Agora a lista 2 exta extendida para a lista 3 \n ",l2,'\n')