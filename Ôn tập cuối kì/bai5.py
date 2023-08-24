#loại bỏ kí tự hong mong mún
n=list(input())
L=[]
for i in n:
    if i!='^' and i!='*':
        L+=i
L=''.join(L)
print(L)

