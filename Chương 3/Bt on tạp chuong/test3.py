import math
n=int(input("n="))
if 2>n or n>1000: 
    print("yêu cầu nhập lại")
n=int(input("n="))

for i in range(2,n+1):
    x=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0: 
            x=1
            break
    if x==0:
        print(i,end=',')