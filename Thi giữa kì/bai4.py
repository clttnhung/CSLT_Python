n=int(input())
i=1
dem=0
while i<=n:
    if i%2==0 and i%3==0:
        dem=dem+1
    i=i+1
print(dem)