number = int(input())
winner_list = []
for i in range(number):
    result = input().split()
    if result[1] == 'win':
        winner_list.append(result[0])
print(winner_list)
print(len(winner_list))
