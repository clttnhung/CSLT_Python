#Hàm update(L, x, y) tìm x trong List L và thay thế bằng y
L=[1,2,3,4,5,6]
x=int(input('x='))
y=int(input('y='))
def update(L,x,y):
    k=0
    M=[]
    for i in L:
        if i!=x:
         M=M+[i]
    for i in L:
        if i!=x:
            k=k+1
        else:
            break
    M=M[:k]+[y]+M[k:]
    return M
print(update(L,x,y))
     

