st='''--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''

L=st.split("\n")
s=''
for i in range(len(L)):
    if i ==0 or i in ['-',' ']:
        s+=L[i]
s=' '.join(s)
print(s)

