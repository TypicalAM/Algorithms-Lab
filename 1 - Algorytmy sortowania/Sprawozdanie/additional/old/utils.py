'''Utils for the testing sorting algorithms project'''

import time
import inspect
from enum import Enum
import numpy as np

recursive = ('heap','merge','quickmid','quicktop')
class Feature(Enum):
    '''Represents the randomizer features'''
    RANDOM, NEARLY_SORTED, LARGE, SMALL = range(4)
def time_all_methods(exclusions: tuple):
    '''A class decorator which applies the timing decorator to all methods'''
    def decorate(cls):
        for name, fn in inspect.getmembers(cls, inspect.isfunction):
            if name not in exclusions:
                setattr(cls, name, timing(fn))
        return cls
    return decorate

def timing(func):
    '''Decorator to measure the time taken to sort'''
    def wrapper(*arg, **kw):
        start = time.time()
        res = func(*arg, **kw)
        end = time.time()-start
        return (end,res)
    return wrapper

def generate_array(size: int, feature: int) -> np.ndarray:
    '''Generate an array of integers from 1 to n of size n'''
    match feature:
        case Feature.RANDOM:
            return np.random.randint(1,size+1,size)
        case Feature.NEARLY_SORTED:
            arr = np.arange(1,size+1)
            for i in range(0,size,10):
                val , val2 = np.random.randint(i,i+9,2)
                arr[val], arr[val2] = arr[val2], arr[val]
            return arr
        case Feature.LARGE:
            return np.random.randint(1, 100*size+1, size)
        case Feature.SMALL:
            upper = int(0.01*size+1)
            return np.random.randint(1, upper, size)

def format_results(results: list, tests: tuple) -> list:
    '''Format the data so that it can be written to a file'''
    data = []
    data.append(list(map(str,tests)))
    data[0].insert(0,'')
    for result in results:
        sort_name, times = result[0], result[1]
        row = [sort_name] + [format(test_time,'0.10f') for test_time in times]
        data.append(row)

    return data

def write_to_file(filename: str, tests: tuple, results: list) -> None:
    '''Write the data to csv format'''
    data = format_results(results, tests)

    with open(filename, 'w', encoding="utf-8") as file:
        for row in data:
            line = ','.join(row) + '\n'
            file.write(line)

def get_methods(cls, inclusions) -> list:
    '''Get the methods for a class'''
    return [(name, func) for name, func in inspect.getmembers(cls, inspect.isfunction) if name in inclusions]

def recursive_timing(name, func, array):
    start = time.time()
    res = func(array) if name not in ['quicktop','quickmid'] else func(array, 0, len(array)-1)
    end = time.time()-start
    return (end, res)
