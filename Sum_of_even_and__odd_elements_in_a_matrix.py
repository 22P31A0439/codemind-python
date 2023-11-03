r,c = map(int,input().split())
mat = []
s = 0
f = 0
for k in range(r):
    a = list(map(int,input().split()))
    mat.append(a)
for i in mat:
    for j in i:
        if j%2==0:
            s = s+j
        else:
            f = f+j
print(s,f,end = "")