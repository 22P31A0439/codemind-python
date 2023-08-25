p,r,t = map(int,input().split())
T = p*pow((1+r/100),t)
print(f"{T:.2f}")