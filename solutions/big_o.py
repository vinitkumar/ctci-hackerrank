''' Time Complexity: Primality '''

def is_prime(number):
    ''' Checks if a number is prime '''
    return False

def main():
    ''' Main function '''
    number_count = int(input().strip())
    for _ in range(number_count):
        number = int(input().strip())
        print(is_prime(number))

if __name__ == '__main__':
    main()
