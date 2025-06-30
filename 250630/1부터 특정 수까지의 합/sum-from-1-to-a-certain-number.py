n = int(input())

# Please write your code here.
def a(n) :
    i = 1
    j = 0
    for _ in range(i, n+1) : 
        j += i
        i += 1
    return j // 10

print(a(n))

