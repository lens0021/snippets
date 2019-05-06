from key_value_binary_tree import DATA, LEFT, RIGHT, KEY, VALUE, print_tree, tree


def tree_add(tree, key, value):
    if not tree:
        tree += [[key, value], None, None]
        return

    parent = node = tree
    while node != None:
        parent = node

        if key < node[DATA][KEY]:
            node = node[LEFT]
        elif key > node[DATA][KEY]:
            node = node[RIGHT]

    if key < parent[DATA][KEY]:
        parent[LEFT] = [[key, value], None, None]
    elif key > parent[DATA][KEY]:
        parent[RIGHT] = [[key, value], None, None]


def tree_search(tree, key):
    node = tree
    while node != None and node[DATA] != None:
        if key == node[DATA][KEY]:
            return node[DATA][VALUE]

        if key < node[DATA][KEY]:
            node = node[LEFT]
        elif key > node[DATA][KEY]:
            node = node[RIGHT]

    return None


def tree_update(tree, key, value):
    node = tree
    while node != None and node[DATA] != None:
        if key == node[DATA][KEY]:
            node[DATA][VALUE] = value
            return

        if key < node[DATA][KEY]:
            node = node[LEFT]
        elif key > node[DATA][KEY]:
            node = node[RIGHT]


def tree_delete(tree, key):
    # 지울 노드와 그 부모를 찾는다
    parent = node = tree
    while node != None and node[DATA][KEY] != key:
        parent = node
        if key < node[DATA][KEY]:
            node = node[LEFT]
        elif key > node[DATA][KEY]:
            node = node[RIGHT]

    # 노드에게 서브트리가 있는지에 따라 분기
    number_of_children = 0
    if node[LEFT] != None:
        number_of_children += 1
    if node[RIGHT] != None:
        number_of_children += 1

    # 노드에게 서브트리가 없다면 부모에서 노드를 지운다.
    if number_of_children == 0:
        if key < parent[DATA][KEY]:
            parent[LEFT] = None
        elif key > parent[DATA][KEY]:
            parent[RIGHT] = None
    # 노드에게 서브트리가 하나 있다면 부모에 서브트리를 바로 잇는다
    elif number_of_children == 1:
        child = node[LEFT] if node[LEFT] != None else node[RIGHT]
        if child[DATA][KEY] < parent[DATA][KEY]:
            parent[LEFT] = child
        elif child[DATA][KEY] > parent[DATA][KEY]:
            parent[RIGHT] = child
    # 노드에게 서브트리가 둘 있었다면 오른쪽 서브트리의 가장 왼쪽 노드를 새 부모로 쓰기로 한다.
    elif number_of_children == 2:
        succ, succ_p = node[RIGHT], node
        while succ[LEFT] != None:
            succ_p = succ
            succ = succ[LEFT]

        if succ_p[LEFT] == succ:
            succ_p[LEFT] = succ[RIGHT]
        else:
            succ_p[RIGHT] = succ[RIGHT]
        node[DATA] = succ[DATA]


height = 4

tree_add(tree, 'if', '만약')
tree_add(tree, 'also', '또한')
tree_add(tree, 'while', '동안')
tree_add(tree, 'for', 'para')
tree_add(tree, 'zero', '제로')
tree_add(tree, 'when', '언제')

print_tree(tree, height)

print('\nalso 삭제')
tree_delete(tree, 'also')
print_tree(tree, height)

print('\nwhile 삭제')
tree_delete(tree, 'while')
print_tree(tree, height)

print('\nfor 변경')
tree_update(tree, 'for', '...에 대한')
print_tree(tree, height)

print('\n추가:switch, break, continue')

tree_add(tree, 'switch', '스위치')
tree_add(tree, 'break', '단절')
tree_add(tree, 'continue', '잇다')
print_tree(tree, height)
