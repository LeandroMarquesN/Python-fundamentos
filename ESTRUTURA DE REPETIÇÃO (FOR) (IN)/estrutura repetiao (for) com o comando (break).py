"""
BREAK = TERMINA O LAÇO ===== ESTE COMANDO E IGUAL O (PARE DO PORTUGOL STUDIO)

"""
texto = 'python'
nova_string =''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break # note que ao chegar nesse ponto do algoritimo ele encontra o comando  (break) e para o nosso laço
    else:
        nova_string = nova_string+letra

print(nova_string) # então ele retorna na tela apenas o a palavra  pyTH