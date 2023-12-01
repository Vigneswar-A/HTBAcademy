def gcd(a, b):
    if b > a:
        return gcd(a, b)
    if b <= 1:
        return a
    return gcd(b, a%b)
print(gcd(66528, 52920))