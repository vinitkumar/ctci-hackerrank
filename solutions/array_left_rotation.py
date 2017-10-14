""" Arrays: Left Rotation """

def array_left_rotation(a, n, k):
    actual_shift = k % n
    final = a[actual_shift:] + a[:actual_shift]
    return final

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
