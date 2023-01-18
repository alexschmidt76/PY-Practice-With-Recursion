# Write code for algorithm 2 below
def natural_numbers(n, i=1):
    # error case
    if n < i:
        print(f'Number must be larger than {i - 1}')
    # base case
    elif i > n:
        return
    # recursive case
    else:
        print(i)
        natural_numbers(n, i + 1)

natural_numbers(5)