# opreador logico de (negação) o (not) muito utilizado para fazer inverções de expressões que retorna um valor.

a = '' #--> valor vazio de uma string
b = 0 # --> valor vazio tambem podemos escrever desta maneira pois 0 é conciderado um boleanao falso

# fazemos desta maneira para checar se o valor da variavel foi digitado pelo usuario 
# caso vc coloque algo entre as chaves vai retornar um obrigado pois não etá mais vazio
# caso vc aperte o enter sem digitar nada vai retornar a mensagem  "por favor preencha o valor"

a= str(input('Digite algo :'))

if not a:
    print('Por favor preencha o valor de  A')
else:
    print("Obrigado!!")

print('\n')

b= str(input('Digite algo novamente :'))

if not b:
    print('Por favor preencha o valor de B')
else:
    print("Obrigado!!")