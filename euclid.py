# Euclidean Algorithm
# ksnt

def gcd(a,b):
    #try:
    #    a % b
    #except ZeroDivisionError:
    #    print("Oops!  You should use not 0 for arguments.  Try again...!")
    if a == 0 or b == 0:
        return("Do not use 0 for arguments!")
    if a % b == 0:
        print(b)
    else:
        if a >= b:
            c = a % b
            gcd(b,c)
        elif a < b:
            c = b % a
            gcd(a,c)
