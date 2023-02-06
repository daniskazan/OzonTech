from collections import namedtuple, Counter
from typing import List

TestCase = namedtuple("TestCase", ["n", ["times"]])
CORRECT_AMOUNT = {1: 4, 2: 3, 3: 2, 4: 1}

def prepare_tests() -> List[TestCase]:
    test_cases = []
    case_count = int(input())
    for _ in range(case_count):
        n = int(input())
        times = [int(x) for x in input().split()]
        test_cases.append(TestCase(n, times))
    return test_cases



def main(ships: list):
    c = Counter(ships)
    if c == CORRECT_AMOUNT:
        return "YES"
    return "NO"



if __name__ == '__main__':
    tests = prepare_tests()
    for t in tests:
        print(main(t.ships))
