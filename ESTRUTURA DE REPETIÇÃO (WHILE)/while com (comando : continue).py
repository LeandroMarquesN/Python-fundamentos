"""
  comando (continue) pula para o proximo laço 

"""
x = 0
while x <10:
    if x == 3:
        x = x+ 1 # se não colocarmos esta linha nosso comando vaificar com um aloço infinito neste ponto pois a noa variavel x nunca vai deixar de ser 3 então resolvemos fazendo este incremento
        continue # com o comando continue o algoritimo pula para o proximo laço! fazendo assim com que nos pulemos o numero 3 pois quando a variavel x possuir o valor 3 ela  vai satisfaszer a condição indo direto para o comando (continue)
    print(x)
    x =x + 1 # aqui sim nossa variavel x vai ter incremento  para que não se caia no loop infinito