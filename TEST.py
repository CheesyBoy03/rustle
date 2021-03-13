from math import sqrt

def check(inp):
    x1, y1, x2, y2, x3, y3 = (int(v) for v in inp.split())
    dots = {(x1, y1), (x2, y2), (x3, y3)}
    tol = 1e-20
    try:
        one_line = ((x3 - x1) / (x2 - x1) - (y3 - y1) / (y2 - y1)) ** 2 <= tol
    except ZeroDivisionError:
        one_line = False
    if one_line or len(dots) < 3:
        return 'L'
    else:
        res = ''
        triangle_length = sorted([sqrt(abs((x2 - x1) ** 2 + (y2 - y1) ** 2)),
                                 sqrt(abs((x3 - x1) ** 2 + (y3 - y1) ** 2)),
                                 sqrt(abs((x3 - x2) ** 2 + (y3 - y2) ** 2))])
        a, b, c = triangle_length
        print(triangle_length)
        if round(c ** 2, 8) == (b ** 2 + a ** 2):
            res += 'R'
        if round(c ** 2, 8) > (b ** 2 + a ** 2):
            print(c**2)
            res += "O"
        if round(c ** 2, 8) < (b ** 2 + a ** 2):
            res += "A"
        if len(set(triangle_length)) == 2:
            res += "E"
        return res

print(check(input()))