# Fermat's Test
# ksnt

# Note: It is known that this way is not perfect.

def fermat_test(n):
    if n <= 1:
        print("Please input the number over 2.")
        return
    for i in range(1,n):
        if (i ** n) % n != i:
            print("Not prime number.")
            return
    print("Prime number.")
