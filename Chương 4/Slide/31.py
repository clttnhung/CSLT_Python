#Sử dụng hàm để thực hiện các yêu cầu sau:
#Nhập liên tục từ bàn phím một số nguyên n:
#Hàm Nhap()
#Nhập liên tực từ bàn phím n số nguyên
#Đếm và in lên màn hình có bao nhiêu chữ số chẵn đã được nhập vào
#Hàm NhapVaDem(n)
#Hàm InKQ(kq)
def Nhap():
    n=int(input('n='))
    return n
def NhapVaDem(n):
    print('Nhap',n,'so nguyen')
    dem=0
    for i in range(1,n+1):
        x=int(input())
        if x%2==0:
            dem=dem+1
    return dem
def InKQ(kq):
    print('So chu so chan la:',kq)
n=Nhap()
kq=NhapVaDem(n)
InKQ(kq)