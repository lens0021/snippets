import random

random.seed(0)
arr = []
DEBUG = False


def log(arg):
    if DEBUG:
        print(arg)


def array_insert(key, score):
    if not arr:
        arr.append((key, score))
        return

    low, high = 0, len(arr)-1
    while high - low > 0:
        log(f'low is {low}, high is {high}')
        middle = (high + low)//2
        log(f'middle is {middle}')
        if key < arr[middle][0]:
            high = middle-1
            log(f'The key({key}) is less than {middle}th element'
                f'({arr[middle][0]}). So decrease high to {middle-1}')
        elif key > arr[middle][0]:
            log(f'The key({key}) is lager than {middle}th element'
                f'({arr[middle][0]}). So increase low to {middle+1}')
            low = middle+1
        log(arr)

    if key > arr[low][0]:
        arr.insert(low+1, (key, score))
    elif key < arr[low][0]:
        arr.insert(low, (key, score))


def array_find(key):
    low, high = 0, len(arr)-1
    while high - low >= 0:
        middle = (high + low)//2
        if key > arr[middle][0]:
            low = middle+1
        elif key < arr[middle][0]:
            high = middle-1
        else:
            return arr[middle][1]

    return None


def array_delete(key):
    low, high = 0, len(arr)
    while high - low >= 0:
        # log(f'{low}, {high}')
        middle = (high + low)//2
        if key > arr[middle][0]:
            log(f'The key({key}) is lager than {middle}th element'
                f'({arr[middle][0]}). So increase low to {middle+1}')
            low = middle+1
        elif key < arr[middle][0]:
            log(f'The key({key}) is less than {middle}th element'
                f'({arr[middle][0]}). So decrease high to {middle-1}')
            high = middle-1
        else:
            return arr.pop(middle)


def array_update(key, score):
    low, high = 0, len(arr)
    while high - low >= 0:
        log(f'{low}, {high}')
        middle = (high + low)//2
        if key > arr[middle][0]:
            low = middle+1
        elif key < arr[middle][0]:
            high = middle-1
        else:
            arr[middle] = (key, score)
            return


def array_range_query(low_key, high_key):
    low_index, high_index = 0, 0

    low, high = 0, len(arr)
    while high - low >= 0:
        middle = (high + low)//2
        if low_key > arr[middle][0]:
            low = middle+1
        elif low_key < arr[middle][0]:
            high = middle-1
        else:
            low_index = middle
            break

    low, high = 0, len(arr)
    while high - low >= 0:
        middle = (high + low)//2
        if high_key > arr[middle][0]:
            low = middle+1
        elif high_key < arr[middle][0]:
            high = middle-1
        else:
            high_index = middle
            break

    return arr[low_index:high_index+1]


for name in [
    '가인',
    '예린',
    '진선',
    '슬미',
    '연정',
]:
    array_insert(name, random.randint(0, 100))

print(arr)

print('연정이의 점수가 몇점일까?')
print(f'우와, {array_find("연정")}점이야!')
print('가인이는 재시험을 칠거래')
print(f'그래서 그 전 점수는 {array_find("가인")}점인데,')
array_update('가인', random.randint(0, 100))
print(f'이제는 {array_find("가인")}점이야')
print('가인: 방예린 학생은 내게 과제를 하지 않았지 자넨 퇴학일세')
array_delete('예린')
print('배열은 어떻게 생겼지?')
print(arr)
print('가인이부터 연정이까지 사이의 학생들 점수를 다 보자')
print(array_range_query('가인', '연정'))

print('배열은 어떻게 생겼지?')
print(arr)
