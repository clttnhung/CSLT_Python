# Viết chương trình:
# Cho phép nhập vào một chuỗi là các số nhị phân 4 chữ số, phân tách bởi dấu phẩy;
# Chương trình kiểm tra xem các số nhị phân trên có chia hết cho 3 không. 
# In lên màn hình dãy số nhị phân chia hết cho 3, nếu có nhiều số thì mỗi số cách nhau bởi 1 dấu phẩy


n=input()
L=n.split(',')
M=[]
for i in L:
    if int(i,2)%3==0:
        M=M+[i]
m=','.join(M)
print(m,end='')