# Nhập từ bàn phím một số nguyên n
# Nhập liên tục n số nguyên và lưu tữ vào 1 list
# Đếm và in lên màn hình số lượng các số chẵn trong List trên

def Nhap():
    n=int(input('n='))
    L=[]
    print('Moi nhap n so nguyen:')
    for i in range(n): 
        x=int(input)
        L=L+[x]
    return L
def Dem(L):
    dem=0
    for x in L: #Duyet cac phan tu trong list
        if x%2==0:
            dem=dem+1
    return dem
def InKQ(kq):
    print('co','kq','so chan')
L=Nhap()
kq=Dem(L) 
InKQ(kq)

        

