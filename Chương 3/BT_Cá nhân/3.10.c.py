#In lên màn hình n dòng, với mỗi dòng là một dãy số từ 1 đến n (mỗi số nhau 1 dấu cách).
n=int(input('n='))
i=1
while i<=n:
    j=1
    while j<=n:
        print(j,end=' ')
        j=j+1
    print()
    i=i+1