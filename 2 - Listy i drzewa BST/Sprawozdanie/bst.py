'''Module to implement the binary search tree structure'''
from enum import Enum

from utils import timing

# pylint: disable=inconsistent-return-statements
class Notation(Enum):
    '''Represents the pprint features for BST'''
    INFIX, POSTFIX, PREFIX = range(3)

class Node:
    '''A single node in a binary tree'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'Node({self.data})'

    def insert(self,data):
        '''Insert a node into the binary tree'''
        if data == self.data:
            return False
        if data < self.data:
            if self.left:
                return self.left.insert(data)
            self.left = Node(data)
            return True
        if self.right:
            return self.right.insert(data)
        self.right = Node(data)
        return True

    def search(self,elem: int):
        '''Search in the binary tree'''
        if not self:
            return 0
        if self.data == elem:
            return self
        if self.data < elem and self.right:
            return self.right.search(elem)
        if self.left:
            return self.left.search(elem)

    def depth(self):
        '''Check the depth of the tree'''
        if self.left and self.right:
            left_depth = self.left.depth()
            right_depth = self.right.depth()
            return left_depth+1 if left_depth > right_depth else right_depth+1
        if self.left:
            return self.left.depth()+1
        if self.right:
            return self.right.depth()+1
        return 1

    def inorder(self):
        '''Traverse the tree inorder'''
        if self.left:
            yield from self.left.inorder()
        yield self.data
        if self.right:
            yield from self.right.inorder()

    def preorder(self):
        '''Traverse the tree preorder'''
        yield self.data
        if self.left:
            yield from self.left.preorder()
        if self.right:
            yield from self.right.preorder()

    def postorder(self):
        '''Traverse the tree postorder'''
        if self.left:
            yield from self.left.postorder()
        if self.right:
            yield from self.right.postorder()
        yield self.data

class Tree:
    '''The binary tree structure'''
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        '''Create a Node and insert it into the binary tree'''
        if self.root:
            return self.root.insert(data)
        self.root = Node(data)
        return True

    def display(self, notation):
        '''Display the binary tree depending on the notation'''
        if self.root:
            match notation:
                case Notation.INFIX:
                    yield from self.root.inorder()
                case Notation.PREFIX:
                    yield from self.root.preorder()
                case Notation.POSTFIX:
                    yield from self.root.postorder()

    def search(self, elem: int):
        '''Search through the binary tree'''
        if self.root:
            return self.root.search(elem)
    def check(self, sorted_arr):
        '''Check if the tree is assembled correctly'''
        assert all(sorted_arr[k] == v for k, v in enumerate(self.display(Notation.INFIX)))
    @timing
    @staticmethod
    def from_array(arr):
        '''Create a binary tree from an array'''
        binary_tree = Tree()
        _ = (binary_tree.insert(elem) for elem in arr)
        return binary_tree
    def checkdepth(self) -> int:
        '''Check the depth of the tree'''
        if not self.root:
            return 0
        return self.root.depth()
    @staticmethod
    def convert_array(arr):
        '''Convert a sorted array so it can be used to create a perfectly balanced tree'''
        if not arr:
            return
        new_arr = []
        mid = len(arr)//2
        new_arr.append(arr[mid])
        new_arr.append(Tree.convert_array(arr[:mid]))
        new_arr.append(Tree.convert_array(arr[mid+1:]))
        new_arr = [x for x in new_arr if x]
        if len(new_arr) > 1:
            return new_arr
        return new_arr[0]
