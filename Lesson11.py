#for文
for i in range(5):
    print(i)

#breake iが3 for終了
for i in range(3):
    if i == 3:
        break
    print(i)

#continue iが3 処理スキップ
for i in range(5):
    if i == 3:
        continue
    print(i)

#for文の中にfor文 for文のnest
for i in range(3):
    for j in range(3):
        print(i,j, sep="-")

#変数を使いリスト中身の表示
arr = [2,4,6,8,10]
sum = 0
for i in arr:
    print(i)
    sum += i
print(sum)
