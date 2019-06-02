from key_only_binary_tree import DATA, LEFT, RIGHT, print_tree, tree
from random import shuffle


def tree_insert(tree, data):
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


visited = []


def tree_dfs(tree):
    if tree == None or tree[DATA] in visited:
        return

    print(tree[DATA], end=' ')
    visited.append(tree[DATA])
    tree_dfs(tree[LEFT])
    tree_dfs(tree[RIGHT])


def tree_bfs(tree):
    should_visit = []
    print(tree[DATA], end=' ')
    should_visit.append(tree[LEFT])
    should_visit.append(tree[RIGHT])

    while should_visit:
        node = should_visit.pop(0)
        if node == None:
            continue
        print(node[DATA], end=' ')

        should_visit.append(node[LEFT])
        should_visit.append(node[RIGHT])


def preorder(tree):
    if tree == None:
        return

    print(tree[DATA], end=' ')
    preorder(tree[LEFT])
    preorder(tree[RIGHT])


def inorder(tree):
    if tree == None:
        return

    inorder(tree[LEFT])
    print(tree[DATA], end=' ')
    inorder(tree[RIGHT])


def postorder(tree):
    if tree == None:
        return

    postorder(tree[LEFT])
    postorder(tree[RIGHT])
    print(tree[DATA], end=' ')


# 무작위로 만들어진 이진 탐색 트리를 준비한다.
NUMBER_OF_NODES = 8
numbers = list(range(NUMBER_OF_NODES))
shuffle(numbers)

for num in numbers:
    tree_insert(tree, num)

print_tree(tree)


print('\nPreorder:')
preorder(tree)
print('\nInorder:')
inorder(tree)
print('\nPostorder:')
postorder(tree)
print('\n너비 우선 탐색:')
tree_bfs(tree)
print('\n깊이 우선 탐색:')
tree_dfs(tree)
print()
