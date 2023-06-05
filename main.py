size = 3
grid = [' '] * size * size


def print_board():
    for y in range(size):
        if y > 0:
            print('\n-----------')

        for x in range(size):
            index = x + (y * size)
            print('', grid[index], '|' if x < size - 1 else '', end='')


while True:
    print_board()

    try:
        index = int(input())
        grid[index] = 'O'
    except (ValueError, IndexError):
        print('That is an invalid input, u stupid?')
