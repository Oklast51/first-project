import random
from numpy import array

t, m = map(int, input().split())


def mode_times(ls):
    temp = 1
    for element in ls:
        if ls.count(element) > temp:
            temp = ls.count(element)
    return temp


def count_money(n):
    dictionary = {1: 0, 2: 1 / 6, 3: 2 / 6}
    return dictionary[n]


def situation(ls, times, t1, t2, t3, sub_mode):
    dictionary = {1: t1, 2: t2, 3: t3}
    while sub_mode:
        dictionary[mode_times(ls)].append(1)
        return array([sum(t1), sum(t2), sum(t3)]) / times


def expected_value(x, times, mode=0):
    ans = 0
    t1, t2, t3 = [], [], []
    for j in range(times):
        result = []
        result.extend([random.randint(1, x)] for k in range(3))
        situation(result, times, t1, t2, t3, mode)
        ans += count_money(mode_times(result))
    if mode != 0:
        print(situation(result, times, t1, t2, t3, mode))
    print(ans / times)


if __name__ == '__main__':
    for i in range(10):
        expected_value(6, t, m)
