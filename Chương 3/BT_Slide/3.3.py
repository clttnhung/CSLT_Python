#Nhập vào số KW điện tiêu thụ của một hộ
#gia đình, sau đó in lên màn hình số tiền mà hộ gia
#đình đó phải trả biết rằng cách tính tiền điện như
#sau:
#- Từ KW 1 đến KW thứ 100: giá 550 đ/1KW
#- Từ KW 101 đến KW thứ 150: giá 750 đ/1KW
#- Từ KW 151 đến KW thứ 200: giá 950 đ/1KW
#- Từ KW 201 trở đi: giá 1350 đ/1KW
#- Thuế VAT là 10%.
#Thành tiền = Số KW tiêu thụ * Đơn giá + VAT
a=float(input('Tieu thu='))
if 1<=a<=100:
    print("Phai tra="+str(a*550+a*550*0.1))
if 101<=a<=150:
   print("Phai tra="+str(100*550+(a-100)*750+0.1*(100*550+(a-100)*750)))
if 151<=a<=200:
    print("Phai tra="+str(100*550+50*750+(a-150)*950+0.1*(100*550+50*750+(a-150)*950)))
if a>=201:
 print("Phai tra="+str(100*550+50*750+50*950+(a-200)*1350+0.1*(100*550+50*750+50*950+(a-200)*1350)))