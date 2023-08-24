#input: Red Green Black
# Blue
#output: cac phan tu chung tu hai danh sach tren

st=input()
L=st.split()
m=input()
for i in range(len(L)):
 L.insert((i-2),m)
print(L)
