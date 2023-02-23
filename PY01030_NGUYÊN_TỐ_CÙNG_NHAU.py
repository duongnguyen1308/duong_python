import math
n,k=(int(x) for x in input().split())
a=10**(k-1)
b=10**k
tong=1
for i in range(a,b):
		if math.gcd(i,n)==1:
			print(i,end=' ')
			if tong%10==0:print()
			tong+=1