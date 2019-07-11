def quick_sort(array):
    start = 0
    end = len(array) -1
    quick_sort_aux(array, start, end)


def quick_sort_aux(array, start, end):
    if start < end:
        boundary = partition(array, start, end)
        quick_sort_aux(array, start, boundary - 1)
        quick_sort_aux(array, boundary + 1, end)


def partition(array, start, end):
    mid = (start + end) // 2
    pivot = array[mid]
    array[start], array[mid] = array[mid], array[start]
    index = start
    for k in range(start + 1, end + 1):
        if array[k] < pivot:
            index += 1
            array[k], array[index] = array[index], array[k]

    array[start], array[index] = array[index], array[start]
    return index
