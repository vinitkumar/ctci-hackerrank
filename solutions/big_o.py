''' Time Complexity: Primality '''

def is_prime(number):
    ''' Checks if a number is prime '''
    upper_bound_check = int(number**(0.5))
    # print("upper_bound_check:", upper_bound_check)

    for factor in range(2, upper_bound_check + 1):
        # print("checking factor:", factor)
        if number % factor == 0:
            return False

    return True

def main():
    ''' Main function '''
    number_count = int(input().strip())
    for _ in range(number_count):
        number = int(input().strip())
        print("Prime" if (number != 1 and is_prime(number)) else "Not prime")

def main_test():
    ''' Main function '''
    input_file = open("tmp/input09.txt")
    number_count = int(input_file.readline().strip())
    for _ in range(number_count):
        number = int(input_file.readline().strip())
        print("Prime" if (number != 1 and is_prime(number)) else "Not prime")

if __name__ == '__main__':
    main()
    # main_test()
