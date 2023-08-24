#Viết chương trình thực hiện tính n!
#Biết rằng: n! = n*(n-1)!
#Và: 0! = 1
#Yêu cầu xây dựng các hàm sau:
#- Hàm nhap(), thực hiện việc nhập một số nguyên dương n từ bàn phím.
#- Hàm giaithua(n), tính và trả về kết quả của phép tính n!
#- Hàm inkq(n,X), thực hiện in lên màn hình kết quả của n!



def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    X=1
    if n==0:
       X=1
    if n>=1:
      for i in range(1,n+1):
       X=X*i
    return X
def inkq(n,X):
    print(str(n)+'!='+str(X))
n=nhap()
X=giaithua(n)
inkq(n,X)
