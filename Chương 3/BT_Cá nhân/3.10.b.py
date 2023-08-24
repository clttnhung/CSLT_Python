#In lên màn hình dãy số từ 1 đến n, với điều kiện mỗi dòng có tối đa 5 chữ số (mỗi số nhau 1 dấu cách).
n=int(input('n='))
i=1
a=0
while i<=n:
    print(i, end=' ')
    a=a+1
    if a%5==0:
        print()
    i=i+1
    
        