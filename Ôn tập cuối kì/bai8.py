n=int(input())
if n!=0:
    L=[]
    for i in range(n):
     a=input()
     L+=[a]
    max=len(L[0])
    imax=0
    for i in range(len(L)):
      if len(L[i])>max:
        imax=i  
else:
    print(None)
print(L[imax])
print(len(L[imax]))


