"""
    Funcão =Len ==> retorna a quantidade de elementos que etão dentro de uma lista.

    lendo elementos de uma lista atraves da estrutura de repetição for.

    video aula : https://www.youtube.com/watch?v=XevXSrM5xEE&ab_channel=OMEROFRANCISCOBERTOL

"""


frutas = ['macã','pera','melancia','jaca']

t = len(frutas) ## aqui estou criado uma variavel para receber a quantidade de elementos que possui a minha lista. posso colocara está estrutra len(frutas)dentro do range que fica : range(len(frutas))

for indice in range(t):
    print(f'vetorFrutas posição {indice} possui ==> {frutas[indice]}')



