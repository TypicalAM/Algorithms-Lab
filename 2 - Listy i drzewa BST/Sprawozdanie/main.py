'''A script to test out bst algorithms and searching'''
from utils import flatten, generate_array, Feature, get_logger, write_to_file
from bst import Tree
from sort_search import b_in_a, a_in_b, x_in_TX, copy_and_sort

def run_test(testcase: int) -> list:
    '''Run a particular testcase'''

    # pylint: disable=invalid-name,unpacking-non-sequence
    logger.info('Running testcase for %d',testcase)
    times = {}
    A = generate_array(testcase, Feature.RANDOM)
    times['Creation_B'],B = copy_and_sort(A)

    times['Search_A'],_=b_in_a(A,B)
    times['Search_B'],_=a_in_b(A,B)

    better_B=flatten(Tree.convert_array(B))
    times['Creation_Tree_A'],tree_A= Tree.from_array(A)
    times['Creation_Tree_B'],tree_B= Tree.from_array(better_B)

    times['Search_Tree_A'],_= x_in_TX(A, tree_A)
    times['Search_Tree_B'],_= x_in_TX(B, tree_B)

    logger.info('The depth of Tree A is equal to %d', tree_A.check_depth())

    return times

def main() -> None:
    '''Driver code'''
    tests = range(10000,52500,2500)
    try:
        results = [run_test(test) for test in tests]
    except KeyboardInterrupt:
        logger.error("Keyboard interrupted")
    else:
        logger.info('Finished! Writing to file...')
        write_to_file('out.csv', tests, results)

logger = get_logger()
if __name__ == '__main__':
    main()
