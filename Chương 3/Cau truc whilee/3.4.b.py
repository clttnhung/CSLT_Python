i=0
j=0
while i<9:
    while j<18:
        if(j<9-i or j>9+i):
            print(' ', end='')
        else: 
            print('*', end = '')
        j=j+1
    print()
    j=0
    i=i+1
    
       