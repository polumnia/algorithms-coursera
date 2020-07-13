from random import shuffle

def swap(inp_array, ind1, ind2):
    inp_array[ind1], inp_array[ind2] = inp_array[ind2], inp_array[ind1]

def quicksort(input_array, lo, hi):
    if lo >= hi:
        return
    partition_index = partition(input_array, lo, hi)
    quicksort(input_array, lo, partition_index - 1)
    quicksort(input_array, partition_index + 1, hi)

def partition(input_array, lo, hi):
    i = lo + 1
    j = hi
    partition_char = input_array[lo]
    while True:
        for char in input_array[i:hi]:
            if char > partition_char:
                break
            i += 1
        for char in input_array[j:lo:-1]:
            if char < partition_char:
                break
            j -= 1
        if i >= j:
            break
        swap(input_array, i, j)
    swap(input_array, lo, j)
    return j

if __name__ == '__main__':
    inp_array = list('KRATELEPUIMQCXOS')
    shuffle(inp_array)
    quicksort(inp_array, 0, len(inp_array) - 1)
    print(inp_array)
