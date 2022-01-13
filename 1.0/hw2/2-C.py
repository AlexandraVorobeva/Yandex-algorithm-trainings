def find_close():
    n = int(input())
    seq = list(map(int, input().strip().split()))
    x = int(input())
    if n == 0:
        return None
    if n == 1:
        return seq[0]
    closest = seq[0]
    dist = abs(x - closest)
    for se in seq[1:]:
        newdist = abs(x - se)
        if newdist < dist:
            dist = newdist
            closest = se
    return closest


print(find_close())