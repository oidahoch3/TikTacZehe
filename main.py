size = 3
grid = [' '] * size * size


def print_board():
    for y in range(size):
        if y > 0:
            print('\n-----------')

        for x in range(size):
            index = x + (y * size)
            print('', grid[index], '|', end='')


while True:
    print_board()

    index = int(input())
    grid[index] = 'O'
