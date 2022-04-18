#Exercicio antecessor e sucesso de um numero !

num = int(input("Digite um numero e vou te falar o antecesso e seu sucessor\n"))
ant =num-1
suce =num+1
print('o sucessor de {} é {} e o antecessor é {} '.format(num,suce,ant),end ='fim \n')
print('o dobro de {} é {} e o triplo é {}'.format(num,(num*2),(num*3)))
#Exercicio comando do print
nome = input("Qual é o seu nome ?\n")
print("Prazer em conhecelo {:^20}".format(nome))

# com esse comando entreas chaves vamos fazer com que o nome fique 
# centralizado dentro de 20 espaços
nome= input("Qual é o seu segundo nome?\n")
print("Lega o seu segundo nome é {:=^20}".format(nome))
# para colocar numeros com casa decimais precisas
n =int(input('Digite um valor\n'))
n2=int(input('Digite outro valor:\n'))
soma = n + n2
mutipl = n * n2
divi = n / n2
divi2 = n // n2
potenc = n**n2
potnec2 = pow(n,n2) # aqui é um segunda maneira de calcular a raiz quadrada!
raiz_quadrada = n**(1/2)
raiz_cubica = n**(1/3)
print('A soma é {} a multiplicação é {} a divisão é {:.3f} '.format(soma,mutipl,divi)) # colocando desta maneira fica com 3 casas decimais!
print('a divisão é {}'.format(divi2))
print('A potencia é {}'.format(potenc))
print("A pontencia é ",potnec2,"\n")
print("A Raiz quadrada é de ",raiz_quadrada,"\n")
print("A raiz cubica é ",raiz_cubica,"\n")