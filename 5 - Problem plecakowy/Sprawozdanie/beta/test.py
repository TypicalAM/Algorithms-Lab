class Node:
    LEVEL = 3
    def __init__(self,key, level=0, parent=None):
        self.left=None
        self.right=None
        self.val=key
        self.level = level
        self.parent = parent

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            self.inorder(node.right)
            print((node.val, node.level), end=" ")

    def expand(self, h):
        self.left=Node(1, Node.LEVEL-h, self)
        self.right=Node(0, Node.LEVEL-h, self)

    def growTree(self, h: int, node):
        if h>0:
            node.expand(h)
            self.growTree(h-1,node.left)
            self.growTree(h-1,node.right)

root = Node('start')
root.growTree(Node.LEVEL, root)
root.inorder(root)

weights = [3,5,4,9,1,2]
values = [10,20,30,40,50,60]
backpack = 10
solutions = []

# pierwszy: nie ma dzieci - patrzymy na wartosc drogi i dodajemy do rozwiaznia
# 
