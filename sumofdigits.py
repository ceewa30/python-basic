# How to find the sum of digits of a  positive number using recursion?

# step 1: Recursive case - the flow
# 10 is  10/10 = 1 and remainder = 0

# 54 is 54/10 = 5 and remainder = 4
# 112 is 112/10 = 11 and remainder = 2
#         11/10 = 1 and remainder = 1

# f(n) = n%10 + f(n/10)

# steip 2: Base case - the stopping criterion
# n = 0

def sumofdigit(n):
    assert n >=0 and int(n) == n , 'Sum of Digit cannot be negative number.'
    if n == 0:
        return n
    else:
        return int(n%10) + sumofdigit(int(n/10))

print(sumofdigit(-10))