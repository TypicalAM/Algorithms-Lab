import itertools
import random

def generate_items(n,size,SIZE,value,VALUE):
    items=[]
    for _ in range(n):
        item=[random.randrange(size,SIZE),random.randrange(value,VALUE)]
        items.append(item)
    return items

def print_items(items):
    print("size: ",end=" ")
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

def backpack(size,keys,items):
    result=[]
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
    return [max_value,best_key]

def packitup(n,l,size,SIZE,value,VALUE):
    items=generate_items(n,size,SIZE,value,VALUE)
    keys=generate_keys(n)
    print("Generated",len(keys),"possible arrangements")
    print('\nGenerated items:')
    print_items(items)
    print("Solution [value, key]:",backpack(l,keys,items))
    
packitup(5,10,1,10,10,20)



