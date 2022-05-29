import itertools
import random
import time

maxVal=0
maxSize=0
class Node:
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
        global maxSize
        global maxVal
        for i in range(len(path)):
            if path[i]==1:
                size+=items[i][0]
                val+=items[i][1]
        if val>maxVal: maxVal=val
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
class Backpack:
    def generate_items(n: int,size: int,SIZE: int,value: int,VALUE: int):
        items=[]
        for _ in range(n):
            item=[random.randrange(size,SIZE+1),random.randrange(value,VALUE+1)]
            items.append(item)
        return items

    def print_items(items):
        print("size:  ",end=" ")
        for i in range(len(items)):
            print(items[i][0],end=",  ")
        print()
        print("value: ",end=" ")
        for i in range(len(items)):
            print(items[i][1],end=",  ")
        print()

    def generate_keys(n):
        keys=[]
        for i in itertools.product([1,0],repeat=n):
            i=list(i)
            keys.append(i)
        return keys

    def print_keys(keys):
        l=len(keys)
        s=len(keys[0])
        for i in range(l):
            for j in range(s):
                print(keys[i][j],end=", ")
            print()

    def BF(size,keys,items,give_key):
        max_value=0
        best_key=[]
        for key in keys:
            total_size=0
            total_value=0
            for i in range(len(key)):
                if key[i]:
                    total_size+=items[i][0]
                    total_value+=items[i][1]
            if total_size<=size:
                if total_value>max_value:
                    max_value=total_value
                    best_key=key.copy()
        if give_key:
            return [max_value,best_key]
        else:
            return max_value


    def packitup(self,n,b,size,SIZE,value,VALUE):
        global maxSize
        global maxVal
        root=Node('s',0)
        print("Generating items...\n")
        items=self.generate_items(n,size,SIZE,value,VALUE)
        print('Generated items:')
        self.print_items(items)
        print()
        print("Generating keys...\n")
        start=time.time()
        keys=self.generate_keys(n)
        print("Generated",len(keys),"possible arrangements")
        print("Calculating BF1...\n")
        print("Best solution for BF1 is:",self.BF(b,keys,items,0))
        print("\nIt took",time.time()-start,"seconds to calculate\n\n")
        print("Generating binary tree for BF2...\n")
        root.growTree(n,root)
        start=time.time()
        print("Calculating BF2...\n")
        items.insert(0,[0,0]) #adding first empty item to list so root won't shit itself
        root.dfs(root,[],b,items)
        print("Best solution for BF2 is:",maxVal)
        print("\nIt took",time.time()-start,"seconds to calculate\n\n")        
backpack=Backpack
backpack.packitup(backpack,21,10,1,5,1,5)

