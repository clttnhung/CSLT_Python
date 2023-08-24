 #Hệ thống Elearning của Trường Đại học Kinh tế, Đại học Đà Nẵng cho phép người dùng đổi mật 
#khẩu khi cần thiết. Để đảm bảo tính an toàn và bảo mật thông tin cho sinh viên, hệ thống yêu cầu mật 
#khẩu phải được đáp ứng các yếu tố an toàn. Bạn hãy viết chương trình để thực hiện kiểm tra tính hợp lệ 
#của mật khẩu mà người dùng nhập vào. Biết rằng, chính sách mật khẩu được quy định như sau:
#- Ít nhất 1 chữ cái nằm trong [a-z]
#- Ít nhất 1 số nằm trong [0-9]
#- Ít nhất 1 kí tự nằm trong [A-Z]
#- Ít nhất 1 ký tự nằm trong [$ # @]
#- Độ dài mật khẩu tối thiểu: 6 ký tự
#- Độ dài mật khẩu tối đa: 17 ký tự

n=input()
if len(n)<=6 or len(n)>=17 or n.isalnum() or n.isupper() or n.islower():
    print(False)
else:
    print(True)