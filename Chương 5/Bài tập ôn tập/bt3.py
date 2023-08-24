#Hàm delete(L,x) xóa tất cả phần tử có giá trị bằng x trong List L.
L=[1,2,3,4,5,6]
x=int(input('x='))
def delete(L):
    M=[]
    for i in L:
        if i!=x:
         M=M+[i]
    return M
print(delete(L))
