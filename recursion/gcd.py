# GCD ( Greatest Commmon Divisor)

# step 1: Recursive case - the flow
#   GCD is the largest positive integer that divides the numbers without a remainder

# gcd(8,12) = 4                   Euclidean Algorithm 
#                                 gcd(48,18)    
# 8 = 2 * 2 * 2                   step 1: 48/18 = 2 remainder 12
# 12 = 2 * 2 * 3                  step 2: 18/12 = 1 remainder 6
#                                 step 3: 12/6 = 2 remainder 0

# gcd(a,o)=a 
# gcd(a,b) = gcd(b,a mod b)

# step 2: Base case - the stopping criterion

#     b = 0

# step 3: Unintentional case - the constraint

#     Positive integers
#     Convert negative numbers to positive

def gcd(a, b):
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(24, 3))
    