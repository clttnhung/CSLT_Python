def LaSoNguyenTo(x):
    checkNum = int(1)
    if x < 2:
        checkNum = 0
    else:
        for i in range(2, x):
            if x % i == 0:
                checkNum = 0
    if checkNum == 1:
        return True     
    else:
        return False

def SoHopLe(x):
    if x <= 1:
        return True
    else:
        return False

def NhapVaDem():
    y = int(0)
    while True:
        x = int(input('Nhap so: '))
        if SoHopLe(x) == True:
            break
        else:
            if LaSoNguyenTo(x) == True:
                y += 1
    return y

a = NhapVaDem()
print(a)