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


print('너비 우선 탐색:')
tree_bfs(tree)
print('깊이 우선 탐색:')
tree_dfs(tree)
