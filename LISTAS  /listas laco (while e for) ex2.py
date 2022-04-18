"""
    listas em Python
    fatiamento 


    funções : append = inserir no final o valor,insert = iseri o valor no inicio
    pop = remove o ultimo elemto da lista
    del = deleta um elemento ou uma fatia
    clear = limpa a lista

     len(variavel do tipo string) --> está função conta quatos caracteres tem na minha string  

    extend,+ = junta a lista com outra
    min,max
aula de3 lista :

https://www.youtube.com/watch?v=CSTb7pLsLZE&list=PLbIBj8vQhvm3l_9X_mFVnvBJ7rh2A6lor&index=16&ab_channel=Ot%C3%A1vioMiranda

"""

#=== jogo de adivinhação da palavra secreta ======

secreto = 'perfume'# -->palavra secreta
digitadas = []# aqui criamos uma lista vazia para adicionar a letras digitadas pelo usuario
chances = 3

while True: # --> criamos um loço infinito por isso que ele ja possui o valor True == verdadeiro Onde ele so vai parar quando o comando break for acionado!
    if chances <= 0:
        print('Você perdeu!!')
        break  # --> comando break para terminar o laço

    letra = input("Digite uma letra:")
    

    if len(letra) > 1: # --> função (len) está função conta quantos caracteres tem na minha string 
        print("<<ERRO valor invalido digite apenas 1 letra>>")
        continue # --> comando continue para pular para o proximo laço
    

    digitadas.append(letra) # --> Aqui estou adicionando a minha variavel letra a letra que o usuario digitoou com a função (append)
   
    if letra in secreto:  # Nesta condição estamos informando  se a variavel letra existe na variavel secreta
        print(f'Parabens você acertou! a letra {letra} existe na palavra secreta. ')
    else:
        print(f'Que pena a letra digitada {letra} não existe na palavra secreta!')
        #como não queremos que o elemento digitado incorrtamente não faça parte da variavel que estamos adicionando as letras corretas da variavel  (digitada) então vamos usar :
        #funcaçao pop() para deletar o ultimo elemnto digitado que está incorreto:
        digitadas.pop()

    secreto_temporario ='' # criamos está variavel para  guardar as letras que foram digitadas pelo usuario! e fazem parte da palvra secreta!
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario = secreto_temporario + letra_secreta
        else:
            secreto_temporario = secreto_temporario + '*' # --> Estamos omitindo as letras que fazem parte da palavra secreta e ainda não foram descobertas pelo usuario

    if secreto_temporario == secreto:
        print(f'Que legal, você ganhouuuu!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances = chances - 1 # ou chances-= 1

        print(f'voce ainda tem {chances} chances.')
        print() # printa para pular um a linha
print()
print()
print('Fim do jogo')
   