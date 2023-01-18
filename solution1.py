# Write code for algorithm 1 below
def count_down(n):
    if n < 0:
        return
    elif n == 0:
        print(n)
        return
    else:
        print(n)
        count_down(n - 1)

count_down(30)