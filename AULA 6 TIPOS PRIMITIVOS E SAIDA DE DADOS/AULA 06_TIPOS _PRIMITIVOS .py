print("Aula de number 06 tipos primitivos e saida de dados!")
#NA linha abaixo com este comando estou pedindo para o usuario digitar um numero que seja do tipo (inteiro) por isso que coloquei o (int) #
numero_1 = int(input("Digite um numero :"))

#na linha abaixo estou  estou fazendo o mesmo procedimento
numero_2 = int(input("Digite mais um numero :"))

#declarei está variavel com o nome de soma para receber a soma de numero_1 com numero_2 #
soma = numero_1+numero_2

#Entre a string e a variavel soma estou usando uma (,)para concatenar a string com a variavel soma pois os inal de (+) não será possivel #
print("A soma entre os numeros é de : ",soma)

#Ou podemos escrever destá maneira que vai dar muito certo papai!! #
print("A soma entre {} e {} vale {}".format(numero_1,numero_2,soma))

2
#Aqui estou exemplificando os doi tipos primitivos de numeros # 

var_tip_inteiro = int(input("Digite um numero do tipo interio ex: 1 ,10 ,15..."))


var_tip_float = float(input("Digite um numero do tipo real ex : 2.0 .3.5 ,0.005 ..."))
print("valor da variavel de tipo inteiro foi :",var_tip_inteiro)
print("valor da variavel de tipo float ou real foi :",var_tip_float)

print("o numero ",var_tip_inteiro," é do tipo :")
print(type(var_tip_inteiro))

print("o numero ",var_tip_float," é do tipo :")
print(type(var_tip_float))

#Aqui vou exemplificar a variavel de tipo bolean ou de valor verdadeiro ou falso
# boleano  (bool)  == verdadeiro ou falso #
n = input('Digite algo :')
print(n.isnumeric())


#Aqui vou exemplificar com uma variavel do tipo string ou um conjunto de caracteres  #
# string ==   (str)   valor de tipo cadeia de caracteres ou uma string #
