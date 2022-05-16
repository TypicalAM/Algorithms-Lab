import itertools
import random
import time

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

def BF(size,keys,items,give_key):
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
    if give_key:
        return [max_value,best_key]
    else:
        return max_value


def smortBF(n,b,items):
    if n==0 or b==0:
        return 0
    if items[n-1][0]>b:
        return smortBF(n-1,b,items)
    else:
        return max(items[n-1][1]+smortBF(n-1,b-items[n-1][0],items),smortBF(n-1,b,items))


def packitup(n,b,size,SIZE,value,VALUE):
    print("Generating items...\n")
    items=generate_items(n,size,SIZE,value,VALUE)
    print('\nGenerated items:')
    print_items(items)
    print()
    start=time.time()
    print("Generating keys...\n")
    keys=generate_keys(n)
    print("Generated",len(keys),"possible arrangements")
    print("Calculating BF1...\n")
    print("Best solution for BF1 is:",BF(b,keys,items,0))
    print("\nIt took",time.time()-start,"seconds to calculate\n")
    start=time.time()
    print("Calculating BF2...\n")
    print("Best solution for BF2 is:",smortBF(n,b,items))
    print("It took",time.time()-start,"seconds to calculate")


packitup(26,50,1,10,1,10)
