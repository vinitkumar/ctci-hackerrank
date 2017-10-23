''' Recursion: Davis' Staircase '''

def get_ways_to_climb(num_steps_left):
    '''
    Given the step units and the number of steps, return the
    number of ways the staircase can be climbed
    '''

    if num_steps_left == 0:
        return 1
    elif num_steps_left == 1:
        return \
            get_ways_to_climb(num_steps_left - 1)
    elif num_steps_left == 2:
        return \
            get_ways_to_climb(num_steps_left - 1) + \
            get_ways_to_climb(num_steps_left - 2)
    else:
        return \
            get_ways_to_climb(num_steps_left - 1) + \
            get_ways_to_climb(num_steps_left - 2) + \
            get_ways_to_climb(num_steps_left - 3)

def main():
    ''' Main function '''
    num_staircases = int(input().strip())
    for _ in range(num_staircases):
        num_steps = int(input().strip())
        print(get_ways_to_climb(num_steps))

if __name__ == '__main__':
    main()
