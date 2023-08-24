import math
n=int(input("n="))
 
x=0 #Biến cờ / Biến trạng thái
for k in range(2,int(math.sqrt(n))+1):    #k=2..(n-1)
    if n%k==0:
        x=1
        break
 
if x==1:
    print(n,"khong la SNT!!!")
else:
    print(n,"la SNT!!!")

   
 