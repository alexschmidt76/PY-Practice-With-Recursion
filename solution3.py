# Write code for algorithm 3 below
def fibonacci_sequence(n):
    # error case
    if n <= 0:
        print('Input must be greater than zero.')
    # base cases
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # recursive case
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

print(fibonacci_sequence(-9))
print(fibonacci_sequence(1))
print(fibonacci_sequence(30))