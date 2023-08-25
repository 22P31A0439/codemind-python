N = int(input())
a = 0
while True:
    r = N%10
    N = N//10
    a = a*10+r
    if (N==0):
      break
print(a)