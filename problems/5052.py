# https://www.acmicpc.net/problem/5052


def insert_with_duplication_check(root, key):
    '''
    Trie에 새 노드를 추가하되, 문제에서 점검하라고 한 경우를 발견한 경우에는 딴 거 안하고
    바로 True를 반환합니다.
    '''
    if root == None:
        root = {}

    pos = root
    for level in range(len(key)):
        index = key[level]
        if index not in pos:
            pos[index] = {}
        elif 'is_end' in pos[index]:
            return True
        pos = pos[index]
    pos['is_end'] = True

    # print('Successfully inserted')
    # print_tree(root)
    return False


def print_tree(node):
    print(node)


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
    numbers = [input() for _ in range(number_of_numbers)]
    test(numbers)
