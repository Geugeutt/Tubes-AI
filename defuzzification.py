from membership import segitiga

def defuzzifikasi(output):
    numerator = 0.0
    denominator = 0.0

    for z in range(0, 101):
        low = min(output['low'], segitiga(z, 0, 0, 50))
        medium = min(output['medium'], segitiga(z, 30, 50, 70))
        high = min(output['high'], segitiga(z, 50, 100, 100))

        mu = max(low, medium, high)
        numerator += mu * z
        denominator += mu

    return numerator / denominator if denominator != 0 else 0.0
