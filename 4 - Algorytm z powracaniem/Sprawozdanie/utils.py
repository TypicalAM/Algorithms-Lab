'''Utilities for the hamiltonian and euclidian cycle algorithms'''
import time
import logging
from typing import Any, Callable, Dict

def average_score(amount_of_tries: int) -> Callable:
    def decorate(func: Callable) -> Callable:
        def wrapper(*arg, **kw) -> Dict:
            result = {}
            tries = [func(*arg, **kw) for _ in range(amount_of_tries)]
            for key in tries[0]:
                result[key] = sum([x[key] for x in tries])/amount_of_tries
            return result
        return wrapper
    return decorate

def timing(func: Callable) -> Callable:
    '''Decorator to measure the time of a function run'''
    def wrapper(*arg, **kw) -> tuple[float, Any]:
        start = time.time()
        res = func(*arg, **kw)
        end = time.time()-start
        return (end,res)
    return wrapper

def write_to_file(filename: str, tests: range, results: list) -> None:
    '''Write the data to csv format'''
    data = format_results(results, tests)

    with open(filename, 'w', encoding="utf-8") as file:
        for row in data:
            line = ','.join(row) + '\n'
            file.write(line)

def format_results(results: list, tests: range) -> list:
    '''Format the data so that it can be written to a file'''
    data = []
    data.append(list(map(str,tests)))
    data[0].insert(0,'')
    for key in results[0]:
        row = [key] + [format(result[key],'0.10f') for result in results]
        data.append(row)

    return data

def get_logger():
    '''Retrieve the logger'''
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    logger.addHandler(handler)
    return logger

