from key_only_binary_tree import DATA, LEFT, RIGHT, print_tree, tree
from random import shuffle


def avl_tree_insert(tree, data):
    if not tree:
        tree += [data, None, None]
        return

    parent = node = tree
    while node != None:
        parent = node

        if data < node[DATA]:
            node = node[LEFT]
        elif data > node[DATA]:
            node = node[RIGHT]

    if data < parent[DATA]:
        parent[LEFT] = [data, None, None]
    elif data > parent[DATA]:
        parent[RIGHT] = [data, None, None]

    rebalance(tree)


def rebalance(tree):
    pass  # TODO


# 무작위로 만들어진 이진 탐색 트리를 준비한다.
NUMBER_OF_NODES = 10
numbers = list(range(NUMBER_OF_NODES))
shuffle(numbers)

for num in numbers:
    avl_tree_insert(tree, num)

print_tree(tree)
