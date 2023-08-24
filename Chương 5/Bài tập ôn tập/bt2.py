#Hàm search(L, x) tìm x trong List L, nếu tìm thấy thì trả về index của x trong L, còn lại trả về None
L=[1,2,3,4,5,6,7,8]
x=int(input('x='))
def seach(L,x):
    k=0
    if x in L:
        for i in L:
            if i!=x:
                k=k+1
            else:
                break
        return k
    else:
        return None
print(seach(L,x))

