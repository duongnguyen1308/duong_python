t=int(input())
def check(s) :
	for i in s:
		if i!='4' and i!='7' : return False
	return True	
for i in range(t):
	s=input()
	if check(s)== True : print("YES")
	else :	print("NO")
