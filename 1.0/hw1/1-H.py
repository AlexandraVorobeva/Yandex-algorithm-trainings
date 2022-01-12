a = int(input())
b = int(input())
n = int(input())
m = int(input())

first_min = (n + (n-1)*a)
first_max = first_min + 2*a

second_min = (m + (m-1)*b)
second_max = second_min + 2*b

ma = min(first_max, second_max)
mi = max(first_min, second_min)

if (first_min > second_max) or (second_min > first_max):
    print(-1)
else:
    print(mi, ma)