import random
rate1, rate2 = 1.1, 9.0
M1, M2 = 100 * rate1, 100 * rate2
result, Money1, Money2, Expected1, Expected2 = [], [], [], [], []
T, Choice, Runtimes = map(int, input('賭的次數,下注(1/2),模擬次數:').split())


def bet(ls, m, n, choice):
    if choice == 1:
        if ls.count(1) in range(m, n + 1):
            Money1.append(M1)
    elif choice == 2:
        if ls.count(1) not in range(m, n + 1):
            Money2.append(M2)


def throw_coin(times, choice):
    for j in range(times):
        temp = []
        temp.extend([random.randint(0, 1) for k in range(10)])
        result.append(temp.count(1))
        bet(temp, 3, 7, choice)


if __name__ == '__main__':
    for i in range(Runtimes):
        throw_coin(T, Choice)
        locals()['Expected' + str(Choice)].append(sum(locals()['Money' + str(Choice)]) / (T * (i + 1)))
        if i % (Runtimes / 10) == 0:
            print('期望值:', sum(locals()['Expected' + str(Choice)]) / len(locals()['Expected' + str(Choice)]))
