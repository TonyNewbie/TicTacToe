digits = input()
entered_number = [int(digit) for digit in digits if digit.isdigit()]
totals_list = [sum(entered_number[:x]) for x in entered_number]
print(totals_list)
