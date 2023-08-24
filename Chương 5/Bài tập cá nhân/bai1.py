#Viết chương trình có sử dụng hàm thực hiện các yêu cầu sau:
#- Hàm Input(): nhập một số nguyên n (n>0) và n số nguyên lưu vào List L, và một số nguyên x;
#- Hàm FirstAndLast(L) trả về và in lên màn hình List mới chỉ gồm phần tử đầu tiên và cuối cùng của L;
# Hàm Search(L,x): xác định x có nằm trong L hay không. Trả về True nếu tìm thấy, còn lại trả về False.

def Input():
 n=int(input('n='))
 L=[]
 M=[]
 for i in range(1,n+1):
    a=int(input())
    L=L+[a]
 x=int(input('x='))
 return n,L,x
def FirstAndLast(L):
    print('[',L[0],', '+L[-1],']')
def Search(L,x):
        if x in L:
            print(True)
        else:
            print(False)
n,L,x=Input()
FirstAndLast(L)
Search(L,x)

      