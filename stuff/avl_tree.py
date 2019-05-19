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
    height_diff = get_height_diff(tree)

    if height_diff > 1:
        if get_height_diff(tree[LEFT]) > 0:
            rotate_ll(tree)
        else:
            rotate_lr(tree)
    if height_diff < -1:
        if get_height_diff(tree[RIGHT]) < 0:
            rotate_rr(tree)
        else:
            rotate_rl(tree)


def rotate_ll(tree):
    left_parent = tree[LEFT][DATA]
    right_parent = tree[DATA]
    most_left_child = tree[LEFT][LEFT]
    middle_child = tree[LEFT][RIGHT]
    most_right_child = tree[RIGHT]

    tree[DATA] = left_parent
    tree[LEFT] = most_left_child
    if tree[RIGHT] == None:
        tree[RIGHT] = [
            right_parent,
            middle_child,
            most_right_child,
        ]


def rotate_rr(tree):
    pass


def rotate_lr(tree):
    pass


def rotate_rl(tree):
    pass


def get_height(tree):
    if tree == None:
        return 0

    height = 0
    left_height = get_height(tree[LEFT])
    right_height = get_height(tree[RIGHT])
    height = left_height if left_height > right_height else right_height

    return height + 1


def get_height_diff(tree):
    if tree == None:
        return 0

    return get_height(tree[LEFT]) - get_height(tree[RIGHT])


# 무작위로 만들어진 이진 탐색 트리를 준비한다.
# NUMBER_OF_NODES = 10
# numbers = list(range(NUMBER_OF_NODES))
# shuffle(numbers)

# for num in numbers:
#     avl_tree_insert(tree, num)


# avl_tree_insert(tree, 0)
# print_tree(tree)
# avl_tree_insert(tree, -1)
# print_tree(tree)
# avl_tree_insert(tree, -2)
# print_tree(tree)

avl_tree_insert(tree, 0)
print_tree(tree)
avl_tree_insert(tree, -2)
print_tree(tree)
avl_tree_insert(tree, -1)
print_tree(tree)
avl_tree_insert(tree, -3)
print_tree(tree)
avl_tree_insert(tree, -4)
print_tree(tree)
