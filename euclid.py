# Euclidean Algorithm
# ksnt

def gcd(a,b):
    if a % b == 0:
        print(b)
    else:
        if a >= b:
            c = a % b
            gcd(b,c)
        elif a < b:
            c = b % a
            gcd(a,c)
