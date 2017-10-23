''' Recursion: Davis' Staircase '''

WAYS_TO_CLIMB_CACHE = dict()

def get_ways_to_climb(num_steps_left):
    '''
    Given the step units and the number of steps, return the
    number of ways the staircase can be climbed
    '''

    if num_steps_left in WAYS_TO_CLIMB_CACHE:
        return WAYS_TO_CLIMB_CACHE[num_steps_left]

    ways_to_climb = 1

    if num_steps_left == 0:
        pass
    elif num_steps_left == 1:
        ways_to_climb = \
            get_ways_to_climb(num_steps_left - 1)
    elif num_steps_left == 2:
        ways_to_climb = \
            get_ways_to_climb(num_steps_left - 1) + \
            get_ways_to_climb(num_steps_left - 2)
    else:
        ways_to_climb = \
            get_ways_to_climb(num_steps_left - 1) + \
            get_ways_to_climb(num_steps_left - 2) + \
            get_ways_to_climb(num_steps_left - 3)

    WAYS_TO_CLIMB_CACHE[num_steps_left] = ways_to_climb

    return ways_to_climb

def main():
    ''' Main function '''
    num_staircases = int(input().strip())
    for _ in range(num_staircases):
        num_steps = int(input().strip())
        print(get_ways_to_climb(num_steps))

if __name__ == '__main__':
    main()
