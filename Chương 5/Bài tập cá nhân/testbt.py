A = []
B = []
for i in range(10):
    a = int(input())
    A += [a]
    B += [a]
for i in range(0, 8, 2):
    B[i] = A[i+1]
    B[i + 1] = A[i]
print(B)
