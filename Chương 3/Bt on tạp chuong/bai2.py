import math 
n=int(input('n='))
if n<2:
    print(n,'khong la SNT')
else:
    for i in range(2,int(math.sqrt(n)+1),1):
        if n%i==0:
            print(n,'khong la SNT')
            break
    else:    
     print(n,'la SNT')    

