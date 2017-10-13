""" Heaps: Find the Running Median """

import os
import heapq


class MedianHeap(object):
    def __init__(self):
        self.small_numbers = []
        self.large_numbers = []

    def insert_new(self, new_number):
        smallest_large_number = heapq.heappushpop(self.large_numbers, new_number)
        largest_small_number = -heapq.heappushpop(self.small_numbers, -smallest_large_number)

        if len(self.large_numbers) > len(self.small_numbers):
            heapq.heappush(self.small_numbers, -largest_small_number)
        else:
            heapq.heappush(self.large_numbers, largest_small_number)

        # print("small heap: ", self.small_numbers)
        # print("large heap: ", self.large_numbers)

    def get_median(self):
        if len(self.large_numbers) > len(self.small_numbers):
            return self.large_numbers[0] / 1
        else:
            return (self.large_numbers[0] - self.small_numbers[0]) / 2


def main():
    """ Main function """
    count_nums = int(input().strip())
    numbers = MedianHeap()
    for _ in range(count_nums):
        new_number = int(input().strip())
        numbers.insert_new(new_number)
        print(numbers.get_median())

def main_test():
    """ Main function """
    with open(os.path.dirname(os.path.abspath(__file__)) + \
            "/../tmp/input03.txt") as input_file:
        count_nums = int(input_file.readline().strip())
        numbers = MedianHeap()
        for _ in range(count_nums):
            new_number = int(input_file.readline().strip())
            numbers.insert_new(new_number)
            print(numbers.get_median())

if __name__ == '__main__':
    main()
    # main_test()
