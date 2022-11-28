# step 1: Getting a number which is positive integer, but not less then 0
# step 2: if the number is greater than or equal to 0
# step 3: number = number plus function number minus 1
# step 4: print the number

def sumofdigit(number):
    assert number >= 0 and int(number) ==  number, 'The number must be a positive integer!'
    if number in [0,1]:
        return 1
    else:
        return number + sumofdigit(number - 1)

print(sumofdigit(5))
