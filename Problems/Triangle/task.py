height = int(input())
for i in range(height):
    print(('#' * (i * 2 + 1)).center(height * 2 - 1))
