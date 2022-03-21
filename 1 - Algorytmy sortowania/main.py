'''Module to test different sorting algorithms'''
import multiprocessing as mp
from sorting import algorithms
from utils import Feature, basic_timing, generate_array, get_logger, write_to_file
import sys

def single_test(func, tests,rand_feature,queue):
    '''Singleton test'''
    times = []
    name = func.__name__
    for size in tests:
        time_avg = []
        for _ in range(3):
            array = generate_array(size, rand_feature)
            try:
                time_taken, _ = basic_timing(func, array)
            except RecursionError:
                logger.info('Recursion depth limit reached for test %s',size)
            else:
                time_avg.append(time_taken)
        avg_time = sum(time_avg)/3
        times.append(avg_time)

    logger.info("Tests finished for %s!",name)
    queue.put((name,times))

def testing_batch(tests, inclusions, rand_feature):
    '''Run sorting algorithms in parrallel with child process pool'''
    logger.info('Testing for %s array sizes',len(tests))
    queue = mp.Queue()
    functions = [func for func in algorithms if func.__name__ in inclusions]
    for func in functions:
        logger.info('Running %s sort', func.__name__)
        process = mp.Process(target=single_test, args=(func, tests, rand_feature, queue))
        process.start()

    results = [queue.get() for _ in functions]
    return results

def run(testname: str, tests: tuple):
    '''Run a specified testgroup'''
    match testname:
        case '2.0':
            inclusions = ('insertion','selection','bubble','counting','heap', 'merge', 'quickmid')
            results = testing_batch(tests, inclusions, Feature.RANDOM)
            write_to_file('out_2.0.csv', tests, results)
        case '2.1':
            inclusions = ('insertion','selection','bubble','counting','heap', 'merge', 'quickmid')
            results = testing_batch(tests, inclusions, Feature.SORTED)
            write_to_file('out_2.1.csv', tests, results)
        case '2.2':
            inclusions = ('insertion','selection','bubble','counting','heap', 'merge', 'quickmid')
            results = testing_batch(tests, inclusions, Feature.REVERSE)
            write_to_file('out_2.2.csv', tests, results)
        case '3.1':
            tests = (300,600,900,1200,1500,1800,2100,2400,2700,3000)
            inclusions = ('quicktop','quickmid','insertion')
            results = testing_batch(tests, inclusions, Feature.RANDOM)
            write_to_file('out_3.1.csv', tests, results)
        case '3.2':
            tests = (300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000)
            inclusions = ('quicktop','quickmid','insertion')
            results = testing_batch(tests, inclusions, Feature.SORTED)
            write_to_file('out_3.2.csv', tests, results)
        case '4.1':
            inclusions = ('counting', 'quickmid')
            results = testing_batch(tests, inclusions, Feature.LARGE)
            write_to_file('out_4.1.csv', tests, results)
        case '4.2':
            inclusions = ('counting', 'quickmid')
            results = testing_batch(tests, inclusions, Feature.SMALL)
            write_to_file('out_4.2.csv', tests, results)

def main() -> None:
    '''Driver code'''
    sys.setrecursionlimit(5000)
    tests = (1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000)
    for test in ['2.1']:
        logger.info('Running test %s...',test)
        run(test, tests)

logger = get_logger()
if __name__=='__main__':
    main()
