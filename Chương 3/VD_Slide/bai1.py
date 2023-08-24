n=int(input('n='))
S=1
if n==0:
    S=1
if n>=1:
    for i in range(1,n+1):
     S=S*i
print(str(n)+'!='+str(S))