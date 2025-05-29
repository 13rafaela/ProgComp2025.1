num = int( input('numero?'))
ndiv = 0
for k in range (1,n +1):
    if n % k == 0:
        ndiv +=1
    if ndiv == 2:
        print('é primo')
