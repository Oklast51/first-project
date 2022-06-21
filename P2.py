n, k = map(int, input().split())
pill, pos = [], -1  # 初始位置不在木樁上，定義為-1
for i in range(n):
    pill.append(list(map(int, input().split())))  # 把木樁的高度和消耗體力值存在pill列表中
# 在倒數第2支木樁(index為n-1-1)或之前，當剩餘體力大於下一木樁消耗體力時能向前走
while pos <= n-2 and k >= pill[pos + 1][1]:
    k -= pill[pos + 1][1]
    pos += 1
if pos == -1:  # 當第一支木樁都走不過，位罝依然為-1時輸出0
    print(0)
else:  # 在能到達的木樁中，找出最高的一支的序號，比它矮的看到數量一定少於或等於它所看到的
    # 生成能到達木樁列表並按高度排行，再取得最高的樁的索引
    h_max = pill.index(max(list(pill[j] for j in range(0, pos + 1)), key=lambda x: x[0]))
    visible = h_max  # 視野範圍的判定，需要記錄到達最高樁h_max(不變)，和一個動態變化的變量visible記錄視野範圍
    # 在倒數第2支樁前(index為n-1-1)，當到達的最高木樁高於下一支木樁時即可以看到下一支
    while visible <= n-2 and pill[h_max][0] >= pill[visible+1][0]:
        visible += 1  # 視野範圍+1
    print(visible + 1)  # python index由0開始，輸出時要+1
