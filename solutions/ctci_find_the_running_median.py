""" Heaps: Find the Running Median """

import os
import heapq


class Heap(object):
    def __init__(self):
        self.numbers = list()

    def size(self):
        return len(self.numbers)

    def __repr__(self):
        return str(self.numbers)


class MinHeap(Heap):

    def push_new(self, number):
        heapq.heappush(self.numbers, number)

    def pop_smallest(self):
        return heapq.heappop(self.numbers)

    def get_smallest(self):
        return heapq.nsmallest(1, self.numbers)[0]

class MaxHeap(Heap):

    def push_new(self, number):
        heapq.heappush(self.numbers, -1 * number)

    def pop_largest(self):
        return -1 * heapq.heappop(self.numbers)

    def get_largest(self):
        return -1 * heapq.nsmallest(1, self.numbers)[0]


class MedianHeap(object):
    def __init__(self):
        self.small_numbers = MaxHeap()
        self.large_numbers = MinHeap()

    def insert_new(self, new_number):
        
        if self.small_numbers.size() == 0:
            self.small_numbers.push_new(new_number)
        elif self.small_numbers.get_largest() < new_number:
            self.large_numbers.push_new(new_number)
        else:
            self.small_numbers.push_new(new_number)

        if self.small_numbers.size() > self.large_numbers.size() + 1:
            number_to_move = self.small_numbers.pop_largest()
            self.large_numbers.push_new(number_to_move)

        if self.large_numbers.size() > self.small_numbers.size() + 1:
            number_to_move = self.large_numbers.pop_smallest()
            self.small_numbers.push_new(number_to_move)

        # print("small heap: ", self.small_numbers)
        # print("large heap: ", self.large_numbers)

    def get_median(self):
        if self.small_numbers.size() > self.large_numbers.size():
            return self.small_numbers.get_largest() / 1
        elif self.large_numbers.size() > self.small_numbers.size():
            return self.large_numbers.get_smallest() / 1
        else:
            return (self.small_numbers.get_largest() + self.large_numbers.get_smallest()) / 2


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
