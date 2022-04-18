"""
        Estrututra de repetição For
        A função len() retorna o numero de elementos da lista.

        range(stop) -> range object range(start, stop[, step]) -> range object

Retorna um objeto que produz uma sequência de inteiros do início (inclusive) ao fim (exclusivo) por etapa. range(i, j) produz i, i+1, i+2, ..., j-1. start padroniza para 0, e stop é omitido! range(4) produz 0, 1, 2, 3. Esses são exatamente os índices válidos para uma lista de 4 elementos. Quando step é dado, ele especifica o incremento (ou decremento).

"""


familia = ["Daniel","Maria","Leandro","leila" ,"Livia","Lavinia",]


for indice in range(len(familia)):
    if familia[indice] == "leila" :
        print(f"\tO integrande {familia[3]} corresponde a está posição e já  não faz mais parte destá familia!!")
        continue    
    print(f'O indice {indice} corresponde ao integrande {familia[indice]}')
    
    
 