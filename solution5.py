# Write code for algorithm 5 below
def is_palindrome(string):
    # base case
    if len(string) == 1 or len(string) == 0:
        return True
    # recursive case
    return (string[0] == string[-1]) and is_palindrome(string[1:-1])

print(is_palindrome('racecar'))
print(is_palindrome('sara'))
print(is_palindrome('g'))