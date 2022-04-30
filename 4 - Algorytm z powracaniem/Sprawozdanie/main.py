from typing import Dict
from utils import get_logger, write_to_file, average_score
from graphs import AdjencencyList

@average_score(3)
def run_test(testcase: int) -> Dict:
    '''Run a particular testcase'''
    times = {}
    logger.info("Running testcase \t\t(size: %d)", testcase)
    sparse_graph = AdjencencyList(size=testcase, density=0.2)
    times['Euler_0.2']          = sparse_graph.find_eulerian_cycle()
    times['First_Hamilton_0.2'] = sparse_graph.find_first_hamiltonian_cycle()
    times['All_Hamilton_0.2']   = sparse_graph.find_all_hamiltonian_cycles()
    logger.info("Running for lower density \t(edges: %d)",sparse_graph.edge_num)

    dense_graph = AdjencencyList(size=testcase, density=0.6)
    logger.info("Running for higher density \t(edges: %d)",dense_graph.edge_num)
    times['Euler_0.6']          = dense_graph.find_eulerian_cycle()
    times['First_Hamilton_0.6'] = dense_graph.find_first_hamiltonian_cycle()
    times['All_Hamilton_0.6']   = dense_graph.find_all_hamiltonian_cycles()
    return times

def main() -> None:
    '''Driver code'''
    tests = range(200,1200,200)
    try:
        results = [run_test(size) for size in tests]
        logger.info("Finished! Writing to a file...")
        write_to_file('out.csv', tests, results)
    except KeyboardInterrupt:
        logger.error("Keyboard interrupted")
    except Exception as e:
        logger.error("Encountered error: %s - %s",e.__class__.__name__, e)

logger = get_logger()
if __name__ == '__main__':
    main()
