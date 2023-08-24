#Viet chuong su dung thuc hien cac yeu cau sau
#Ham LaSoDUong(x): hafm ktra so nguyen x, neu x<=o thi tra ve 0, con lai tra ve 1
#Ham Xulu(): Nhap tu ban phim n so nguyen, tra ve luong so nguyen duong va chan
#Ham InKq(soluong): in len man hinh gia tri bien soluong

def Nhap():
    n=int(input('n='))
    return n
def LaSoDuong(x):
    if x>0 and x%2==0:
        return 1
    else:
        return 0
def Xuly(n):
    dem=0
    for i in range(1,n+1):
        x=int(input())
        if LaSoDuong(x)==1:
            dem=dem+1
    return dem
def InKQ(soluong):
    print('Co',soluong,'so nguyen duong va chan')

n=Nhap()
soluong=Xuly(n)
InKQ(soluong)
