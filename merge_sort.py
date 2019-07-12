def merge_sort(array):
    temp = [None] * len(array)
    start = 0
    end = len(array) - 1
    merge_sort_aux(array, start, end, temp)


def merge_sort_aux(array, start, end, temp):
    if start < end:
        mid = (start + end) // 2
        
        merge_sort_aux(array, start, mid, temp)
        merge_sort_aux(array, mid + 1, end, temp)
        
        merge_array(array, start, mid, end, temp)
        
        for i in range(start, end + 1):
            array[i] = temp[i]


def merge_array(array, start, mid, end, temp):
    i = start
    j = mid + 1
    for k in range(start, end + 1):
        if i > mid:
            temp[k] = array[j]
            j += 1
        elif j > end:
            temp[k] = array[i]
            i += 1
        elif array[i] <= array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
