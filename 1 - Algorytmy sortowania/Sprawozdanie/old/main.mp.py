'''Small program to test sorting algorithms'''

import multiprocessing
import numpy as np

from utils import Feature, generate_array, write_to_file, get_methods, recursive_timing, recursive
from sorting import Sort

def single_test(name ,func , tests , rand_feature, queue):
    '''Singleton test'''
    times = []
    for size in tests:
        array = generate_array(size, rand_feature)
        time_taken, _ = func(array) if name not in recursive else recursive_timing(name, func,array)
        times.append(time_taken)
#        print(f'[{name}]:\tn={size}\ttime={time_taken}s')
    queue.put((name,times))

def test_sorts(tests: tuple, inclusions: tuple, rand_feature) -> list:
    print(f'[main]:\t\tTesting for {len(tests)} array sizes')
    queue = multiprocessing.Queue()
    methods = get_methods(Sort, inclusions)
    for name, func in methods:
        print(f'[main]:\t\tRunning {name} sort')
        p = multiprocessing.Process(target=single_test, args=(name, func, tests, rand_feature, queue))
        p.start()

    results = []
    for _ in range(len(methods)):
        results.append(queue.get())
    return results

def main() -> None:
    '''Driver code'''
    tests = (1000,2000,3000)

    print('[main]:\t\tRunning test 2...')
    inclusions = ('bubble', 'counting', 'heap', 'insertion', 'merge', 'quickmid', 'selection')
    results = test_sorts(tests, inclusions, Feature.RANDOM)
    write_to_file('out_first.csv', tests, results)

    print('[main]:\t\tRunning test 3.1...')
    inclusions = ('quicktop','quickmid','insertion')
    results = test_sorts(tests, inclusions, Feature.RANDOM)
    write_to_file('out_second_random.csv', tests, results)

    print('[main]:\t\tRunning test 3.2...')
    results = test_sorts(tests, inclusions, Feature.NEARLY_SORTED)
    write_to_file('out_second_nearly.csv', tests, results)

    print('[main]:\t\tRunning test 4.1...')
    inclusions = ('counting', 'quickmid')
    results = test_sorts(tests, inclusions, Feature.LARGE)
    write_to_file('out_third_100n.csv', tests, results)

    print('[main]:\t\tRunning test 4.2...')
    results = test_sorts(tests, inclusions, Feature.SMALL)
    write_to_file('out_third_0.01n.csv', tests, results)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[main]\t\tExecution interrupted...')
