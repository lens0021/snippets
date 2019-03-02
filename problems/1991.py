# https://www.acmicpc.net/problem/1991

number_of_nodes = int(input())

tree = {}
for _ in range(number_of_nodes):
    parent, left, right = input().split(' ')
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[parent] = (left, right)


def preorder(parent):
    left, right = tree[parent]
    print(parent, end='')
    if left != None:
        preorder(left)
    if right != None:
        preorder(right)


def inorder(parent):
    left, right = tree[parent]
    if left != None:
        inorder(left)
    print(parent, end='')
    if right != None:
        inorder(right)


def postorder(parent):
    left, right = tree[parent]
    if left != None:
        postorder(left)
    if right != None:
        postorder(right)
    print(parent, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
