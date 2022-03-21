def insertion(arr):
    for i in range(1, len(arr)):
        cur=arr[i]
        index=i
        while index>0 and arr[index-1]>cur:
            arr[index]=arr[index-1]
            index-=1
        arr[index]=cur
    return arr

def selection(arr):
    end=len(arr)
    for i in range(end):
        m=i
        for j in range(i+1, end):
            if arr[j]<arr[m]:
                m=j
        arr[i],arr[m]=arr[m],arr[i]
    return arr

def bubble(arr):
    flag=1
    while(flag):
        flag=0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=1
    return arr

def counting(arr):
    maxv=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxv:
            maxv=arr[i]
    counter=[0 for _ in range(maxv+1)]
    result=[0] * len(arr)
    for i in arr:
        counter[i]+=1
    for i in range(1,maxv):
        counter[i+1]+=counter[i]
    for i in range(len(arr)):
        result[counter[arr[i]]-1]=arr[i]
        counter[arr[i]]-=1
    return result

def merge(arr):
    if len(arr)>1:
        #dividing
        mid=len(arr)//2
        left=arr[:mid].copy()
        right=arr[mid:].copy()
        merge(left)
        merge(right)
        i=j=c=0
        #sorting
        while(i<len(left) and j<len(right)):
            if left[i]<right[j]:
                arr[c]=left[i]
                i+=1
            else:
                arr[c]=right[j]
                j+=1
            c+=1
        #leftovers
        for x in range(i,len(left)):
            arr[c]=left[x]
            c+=1
        for x in range(j,len(right)):
            arr[c]=right[x]
            c+=1
    return arr

def quickmid(arr,s,e):
    pivot=arr[(s+e)//2]
    i=s
    j=e
    if(s>=e):
        return
    while(i<=j):
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    quickmid(arr,s,j)
    quickmid(arr,i,e)
    return arr

def divide(arr,s,e):
    pivot=arr[e]
    i=s-1
    for j in range(s,e):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[e]=arr[e],arr[i+1]
    return i+1
def quicktop(arr,s,e):
    if s<e:
        pivot=divide(arr,s,e)
        quicktop(arr,s,pivot-1)
        quicktop(arr,pivot+1,e)
    return arr

def buildheap(arr,n,i):
    maxv=i
    a=2*i
    b=2*i+1
    if a<n and arr[i]<arr[a]:
        maxv=a
    if b<n and arr[maxv]<arr[b]:
        maxv=b
    if maxv!=i:
        arr[i],arr[maxv]=arr[maxv],arr[i]
        buildheap(arr,n,maxv)

def heap(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        buildheap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        buildheap(arr,i,0)
    return arr

algorithms = [insertion, selection, bubble, counting, merge, quickmid, quicktop, heap]
