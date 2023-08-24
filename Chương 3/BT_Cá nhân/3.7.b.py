#Viết chương trình thực hiện tính n!
#Biết rằng: n!=n*(n-1)!
#0!=1
#b. Sử dụng vòng lặp for
#Trong đó:
# n được nhập vào từ bàn phím
# Chương trình có thể lặp lại việc nhập giá trị n và tính n!, cho đến khi n<0 thì dừng.
n=int(input())
while n>=0:
 if n==0:
    print(1)
 elif n>0:
      s=1
 for i in range(1,n+1):
    s=s*i
 print(s)
 s=1
 n=int(input())




 



