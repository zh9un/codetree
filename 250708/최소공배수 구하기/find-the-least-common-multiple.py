n, m = map(int, input().split())

# Please write your code here.



def a(n,m):
    while m != 0 :
        n = m
        m = n % m
    x = n * m
    n //= x
    return n

print(a(n,m))