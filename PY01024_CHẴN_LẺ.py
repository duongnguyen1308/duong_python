def check(s):
    n=int(s)
    tong=0
    while(n>0) :
        tong+=n%10
        n=int(n/10)
    if tong%10!=0 : return False
    for i in range(1,len(s)):
        if abs(int(s[i])-int(s[i-1]))!=2 : return False
    return True

    if  check(s)==True :print("YES")
    else:print("NO")             