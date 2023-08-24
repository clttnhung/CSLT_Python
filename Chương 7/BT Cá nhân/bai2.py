#Viết chương trình:
#- Cho phép nhập vào một chuỗi ký tự bất kỳ;
#- Chương trình thực hiện làm sạch chuỗi ký tự trên. Biết rằng một chuỗi được gọi là “sạch” nếu: 
# Không bắt đầu và kết thúc bằng các ký tự trắng;
# Mỗi từ chỉ được cách nhau bằng đúng 1 ký tự trắng;
# Chỉ được phép viết hoa chữ cái đầu tiên của chuỗi;
# Trước các dấu câu (phẩy, chấm phẩy, hai chấm, chấm) không có ký tự trắng;

n=input().lower().capitalize()
L=n.split()
for i in range(len(L)):
    L=' '.join(n.split())
dauphay=n.find(',')
L=L[:dauphay-1]+L[dauphay:]
print(L)



