# step 1: Getting the number of base and expoenent
# step 2: exponent is equal to zero, return 1
# step 3: exponent is less then zero 
# step 4: 1/base * power(base, exponent + 1)
# step 5: base * power(base, exponent -1)
# step 6: print the result

# how to calculate power of a number using Recursion

# x ^ n = x * x * x * ... (n times) .. ^ n 

# step 1: Recursive case - the flow

# 2 ^ 4 = 2 * 2 * 2 * 2

# x^a x^b = x ^ a+b 

# x^3 * x^4 = x^ 3+4

# x^n = x * x^n-1

# step 2: Base case - the stopping criterion

# n = 0

# step 3: Unintentional case - the constraint

# power(-1,2) ??
# power(3.2,2) ??
# power(2,1.2) ??
# power(2,-1) ??

def power(base, exponent):
    assert int(exponent) == exponent, 'The exponent must be integer number only'  # power(2,1.2) ??
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * power(base, exponent + 1)
    return base * power(base, exponent - 1)

print(power(2, 3))
