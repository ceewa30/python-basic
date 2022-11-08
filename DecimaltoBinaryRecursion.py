# Step 1: Recursive case - the flow

# step: 1 Divide the number by 2
# step 2: Get the integer quotient for the next iteration 
# step 3: Get the remainder for the binary digit 
# step 4: Repeat the steps until the quotient is equal to 0 

# 10 to binary

# Division by   Quotient  Remainder

# 10/2             5          0
# 5/2              2          1       101 * 10 + 0 = 1010  = > f(n) =  n mod 2 + 10 * f(n/2)
# 2/2              1          0     10 * 10 + 1 = 101
# 1/2              0          1   1 * 10 + 0 = 10

def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only!'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(13))
