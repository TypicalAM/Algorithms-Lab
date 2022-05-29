import random
import itertools
from abc import ABCMeta, abstractstaticmethod
from representation import Courier
from utils import timing

class Strategy(metaclass=ABCMeta):
    '''A strategy interface class from which all solutions should inherit from'''

    @abstractstaticmethod
    def get_best_value(courier) -> int:
        '''Takes an instance of the courier and computes the maximum possible value'''
        ...

class Node:
    maxval = 0

    def __init__(self,key,level):
        self.left=None
        self.right=None
        self.val=key
        self.level=level
        self.flag=0

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print((node.val,node.level),end=' ')

    def expand(self):
        self.left=Node(1,self.level+1)
        self.right=Node(0,self.level+1)

    def growTree(self, h: int, node):
        if h>0:
            node.expand()
            self.growTree(h-1,node.left)
            self.growTree(h-1,node.right)

    def checkInside(self,path,items):
        size=0
        val=0
        for i in range(len(path)):
            if path[i]==1:
                size+=items[i][0]
                val+=items[i][1]
        if val>Node.maxval: Node.maxval=val
        return size

    def dfs(self,node,path,maxSize,items):
        if not node.flag:
            path.append(node.val)
        else:
            path.pop()
            return
        if node.left==None:
            node.flag=1
            self.checkInside(path,items)
            path.pop()
            return

        if self.checkInside(path,items)+items[node.level+1][0]<=maxSize:
            self.dfs(node.left,path,maxSize,items)
        self.dfs(node.right,path,maxSize,items)
        path.pop()

class HeuristicRandom(Strategy):
    @timing
    @staticmethod
    def get_best_value(courier: Courier) -> int:
        available = courier.capacity
        items_added = []

        while True:
            index = random.randint(0,courier.size-1)
            if index not in items_added:
                if available < courier.weights[index]:
                    break
                items_added.append(index)
                available-=courier.weights[index]

#        print(f'{items_added=}') # FIX FIX
        return sum([courier.values[i] for i in items_added])

class HeuristicByValue(Strategy):
    @timing
    @staticmethod
    def get_best_value(courier: Courier) -> int:
        available = courier.capacity
        items_added = []

        sorted_values, sorted_weights = (tuple(t) for t in zip(*sorted(zip(courier.values, courier.weights),reverse=True)))
        for i in range(courier.size):
            if available < sorted_weights[i]:
                break
            items_added.append(i)
            available-=sorted_weights[i]
        return sum([sorted_values[i] for i in items_added])

class HeuristicByWeight(Strategy):
    @timing
    @staticmethod
    def get_best_value(courier: Courier) -> int:
        available = courier.capacity
        items_added = []

        sorted_weights, sorted_values = (tuple(t) for t in zip(*sorted(zip(courier.weights, courier.values))))
        for i in range(courier.size):
            if available < sorted_weights[i]:
                break
            items_added.append(i)
            available-=sorted_weights[i]
#        print(f'{items_added=}')
        return sum([sorted_values[i] for i in items_added])

class HeuristicByProportion(Strategy):

    @timing
    @staticmethod
    def get_best_value(courier: Courier) -> int:
        available = courier.capacity
        items_added = []

        sort_order = tuple(range(courier.size))
        proportions = [round(courier.values[i]/courier.weights[i]) for i in sort_order]
        proportions , sort_order = (tuple(t) for t in zip(*sorted(zip(proportions, sort_order),reverse=True)))
        sorted_weights = [courier.weights[i] for i in sort_order]
        sorted_values = [courier.values[i] for i in sort_order]
        for i in range(courier.size):
            if available < sorted_weights[i]:
                break
            items_added.append(i)
            available-=sorted_weights[i]
#        print(f'{items_added=}')
        return sum([sorted_values[i] for i in items_added])

class Dynamic(Strategy):

    @timing
    @staticmethod
    def get_best_value(courier: Courier) -> int:
       return(Dynamic.helper(courier, courier.size, courier.capacity))

    @staticmethod
    def helper(courier: Courier, index: int, available: int):
        if not available or not index:
            return 0
        if courier.weights[index-1] > available:
            return Dynamic.helper(courier, index-1, available)
        return max(
                Dynamic.helper(courier, index-1, available),
                Dynamic.helper(courier, index-1, available-courier.weights[index-1]) + courier.values[index-1]
                )

    @staticmethod
    def display_matrix(courier: Courier) -> None:
        res = []
        for i in range(courier.size+1):
            res.append([])
            for j in range(courier.capacity+1):
                res[i].append(Dynamic.helper(courier, i, j))
        for row in res:
            print(*row)

class BruteForce(Strategy):
    '''Use backtracking to brute force the best result'''

    @staticmethod
    def generate_candidates(courier: Courier) -> list:
        return [list(i) for i in itertools.product([1,0],repeat=courier.size)]

    @timing
    @staticmethod
    def get_best_value(courier: Courier) -> int:
        max_val = 0
        for possible_solution in BruteForce.generate_candidates(courier):
            weight = sum(
                    courier.weights[k] for k,i
                    in enumerate(possible_solution) if i
                    )
            if weight <= courier.capacity:
                max_val = max(
                        max_val,
                        sum(
                            courier.values[k] for k, i
                            in enumerate(possible_solution) if i
                            )
                        )
        return max_val

class Backtracking(Strategy):
    '''Strategy using an algorithm with backtracking'''

    @staticmethod
    def get_best_value(courier: Courier) -> tuple[float, int]:
        Node.maxval=0
        root=Node('s',0)
        root.growTree(courier.size,root)
        courier.weights = [0]+list(courier.weights)
        courier.values = [0]+list(courier.values)
        return Backtracking.helper(courier, root)

    @timing
    @staticmethod
    def helper(courier: Courier, root: Node):
        root.dfs(root,[],courier.capacity,list(zip(courier.weights,courier.values)))
        courier.weights = courier.weights[1:]
        courier.values = courier.values[1:]
        return Node.maxval



