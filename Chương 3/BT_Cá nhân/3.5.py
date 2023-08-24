#Viết chương trình sử dụng cấu trúc if thực hiện các yêu cầu sau:
#- Nhập vào Số ngày nghỉ của nhân viên
#- Thực hiện Xếp loại nhân viên dựa vào Số ngày nghỉ theo quy tắc:
# Nếu không nghỉ ngày nào thì: “Xếp loại A”
# Nếu Số ngày nghỉ dưới 2 ngày thì: “Xếp loại B”
# Nếu Số ngày nghỉ dưới 4 ngày thì: “Xếp loại C”
# Còn lại “Xếp loại D”
a=int(input())
if a==0:
     print('Xep loai A')
elif a<2:
    print('Xep loai B')
elif a<4:
    print('Xep loai C')
else:
    print('Xep loai D')