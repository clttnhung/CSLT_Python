#Mã code có dạng:XXXX.XXXX.XXXX
#Xóa các chữ A ở đầu 1 chuỗi sau dấu chấm
# Input: BEF.ASBDAAA.ACACAAC
# Output: BEF.SBCDAAA.CACAC

#C1
#L=input()
#L='.'.join(L.split('.A'))
#print(L)

#C2
L=input()
L=L.replace('.A','.')
print(L)