''' Binary Search: Ice Cream Parlor '''

def get_ice_cream_choices(money, ice_cream_prices):
    ''' Get ice-cream choices that fit in the given budget '''
    return ['1', '2']


def main():
    ''' Main function '''

    trips = int(input().strip())
    for _ in range(trips):
        money = int(input().strip())
        ice_cream_count = int(input().strip())
        ice_cream_prices = list(map(int, input().strip().split(' ')))[:ice_cream_count]

        ice_cream_choices = get_ice_cream_choices(money, ice_cream_prices)
        print(" ".join(ice_cream_choices))


if __name__ == '__main__':
    main()
