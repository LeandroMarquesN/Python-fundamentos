n = input('Digite algo  que contenha somente numeros para retornar verdadeiro:') #Estou perguntando se o que o usuario digiou é um numero #
print(n.isnumeric())
m = input('digite algo Novamente que contenha somente letras para retornar verdadeiro :') #Estou perguntando se o que o usuario digitou é uma letra ! #
print(m.isalpha())

o = input("Digite mais uma vez alguma coisa que contenha numeros e letras  para retornar verdadeiro!") #nesta linha estou perguntando se o que o usuario digitou é alphanumerico#
                                                #quero saber se contem numeros ou letras! #
print(o.isalnum())

p = input("Digite algo novamente em letras maiusculas para retornar verdadeiro :")
print(p.isupper())  #nesta linha estou perguntando  se a palavra está em letras maiusculas se sim vai retornar verdadeiro #
                    # se não retorna  falso ou seja true ou false #
q = input("digite algo em letras minusculas para retornar verdadeiro :")
print(q.islower())

#Quando leio algo com input ele sempre retorna um valor do tipo string independente do que eu coloque #
#para fazer a conversão do valor do tipo primitivo que quero que leia tenho que deixar especificado no comando #

#Neste comando estou recebendo uma variavel do tipo inteiro : #
# numero_2 = int(input("Digite mais um numero :")) #

#Neste comando estou recebendo uma variavel do tipo float : #
# numero_2 = float(input("Digite mais um numero :")) #
#============================================================
#=========== Aula 06 tipos primitivos =======================
num1 = int(input('Digite um numero'))
num2 = int(input('Digite outro numero'))
soma = num1+num2

print('A soma entre {} e {} vale {}'.format(num1, num2, soma))

#========================================================