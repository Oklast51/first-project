n, k = map(int, input().split())
ls = []
for i in range(n):
    ls.append(input().split())  # 把每個小朋友的姓名和身高的數據存在同一個列表中，並加入到列表ls中
ls.sort(key=lambda students: students[0])  # 對ls進行按名字字典序的排列(要按全名每字符對比，不能只按第一個字母排序)
for i in range(0, n, int(n/k)):  # 把列表分為k段，即k隊，由0開始輸出，步長為n/k，每次輸出的長度都是n/k個人
    team = sorted(ls[i:i+int(n/k)], key=lambda students: int(students[1]))  # 對切片後的列表按身高排序
    for student in team:
        print(student[0], end=' ')  # 依次輸出對應的名字，名字之間隔一個空格
    if i != n-int(n/k):  # 每輸出一隊換行，最後一次輸出不需要再換行
        print()
