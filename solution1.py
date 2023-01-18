# Write code for algorithm 1 below
def count_down(n):
    # error case
    if n < 0:
        print('No negative numbers!')
        return
    # base case
    elif n == 0:
        print(n)
        return
    # recursive case
    else:
        print(n)
        count_down(n - 1)

count_down(30)