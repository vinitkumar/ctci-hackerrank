''' Sorting: Bubble Sort '''

def bubble_sort(numbers):
    ''' Runs bubble sort in place on an array '''
    total_swaps = 0
    for _ in range(len(numbers)):
        iteration_swaps = 0
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                iteration_swaps += 1

        if not iteration_swaps:
            break
        else:
            total_swaps += iteration_swaps

    print("Array is sorted in", total_swaps, "swaps.")
    return numbers


def main():
    ''' Main function '''
    _ = int(input().strip())
    numbers = list(map(int, input().strip().split(' ')))
    sorted_numbers = bubble_sort(numbers)
    print("First Element:", sorted_numbers[0])
    print("Last Element:", sorted_numbers[-1])

if __name__ == '__main__':
    main()
