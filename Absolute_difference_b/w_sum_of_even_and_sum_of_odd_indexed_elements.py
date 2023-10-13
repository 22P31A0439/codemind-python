n = int(input())
a = list(map(int,input().split()))
p = 0
q = 0
for i in range(0,n):
    if (i%2==0):
        p = p + a[i]
for j in range(0,n):
    if (j%2==1):
        q = q + a[j]
s = p - q
print(s)