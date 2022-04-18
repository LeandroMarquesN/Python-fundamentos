"""
    COMADO :
    CONTINUE = PULA PARA O PROXIMO LAÇO
    
"""

texto = 'python'
nova_string =''
print('\n',texto,'\n')
for letra in texto:
    if letra == 't':
        continue # note que ao chegar nesse ponto do algoritimo ele encontra o comando  (continue) e pula para o proximo laço
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string = nova_string+letra

print(nova_string)# Fazendo com que a  letra (t) não seja inclusa na nova_string 
#================== retornando entrão a string pyHon

