import math 
n=x=int(input('n='))
i=n
while i>=1:
   for i in range(2,int(math.sqrt(n)+1),1):
        if n%i==0:
            print()
            continue;
   else:
      print(i)  
      continue;   
i=i-1
 
 

   