# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n, k = map(int, input().split())
pileh = [0]
pilek = [0]
for i in range(n):
    a, b = map(int, input().split())
    pileh.append(a)
    pilek.append(b)


if k-pilek[1]>=0:
    pos = 0
    for i in range(1, n + 1):
        while k >= pilek[i]:
            pos = pos + 1
            k = k - pilek[i]
    print(pos, k)

    temp = []
    for i in range(1, pos):
        temp.append(pileh[i])
    highest = max(temp)
    poshighest = pileh.index(highest)
    ans = 0
    for i in range(n):
        if (i > poshighest) and (pileh[poshighest] >= pileh[i]):
            ans += 1
            print(i, pileh[poshighest], pileh[i])
        if (i > poshighest) and (pileh[poshighest] < pileh[i]):
            break
    ans += poshighest
else:
    ans = 0
print(ans)
print(pileh)
print(pilek)