import math
def nto(s):
    if s<2 :return False
    for i in range(2,int(math.sqrt(s))+1) :
        if s%i==0 : return False
    return True    
def tongchuso(n):
    tong=0
    while(n>0) :
        tong+=n%10
        n=int(n/10)
    return tong      
t=int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    s=math.gcd(n,k) 
    if nto(tongchuso(s))==True : print("YES")
    else : print("NO")  
