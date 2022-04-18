"""
    Estrutura de repetição For com listas e tambem com condicionais. 

"""
familia = ['daniel','maria','livia','lavinia','leandro']

for indice in range(len(familia)):
    print(f'NO indice {indice} integrante {familia[indice]}')

    if familia[indice] == 'daniel' :
        print(f'Esse é o {familia[indice]} chefe da familia!!')
    if familia[indice] == 'livia':
        print(f'Essa é a {familia[indice]} ela é muito danada!!')
    