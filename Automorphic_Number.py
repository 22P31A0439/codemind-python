n = int(input())
x = len(str(n))
sq = n*n
q = sq
r = q%(10**x)
if r == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")