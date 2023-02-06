from collections import namedtuple


TestCase = namedtuple("TestCase", field_names=["blocks_amount", "symbol_of_i_block", "amount"])


def prepare_strings():
    tests = []
    strings = []
    for _ in range(2):
        blocks_amount = int(input())
        symbol_of_i_block = [str(x) for x in input().split()]
        amount = [int(x) for x in input().split()]
        t = TestCase(blocks_amount, symbol_of_i_block, amount)
        tests.append(t)
    for t in tests:
        res = ""
        for s in t.symbol_of_i_block:
            idx = t.symbol_of_i_block.index(s)
            res += s*t.amount[idx]
        strings.append(res)
    return strings

def diff(a, b):
    return [i+1 for i in range(len(a)) if a[i] != b[i]]


if __name__ == '__main__':
    s1, s2 = prepare_strings()
    print(sum(diff(s1, s2)))