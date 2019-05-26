from key_only_binary_tree import DATA, LEFT, RIGHT, print_tree, tree
from random import shuffle


def splay_tree_insert(tree, data):
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

    splaying(tree)


def splay_tree_find(tree, data):
    if not tree:
        return None

    parent = node = tree
    while node != None:
        parent = node

        if data < node[DATA]:
            node = node[LEFT]
        elif data > node[DATA]:
            node = node[RIGHT]

    rt = None
    if data < parent[DATA]:
        rt = parent[LEFT]
    elif data > parent[DATA]:
        rt = parent[RIGHT]

    splaying(tree)
    return rt


def splaying(tree):
    # TODO
    pass


def zig(tree):
    # TODO
    pass


def zag(tree):
    # TODO
    pass


# 무작위로 만들어진 이진 탐색 트리를 준비한다.
# NUMBER_OF_NODES = 10
# numbers = list(range(NUMBER_OF_NODES))
# shuffle(numbers)

# for num in numbers:
#     splay_tree_insert(tree, num)


# splay_tree_insert(tree, 0)
# print_tree(tree)
# splay_tree_insert(tree, -1)
# print_tree(tree)
# splay_tree_insert(tree, -2)
# print_tree(tree)

splay_tree_insert(tree, 0)
print_tree(tree)
splay_tree_insert(tree, -2)
print_tree(tree)
splay_tree_insert(tree, -1)
print_tree(tree)
splay_tree_insert(tree, -3)
print_tree(tree)
splay_tree_insert(tree, -4)
print_tree(tree)
