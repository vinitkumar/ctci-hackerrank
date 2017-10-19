''' DFS: Connected Cell in a Grid '''

def get_biggest_region(matrix):
    ''' Calculates the number of cells in the biggest region of 1s'''
    pass

def main():
    ''' Main function '''
    num_rows = int(input().strip())
    num_cols = int(input().strip())
    grid = []
    for _ in range(num_rows):
        grid_t = list(map(int, input().strip().split(' ')))
        grid.append(grid_t[:num_cols])
    print(get_biggest_region(grid))

if __name__ == '__main__':
    main()
