''' DFS: Connected Cell in a Grid '''

def traverse_neighbourhood(matrix, row_number, column_number, traversed_ones, ones_count):
    '''
    Given the location of a 1, traverse it's neighbourhood, count all the
    other 1s it's connected to, update the traversed_ones set, and
    return the number of 1s in that area
    '''

    traversed_ones.add((row_number, column_number))
    region_offsets = [-1, 0, 1]

    for row_offset in region_offsets:
        for col_offset in region_offsets:
            adjacent_row_number = max(0, row_number + row_offset)
            adjacent_col_number = max(0, column_number + col_offset)
            try:
                if matrix[adjacent_row_number][adjacent_col_number] == 1 \
                        and (adjacent_row_number, adjacent_col_number) not in traversed_ones:
                    # print("recursing at ", (adjacent_row_number, adjacent_col_number))
                    ones_count += traverse_neighbourhood(
                        matrix, adjacent_row_number, adjacent_col_number,
                        traversed_ones, ones_count)
            except IndexError:
                pass

    return ones_count

def get_biggest_region(matrix, num_rows, num_cols):
    ''' Calculates the number of cells in the biggest region of 1s'''

    traversed_ones = set()
    max_ones_region_count = 0

    for row_number in range(num_rows):
        for column_number in range(num_cols):
            if matrix[row_number][column_number] == 1 \
                    and (row_number, column_number) not in traversed_ones:

                # print("found seed point at ", (row_number, column_number))
                ones_count = traverse_neighbourhood(
                    matrix, row_number, column_number, traversed_ones, 1)

                max_ones_region_count = ones_count \
                    if ones_count > max_ones_region_count else max_ones_region_count

    return max_ones_region_count

def main():
    ''' Main function '''
    num_rows = int(input().strip())
    num_cols = int(input().strip())
    grid = []
    for _ in range(num_rows):
        grid_t = list(map(int, input().strip().split(' ')))
        grid.append(grid_t[:num_cols])
    print(get_biggest_region(grid, num_rows, num_cols))

if __name__ == '__main__':
    main()
