from fuzzification import fuzz_income, fuzz_house_age, fuzz_rooms
from inference import inferensi, agregasi
from defuzzification import defuzzifikasi
import csv


import csv

def read_data(filename):
    data = []
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Skip baris jika ada data kosong
            if (
                row['avg_income'] == '' or
                row['avg_area_house_age'] == '' or
                row['avg_area_num_rooms'] == ''
            ):
                continue

            data.append({
                'income': float(row['avg_income']),
                'age': float(row['avg_area_house_age']),
                'rooms': float(row['avg_area_num_rooms']),
                'address': row['address']
            })

    return data

def main():
    data = read_data('house_price_prediction.csv')
    results = []

    for d in data:
        income = fuzz_income(d['income'])
        age = fuzz_house_age(d['age'])
        rooms = fuzz_rooms(d['rooms'])

        rules = inferensi(income, age, rooms)
        output = agregasi(rules)
        score = defuzzifikasi(output)

        results.append({'address': d['address'], 'score': score})

    results.sort(key=lambda x: x['score'], reverse=True)
    top5 = results[:5]

    with open('output.csv', 'w') as f:
        f.write('address,score\n')
        for r in top5:
            f.write(f"{r['address']},{r['score']:.2f}\n")
    
    print("\nTop 5 Rumah Paling Layak:\n")
    print_table(top5)


def print_table(data):
    print("+----+--------------------------------------+-----------+")
    print("| No | Address                              | Score     |")
    print("+----+--------------------------------------+-----------+")

    for i, row in enumerate(data, start=1):
        address = row['address'].split('\n')[0]  # ambil baris pertama alamat
        score = f"{row['score']:.2f}"
        print(f"| {i:<2} | {address:<36} | {score:<9} |")

    print("+----+--------------------------------------+-----------+")


if __name__ == "__main__":
    main()