from membership import member # Mengimpor fungsi keanggotaan

def fuzz_income(x):
    # Mengubah nilai pendapatan menjadi nilai fuzzy
    return {
        'low': member(x, 30000, 30000, 60000),
        'medium': member(x, 50000, 65000, 80000),
        'high': member(x, 70000, 90000, 90000)
    }

def fuzz_house_age(x):
    # Mengubah nilai usia rumah menjadi nilai fuzzy
    return {
        'new': member(x, 0, 0, 5),
        'medium': member(x, 3, 6, 9),
        'old': member(x, 7, 10, 10)
    }

def fuzz_rooms(x):
    # Mengubah jumlah ruangan menjadi nilai fuzzy
    return {
        'few': member(x, 0, 0, 5),
        'enough': member(x, 4, 6, 8),
        'many': member(x, 7, 10, 10)
    }
