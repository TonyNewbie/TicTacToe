digits = input()
odd_digits = [int(odd) for odd in digits if int(odd) % 2 != 0]
print(odd_digits)
