a, b = map(int, input().split())

# Please write your code here.
def samyukgu(n) :
    return '3' in str(n) or '6' in str(n) or '9' in str(n)

def three(n) :
   return n % 3 == 0

count = 0
for i in range (a, b+1) :
    if samyukgu(i) or three(i) :
        count += 1

print(count)