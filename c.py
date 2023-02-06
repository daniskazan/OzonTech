from collections import namedtuple
from typing import List
import re


TestCase = namedtuple("TestCase", ["sequence"])


def prepare_tests() -> List[TestCase]:
    test_cases = []
    case_count = int(input())
    for _ in range(case_count):
        s = input()
        test_cases.append(TestCase(sequence=s))
    return test_cases

def is_valid_partition(s):
    pattern_first = re.compile("[A-Z][0-9][0-9][A-Z][A-Z]")
    pattern_second = re.compile("[A-Z][0-9][A-Z][A-Z]")

    i = 0
    while i < len(s):
        if re.match(pattern_first, s[i:i + 5]):
            i += 5
        elif re.match(pattern_second, s[i:i + 4]):
            i += 4
        else:
            return False
    return True


def partition_string(s):
    pattern_first = re.compile("[A-Z][0-9][0-9][A-Z][A-Z]")
    pattern_second = re.compile("[A-Z][0-9][A-Z][A-Z]")

    partition = []
    i = 0
    while i < len(s):
        if re.match(pattern_first, s[i:i + 5]):
            partition.append(s[i:i + 5])
            i += 5
        elif re.match(pattern_second, s[i:i + 4]):
            partition.append(s[i:i + 4])
            i += 4
    return partition


if __name__ == '__main__':
    tests = prepare_tests()

    for t in tests:
        if is_valid_partition(t.sequence):
            print(*partition_string(t.sequence))
        else:
            print("-")

