import math

#n = int(input())
#m = int(input())

def f13(n, m):
    sum1 = 0
    sum2 = 0

    for i in range(1, n + 1):
        sum1 += ((23 * math.pow(i, 6)) - math.sin(i))

    for i in range(1, n + 1):
        sum3 = 0
        for j in range(1, m + 1):
            sum2 += ((7 * math.pow(j, 7)) - math.log(j) - 1)
        sum3 += sum2

    result = (sum1 - (92 * sum3))

    return "{:.2e}".format(result)

#print(f13(n, m))

#f(33,46) = ‐5.80e+16