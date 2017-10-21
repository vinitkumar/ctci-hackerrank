''' Binary Search: Ice Cream Parlor '''

def get_index_mapping_for_prices(ice_cream_prices):
    ''' get mapping of prices to list of indices it can be found at '''

    mapping = dict()
    for index, price in enumerate(ice_cream_prices):
        if price in mapping:
            index_list = mapping[price]
        else:
            index_list = list()

        index_list.append(index)
        mapping[price] = index_list

    return mapping


def does_other_price_exist(numbers, sought_number, low, high):
    ''' Binary search to find a number in a list '''

    if high < low:
        return False

    # print("low:", low, ", high:", high)
    midpoint = (low + high) // 2
    # print("midpoint:", midpoint)
    if sought_number == numbers[midpoint]:
        return True
    elif sought_number < numbers[midpoint]:
        # print("sought_number ", sought_number, " less that midpoint", numbers[midpoint])
        return does_other_price_exist(numbers, sought_number, low, midpoint - 1)
    else:
        # print("sought_number ", sought_number, " greater that midpoint", numbers[midpoint])
        return does_other_price_exist(numbers, sought_number, midpoint + 1, high)


def get_ice_cream_choices(money, ice_cream_prices):
    ''' Get ice-cream choices that fit in the given budget '''
    sorted_ice_cream_prices = sorted(ice_cream_prices)
    index_mapping = get_index_mapping_for_prices(ice_cream_prices)
    # print(index_mapping)

    for index, price in enumerate(sorted_ice_cream_prices):
        other_price = money - price
        # print("evaluating", price, "and", other_price)
        other_price_exists = \
            does_other_price_exist(sorted_ice_cream_prices, other_price, \
                    index + 1, len(sorted_ice_cream_prices) - 1)

        if other_price_exists:
            first_index = index_mapping[price][0]
            if price == other_price:
                second_index = index_mapping[price][1]
            else:
                second_index = index_mapping[other_price][0]

            return sorted([first_index + 1, second_index + 1])


def main():
    ''' Main function '''

    trips = int(input().strip())
    for _ in range(trips):
        money = int(input().strip())
        ice_cream_count = int(input().strip())
        ice_cream_prices = list(map(int, input().strip().split(' ')))[:ice_cream_count]

        ice_cream_choices = get_ice_cream_choices(money, ice_cream_prices)
        # print(ice_cream_choices)
        print(ice_cream_choices[0], ice_cream_choices[1])

def main_test():
    ''' Main test function '''

    input_file = open("solutions/tmp/input01.txt")
    trips = int(input_file.readline().strip())
    for _ in range(trips):
        money = int(input_file.readline().strip())
        ice_cream_count = int(input_file.readline().strip())
        ice_cream_prices = \
            list(map(int, input_file.readline().strip().split(' ')))[:ice_cream_count]

        ice_cream_choices = get_ice_cream_choices(money, ice_cream_prices)
        # print(ice_cream_choices)
        print(ice_cream_choices[0], ice_cream_choices[1])

if __name__ == '__main__':
    main()
    # main_test()
