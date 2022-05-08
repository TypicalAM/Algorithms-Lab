from typing import Dict
from utils import GraphType, get_logger, write_to_file, average_score
from graphs import AdjencencyList, Euler, Hamilton

@average_score(3)
def run_test(testcase: int) -> Dict:
    times = {}
    small_test = testcase < 13

    logger.info("Running testcase \t\t(size: %d)", testcase)
    G = AdjencencyList(testcase, 0.2)

    times['Euler_0.2'], _               = Euler.check(G)
    times['First_Hamilton_0.2'], _      = Hamilton.check(G)
    times['All_Hamilton_0.2'], cycles   = Hamilton.check(G, find_all=True) if small_test else (0, 0)
    times['Cycles_0.2']                 = cycles

    logger.info("Running for lower density \t(edges: %d)",G.edge_num)
    logger.info("Found hamiltonian cycles:\t %d", cycles)

    G = AdjencencyList(testcase, 0.6)

    times['Euler_0.6'], _               = Euler.check(G)
    times['First_Hamilton_0.6'], _      = Hamilton.check(G)
    times['All_Hamilton_0.6'], cycles   = Hamilton.check(G, find_all=True) if small_test else (0, 0)
    times['Cycles_0.6'] = cycles

    logger.info("Running for higher density \t(edges: %d)",G.edge_num)
    logger.info("Found hamiltonian cycles:\t %d", cycles)

    return times

def main() -> None:
    '''Driver code'''
    tests = (7,8,9,10,11,12,20,30,40,50,100,200,300,400,500)
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
