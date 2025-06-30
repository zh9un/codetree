n, m = map(int, input().split())

# Please write your code here.


def a(n,m):
    x = m
    y = n
    while m != 0 :
        n,m = m, n%m
    z = x * y
    z //= n
    return z

print(a(n,m))