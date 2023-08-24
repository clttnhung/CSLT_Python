#Yêu cầu xây dựng các hàm sau:
#- Hàm LaSoNguyenTo(x): trả về True nếu x là số nguyên tố, còn lại trả về False;
#- Hàm SoHopLe(x): trả về True nếu x<=1, còn lại trả về False;
#- Hàm NhapVaDem(): thực hiện nhập liên tục các số nguyên cho đến khi số được nhập vào là
#số <=1 thì dừng. Sử dụng hàm SoHopLe(x) ở trên để kiểm tra một số x có <=1 hay không. Sử
#dụng hàm LaSoNguyenTo(x) ở trên để kiểm tra và đếm có bao nhiêu số nguyên đã được
#nhập là số nguyên tố. Kết quả được trả về qua tên hàm.
#- Hàm InKQ(kq): in lên màn hình kết quả theo mẫu sau
import math
def LaSoNguyenTo(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x)+1),1):
        if x%i==0:
            return False
    return True
def SoHopLe(x):
    if x<=1:
        return True
    else:
         return False
def NhapVaDem():
    a=0
    while True:
        x=int(input())
        if SoHopLe(x)==True:
          break
        if LaSoNguyenTo(x)==True:
            a=a+1
    return a
def inkq(a):
    print('Co',a,'so nguyen to')
print('Nhap day so:')
a=NhapVaDem()
inkq(a)

