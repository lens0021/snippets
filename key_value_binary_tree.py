import math

tree = []

DATA = 0
LEFT = 1
RIGHT = 2

KEY = 0
VALUE = 1


def print_tree(tree, height=5):
    # 일차원 배열로 대강 변환한다.
    # [루트, 루트의 왼쪽 자식, 루트의 오른쪽 자식, ..., (계속)]
    arr = []
    length_of_arr = 2**height-1

    # 완전이진트리로 가정하고 각 자리에 들어갈 수를 구한다.
    for i in range(length_of_arr):
        node = i
        parents = []
        while node != 0:
            # 노드에서 루트까지 올라가려면 어떻게 이동하는지를 기록
            if node % 2 == 0:
                parents.append(RIGHT)
                node = node//2 - 1
            else:
                parents.append(LEFT)
                node = node//2

        # 위에서 기록한 걸 거꾸로 실행하여 노드까지 이동함
        node = tree
        while parents and node != None:
            node = node[parents.pop()]

        if node != None:
            arr.append(node[DATA][KEY])
        else:
            arr.append(None)

    max_number_of_column = 2 ** math.floor(math.log(length_of_arr, 2))
    WIDTH_OF_NODE = 5
    GAP = 0
    max_width = max_number_of_column * WIDTH_OF_NODE \
        + (max_number_of_column-1) * GAP
    power_of_two = 1
    level = 0
    for i, num in enumerate(arr):
        if i == power_of_two - 1:
            level += 1
            power_of_two *= 2
            if i != 0:
                print('')

            number_in_columns = 2**(level-1)
            print_space(
                (max_width - (number_in_columns * WIDTH_OF_NODE)
                 )//(number_in_columns * 2)
            )

        out = '-'

        if num != None:
            out = str(num)
        print(('{0: >'+str(WIDTH_OF_NODE)+'}').format(out), end='')

        if level == math.ceil(math.log(length_of_arr, 2)):
            print_space(GAP)
        else:
            print_space(
                (max_width - (number_in_columns * WIDTH_OF_NODE))//number_in_columns
            )
    print('')


def print_space(width: int):
    for _ in range(width):
        print(' ', end='')
