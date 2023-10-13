n = int(input())
a = list(map(int,input().split()))
x = int(input())
s=0
for i in a:
    if i==x:
        print("True")
        break
    else:
        s=s+1
if s==n:
    print("False")
  