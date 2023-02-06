from collections import namedtuple
from typing import List

TestCase = namedtuple("TestCase", ["n", "times"])

def prepare_tests() -> List[TestCase]:
    test_cases = []
    case_count = int(input())
    for _ in range(case_count):
        n = int(input())
        times = [int(x) for x in input().split()]
        test_cases.append(TestCase(n=n, times=times))
    return test_cases

"""
20 10 20 30
[10, 20, 20, 30]
"""
def assign_places(test: TestCase):
    result = []
    lst: list = test.times
    sorted_t = sorted(lst)
    for place, time in list(enumerate(sorted_t, start=1)):
        pass

    return result



if __name__ == '__main__':
    tests = prepare_tests()
    for t in tests:
        print(assign_places(t))
