"""
         comando break : ele para o laço e pula para fora do loop

"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break # quando encontra este comando ele para e pula para fora do laço
    print(x)
    x = x + 1
print('Acabou')

