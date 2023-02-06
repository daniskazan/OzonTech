from difflib import SequenceMatcher
import itertools

from collections import namedtuple
from typing import List


TestCase = namedtuple("TestCase", ["combinations"])


def prepare_tests() -> List[TestCase]:
    test_cases = []
    case_count = int(input())
    for _ in range(case_count):
        n = int(input())
        words = []
        for _ in range(n):
            words.append(input())
        test_cases.append(TestCase(combinations=list(itertools.combinations(words, 2))))
    return test_cases



def solve(n, arr):
    res = []
    h = {}
    for i in range(n):
        s = arr[i]
        t = ''
        cnt = 1
        for j in range(1, len(s)):
            if s[j] == s[j - 1]:
                cnt += 1
            else:
                t += s[j - 1] + str(cnt)
                cnt = 1
        t += s[-1] + str(cnt)
        if t not in h:
            h[t] = 1
            res.append(s)
    return len(res)


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = [input().strip() for i in range(n)]
    print(solve(n, arr))

