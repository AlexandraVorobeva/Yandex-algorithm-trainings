def is_enough(h, w, n, mid):
    tiles_need = h * mid * 2 + abs(w - 2 * mid) * mid * 2
    return tiles_need <= n


def find_foad(h, w, n):
    l = 0
    r = min(h, w)
    while l < r:
        mid = (l + r +1) //2
        if is_enough(h, w, n, mid):
            l = mid
        else:
            r = mid - 1

    return l


h = int(input())
w = int(input())
n = int(input())
print(find_foad(h, w, n))