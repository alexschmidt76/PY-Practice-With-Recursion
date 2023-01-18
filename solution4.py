# Write code for algorithm 4 below
def a_to_b(a, b):
    # error case
    if b < 0:
        print('b must be greater than zero')
        return
    # base cases
    if b == 0: 
        return 1
    if b == 1:
        return a
    # recursive case
    return a * a_to_b(a, b - 1)

print(a_to_b(2, 3))
print(a_to_b(3, 16))
print(a_to_b(15, 0))
print(a_to_b(4, -9))