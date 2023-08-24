# Nhập từ bàn phím một số nguyên n (n>0), và n số nguyên lưu trữ vào một List.
#In lên màn hình: 
#- Số lượng các số nguyên DƯƠNG
#- Trung bình cộng của các số nguyên chẵn được lưu trữ trong List trên

n=int(input('n='))
L=[]
k=0
tong=0
m=0
for i in range(1,n+1):
 a=int(input())
 L=L+[a]
 if a>0:
    k=k+1
 if a%2==0:
    tong=tong+a
    m=m+1
 if m==0:
   h=0
 else:h=tong/m
print('SND='+str(k))
print('TBC='+str(h))



