'''A script to test out bst algorithms and searching'''
from typing import Dict
from utils import average_score, flatten, generate_array, Feature, get_logger, write_to_file
from bst import Notation, Tree
from sort_search import b_in_a, a_in_b, x_in_TX, copy_and_sort

@average_score(1)
def run_test(testcase: int) -> Dict:
    '''Run a particular testcase'''

    # pylint: disable=invalid-name,unpacking-non-sequence

    times = {}
    logger.info('Running testcase for %d',testcase)
    A = generate_array(testcase, Feature.RANDOM)
    times['Creation_B'],B = copy_and_sort(A)

    times['Search_A'],_=b_in_a(A,B)
    times['Search_B'],_=a_in_b(A,B)

    better_B=flatten(Tree.convert_array(B))
    times['Creation_Tree_A'],tree_A= Tree.from_array(A)
    times['Creation_Tree_B'],tree_B= Tree.from_array(better_B)
    tree_A.check(B)
#   print(*tree_A.display(Notation.INFIX))

    times['Search_Tree_A'],_= x_in_TX(A, tree_A)
    times['Search_Tree_B'],_= x_in_TX(B, tree_B)

    logger.info('The depth of Tree A is equal to %d', tree_A.check_depth())
    logger.info('The depth of Tree B is equal to %d', tree_B.check_depth())

    return times

def main() -> None:
    '''Driver code'''
    tests = (1023,4095,8191)
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
