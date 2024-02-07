import math

num = int(input())
ans = 0

max = math.sqrt(num)

if max ** 2 == num:
    print(max)

else:
    max = int(max)
    for temp in range(1, num):
        if temp ** 2 < num:
            ans = temp
        else:
            print(ans)
            break