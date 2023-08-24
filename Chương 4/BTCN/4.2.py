#Viết chương trình nhập từ bàn phím một số nguyên n (n>=2),in lên màn hình các số nguyên
#chẵn trong n số tự nhiên đầu tiên.
#Yêu cầu xây dựng các hàm sau:
#- Hàm nhap(),thực hiện việc nhập một số nguyên dương n;
#- Hàm inkq(n),thực hiện in lên màn hình các số nguyên chẵn trong n số tự nhiên đầu tiên;
#- Chương trình có thể lặp lại các công việc trên cho đến khi bấm phím k hoặc K thì kết
#thúc.
from calendar import c


def nhap():
    n=int(input('n='))
    return n
def inkq(n):
    for i in range(1,n+1):
        if i%2==0:
             print(i,end=' ')             
while True:
 n=nhap()
 inkq(n)
 c=str(input('\nTiep tuc khong?')) 
 if c=='k' or c=='K':
     break