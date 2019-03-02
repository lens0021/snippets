from time import time
from heapq import heappush, heappop
import math
import random

_ = int(input())
numbers = [int(param) for param in input().split(' ')]
numbers = [random.randint(0, 10000) for _ in range(50)]


def bubble_sort(l):
    l = l.copy()

    for i in range(len(l)-1, 0, -1):
        for j in range(0, i):
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

    for i in range(0, len(l)):
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


def merge_sort_in_place(lst: list, left: int, right: int) -> None:
    """
    Args:
        left (int): inclusive
        right (int): exclusive
    """
    if right - left == 1:
        return

    mid = (right + left) // 2
    merge_sort_in_place(lst, left, mid)
    merge_sort_in_place(lst, mid, right)

    merged_array = []
    i, j = left, mid
    while i < mid and j < right:
        if lst[i] <= lst[j]:
            merged_array.append(lst[i])
            i += 1
        else:
            merged_array.append(lst[j])
            j += 1

    if i < mid:
        merged_array += lst[i:mid]
    else:
        merged_array += lst[j:right]

    for i in range(left, right):
        lst[i] = merged_array.pop(0)


def quick_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    index_of_pivot = 0  # TODO Use the median
    pivot = lst[index_of_pivot]

    left, right = [], []

    for idx, val in enumerate(lst):
        if idx == index_of_pivot:
            continue
        elif val < pivot:
            left.append(val)
        else:
            right.append(val)

    left = quick_sort(left)
    left.append(pivot)
    right = quick_sort(right)

    return left + right


def quick_sort_in_place(lst: list, left: int, right: int):
    """
    Args:
        left (int): inclusive
        right (int): inclusive
    """
    if not left < right:
        return

    index_of_pivot = left  # TODO Use the median
    pivot = lst[index_of_pivot]

    low, high = left + 1, right
    while True:
        # Find a element greater then pivot
        while low <= right and lst[low] < pivot:
            low += 1

        # Find a element less then pivot
        while left <= high and lst[high] > pivot:
            high -= 1

        if not low < high:
            break
        else:
            lst[low], lst[high] = lst[high], lst[low]

    lst[index_of_pivot], lst[high] = lst[high], lst[index_of_pivot]
    index_of_pivot = high

    quick_sort_in_place(lst, left, index_of_pivot - 1)
    quick_sort_in_place(lst, index_of_pivot + 1, right)


def heap_sort_with_built_in(lst: list) -> list:
    heap = []
    for item in lst:
        heappush(heap, item)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    return ordered


def heap_sort(lst: list) -> list:
    if not lst:
        return lst.copy()

    heap = []

    def heap_parent_of(i: int) -> int:
        if i == 0:
            raise Exception
        return ((i+1)//2)-1

    def heap_left_node_of(i: int) -> int:
        return i*2 + 1

    for item in lst:
        heap.append(item)
        i = len(heap)-1
        while i > 0 and (item < heap[heap_parent_of(i)]):
            heap[i] = heap[heap_parent_of(i)]
            i = heap_parent_of(i)
        heap[i] = item
    ordered = []
    while heap:
        if len(heap) == 1:
            ordered.append(heap[0])
            break

        item = heap[0]
        temp = heap.pop()
        ordered.append(item)
        parent = 0
        child = 1
        while child < len(heap)-1:
            if child+1 < len(heap)-1 and heap[child+1] < heap[child]:
                child += 1
            if temp <= heap[child]:
                break
            heap[parent] = heap[child]
            parent = child
            child = heap_left_node_of(child)
        heap[parent] = temp

    return ordered


def radix_sort(lst: list) -> list:
    lst = lst.copy()

    digits = int(math.log10(max(lst)))+1
    number_of_bucket = 10
    buckets = [[] for _ in range(number_of_bucket)]

    for radix in range(1, digits+1):
        for element in lst:
            index = element//int(10**(radix-1))
            index %= number_of_bucket
            buckets[index].append(element)

        lst = []
        for bucket in buckets:
            lst += bucket
            bucket.clear()

    return lst


global start

start = time()


def show_time():
    global start
    print(time() - start)
    start = time()


do_print = False
if do_print:
    print('source         : '+(' '.join(str(num) for num in numbers)))
result = sorted(numbers)
show_time()
if do_print:
    print('built-in       : '+(' '.join(str(num) for num in result)))
result = bubble_sort(numbers)
show_time()
if do_print:
    print('bubble         : '+(' '.join(str(num) for num in result)))
result = insertion_sort(numbers)
show_time()
if do_print:
    print('insertion      : '+(' '.join(str(num) for num in result)))
result = selection_sort(numbers)
show_time()
if do_print:
    print('selection      : '+(' '.join(str(num) for num in result)))
result = merge_sort(numbers)
show_time()
if do_print:
    print('merge          : '+(' '.join(str(num) for num in result)))
numbers2 = numbers.copy()
merge_sort_in_place(numbers2, 0, len(numbers2))
show_time()
if do_print:
    print('merge(in-place): '+(' '.join(str(num) for num in numbers2)))
result = quick_sort(numbers)
show_time()
if do_print:
    print('quick          : '+(' '.join(str(num) for num in result)))
numbers2 = numbers.copy()
quick_sort_in_place(numbers2, 0, len(numbers2)-1)
show_time()
if do_print:
    print('quick(in-place): '+(' '.join(str(num) for num in numbers2)))
result = heap_sort_with_built_in(numbers)
show_time()
if do_print:
    print('heap(built-in) : '+(' '.join(str(num) for num in result)))
result = heap_sort(numbers)
show_time()
if do_print:
    print('heap           : '+(' '.join(str(num) for num in result)))
result = radix_sort(numbers)
show_time()
if do_print:
    print('radix          : '+(' '.join(str(num) for num in result)))
