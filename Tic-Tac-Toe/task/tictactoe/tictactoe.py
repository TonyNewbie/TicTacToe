# write your code here
def table_printer(table):
    print('---------')
    print(f'| {table[0][0]} {table[0][1]} {table[0][2]} |')
    print(f'| {table[1][0]} {table[1][1]} {table[1][2]} |')
    print(f'| {table[2][0]} {table[2][1]} {table[2][2]} |')
    print('---------')


def check_table(table):
    x_wins = ((table[0].count('X') == 3) or (table[1].count('X') == 3) or (table[2].count('X') == 3)
              or (table[0][0] == table[1][0] == table[2][0] == 'X')
              or (table[0][1] == table[1][1] == table[2][1] == 'X')
              or (table[0][2] == table[1][2] == table[2][2] == 'X')
              or (table[0][0] == table[1][1] == table[2][2] == 'X')
              or (table[0][2] == table[1][1] == table[2][0] == 'X'))
    y_wins = ((table[0].count('O') == 3) or (table[1].count('O') == 3) or (table[2].count('O') == 3)
              or (table[0][0] == table[1][0] == table[2][0] == 'O')
              or (table[0][1] == table[1][1] == table[2][1] == 'O')
              or (table[0][2] == table[1][2] == table[2][2] == 'O')
              or (table[0][0] == table[1][1] == table[2][2] == 'O')
              or (table[0][2] == table[1][1] == table[2][0] == 'O'))
    table_printer(table)
    if x_wins:
        return 'X wins'
    elif y_wins:
        return 'O wins'
    elif table[0].count(' ') == 0 and table[1].count(' ') == 0 and table[2].count(' ') == 0:
        return 'Draw'
    else:
        return 'Game not finished'


game_table = [[' ' for j in range(3)] for i in range(3)]
symbol = 'X'
game_status = check_table(game_table)
coordinates = input('Enter the coordinates: ').split()
while game_status == 'Game not finished':
    if len(coordinates) < 2:
        print('You should enter numbers')
        coordinates = input('Enter the coordinates: ').split()
    elif (not coordinates[0].isdigit()) or (not coordinates[1].isdigit()):
        print('You should enter numbers')
        coordinates = input('Enter the coordinates: ').split()
    elif (not (0 < int(coordinates[0]) < 4)) or (not (0 < int(coordinates[1]) < 4)):
        print('Coordinates should be from 1 to 3!')
        coordinates = input('Enter the coordinates: ').split()
    elif game_table[3 - int(coordinates[1])][int(coordinates[0]) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        coordinates = input('Enter the coordinates: ').split()
    else:
        game_table[3 - int(coordinates[1])][int(coordinates[0]) - 1] = symbol
        game_status = check_table(game_table)
        if game_status == 'X wins' or game_status == 'O wins' or game_status == 'Draw':
            print(game_status)
        else:
            if symbol == 'X':
                symbol = 'O'
            else:
                symbol = 'X'
            coordinates = input('Enter the coordinates: ').split()
