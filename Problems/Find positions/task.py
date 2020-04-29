# put your python code here
sequence = input().split()
x = input()
if x not in sequence:
    print('not found')
else:
    positions = [str(position) for position in range(len(sequence)) if x == sequence[position]]
    print(' '.join(positions))
