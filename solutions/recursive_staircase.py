''' Recursion: Davis' Staircase '''

STEP_UNITS = [1, 2, 3]

def get_ways_to_climb(num_steps):
    '''
    Given the step units and the number of steps, return the
    number of ways the staircase can be climbed
    '''
    return 0

def main():
    ''' Main function '''
    num_staircases = int(input().strip())
    for _ in range(num_staircases):
        num_steps = int(input().strip())
        print(get_ways_to_climb(num_steps))

if __name__ == '__main__':
    main()
