
vetor = ['Luis', 'aJoao', 'maria']

for valor in vetor:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe nehuma palavra dentro da lista que começa com a letra j')