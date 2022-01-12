nn = int(input())

se = set()
cnt = 0

for _ in range(nn):
    ahead, behind = map(int, input().split(" "))
    if (ahead >= 0) and (behind >= 0) and (ahead + behind + 1 == nn) and ((ahead, behind) not in se):
        se.add((ahead, behind))
        cnt += 1

print(cnt)