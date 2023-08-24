#Viết chương trình nhập vào một số nguyên n (n>0), và n số nguyên lưu trữ vào List A. In lên màn 
#hình: tổng giá trị của các phần tử ở vị trí có thứ tự chẵn trong List A (biết rằng phần tử thứ 1 có số chỉ 
#mục là 0 sẽ có thứ tự là 1, …)
#Gợi ý: Để xác định phần tử ở vị trí chẵn, sử dụng cấu trúc lặp i=0..(n-1), nếu i lẻ tức là phần tử đó ở vị trí chẵn.


n=int(input('n='))
A=[]
s=0
for i in range(0,n):
 a=int(input())
 A=A+[a]
 if i!=0 and i%2!=0:
  s=s+A[i]
print('Tong='+str(s))
