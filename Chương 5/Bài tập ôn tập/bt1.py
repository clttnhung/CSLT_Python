#Hàm add(L, x, k) thêm phần tử x vào List L tại vị trí k, nếu k lớn hơn số phần tử của L thì thêm x vào cuối L
L=[1,2,3,4,5,6,7,8]
x=int(input('x='))
k=int(input('k='))
def add(L,x,k):
    if k>len(L):
        L=L+[x]
    else:
        L=L[:k]+[x]+L[k:]
    return L
print(add(L,x,k))
