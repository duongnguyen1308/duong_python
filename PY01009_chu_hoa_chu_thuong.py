s=input()
chuhoa=chuthuong=0
for i in s:
	if i.isupper() : chuhoa+=1
	else :chuthuong+=1
if chuthuong<chuhoa :print(s.upper())
else :print(s.lower())
		
