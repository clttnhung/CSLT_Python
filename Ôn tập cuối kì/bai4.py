#in phần tử trùng nhau
L=input().split()
M=input().split()
N=''
for l in range(len(L)):
    for m in range(len(M)):
        if L[l]==M[m]:
            N+=L[l]+' '
N=N.split()
print(N)