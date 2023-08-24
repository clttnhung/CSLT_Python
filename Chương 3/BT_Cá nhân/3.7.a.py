#Viết chương trình thực hiện tính n!
#Biết rằng: n!=n*(n-1)!
#0!=1
#a. Sử dụng vòng lặp while
#Trong đó:
# n được nhập vào từ bàn phím
# Chương trình có thể lặp lại việc nhập giá trị n và tính n!, cho đến khi n<0 thì dừng.
n=int(input())
s=1
while n>=0:
 if n==0:
  print(1)
 elif n>0:
    while n>0:
      s=s*n
      n=n-1
    print(s)
    s=1
 n=int(input())
  


    












    

