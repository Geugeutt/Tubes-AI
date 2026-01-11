def inferensi(income, age, rooms):
    # Menentukan aturan IF-THEN berdasarkan nilai fuzzy input
    rules = []

    # Sangat layak
    rules.append((min(income['high'], age['new'], rooms['many']), 'high'))

    # Cukup layak
    rules.append((min(income['medium'], rooms['enough']), 'medium'))
    rules.append((min(income['high'], rooms['enough']), 'medium'))
    rules.append((min(income['medium'], age['new']), 'medium'))

    # Tidak layak
    rules.append((max(income['low'], age['old']), 'low'))
    rules.append((min(income['low'], rooms['few']), 'low'))

    return rules


def agregasi(rules):
    # Menggabungkan hasil inferensi 
    output = {'low': 0.0, 'medium': 0.0, 'high': 0.0}
    for value, label in rules:
        output[label] = max(output[label], value)
    return output
