#loai tu trung lap

L=input().split()
M=''
for i in L:
    if i not in M:
        M=M+i+' '
M=(''.join(M)).split()
print(M)

