from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node: Node):
    if node == None:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)


def postorder(node: Node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)


length = randint(1000, 10000)
max_num = 1000000
# length = 10
# max_num = 100
nums = list(randint(0, max_num) for _ in range(length))

root = Node(nums[0])
parent, node = None, None
for num in nums[1:]:
    parent = None
    node = root
    while node != None:
        parent = node
        if num < node.value:
            node = node.left
        else:
            node = node.right

    new_node = Node(num)
    if num > parent.value:
        parent.right = new_node
    else:
        parent.left = new_node

preorder(root)
