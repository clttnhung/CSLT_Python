L=input().split()
M=[]
N=[]
for i in L:
    if int(i)%2!=0:
        M=M+[int(i)]
    else:
        N=N+[int(i)]
print(M)
print(N)