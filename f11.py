import math

#x = float(input())
#y = float(input())
#z = float(input())

def f11(x, y, z):
    f = ((23 * math.pow(z, 6.0) - math.sin(x))/(math.tan(math.sin(z)-(math.pow(x, 7.0)/26.0)-64.0) + math.pow(y, 4.0))) - (z - math.pow(z, 2.0)) - (math.sqrt(6 * math.pow(z, 7.0) + abs(y)))
    return "{:.2e}".format(f)

#print(f11(x, y, z))

#f(‐51,75,50) = ‐2.15e+06
