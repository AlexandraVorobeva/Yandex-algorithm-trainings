n = int(input())
se = set()
cnt = 0

for _ in range(n):
    x, y = map(int, input().split(" "))
    if x not in se:
        se.add(x)
        cnt +=1
print(cnt)