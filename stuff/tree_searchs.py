DATA = 0
LEFT = 1
RIGHT = 2


tree = [
    'a',
    [
        'b',
        None,
        [
            'c',
            None,
            None
        ]
    ],
    [
        'd',
        [
            'e',

            [
                'f',
                None,
                None,
            ],
            None,
        ],
        [
            'g',
            None,
            None,
        ],
    ]
]

visited = []


def tree_dfs(tree):
    if tree == None or tree[DATA] in visited:
        return

    print(tree[DATA])
    visited.append(tree[DATA])
    tree_bfs(tree[LEFT])
    tree_bfs(tree[RIGHT])


should_visit = []


def tree_bfs(tree):
    print(tree[DATA])
    should_visit.append(tree[LEFT])
    should_visit.append(tree[RIGHT])

    while should_visit:
        node = should_visit.pop(0)
        if node == None:
            continue
        print(node[DATA])

        should_visit.append(node[LEFT])
        should_visit.append(node[RIGHT])


def preorder(tree):
    if tree == None:
        return

    print(tree[DATA])
    preorder(tree[LEFT])
    preorder(tree[RIGHT])


def inorder(tree):
    if tree == None:
        return

    inorder(tree[LEFT])
    print(tree[DATA])
    inorder(tree[RIGHT])


def postorder(tree):
    if tree == None:
        return

    postorder(tree[LEFT])
    postorder(tree[RIGHT])
    print(tree[DATA])


print('너비 우선 탐색:')
tree_bfs(tree)
print('깊이 우선 탐색:')
tree_dfs(tree)
print('Preorder:')
preorder(tree)
print('Inorder:')
inorder(tree)
print('Postorder:')
postorder(tree)
