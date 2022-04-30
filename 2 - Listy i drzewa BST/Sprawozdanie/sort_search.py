'''Sorting and searching algorithms for the bst project'''
import numpy as np
from utils import timing
# pylint: disable=invalid-name

def quicksort(arr,left,right):
    '''Quicksort algorithm with pivot element in the middle'''
    pivot=arr[(left+right)//2]
    i=left
    j=right
    if left>=right:
        return
    while i<=j:
        while arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    quicksort(arr,left,j)
    quicksort(arr,i,right)
    return arr

def linear_search(arr, elem: int):
    '''Search for an element in an array linearly'''
    return any(i == elem for i in arr)

def binary_search(arr, elem: int, left: int, right: int):
    '''Search for an element in a sorted array using binary search'''
    if left > right:
        return 0
    mid = (left+right)//2
    if arr[mid] == elem:
        return mid+1
    if arr[mid] > elem:
        return binary_search(arr, elem, left, mid-1)
    return binary_search(arr, elem, mid+1, right)

@timing
def b_in_a(A, B):
    '''Check if all B elements are in A'''
    return all(linear_search(A,elem) for elem in B)

@timing
def a_in_b(A, B):
    '''Check if all A elements are in B'''
    return all(binary_search(B,elem,0,len(B)-1) for elem in A)

@timing
def x_in_TX(X, tree_X):
    '''Check if all elements from an array are in the tree'''
    return all(tree_X.search(elem).data == elem for elem in X)

@timing
def copy_and_sort(A) -> np.ndarray:
    '''Copy and sort an array'''
    arr = A.copy()
    arr = quicksort(arr,0,len(arr)-1)
    return arr
