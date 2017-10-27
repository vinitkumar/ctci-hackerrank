''' Merge Sort: Counting Inversions '''

def merge_sorted_lists(list_1, size_1, list_2, size_2):
    '''
    Merges 2 sorted lists and returns a merged list
    and the count of inversions done
    '''

    # print("merging ", list_1, "and", list_2)

    index_1 = 0
    index_2 = 0
    merged_list = list()
    inversions = 0

    while index_1 < size_1 and index_2 < size_2:
        if list_1[size_1 - 1] < list_2[index_2]:
            merged_list.extend(list_1[index_1:])
            merged_list.extend(list_2[index_2:])
            return merged_list, inversions
        elif list_2[size_2 - 1] < list_1[index_1]:
            merged_list.extend(list_2[index_2:])
            merged_list.extend(list_1[index_1:])
            return merged_list, \
                inversions + ((size_2 - index_2) * (size_1 - index_1))

        if list_1[index_1] <= list_2[index_2]:
            merged_list.append(list_1[index_1])
            index_1 += 1
        else:
            merged_list.append(list_2[index_2])
            index_2 += 1
            inversions += size_1 - index_1

    if index_1 < size_1:
        merged_list += list_1[index_1:]
    else:
        merged_list += list_2[index_2:]

    return merged_list, inversions


def merge_sort(numbers, numbers_size):
    ''' Performs a divide-and-conquer merge sort '''

    if numbers_size <= 1:
        return numbers, 0

    mid = numbers_size // 2
    first_half, first_half_inversions = \
        merge_sort(numbers[:mid], mid)
    second_half, second_half_inversions = \
        merge_sort(numbers[mid:], numbers_size - mid)
    # print("first_half_inversions:", first_half_inversions)
    # print("second_half_inversions:", second_half_inversions)

    merged_list, merge_inversions = \
        merge_sorted_lists(first_half, mid, second_half, numbers_size - mid)
    # print("merge_inversions:", merge_inversions)

    return \
        merged_list, \
        merge_inversions + first_half_inversions + second_half_inversions

def count_inversions(numbers):
    ''' Counts the number of inversions required to sort an array '''

    _, inversions = merge_sort(numbers, len(numbers))
    return inversions


def main():
    ''' Main function '''
    num_datasets = int(input().strip())
    for _ in range(num_datasets):
        dataset_size = int(input().strip())
        numbers = list(map(int, input().strip().split(' ')))[:dataset_size]
        result = count_inversions(numbers)
        print(result)

def main_test():
    ''' Main function '''

    input_file = open("tmp/input13.txt")
    num_datasets = int(input_file.readline().strip())
    for _ in range(num_datasets):
        dataset_size = int(input_file.readline().strip())
        numbers = list(map(int, input_file.readline().strip().split(' ')))\
                [:dataset_size]
        result = count_inversions(numbers)
        print(result)

if __name__ == '__main__':
    # main()
    main_test()
