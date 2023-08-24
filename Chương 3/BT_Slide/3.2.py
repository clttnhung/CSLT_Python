# Một hãng máy tính có chính sách khuyến
#mại, cứ mua từ 5 máy trở lên thì giá một máy sẽ là
#450$ còn không thì giá một máy sẽ là 500$. Viết
#chương trình yêu cầu người dùng nhập vào số máy
#muốn mua, sau đó in ra màn hình số tiền người đó
#phải trả cho hãng.

a=int(input('So may='))
if a>=5:
    print('So tien='+str(a*450))
else:
    print('So tien='+str(a*500))
