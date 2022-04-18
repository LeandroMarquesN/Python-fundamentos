
vetor = ['Luis','aJoao','maria'] # coloquei um a na frente do nome joão para não ter que alterar o codigo
#bnvbn
# para chegar no comando break temos que tirar o a da frente do nome do joao

for valor in vetor:
    if valor.lower().startswith('j'):
        print('\n\nChegou no comando break\n\n')
        break
else:
    print('\n\nNão existe nehuma palavra dentro da lista que começa com a letra j\n\n')

"""
    Com a função .Lower() colocamos a variavel valor que está dentro do vetor em letras minusculas 
    e com a .startswith('j') queremos saber se a string começa com uma letra 'j'


"""