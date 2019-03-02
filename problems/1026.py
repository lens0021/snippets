# https://www.acmicpc.net/problem/1026

_ = input()  # Drop the length of input array
lst_a = list(map(int, input().split(' ')))
lst_b = list(map(int, input().split(' ')))


def bucket_sort(lst: list, digits: int, largest_first: bool):
    for digit in range(digits):
        buckets = [[] for _ in range(10)]
        for element in lst:
            radix = element // (10**digit)
            radix = radix % 10
            buckets[radix].append(element)
        del(lst[:])

        for bucket in (reversed(buckets) if largest_first else buckets):
            for element in bucket:
                lst.append(element)


# Order list A ascending
if 100 not in lst_a:
    bucket_sort(lst_a, 2, False)
else:
    number = lst_a.count(100)
    lst_a[:] = (ele for ele in lst_a if ele != 100)
    bucket_sort(lst_a, 2, False)
    lst_a = lst_a + [100 for _ in range(number)]
# Order list B descending
if 100 not in lst_a:
    bucket_sort(lst_b, 2, True)
else:
    number = lst_b.count(100)
    lst_b[:] = (ele for ele in lst_b if ele != 100)
    bucket_sort(lst_b, 2, True)
    lst_b = [100 for _ in range(number)] + lst_b

# Multiply
print(sum([a * b for a, b in zip(lst_a, lst_b)]))
