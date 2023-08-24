#tìm số nguyên tố lớn nhất khác n
import math
a=int(input())
n=a-1
i=1
for i in range(2,int(math.sqrt(n))+1):    #k=2..(n-1)
    if n%i==0:
        n=max
    print(max)
