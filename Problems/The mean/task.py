sequence = input()
digit_list = [int(digit) for digit in sequence]
mean = sum(digit_list) / len(digit_list)
print(mean)
