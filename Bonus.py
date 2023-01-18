def greatest_common_divisor(x, y):
    # base case
    if y == 0:
        return x
    # recursive case
    else:
        return greatest_common_divisor(y, x % y)

print(greatest_common_divisor(5, 10))
print(greatest_common_divisor(81, 18))
print(greatest_common_divisor(23, 199))