#Nhập vào một dãy các số nguyên tùy ý, cho đến khi bấm số 0 thì kết thúc nhập. Cho biết có bao
#nhiêu số âm và bao nhiêu số dương đã được nhập vào trong dãy số trên.
n=int(input())
a=0
b=0
while n!=0:
    n=int(input())
    if n>=0:
        a=a+1
    if n<0:
        b=b+1
print(a,'so duong')
print(b,'so am')
