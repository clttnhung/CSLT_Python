#Công ty điện lực quy định tiền điện hàng tháng như sau:
#- Mức 1: mỗi chữ điện trong 100 Kw đầu, có đơn giá M1 VNĐ/Kw;
#- Mức 2: mỗi chữ điện từ Kw 101 đến 150, có đơn giá M2 VNĐ/Kw;
#- Mức 3: mỗi chữ điện từ Kw 151 trở lên, có đơn giá M3 VNĐ/Kw;
#Viết chương trình nhập vào M1, M2, M3 và số điện năng tiêu thụ S. Hãy tính và
#in lên màn hình số tiền điện phải trả. Chương trình nhập xuất theo mẫu bên
m1=int((input('M1=')))
m2=int((input('M2=')))
m3=int((input('M3=')))
s=int((input('S=')))
if 0<=s<=100:
    print('Phai tra='+str(m1*s))
elif 101<=s<=150:
    print('Phai tra='+str((m1*100+(s-100)*m2)))
else:
    print('Phai tra='+str((m1*100+m2*50+(s-150)*m3)))
