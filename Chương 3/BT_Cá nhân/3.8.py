#Nhập vào một ký tự bất kỳ và một số nguyên n (1<=n<=20), chương trình in lên màn hình trang trí
#theo cấu trúc bên dưới.
a=input()
n=int(input())
i=1
if 1<=n<=20:
 while i<=n:
    j=1
    while j<=i:
        if j==i:
            print (a,end='')
        else:
          print(a,end=' ')
        j=j+1
    print()
    i=i+1