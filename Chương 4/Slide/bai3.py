#Viết chương trình sử dụng hàm, in lên màn hình các số nguyên tố nằm trong dãy số từ 2 đến n.
#-          Nhap(): nhập vào 1 số nguyên n (n>=2)
#-          LaSNT(x): kiểm tra số nguyên x có phải là số nguyên tố hay không, nếu là số nguyên tố thì trả về true, còn lại trả về số false
#          InKQ(n): in lên màn hình các số nguyên tố nằm trong dãy số từ 2 đến n.
#Gợi ý:
#     Sử dụng vòng lặp x=1..n
#Sử dụng hàm LaSNT(x) để kiểm tra x có phải là SNT hay không, nếu đúng thì in x lên màn hình.
def Nhap():
   n=int(input("n="))
   n>=2
   return n 
def LaSNT(x):
    for i in range(2,x):
        if x%i==0:
            return False 
    return True 
def InKQ(n):
    for i in range(2,n+1):
        if LaSNT(i):
            print(i,end=" ")
n=Nhap()
InKQ(n)