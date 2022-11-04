from tkinter import N

from symbol import flow_stmt


# how to calculate power of a number using Recursion

# x ^ n = x * x * x * ... (n times) .. ^ n 

# step 1: Recursive case - the flow

# 2 ^ 4 = 2 * 2 * 2 * 2

# x^a x^b = x ^ a+b 

# x^3 * x^4 = x^ 3+4

# x^n = x * x^n-1

