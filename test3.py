
def decimal_to_base(decimal, base):
    if decimal == 0:
        return '0'
    result = []
    digits = "0123456789ABCDEF"
    while decimal >0 :
        remainder = decimal % base
        decimal= decimal // base
        if(remainder > 9 ):
            result.append(digits[remainder])
        else:
            result.append(str(remainder))
    result.reverse()
    return ''.join(result)
for i in range(int(input())):
    base = int(input())
    binary = input()
    decimal = int(binary,2)
    result = decimal_to_base(decimal,base)
    print(result)