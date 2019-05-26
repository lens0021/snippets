# https://www.acmicpc.net/problem/5052
from sys import stdin


def insert_with_duplication_check(root, key):
    '''
    Trie에 새 노드를 추가하되, 문제에서 점검하라고 한 경우를 발견한 경우에는 딴 거 안하고
    바로 True를 반환합니다.
    '''
    if root == None:
        root = {}

    current = root
    for level in range(len(key)):
        index = key[level]
        if index not in current:
            current[index] = {}
        elif 'is_end' in current[index]:
            return True
        current = current[index]

    if current:
        return True
    current['is_end'] = True

    # print('Successfully inserted')
    # print(root)
    return False


def test(numbers):
    trie = {}

    for num in numbers:
        if insert_with_duplication_check(trie, num):
            print('NO')
            return

    print('YES')


number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    number_of_numbers = int(input())
    numbers = [stdin.readline().rstrip() for _ in range(number_of_numbers)]
    test(numbers)
