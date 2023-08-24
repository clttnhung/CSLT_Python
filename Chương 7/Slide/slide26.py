#Viết chương trình nhập vào mật khẩu là một chuỗi ký tự chỉ bao gồm
#chữ cái và chữ số, chương trình kiểm tra và yêu cầu nhập lại cho đến khi hợp lệ.
while True:
    print('Select a new password (letters and numbers only):')
    password=input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')
