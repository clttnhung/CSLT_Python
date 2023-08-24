#n nhaf so 1->n ,trai la so le, phai chan, nham so ben trai.
n=int(input())
i=1
s=0
while i<=n:
    if i%2!=0:
        s=s+i
    i=i+1
print(s)