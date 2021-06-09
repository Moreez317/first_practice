import math

#x = int(input())

def f12(x):
    if x < 48:
        result = ((23 * math.pow(((62 * math.pow(x, 2)) - math.exp(x)), 6)) - math.log(x))
    elif 48 <= x < 69:
        result = (math.pow(x, 6) - (6 * x))
    elif 69 <= x < 125:
        result = (math.log((55 * x) - math.pow(x, 8)) + (37 * math.pow(x, 6)))
    elif 125 <= x < 179:
        result = (math.log(math.exp(x)) + (79 * math.pow(x, 7)) - 85)
    elif x >= 179:
        result = (math.pow((math.pow(x, 7) + math.pow(x, 6)), 8) - math.cos(x))
    return "{:.2e}".format(result)

#print(f12(x))

#f(257) = 9.33e+134