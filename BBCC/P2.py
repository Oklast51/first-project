n, k = map(int, input().split())
pill, ans, pos_max = [], [], -1  # 初始位置不在木樁上，定義為-1
for i in range(n):
    pill.append(list(map(int, input().split())))  # 把柱子# 的高度和消耗體力值存在pill列表中
while pos_max <= n-2 and k >= pill[pos_max + 1][1]:  # 在倒數第2支柱子或之前，剩餘體力大於下一柱子體力值時能向前走
    k -= pill[pos_max + 1][1]  # 扣除體力值
    pos_max += 1  # 位置向前一格
if pos_max == -1:  # 當第一支柱子都走不過，位罝依然為-1時輸出0
    print(0)
else:
    for pos in range(0, pos_max+1):  # 對所有能到達的柱子
        pos_t, visible, mid = pos, pos, []  # target為要判定的柱子index,visible為可視範圍,middle是當前柱子和判定柱子之間的柱子列表
        while pos_t <= n-2 and pill[pos][0] >= pill[pos_t+1][0]:  # 當pos_t在尾2格或之前且其下一柱子比當前柱子矮時
            mid.append(pill[pos_t + 1])  # mid是當前柱子和判定柱子之間的柱子列表(不包含當前柱子但包含判定柱子)
            if pill[pos_t+1] == max(list(mid[j] for j in range(len(mid))), key=lambda x: x[0]):  # 當判定的柱子是mid中最高時
                visible = pos_t + 1  # 可以看到index為target+1的柱子
            pos_t += 1  # 判定下一根柱子
        ans.append(visible + 1)  # python index由0開始，輸出時要+1
    print(max(ans))
