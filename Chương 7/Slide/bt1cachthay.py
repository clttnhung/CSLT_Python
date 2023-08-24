#Viết chương trình nhập vào một xâu ký tự st1
#Nhập vào 1 xâu st2, kiểm tra nếu st2 xuất hiện trong xâu st1 thì yêu cầu nhập lại xâu khác, còn lại thì dừng lại.(Không phân chữ hoa hay thường)
st1=input().upper()
while True:
    st2=input().upper()
    if st2 not in st1:
        break