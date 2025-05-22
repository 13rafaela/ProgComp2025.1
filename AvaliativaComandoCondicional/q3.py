from random import randint
num = randint(1,100)
print('escolha um núnero entre 1 e 100:( você tem 4 tentativas)')
# tentativas
palpite = int(input( 'tentativa 1:'))
if palpite == num:
    print('acertou, parabens!')
else:
    print('maior' if palpite < num else 'menor')
    palpite = int(input('tentativa 2:'))
    if palpite == num:
        print('acertou na segunda tentaiva!')
    else:
        print('maior' if palpite < num else 'menor')
    palpite = int(input('tentativa 3:'))
    if palpite == num:
        print('acertou na segunda tentativa!')
    else:
        print('maior' if palpite < num else 'menor')
        palpite = int(input('ultima tentativa, boa sorte!:'))
        if palpite == num:
            print('acertou na ultima tentativa!')
        else:
            print('você perdeu! o numero era', num)