#xóa index
L=input().split()
M=''
for i in range(len(L)):
    if i!=1 and i!=3 and i!=4:
        M=M+L[i]+' '
M=M.split()
print(M)