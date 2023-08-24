st='''--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''

L=st.split("\n")
for i in range(len(L)):
    s=' '.join(L[i].split("-"))
    s=' '.join(s.split()) #loại bỏ dấu cách thừa
    print(s)
