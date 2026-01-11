def member(x, a, b, c):
    # Menghitung derajat keanggotaan nilai x
    if x <= a or x >= c:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    return 0.0