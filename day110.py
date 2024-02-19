'''import math
n = int(input())
m = int(input())
print(math.ceil((n*m/4)))'''

#watermelon to get equal halfs of even weight
w = int(input())
if w >2:#w%2==0 and w>2 not require if-else
    if w%2==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
