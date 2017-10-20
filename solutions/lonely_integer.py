''' Bit Manipulation: Lonely Integer '''

from functools import reduce

def lonely_integer(integers):
    ''' Identifies lonely integer '''
    return reduce(lambda x, y: x ^ y, integers)

def main():
    ''' Main function '''
    integer_count = int(input().strip())
    integers = [int(a_temp) for a_temp in input().strip().split(' ')][:integer_count]
    print(lonely_integer(integers))

if __name__ == '__main__':
    main()
