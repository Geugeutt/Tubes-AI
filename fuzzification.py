from membership import segitiga

def fuzz_income(x):
    return {
        'low': segitiga(x, 30000, 30000, 60000),
        'medium': segitiga(x, 50000, 65000, 80000),
        'high': segitiga(x, 70000, 90000, 90000)
    }

def fuzz_house_age(x):
    return {
        'new': segitiga(x, 0, 0, 5),
        'medium': segitiga(x, 3, 6, 9),
        'old': segitiga(x, 7, 10, 10)
    }

def fuzz_rooms(x):
    return {
        'few': segitiga(x, 0, 0, 5),
        'enough': segitiga(x, 4, 6, 8),
        'many': segitiga(x, 7, 10, 10)
    }
