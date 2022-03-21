test=[-6,-7,0,4, 2, 5, 6, 1, 4, 6, 6, 4]

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
    minv=arr[0]
    maxv=arr[0]
    result=[]
    for i in range(len(arr)):
        if arr[i]<minv:
            minv=arr[i]
        if arr[i]>maxv:
            maxv=arr[i]
    counter = {}
    for i in range(minv,maxv+1):
        counter[i]=0
    for i in arr:
        counter[i]+=1
    for i in counter:
        for _ in range(counter[i]):
            result.append(i)
    return result

print(counting(test))
print(insertion(test))
print(selection(test))
print(bubble(test))
