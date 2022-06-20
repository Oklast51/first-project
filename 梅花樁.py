n, k = map(int, input().split())
pill, pos = [], -1  # 初始位置不在木樁上，定義為-1
for i in range(n):
    pill.append(list(map(int, input().split())))  # 把木樁的高度和消耗體力值存在pill列表中
while k > 0 and k - pill[pos + 1][1] >= 0:  # 當體力為正且大於下一木樁消耗體力時能向前走
    k -= pill[pos + 1][1]
    pos += 1
if pos == -1:  # 當第一支木樁都走不過，位罝依然為-1時輸出0
    print(0)
else:
    # 在能到達的木樁中，找出最高的一支的序號，比它矮的看到一定少於或等於最高的樁
    hmax = pill.index(max(list(pill[j] for j in range(0, pos + 1)), key=lambda x: x[0]))  # 生成能到達木樁列表並按高度排行，再用index取得它的索引
    visible = hmax  # 視野範圍的判定，需要記錄到達皂最高樁hmax(不變)，和一個動態變化的變量記錄視野範圍
    while pill[hmax][0] >= pill[visible + 1][0]:  # 當所到達的最高木樁高於視野中的木樁時即可以看到
        visible += 1  # 視野範圍+1
    print(visible + 1)  # python中的list的index是由0開始，因此輸出時要+1
