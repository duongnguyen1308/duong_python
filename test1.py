n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if len(b) == 0:
        b = b + [i]
        print('buoc1',b)
    else:
        if (b[-1] + i) % 2 == 0:
            b.pop()
            print('buoc2',b)
        else:
            b = b + [i]
            print('buoc3',b)
print(len(b))