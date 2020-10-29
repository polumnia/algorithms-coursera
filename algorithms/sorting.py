def selection_sort(input_array):
    array_size = len(input_array)
    for i in range(array_size):
        min_id = i
        for j in range(i+1, array_size):
            if input_array[j] < input_array[min_id]:
                min_id = j
        swap(input_array, i, min_id)


def new_insertion_sort(input_array):
    for j in range(1, len(input_array)):
        key = input_array[j]
        i = j - 1
        while i >= 0 and input_array[i] > key:
            input_array[i + 1] = input_array[i]
            i = i - 1
        input_array[i + 1] = key


def insertion_sort(input_array):
    array_size = len(input_array)
    for i in range(array_size):
        for j in range(i, 0, -1):
            if input_array[j] < input_array[j-1]:
                swap(input_array, j, j-1)
            else:
                break

def shellsort(input_array):
    array_size = len(input_array)
    h = 1
    while h < array_size / 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, array_size):
            for j in range(i, h-1, -h):
                if input_array[j] < input_array[j-h]:
                    swap(input_array, j, j-h)
                else:
                    break
        h = h // 3


def swap(inp_array, ind1, ind2):
    inp_array[ind1], inp_array[ind2] = inp_array[ind2], inp_array[ind1]

def merge(input_array, aux_array, lo, mid, hi):
    for i in range(lo, hi + 1):
        aux_array[i] = input_array[i]
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            input_array[k] = aux_array[j]
            j += 1
        elif j > hi:
            input_array[k] = aux_array[i]
            i += 1
        elif aux_array[i] <= aux_array[j]:
            input_array[k] = aux_array[i]
            i += 1
        else:
            input_array[k] = aux_array[j]
            j += 1
    return input_array

def _mergesort(input_array, aux_array, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    _mergesort(input_array, aux_array, lo, mid)
    _mergesort(input_array, aux_array, mid + 1, hi)
    merge(input_array, aux_array, lo, mid, hi)

def mergesort(input_array):
    array_size = len(input_array)
    _mergesort(input_array, [None] * array_size, 0, array_size - 1)
