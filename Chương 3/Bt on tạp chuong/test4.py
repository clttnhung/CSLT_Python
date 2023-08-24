a = int(input('Nhap a: '))
b = x = int(0)
for i in range(2, a+1, 1):
    
    for j in range(2, i , 1):
        if(i % j == 0):
            x = 1
            break;
    if x == 0:        
        if b != 0:
            print(', ', end = '')
        print(i, end = '')
        b = 1 
    x = 0