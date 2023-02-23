import math
for i in range(int(input())):
    s=input()
    t=s[::-1]
    if math.gcd(int(s),int(t))==1 :print("YES")
    else:print("NO")