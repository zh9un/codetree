n, m = map(int, input().split())

# Please write your code here.
def a(n,m):
    x = 0
    while m != 0 :
        x = n % m
        n = m
        m = x
    return n

print(a(n,m))
