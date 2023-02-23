import math
def check(n):
	if n<2 : return False
	for i in range(2,int(math.sqrt(n))+1):
		if(n%i==0) : return False
	return True
t=int(input())
for i in range(t):
	n=int(input())
	count=0
	for i in range(1,n) :
		if math.gcd(i,n)==1: count+=1
	if check (count)== True : print("YES")
	else : print("NO")	