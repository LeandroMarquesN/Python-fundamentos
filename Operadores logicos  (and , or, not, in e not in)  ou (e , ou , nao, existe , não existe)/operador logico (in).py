# neste programa vou 
#Utiliza o operador logico (in) pois ela retorna um valor boleano

#Onde vamos vericar se existe um elemento especifico no valor digitado

# Aqui vamos pedir um nome e verificar se existe a letra u
nome = str(input('Digite um nome que tenha letra u ;\n'))

if 'u' in nome: # está esta indicando : se a string 'u' existe na vairavel 'nome'
    print('Existe um aletra u no seu nome\n')
else:
    print('Não existe uma letra u no seu nome')

# podemos usar de outras maneira tambe:

palavra= str(input("Digete alguma frase qu e contenha a palavra amor : \n"))

if ' amor ' in palavra:
    print("Encontrei a palavra amor em sua frase")
else:
    print("Não encontrei a palavra amor em sua frase!!")

