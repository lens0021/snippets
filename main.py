_ = int(input())
numbers = [int(param) for param in input().split(' ')]

def bubble_sort(l):
    l = l.copy()

    for i in range(len(l)-1, 0, -1):
        for j in range(0,i):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l

def insertion_sort(l):
    l = l.copy()

    # Select one element (first element is skipped because it is a 1-length array which is sorted already)
    for i in range(1, len(l)):
        # Find certain position of the element
        tmp = l[i]
        j = i-1
        while j >= 0 and l[j] > tmp:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = tmp

    return l

def selection_sort(l):
    l = l.copy()

    for i in range(0,len(l)):
        # Select the min element of the subset
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

def merge_sort(lst: list) -> list:
    length = len(lst)

    if length <= 1:
        return lst

    mid = length // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    merged_array = []
    while left and right:
        if left[0] <= right[0]:
            merged_array.append(left.pop(0))
        else:
            merged_array.append(right.pop(0))

    if left:
        merged_array += left
    else:
        merged_array += right

    return merged_array

# start is inclusive
# end is exclusive
def merge_sort_in_place(lst: list, start: int, end: int) -> None:
    if end - start == 1:
        return

    mid = (end + start) // 2
    merge_sort_in_place(lst, start, mid)
    merge_sort_in_place(lst, mid, end)

    merged_array = []
    i, j = start, mid
    while i < mid and j < end:
        if lst[i] <= lst[j]:
            merged_array.append(lst[i])
            i += 1
        else:
            merged_array.append(lst[j])
            j += 1

    if i < mid:
        merged_array += lst[i:mid]
    else:
        merged_array += lst[j:end]

    for i in range(start, end):
        lst[i] = merged_array.pop(0)


result = sorted(numbers)
print('built-in       : '+(' '.join(str(num) for num in result)))
result = bubble_sort(numbers)
print('bubble         : '+(' '.join(str(num) for num in result)))
result = insertion_sort(numbers)
print('insertion      : '+(' '.join(str(num) for num in result)))
result = selection_sort(numbers)
print('selection      : '+(' '.join(str(num) for num in result)))
result = merge_sort(numbers)
print('merge          : '+(' '.join(str(num) for num in result)))
numbers2 = numbers.copy()
merge_sort_in_place(numbers2, 0, len(numbers2))
print('merge(inplace) : '+(' '.join(str(num) for num in numbers2)))
