from tracemalloc import start

"""
For in em Python
Iterando string com for

Função range(start=0, stop, step =1)

Este laço de  repetição é exatamente igual ao (para)
do portugolStudio porem temos um função que recebe os parametros (range)

Função range(start=0, stop, step =1)


bom ja sabemos que essse tipo de estrutura é usada quando sabemos o final da repetição
ou quando sabemos quantas veses vai se repetir! então precizamos de uma variavel de controle!

"""
print("Começando a contagem crescente \n")

for n in range(1,10,+1):
    print(f'{n} ')

print("Começando a contagem decrescente \n")

for n in range(10,0,-1):
    print(f'{n} ')

print("fazendo a contagem pulando de 2 em  2 \n")

for n in range(0,-10,-2):
    print(f'{n} ')

print("fazendo a contagem  descrescente voltando  de 2 em  2 \n")

for n in range(0,10,-2):
    print(f'{n} ')
