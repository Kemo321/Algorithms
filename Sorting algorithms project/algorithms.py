def selection_sort(list: list) -> list:
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def quick_sort(list: list) -> list:
    length = len(list)
    if length <= 1:
        return list
    if length == 2:
        if list[0] > list[1]:
            list[0], list[1] = list[1], list[0]
        return list
    pivot = length // 2
    list[-1], list[pivot] = list[pivot], list[-1]
    pivot = list[-1]

    p = 0
    q = length - 2

    while p != q:
        while list[q] >= pivot:
            q -= 1
            if p == q:
                break
        if p == q:
            break
        while list[p] < pivot:
            p += 1
            if p == q:
                break
        list[p], list[q] = list[q], list[p]
    if list[p] < pivot:
        p += 1
    list[p], list[-1] = pivot, list[p]
    list[0:p] = quick_sort(list[0:p])
    list[p+1: length] = quick_sort(list[p+1: length])
    return list


def merge_sort(list: list) -> list:
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                list[k] = right[j]
                j += 1
            else:
                list[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


def insertion_sort(list: list) -> list:
    sorted_index = 1
    for i in range(1, len(list)):
        for j in range(0, sorted_index):
            if list[j] >= list[i]:
                list.insert(j, list.pop(i))
        sorted_index += 1
    return list


def bubble_sort(list: list) -> list:
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(list) - 1):
            if list[i+1] < list[i]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_sorted = False
    return list
