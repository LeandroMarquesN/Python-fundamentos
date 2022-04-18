"""
    listas em Python
    fatiamento 
    append,insert,pop,del,clear,extend,+
    min,max
    range

"""

l1 =[1,2,3,]
l2 = ['a','b','c']
print(f'lista 1 {l1}.')
print(f'lista 2 {l2}.')

#========= função append ============

l2.append('d')# com o (append ) estou adicionando o elemento (d) na lista 2
print(f'adicionando o elemento (d) na posição 3 da lista 2 {l2}.  ')
print('lembrando que vetor  array ou lists começam em  0')

#====== função insert ===========

l1.insert(0,'banana')# estou adicionando o elemento banana na posição 0 da lista 1
print(f'estou adicionando o elemento banana na posição 0 da lista 1')
print(l1)
l1.insert(2,'melão')#estou adicionando o elemento melão na posição 2 da lista 1
print(f'estou adicionando o elemento melão na posição 2 da lista 1')
print(l1)

# ====== Funão (POP) deleta um elemento do final da lista ====

l1.pop()#--> vou deletar o ultimo elemnto da lista1
print(f'deletei o ultimo elemento da lista 1\n{l1}')

#====== Função Del deleta elementos da lista ==========
l3 = [1,2,3,4,5,6,7,8,'coco',9]
print(f'Criei mais uma  lista 3 \n {l3}.')
# com a função del podemos eliminar uma fatia da lista por exemplo da posição 3 ate a  5  [3:5] lembrando que o ultimo elemnto não é escluido
del(l3[3:5]) 
print(f'vou escluir o elemento 4 e 5 da lsita 3\n{l3}') 
del(l3[6])# Estou escluindo o elemento coco que está na posição 6 da lisyta 3 ( jaque o elemento 4 e 5 foram deletados)
print(f'Estou escluindo o elemento coco que está na posição 6 da lisyta 3  jaque o elemento 4 e 5 foram deletados {l3}.')

#======== Função max e min ==============
# mostra na tela o valor maximo da lista e min mostra o valor minimo da lista.

print(f'O valor maximo da lista 3 é ===> {max(l3)}')
print(f'O valor minimo da lista 3 é ==> {(min(l3))}')

#==== Função extend =============

l5 =[1,2,3]
l6 =['a','b','c']
l7 = l5 + l6
# função extend = extendi uma lista pra outra lista ja existente
l6.extend(l7)

print('lista 5 ',l5,"\n")
print('lista 6 ',l6,"\n")
print("lista 7 é a junção da lista 5 e 6 \n",l7,'\n'
)
print("Agora a lista 6 exta extendida para a lista 7 \n ",l6,'\n')

#===== Função Clear ==============
# Clear == Limpa a lista
print(f'Estou mostrando na tela a lista  6 para limpala com o comando clear {l6}')
l6.clear()# aqui eue limpei os valores da lsita
l6 = [0,0,0,0,0,0,0,0,0] # Estou atribuindo novos valores a lista 6 nesta linha para exemplificar que a função clear limpou os dados da lsiat 6 
print(f'Lista 6 agora está vazia !! com a função clear \n E atribui valores de 0 as posições para mostrar na tela{l6}.')