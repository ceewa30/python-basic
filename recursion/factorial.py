# step 1: the number should be a positive integer and greater than 0
# step 2: if the number is greater then or equal to 0
# step 3: return 1
# step 4: number multiple by function number minus 1


def factorial(n):
    assert n >=0 and int(n) == n, 'The number must be a positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num-1)
