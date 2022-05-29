from typing import Dict

from strategy import Dynamic as PD
from strategy import BruteForce as BF1
from strategy import Backtracking as BF2
from strategy import HeuristicRandom as GH1
from strategy import HeuristicByWeight as GH2
from strategy import HeuristicByValue as GH3
from strategy import HeuristicByProportion as GH4

from utils import average_score, get_logger, write_to_file
from representation import Courier


@average_score(1)
def run_testcase_2(testcase: int) -> Dict:
    """Run an int testcase for the second exercise"""
    logger.info("Running testcase for %d", testcase)
    times = {}

    c = Courier(testcase, 0.5)
    times["PD"], _ = PD.get_best_value(c)
    times["BF1"], _ = BF1.get_best_value(c)
    times["BF2"], _ = BF2.get_best_value(c)
    times["GH4"], _ = GH4.get_best_value(c)
    logger.info("Finished testcase for %d", testcase)

    return times


@average_score(1)
def run_testcase_3(testcase: int) -> Dict:
    """Run an int testcase for the third exercise"""
    logger.info("Running testcase for %d", testcase)
    times = {}

    c = Courier(testcase, 0.25)
    times["PD"], _ = PD.get_best_value(c)
    times["BF1"], _ = BF1.get_best_value(c)
    times["BF2"], _ = BF2.get_best_value(c)
    times["GH4"], _ = GH4.get_best_value(c)

    c = Courier(testcase, 0.75)
    times["PD_2"], _ = PD.get_best_value(c)
    times["BF1_2"], _ = BF1.get_best_value(c)
    times["BF2_2"], _ = BF2.get_best_value(c)
    times["GH4_2"], _ = GH4.get_best_value(c)

    return times


@average_score(1)
def run_testcase_4(testcase: int) -> Dict:
    """Run an int testcase for the fourth exercise"""
    logger.info("Running testcase for %d", testcase)
    gh_values = [0, 0, 0, 0]
    times = {}

    logger.info("Running for density modifier of 25")
    c = Courier(testcase, 0.25)
    times["PD_25"], target = PD.get_best_value(c)
    times["GH1_25"], gh_values[0] = GH1.get_best_value(c)
    times["GH2_25"], gh_values[1] = GH2.get_best_value(c)
    times["GH3_25"], gh_values[2] = GH3.get_best_value(c)
    times["GH4_25"], gh_values[3] = GH4.get_best_value(c)
    times["GH1_25_BLAD"] = (target - gh_values[0]) / target
    times["GH2_25_BLAD"] = (target - gh_values[1]) / target
    times["GH3_25_BLAD"] = (target - gh_values[2]) / target
    times["GH4_25_BLAD"] = (target - gh_values[3]) / target

    logger.info("Running for density modifier of 50")
    c = Courier(testcase, 0.50)
    times["PD_50"], target = PD.get_best_value(c)
    times["GH1_50"], gh_values[0] = GH1.get_best_value(c)
    times["GH2_50"], gh_values[1] = GH2.get_best_value(c)
    times["GH3_50"], gh_values[2] = GH3.get_best_value(c)
    times["GH4_50"], gh_values[3] = GH4.get_best_value(c)
    times["GH1_50_BLAD"] = (target - gh_values[0]) / target
    times["GH2_50_BLAD"] = (target - gh_values[1]) / target
    times["GH3_50_BLAD"] = (target - gh_values[2]) / target
    times["GH4_50_BLAD"] = (target - gh_values[3]) / target

    logger.info("Running for density modifier of 75")
    c = Courier(testcase, 0.75)
    times["PD_75"], target = PD.get_best_value(c)
    times["GH1_75"], gh_values[0] = GH1.get_best_value(c)
    times["GH2_75"], gh_values[1] = GH2.get_best_value(c)
    times["GH3_75"], gh_values[2] = GH3.get_best_value(c)
    times["GH4_75"], gh_values[3] = GH4.get_best_value(c)
    times["GH1_75_BLAD"] = (target - gh_values[0]) / target
    times["GH2_75_BLAD"] = (target - gh_values[1]) / target
    times["GH3_75_BLAD"] = (target - gh_values[2]) / target
    times["GH4_75_BLAD"] = (target - gh_values[3]) / target

    return times


def main() -> None:
    tests = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    logger.info("Running the second exercise")
    results = [run_testcase_2(test) for test in tests]
    logger.info("Finished, writing to file...")
    write_to_file("out_2.csv", tests, results)

    tests = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    logger.info("Running the third exercise")
    results = [run_testcase_3(test) for test in tests]
    logger.info("Finished, writing to file...")
    write_to_file("out_3.csv", tests, results)

    tests = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
    logger.info("Running the fourth exercise")
    results = [run_testcase_4(test) for test in tests]
    logger.info("Finished, writing to file...")
    write_to_file("out_4.csv", tests, results)


logger = get_logger()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Execution stopped (Keyboard interruption)")
    except Exception:
        logger.info("Enountered an error on the way")
