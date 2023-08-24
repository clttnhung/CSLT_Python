a=int(input('yrs0fservice = '))
b=int(input('salary = '))
bonus = 0
M1=int(input('M1= '))
M2=int(input('M2= '))
M3=int(input('M3= '))
if a<5:
    if b<500:
        bonus = M1
    else:
        bonus = M2
else:
 bonus = M3
print('Bonus amount: ',bonus)
