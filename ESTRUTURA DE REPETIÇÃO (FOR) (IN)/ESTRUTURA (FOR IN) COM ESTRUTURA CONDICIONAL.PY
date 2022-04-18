texto = 'python'
nova_string =''
print('\n',texto,'\n')
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string = nova_string+letra
print('Antes da função a palavra python tinha o t e o h minuculos depois da função temos o th maiusculos\n')
print(nova_string)
