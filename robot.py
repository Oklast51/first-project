n, e = map(int, input().split())
y = list(map(int, input().split()))
start = 0
end = 1
length = 1
area = [y[0]]
ans = []
while n - end:
    if abs(y[end]-y[start]) <= e and abs(min(area) - y[end]) <= e and abs(max(area) - y[end]) <= e:
        area.append(y[end])
        length += 1
        end += 1
        ans.append(length)
    else:
        start += 1
        end = start+1
        area = [y[start]]
        length = 1
print(max(ans))
