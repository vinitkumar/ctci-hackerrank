''' DP: Coin Change '''

def make_change(coin_denominations, amount):
    '''
    Gets the number of combinations coin_denominations can be used in,
    to create amount
    '''
    pass

def main():
    ''' Main function '''
    amount, coin_type_count = input().strip().split(' ')
    amount, coin_type_count = [int(amount), int(coin_type_count)]
    coin_denominations = \
        [int(coins_temp) for coins_temp in input().strip().split(' ')]
    print(make_change(coin_denominations, amount))

if __name__ == '__main__':
    main()
