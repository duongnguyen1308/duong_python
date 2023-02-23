def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

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
    decimal = binary_to_decimal(binary)
    result = decimal_to_base(decimal,base)
    print(result)