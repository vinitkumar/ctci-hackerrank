''' Merge Sort: Counting Inversions '''

def count_inversions(numbers):
    ''' Counts the number of inversions required to sort an array '''
    return 0

def main():
    ''' Main function '''
    num_datasets = int(input().strip())
    for _ in range(num_datasets):
        dataset_size = int(input().strip())
        numbers = list(map(int, input().strip().split(' ')))[:dataset_size]
        result = count_inversions(numbers)
        print(result)

if __name__ == '__main__':
    main()
