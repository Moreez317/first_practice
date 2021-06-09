import math

#count = int(input())

def f14(n):
    if n == 0:
        return 4
    else:
        return math.cos(f14(n - 1)) - math.tan(f14(n - 1))

#print("{:.2e}".format(f14(count)))

#f(3) = 1.98


