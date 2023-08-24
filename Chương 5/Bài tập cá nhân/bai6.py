#Viết chương trình nhập vào từ bàn phím 10 số nguyên và lưu vào một List A. Hãy hoán đổi giá trị
#của 2 phần tử nằm cạnh nhau (theo từng đôi) trong List. Và in lên màn hình List kết quả sau khi xử lý.
#Gợi ý: 
#- Để hoán đổi giá trị theo cặp phần tử, sử dụng thêm List B để lưu trữ tập kết quả
# Cho vòng lặp i=0.. (n-2) step=2
# B[i]=A[i+1]
# B[i+1]=A[i]

A=[]
B=[]
for i in range(10):
 a=int(input())
 A=A+[a]
 B=A.copy()
for i in range(0,10,2):
    B[i]=A[i+1]
    B[i+1]=A[i]
for i in B:
    if i==B[-1]:
        print(i,end='')
    else:
        print(i,end=' ')   
