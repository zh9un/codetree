n = int(input())

# Please write your code here.
def a(n) :
    x = n // 10
    y = n % 10
    z = x + y
    if n % 2 == 0 and z % 5 == 0:
        print("Yes")
    else : print("No")

a(n)

