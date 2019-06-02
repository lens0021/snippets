import random

arr = []


def insert(name, score):
    # TODO complete
    if not arr:
        arr.append((name, score))
        return

    low, high = 0, len(arr)

    while high - low > 1:
        middle = (high - low)//2
        if name > arr[middle][0]:
            low = middle
        else:
            high = middle

    print(arr)
    print(f'{low}, {high}')
    arr.insert(low, (name, score))


def find(key):
    # TODO Binary search
    for element in arr:
        if element[0] == key:
            return element[1]


def delete(key):
    # TODO
    pass


def update(key, score):
    pass


def range_query(low_key, high_key):
    pass


for name in [
    '가인',
    '예린',
    '진선',
    '슬미',
    '연정',
]:
    insert(name, random.randint(0, 100))

print(arr)


print('연정이의 점수가 몇점일까?')
print(f'우와, {find("연정")}점이야!')
print('가인이는 재시험을 칠거래')
print(f'그래서 그 전 점수는 {find("가인")}점인데,')
update('가인', random.randint(0, 100))
print(f'이제는 {find("가인")}점이야')
print('가인: 방예린 학생은 내게 과제를 하지 않았지 자넨 퇴학일세')
delete('예린')
print('가인이부터 연정이까지 사이의 학생들 점수를 다 보자')
print(range_query('가인', '연정'))

print('배열은 어떻게 생겼지?')
print(arr)
