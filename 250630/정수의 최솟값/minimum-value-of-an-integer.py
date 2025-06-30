a, b, c = map(int, input().split())

# Please write your code here.
def min(a,b,c) :
    if a > b :
        a = b
    if a > c :
        a = c
    return a

print(min(a,b,c))