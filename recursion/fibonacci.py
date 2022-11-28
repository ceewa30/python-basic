def fibonacci(number):
    assert number >= 0 and int(number) == number, 'Fibonacci must be a integer number!'
    if number in [0,1]:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(10))