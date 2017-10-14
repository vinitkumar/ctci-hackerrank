''' DP: Coin Change '''


def make_change(coin_denominations, amount):
    '''
    Gets the number of combinations coin_denominations can be used in,
    to create amount
    '''
    coin_denominations = sorted(coin_denominations)
    dp_matrix = [[1 for _ in range(amount + 1)] for _ in range(len(coin_denominations))]

    for coin_index, coin_denomination in enumerate(coin_denominations):
        for amount_value in range(amount + 1):
            if coin_index == 0:
                if amount_value % coin_denomination == 0:
                    dp_matrix[coin_index][amount_value] = 1
                else:
                    dp_matrix[coin_index][amount_value] = 0
            elif coin_denomination <= amount_value:
                dp_matrix[coin_index][amount_value] = \
                    dp_matrix[coin_index - 1][amount_value] + \
                    dp_matrix[coin_index][amount_value - coin_denomination]
            else:
                dp_matrix[coin_index][amount_value] = dp_matrix[coin_index - 1][amount_value]

    # print(dp_matrix)

    return dp_matrix[len(coin_denominations) - 1][amount]


def main():
    ''' Main function '''
    amount, coin_type_count = input().strip().split(' ')
    amount, coin_type_count = [int(amount), int(coin_type_count)]
    coin_denominations = \
        [int(coins_temp) for coins_temp in input().strip().split(' ')]
    print(make_change(coin_denominations, amount))

if __name__ == '__main__':
    main()
