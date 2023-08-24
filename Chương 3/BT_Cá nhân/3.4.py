 #Viết chương trình sử dụng cấu trúc if thực hiện yêu cầu sau:
#- Nhập vào điểm thi lần lượt của 3 môn: Toán, Lý và Hoá
#- Tính điểm trung bình, biết rằng: Toán có hệ số 2, Lý hệ số 3;
#- Thực hiện xếp loại cho học sinh trên với điều kiện:
#ĐTB <3 thì xếp loại Kém
#3<= ĐTB <5 thì xếp loại Yếu
#5<= ĐTB <6 thì xếp loại Trung bình
#6 <= ĐTB < 7 thì xếp loại Trung bình Khá
#7 <= ĐTB < 8 thì xếp loại Khá
#8 <= ĐTB < 9 thì xếp loại Giỏi
#9 <= ĐTB < 10 thì xếp loại Xuất sắc
#In lên màn hình: kết quả xếp loại của học sinh
toan=float(input())
ly=float(input())
hoa=float(input())
d=float((toan*2+ly*3+hoa)/6)
if d<3:
    print('Kem')
elif 3<=d<5:
    print('Yeu')
elif 5<=d<6:
    print('Trung binh')
elif 6<=d<7:
    print('Trung binh Kha')
elif 7<=d<8:
    print('Kha')
elif 8<=d<9:
    print('Gioi')
elif 9<=d<10:
    print('Xuat sac')
