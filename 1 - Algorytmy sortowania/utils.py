'''Utilities for the sorting project'''
import time
import logging
import random
from enum import Enum
import numpy as np

def get_logger():
    '''Retrieve the logger'''
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    logger.addHandler(handler)
    return logger
class Feature(Enum):
    '''Represents the randomizer features'''
    RANDOM, SORTED, NEARLY_SORTED, LARGE, SMALL, REVERSE = range(6)
def basic_timing(func, array) -> tuple:
    '''Basic function timing (decorators won't work due to recursion depth)'''
    name = func.__name__
    start = time.time()
    result = func(array) if name not in ('quickmid','quicktop') else func(array, 0, len(array)-1)
    end = time.time() - start
    return (end, result)

def write_to_file(filename: str, tests: tuple, results: list) -> None:
    '''Write the data to csv format'''
    data = format_results(results, tests)

    with open(filename, 'w', encoding="utf-8") as file:
        for row in data:
            line = ','.join(row) + '\n'
            file.write(line)

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

def generate_array(size: int, feature: int) -> np.ndarray:
    '''Generate an array of integers from 1 to n of size n'''
    match feature:
        case Feature.RANDOM:
            array = np.arange(1,size+1)
            np.random.shuffle(array)
            return array
        case Feature.LARGE:
            return np.random.randint(1, 100*size+1, size)
        case Feature.SMALL:
            upper = int(0.01*size+1)
            return np.random.randint(1, upper, size)
        case Feature.SORTED:
            return np.arange(1,size+1)
        case Feature.REVERSE:
            return np.arange(size,0,-1)
        case Feature.NEARLY_SORTED:
            arr = np.arange(1,size+1)
            for i in range(0,size,10):
                val , val2 = np.random.randint(i,i+9,2)
                arr[val], arr[val2] = arr[val2], arr[val]
            return arr
