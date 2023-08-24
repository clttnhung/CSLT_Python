#Nhập vào số nguyên n (2<=n<=50), in lên màn hình các số nguyên chẵn đầu tiên.
#Ví dụ: nếu nhập vào n=10 thì dãy số được in trên màn hình như sau (trong dãy số, mỗi số cách nhau 1
#dấu cách):
#10
#2 4 6 8 10
n=int(input())
for i in range(2,n+1,1):
    if i%2==0:
        print(i, end=' ')