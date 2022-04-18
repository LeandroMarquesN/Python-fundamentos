num =int(input('Digite um numero :\n'))

# if == se elif == senao se  else == senao ( Está sintase é a mesma  cois do portugol)

if num == 0 :
    print(f'O numero {num} é igual a zero.\n')  # precizamos de 4 espaços para determinar o blçoco 
elif num == 1:
    print(f'O numero {num} é igual a 1')
elif num == 2:
    print(f'O numero {num} é igual a 2 então é par \n.')
elif num == 3:
    print(f'O numero {num} é igual a 3 então é impar \n')
elif num == 4:
    print(f'O numero {num} é igual a 4 então é par\n')
elif num >= 5:
    print(f'O numro {num} é maior que 0 .\n')
else:
    print(f'O numero {num} é um numero negativo !')