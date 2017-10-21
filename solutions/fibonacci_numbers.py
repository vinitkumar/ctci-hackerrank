''' Recursion: Fibonacci Numbers '''

def fibonacci(number):
    ''' Calculates the nth fibonacci number '''
    return fibonacci(number - 1) + fibonacci(number - 2) if number > 1 else number


def main():
    ''' Main function '''
    number = int(input())
    print(fibonacci(number))


if __name__ == '__main__':
    main()
