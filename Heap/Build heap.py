def heapify(array, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if (l < len(array) and array[l] > array[largest]):
        largest = l
    if (r < len(array) and array[r] > array[largest]):
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest)


def build_heap(array):
    pos = len(array) // 2 - 1
    for i in range(pos, -1, -1):
        heapify(array, i)
    return array

if __name__ == '__main__':
    array = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    build_heap(array)
    print(array)
