""" Heaps: Find the Running Median """

def get_insertion_index(numbers, new_number, high_index, low_index):
    """
    Given a sorted array, returns the index at which to 
    insert the new number
    """

    if high_index == low_index:
        return low_index

    midpoint_index = (low_index + high_index) // 2
    if new_number >= numbers[midpoint_index] and new_number <= numbers[midpoint_index + 1]:
        return midpoint_index + 1
    elif new_number < numbers[midpoint_index]:
        return get_insertion_index(numbers, new_number, midpoint_index, low_index)
    else:
        return get_insertion_index(numbers, new_number, high_index, midpoint_index + 1)


def get_array_after_insertion(numbers, new_number):
    """
    Given a sorted array, adds a new number and keeps
    the array sorted
    """

    if new_number < numbers[0]:
        return [new_number] + numbers

    for index in range(len(numbers) - 1):
        if new_number > numbers[index] and new_number <= numbers[index + 1]:
            return numbers[:index + 1] + [new_number] + numbers[index + 1:]
    
    return numbers + [new_number]


class SortedList(object):
    def __init__(self):
        self.numbers = list()

    def insert_new(self, new_number):
        if self.numbers:
            insertion_index = get_insertion_index(
                self.numbers, new_number, len(self.numbers), 0)
            
            if insertion_index == len(self.numbers):
                self.numbers.append(new_number)
            else:
                self.numbers = self.numbers[:insertion_index] + [new_number] + \
                        self.numbers[insertion_index:]
            # self.numbers = get_array_after_insertion(self.numbers, new_number)
        else:
            self.numbers.append(new_number)

    def get_median(self):
        list_length = len(self.numbers)
        if list_length % 2 == 0 and list_length != 0:
            return float((self.numbers[(list_length // 2) - 1] + \
                    self.numbers[(list_length // 2)]) / 2)
        else:
            return float(self.numbers[list_length // 2])


def main():
    """ Main function """
    count_nums = int(input().strip())
    numbers = SortedList()
    for _ in range(count_nums):
        new_number = int(input().strip())
        numbers.insert_new(new_number)
        print(numbers.get_median())


if __name__ == '__main__':
    main()
